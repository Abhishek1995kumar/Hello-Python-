from bs4 import BeautifulSoup
import time
import csv
import re
import requests
import matplotlib

"""scrape youtube channel to built table of contents html file 
and csv of video information data for excel file note this code has a
slow down delay to meet youtube turms of user"""

# Set youtube channel name here
channel_name = 'AajTak'

def get_soup_data(url):

    """Open url and return BeautifulSoup Object, or None if site does not exist"""

    url = 'https://www.youtube.com/watch?v=IupK-KpnSe4&ab_channel=AajTak'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    time.sleep(10)      # slow down as per YouTube videos
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.text

def aajtak_links():
    """List of {Title : <section_title>, 'Links' :<url to section play list>}"""
    soup1 = get_soup_data(f'https://www.youtube.com/user/{channel_name}/playlists')
    if 'This channel does not exist' in soup1.text:
        raise ValueError('This channel does not exist :' + channel_name)

    play_list_atag = soup1.find_all('a',{'href': re.compile(f'{channel_name}/playlists)')})
    element = [{'title': x.text.strip(), 'link' : fix_url(x['href'])} for x in play_list_atag if x.span
               and ('shelf_id=0' not in x['href'])] # Filter out non user play list

    if len(element) ==0:
        element = [{
            'title' : 'section',
            'link' : f'https://www.youtube.com/{channel_name}/playlists'
        }]
        return element

def fix_url(url):
    if url[0] == '/':
        return 'https://www.youtube.com' + url
    else:
        return url

def get_playlist(section):
    # return list of list
    print(f'Getting Playlists for Section : {section["title"]}')
    soup1 = get_soup_data(section['link'])
    if soup1 == None:
        return [{'title':'No Playlists','link' : f'https://www.youtube.com/{channel_name}/live_video'}]
    divs = soup1('a',class_='yt-uix-tile-link')       # modifing here

    playlists = []
    for d in divs:
        title = d.text
        if title != 'Liked video':
            link = fix_url(d['href'])
            playlists.append({'title': title, 'link': link})
    if playlists == []:
        return  [{
            'title' : 'No Playlists',
            'link' : f'https://www.youtube.com/{channel_name}/live_video'
        }]
    return playlists

def add_video(playlist):
    soup1 = get_soup_data(playlist['link'])
    print(f'Playlist for title : {playlist["title"]}')
    item = soup1('a',class_='yt-uix-tile-link')

    video = []
    for y in item:
        d = {}
        d['title'] = y.text.strip()
        link = fix_url(y['href'])
        d['link'] = link
        t = y.find.next('span',{'aria-label': True})
        d['time'] = t.text if t else 'NA'
        print(f'Open Video "{d["title"]}" for details', end=" ")
        vsoup = get_soup_data(link)
        print('* read,now processor', end="")

        views = vsoup.find('div',class_='watch-view-count').extract
        d['views'] = ''.join(c for c in views if c in '01234')
        d['publication_date'] = vsoup.find(
            'strong',
            class_= 'watch-time-text'
        ).extract[len('Published On ')-1:]

        d['discription'] = vsoup.find('div',id='watch-discription-text').extract

        id = vsoup.find('meta',itemprop='videoid')['content']
        d['short_link'] = f'https://www.youtube/{id}'
        like = vsoup.find('button',class_='like-button-renderer-like-button')
        d['likes'] = like.find('span',class_='yt-uix-button-content').extract

        dislike = vsoup.find('button',class_='like-button-renderer-like-button')
        d['dislikes'] = dislike.find('span', class_='yt-uix-button-content').extract
        video.append(d)
        print('* finished aajtak video')

        playlist['videos'] = video

def tag(t,c):
    return f'<{t}>{c}</{t}>'

def link(text,url):
    return f'<a href="{url}">{text}</a>'

def html_out_data(channel,sections):
    title = f'YouTube Channel {channel}'
    f = open(f'{channel}.html',"w")
    templete = '<!doctype html>\n<html lang="en-US">\n<head>\n<meta http-equiv="origin-trial">' + \
               '<title>{}</title>\n<head>\n<body>\n{}\n</body>\n</html>'

    part = []
    part.append(tag('h1',title))

    for section in sections:
        part.append(tag('h2',link(section['title'], section['link'])))
        for playlist in section['playlists']:
            part.append(tag('h3',link(playlist['title'], playlist['link'])))
            part.append('<ol>')
            for video in playlist['videos']:
                part.append(tag('l1', link(video['title'], video['short_link']) \
                                + '(' + video['time'] + ")"))

            part.append('</ol>')
    f.write(templete.format(channel,str('\n'.join(part))))
    f.close()
    pass

def csv_file_out(channel,sections):
    headers = 'channel,section,playlist,video' + \
               'link,time,views,publication_date,likes,dislikes,discription'.split(",")

    with open(f'{channel}.csv',"w") as csv_file:
        csvf = csv.writer(csv_file,delimiter=',')
        csvf.writerrow(headers)

        for section in sections:
            for playlist in section['playlists']:
                for video in playlist['videos']:
                    v = video
                    line = [channel,section['title'], playlist['title'], v['title']]
                    line.extend([v['short_link'],v['time'],v['views'],v['publication_date'],
                                v['likes'],v['dislikes'],v['discription']])

                    csvf.writerow(line)

if __name__ == '__main__':
    """Find channel name by going to channel and  picking test element for channel  url
    for ex :- AajTak channel url is 'https://www.youtube.com/watch?v=IupK-KpnSe4&ab_channel=AajTak'
    My channel name is AajTak in this url
    This is set near top of file"""
    print('finding sections')
    sections = aajtak_links()
    for section in sections:
        section['playlists'] =  get_playlist(section)
        for playlist in section['playlists']:
            add_video(playlist)

    html_out_data(channel_name,sections)  # Create Web page of channel link
    csv_file_out(channel_name,sections)   # Create a csv file of video info for import into spreadsheet
    print(f'Program Complete,\n {channel_name}.htm,and "__\
          f"{channel_name}.csv')