import urllib.request
from bs4 import BeautifulSoup
import requests
import ssl
import pandas as pd
import lxml
import openpyxl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.newsnationtv.com/?ref=nn-old"
html_file = urllib.request.urlopen(url,context=ctx).read()

soup = BeautifulSoup(html_file,'lxml')

# In[331]:

url_lst,news_cat_lst = [],[]
live_news = soup.find_all('ul',{'class':'sty-list flex-height'})
li_tags = live_news[0].find_all('li')
for a in li_tags:
    news_cat = a.find_all('span',{'class':'cat-txt'})
    news_cat_lst.append(news_cat[0].text)
    a_tags = a.find_all('a')
    for links in a_tags:
        url = links.get('href')
    url_lst.append(url)
# In[338]:
time_frame_lst,heading_lst,summary_lst,news_data_lst = [],[],[],[]
for link in url_lst:
    ul = urllib.request.urlopen(link,context=ctx).read()
    sp = BeautifulSoup(ul,'lxml')
    time_frame = sp.find('div',class_='float-left update').text.split('Updated on:')[-1]
    time_frame_lst.append(time_frame)
    heading = sp.find('h1').text
    heading_lst.append(heading)
    summary = sp.find('h2').text
    summary_lst.append(summary)
    news_data = sp.find_all('p')
    news_data_lst.append(news_data)

article_lst = [[] for i in range(len(url_lst))]
for article in range(len(article_lst)):
    for i in news_data_lst[article]:
        t =  "".join(i.text)
        article_lst[article].append(t)

# In[360]:

live_news = {'Date and Time': time_frame_lst,'Category':news_cat_lst,'Heading':heading_lst,'Summary':summary_lst,'Article':article_lst,'URL':url_lst}
live_news_df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in live_news.items()]))

# In[361]:

live_news_df.to_excel('Live_News.xlsx')

# In[342]:

top_stories_news_url_lst,category_lst = [],[]
top_stories_news = soup.find_all('ul',{'class':'bg-light p-2 list-top w-100 float-left flex-height'})
table_below_top_stories = top_stories_news[0].find_all('li')
for tags in table_below_top_stories:
    tag = tags.find_all('a')
    category = tags.find_all('span',{'class':'cat-txt'})
    category_lst.append(category[0].text)
    for href_value in tag:
        href = href_value.get('href')
    top_stories_news_url_lst.append(href)

# In[353]:

top_news_time_frame_lst,top_news_heading_lst,top_news_summary_lst,top_news_data_lst = [],[],[],[]
for top_stories_url in top_stories_news_url_lst:
    news_url = urllib.request.urlopen(top_stories_url,context=ctx).read()
    top_news_sp = BeautifulSoup(news_url,'lxml')
    top_news_time_frame = top_news_sp.find('div',class_='float-left update').text.split('Updated on:')[-1]
    top_news_time_frame_lst.append(top_news_time_frame)
    top_news_heading = top_news_sp.find('h1').text
    top_news_heading_lst.append(top_news_heading)
    top_news_summary = top_news_sp.find('h2').text
    top_news_summary_lst.append(top_news_summary)
    top_news_data = top_news_sp.find_all('p')
    top_news_data_lst.append(top_news_data)

top_stories_article_lst = [[] for i in range(len(top_stories_news_url_lst))]
for top_stories in range(len(top_stories_article_lst)):
    for j in top_news_data_lst[top_stories]:
        story =  "".join(j.text)
        top_stories_article_lst[top_stories].append(story)

# In[354]:

top_stories = {'Date and Time': top_news_time_frame_lst,'Category':category_lst,'Heading':top_news_heading_lst,'Summary':top_news_summary_lst,'Article':top_stories_article_lst,'URL':top_stories_news_url_lst}
top_stories_df = pd.DataFrame(dict([(k,pd.Series(v)) for k,v in top_stories.items()]))

# In[359]:

top_stories_df.to_excel('Top_Stories.xlsx')