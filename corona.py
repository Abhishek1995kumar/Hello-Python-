
import requests
from bs4 import BeautifulSoup
import datetime
import time         
import threading
import plyer as py   
import lxml
from PIL import Image
from PIL import ImageEnhance
import tkinter as tk
from tkinter import ttk



# Get Html Data from WebSites
def corono_data_bharat(url):    
    data = requests.get(url)
    return data

# Get URL Data from WebSites
def corona_bharat():
    url = "https://www.mohfw.gov.in/"
    url_data = corono_data_bharat(url)
    #print(url_data.text)  
    soup = BeautifulSoup(url_data.text,'lxml')
    #print(soup.prettify())
    div_data = soup.find_all('div', class_='information_row', id_= 'dashboard').find_all('div', class_='iblock active-case')
    #corona = div_data.find_all('div', class_='iblock')
    #print(div_data)
    #print(div_data)
    #print(len(div_data))

    details = ''

    for iblock in div_data:
        #print(iblock)
        count = iblock.find('span', class_= 'icount').get_text()
        text = iblock.find('div', class_= 'info_label').get_text()
        incre = iblock.find('div', class_= 'increase_block')
        #print(text + ' : ' + count + ' : ' + incre)
        details = details + text + ':' + count + ':' + incre + '\n'  # ye line append ke liye use ho raha hai

    return details


# This Func used to data refresh or updated from Web Sites
def refresh_button():
    updated_data = corona_bharat() 
    print('Refreshing Updated Corona Data')
    name_label['text'] = updated_data 


# This Func used to Notified me by Web Sites
def notice():    
    while True:
        py.notification.notify(
            head = 'COVID 19 BHARAT',
            msg = 'corona_bharat()',
            timeout = 20 ,            
            datetime = ' ',
            image_path = 'coronasmall.png'
        )
        time.sleep(600)

#corona_bharat() 

# This Func are call main Function
def main():
    corona_bharat()

if __name__ == '__main__':
    main()


# Create GUI & EDITING IMAGE
img = Image.open('corona.jpg') 
max_size = (250,250)
img.thumbnail(max_size)
img.save('coronasmall.png')


# Create Window 
window =  tk.Tk()
window.geometry(900*800)
window.iconbitmap('coronasmall.png')
window.title('CORONA DATA - BHARAT')
s = ('poppins',30,'bold')  

window.configure(background='blue')

image_data = tk.PhotoImage(file='coronasmall.png')
image_label = tk.Label(window,image='image_data')
image_label.grid()

name_label = tk.Label(window, text=corono_data_bharat(), font=s) 
name_label = tk.Label(window, text=corono_data_bharat(), font='f',background='yellow') 
name_label.grid()
name_label.configure(background='yellow')

Radiobtn = tk.Button(window,text ='REFRESH',font=s,relief='purpul',command='refresh_button')
Radiobtn.grid()


thread1 = threading.Thread(target=notice())
thread1.setDaemon(True)  
thread1.start()


window.mainloop()