import cv2

img = cv2.imread("Meter_reading.jpg")
print(img.shape)

imgresize = cv2.resize(img,(500,500))

imgCroppedCANumber = img[170:190,825:1000]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgCroppedCANumber)

# imgCropped = img[0:170,0:1200]
imgCropped1 = img[130:150,700:900]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgCropped1)

cv2.waitKey()





import cv2

img = cv2.imread("Meter_reading.jpg")
print(img.shape)

imgAmountCropped = img[350:380,535:900]
imgCANumberCropped = img[170:190,825:1000]
imgDueDateCropped = img[130:150,700:900]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgAmountCropped)
cv2.imshow("Image Resize",imgCANumberCropped)
cv2.imshow("Image Resize",imgDueDateCropped)
cv2.waitKey()
cv2.waitKey()
cv2.waitKey()

data = (imgAmountCropped+imgCANumberCropped+imgDueDateCropped)
cv2.imshow("Image",data)
cv2.waitKey()



import cv2
import numpy

import pytesseract

img = cv2.imread("Meter.png",0)

print(img.shape)

cv2.imshow("Image",img)

imgAmountCropped = img[690:705,682:800]
cv2.imshow("Amount",imgAmountCropped)
cv2.waitKey()

imgCANumberCropped = img[120:135,775:900]
cv2.imshow("CA",imgCANumberCropped)
cv2.waitKey()

imgDueDateCropped = img[83:110,660:800]
cv2.imshow("Date",imgDueDateCropped)

cv2.waitKey()

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("Amount.png")
cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow("Extract Electric Data",img)
cv2.waitKey()

img1 = cv2.imread("CA.png")
cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img1))
cv2.imshow("Extract Electric Data",img1)
cv2.waitKey()

img2 = cv2.imread("Date.png")
cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img2))
cv2.imshow("Extract Electric Data",img2)

cv2.waitKey()






import cv2
import numpy

img = cv2.imread("Meter.png",0)

print(img.shape)

cv2.imshow("Image",img)

imgAmountCropped = img[690:705,682:744]
cv2.imshow("Amount",imgAmountCropped)
cv2.waitKey()






import cv2
import numpy

import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("Meter.png")
if img[83:110,660:800]:
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    cv2.imshow("Extract Electric Data", img)
elif img[690:705,682:800]:
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    cv2.imshow("Extract Electric Data", img)
elif img[120:135,775:900]:
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    cv2.imshow("Extract Electric Data", img)

cv2.imshow("Image",img)
cv2.waitKey()






import cv2
import numpy
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread("Meter.png")
print(pytesseract.image_to_string(img[83:110,660:800]))
cv2.imshow("Image",img)
cv2.waitKey(0)

img1 = cv2.imread("Meter.png")
print(pytesseract.image_to_string(img1[690:705,682:800]))
cv2.imshow("Image",img1)
cv2.waitKey(0)

img2 = cv2.imread("Meter.png")
print(pytesseract.image_to_string(img2[120:135,775:900]))
cv2.imshow("Image",img2)
cv2.waitKey(0)






import cv2
import numpy
import pytesseract


class Electric_Image:
    def Image_detected(self):
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
        img = cv2.imread("Meter.png")
        Amount = img[83:110, 660:800]
        Last_Date = img[690:705, 682:800]
        CA_Number = img[120:135, 775:900]
        for csv in Amount:
            print(pytesseract.image_to_string(img[83:110, 660:800]))

        cv2.imshow("Image", img)
        cv2.waitKey(0)



import cv2
import pytesseract

# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

# Read image from which text needs to be extracted
img = cv2.imread("Meter.png")

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

# Appplying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Creating a copy of image
im2 = img.copy()

# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()

# Looping through the identified contours , Then rectangular part is cropped and passed on , to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    cropped = im2[83:110, 660:800]

    # Open the file in append mode
    file = open("recognized.txt", "a")

    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)

    # Appending the text into file
    file.write(text)
    file.write("\n")

    # Close the file
    file.close






import cv2
import pytesseract

image = cv2.imread("Meter.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# performing Canny edge detection to remove non essential objects from image
edges = cv2.Canny(gray_image, 400, 300, apertureSize=3)
# since findContours affects the original image, we make a copy
image_ret = edges.copy()

# converting image to binary
ret, thresh = cv2.threshold(image_ret, 127, 255, 0)
# getting the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

digits = dict()

# getting bounding boxes having a minimum area
# this large area is surely to contain the output values
for (i, c) in enumerate(contours):
    if cv2.contourArea(c) > 10000:
        (x, y, w, h) = cv2.boundingRect(c)
        roi = thresh[y:y + h, x:x + w]
        digits[i] = roi
        break

cv2.imshow(digits[i])

# we just need the numbers
custom_config = r'--oem 3 --psm 7 outbase digits'
print(pytesseract.image_to_string(digits[i], config=custom_config))




import PIL
import cv2
import pytesseract
from pytesseract import image_to_string

img = img = cv2.imread("Meter.png")
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

txt = image_to_string(img)

print(txt)

from WordToNum import img2textdir as imt





import pytesseract
import os
import sys


img = "D:\\Meter_reading.jpg"

def read_image(img):

    try:
        return pytesseract.image_to_string(img)
    except:
        return "[ERROR] Unable to process file: {0}".format(img)

def read_images_from_dir(dir_path, write_to_file=False):

    converted_text = {}
    for file_ in os.listdir(dir_path):
        if file_.endswith(('png', 'jpeg', 'jpg')):
            text = read_image(os.path.join(dir_path, file_), lang=lang)
            converted_text[os.path.join(dir_path, file_)] = text
    if write_to_file:
        for file_path, text in converted_text.items():
            _write_to_file(text, os.path.splitext(file_path)[0] + ".txt")
    return converted_text

def _write_to_file(text, file_path):
    print("[INFO] Writing text to file: {0}".format(file_path))
    with open(file_path, 'w') as fp:
        fp.write(text)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("python3 ocr.py <path>")
        print("Provide the path to an image or the path to a directory containing images")
        exit(1)

    if os.path.isdir(sys.argv[1]):
        converted_text_map = read_images_from_dir(sys.argv[1], write_to_file=True)
    elif os.path.exists(sys.argv[1]):
        print(read_image(sys.argv[1]))
    else:
        print("Unable to process this file. Please check if it exists and is readable.")





import cv2
import pytesseract

img = cv2.imread("Meter.png")
print(img.shape)
cv2.waitKey()

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

cv2.imshow("Extract Data From Image",img)
print(pytesseract.image_to_string(img[690:705, 682:800]))
cv2.waitKey(0)

cv2.imshow("Extract Data From Image",img)
print(pytesseract.image_to_string(img[83:110,660:800]))
cv2.waitKey(0)

cv2.imshow("Extract Data From Image",img)
print(pytesseract.image_to_string(img[120:135, 775:900]))
cv2.waitKey(0)


cv2.imshow("Extract Data From Image",img)

cv2.destroyAllWindows()







1 :-
import cv2

import pytesseract

def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img = cv2.imread("Meter.png",0)

    print(pytesseract.image_to_string(img[690:705, 682:800]))
    print(pytesseract.image_to_string(img[83:110,660:800]))
    print(pytesseract.image_to_string(img[120:135, 775:900]))

    cv2.imshow("Extract Data From Image",img)

extract = Extract_Data_From_Image()
cv2.waitKey(0)




2 :-
import cv2

import pytesseract

def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img = cv2.imread("Meter.png",0)

    print(pytesseract.image_to_string(img[686:707, 682:800]))   # Amount Co-ordinate
    print(pytesseract.image_to_string(img[83:110,660:800]))     # Date Co-ordinate
    print(pytesseract.image_to_string(img[120:135, 775:900]))   # CA Number Co-ordinate

    cv2.imshow("Extract Data From Image",img)

extract = Extract_Data_From_Image()
cv2.waitKey(0)








This Value coming from Meter.png
[85:110,650:850] Date
[690:705,680:800] Amount
[120:134,773:900] CA




This Value are coming from Image.png

img[90:103,1030:1120] CA
img[70:85,900:1050] Date
img[535:550,900:1050] Amount


import cv2

import pytesseract

def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img = cv2.imread("Meter.png",0)

    print(pytesseract.image_to_string(img[83:110,660:800]))
    print(pytesseract.image_to_string(img[120:135, 775:900]))
    print(pytesseract.image_to_string(img[684:709, 682:800]))

    cv2.imshow("Extract Data From Image",img)
extract = Extract_Data_From_Image()
cv2.waitKey(0)




























# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
import cv2
import numpy
import pytesseract

img = cv2.imread("Meter.png", 1)
print(img.shape)

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Bill_Amount=img[685:705,683:790]
print(pytesseract.image_to_string(Bill_Amount))
cv2.imshow("Extract",Bill_Amount)

cv2.imshow("Image",img)
cv2.waitKey()



# Complete Project :-

import cv2

import pytesseract

img = cv2.imread("Meter.png", 0)

Bill_Amount = img[685:705,683:790]

Due_Date = img[83:110, 660:800]

CA_No = img[120:135, 775:900]

def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    cv2.imshow("Extract Data From Image", img)

    cv2.waitKey()

    print(pytesseract.image_to_string(Due_Date))

    print(pytesseract.image_to_string(CA_No))

    print(pytesseract.image_to_string(Bill_Amount))


if __name__ == "__main__":
    Extract_Data_From_Image()






import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("Electric_Bill_Details")

lab1 = ttk.Label(win, text='Image Uploading')
lab1.grid(row=0,column=0)

lab2 = ttk.Label(win, text='Electric Due Date')
lab2.grid(row=1,column=0,sticky=tk.W)

lab3 = ttk.Label(win, text='Account Number')
lab3.grid(row=2,column=0,sticky=tk.W)

lab4 = ttk.Label(win, text='Electric Amount')
lab4.grid(row=3,column=0,sticky=tk.W)

win.mainloop()


'''

import cv2

import tornado.web

import tornado.ioloop

import cgi

from csv import writer

import pytesseract

img = cv2.imread("Meter.png", 0)

Bill_Amount = img[685:705, 683:790]

Due_Date = img[83:110, 660:800]

CA_No = img[120:135, 775:900]


def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    cv2.imshow("Extract Data From Image", img)

    cv2.waitKey()

    print(pytesseract.image_to_string(Due_Date))

    print(pytesseract.image_to_string(CA_No))

    print(pytesseract.image_to_string(Bill_Amount))

    # print("""
    # <html>
    #   <Title>Hello in HTML</Title>
    # <body>
    #   <p>Hello There!</p>
    #   <p><b>Hi There!</b></p>
    # </body>
    # </html> """)

class uploadHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("index.html")

    def post(self):

        files = self.request.files["img"]

        for f in files:

            fh = open(f"img/{f.bill_details}","wb")

            fh.write(f.body)                         # This is used when i used html process

            fh.close()

        self.write("<a href = 'http://localhost:8080/img/{f.Image}'")

if (__name__ == "__main__"):

    Extract_Data_From_Image()

    data = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler,{"path" : "C:\\Users\\annaa\\PycharmProjects\\OCR_Project\\Image"})
    ])

    data.listen(8080)
    print("Localhost 8080")
    tornado.ioloop.IOLoop.instance().start()









'''
import cv2
import numpy
import pytesseract

img = cv2.imread("Meter.png", 1)
print(img.shape)

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Bill_Amount=img[685:705,683:790]
print(pytesseract.image_to_string(Bill_Amount))
cv2.imshow("Extract",Bill_Amount)

cv2.imshow("Image",img)
cv2.waitKey()



# Complete Project :-

import cv2

import pytesseract

img = cv2.imread("Meter.png", 0)

Bill_Amount = img[685:705,683:790]

Due_Date = img[83:110, 660:800]

CA_No = img[120:135, 775:900]

def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    cv2.imshow("Extract Data From Image", img)

    cv2.waitKey()

    print(pytesseract.image_to_string(Due_Date))

    print(pytesseract.image_to_string(CA_No))

    print(pytesseract.image_to_string(Bill_Amount))


if __name__ == "__main__":
    Extract_Data_From_Image()






import tkinter as tk

from tkinter import ttk

win = tk.Tk()

win.title("Electric_Bill_Details")

lab1 = ttk.Label(win, text='Image Uploading')
lab1.grid(row=0,column=0)

lab2 = ttk.Label(win, text='Electric Due Date')
lab2.grid(row=1,column=0,sticky=tk.W)

lab3 = ttk.Label(win, text='Account Number')
lab3.grid(row=2,column=0,sticky=tk.W)

lab4 = ttk.Label(win, text='Electric Amount')
lab4.grid(row=3,column=0,sticky=tk.W)

win.mainloop()


'''









import cv2

import tornado.web

import tornado.ioloop

from csv import writer

import pytesseract

import mysql.connector
from mysql.connector import Error

img = cv2.imread("Meter.png", 0)

Bill_Amount = img[685:705, 683:790]

Due_Date = img[83:110, 660:800]

CA_No = img[120:135, 775:900]


def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    cv2.imshow("Extract Data From Image", img)

    cv2.waitKey()

    print(pytesseract.image_to_string(Due_Date))

    print(pytesseract.image_to_string(CA_No))

    print(pytesseract.image_to_string(Bill_Amount))


def convertToBinaryData(filename):  # For MySQL where image are upload
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(Meter, Due_Date, CA_No, Bill_Amount, biodataFile):   # For MySQL where image are upload
    print("Inserting BLOB into Image_details table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_ocr_db',
                                             user='ocr_python',
                                             password='abhishek_kumar')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO Image_details
                          (photo,Due_Date,CA_No,Bill_Amount) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(Meter)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (Due_Date, CA_No, Bill_Amount)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into Image_details table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


class uploadHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("index.html")

    def post(self):

        files = self.request.files["img"]

        for f in files:

            fh = open(f"img/{f.bill_details}","wb")

            fh.write(f.body)                         # This is used when i used html process

            fh.close()

        self.write("<a href = 'http://localhost:8080/img/{f.Image}'")

if (__name__ == "__main__"):

    Extract_Data_From_Image()

    data = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler,{"path" : "C:\\Users\\annaa\\PycharmProjects\\OCR_Project\\Image"})
    ])

    data.listen(8080)
    print("Localhost 8080")
    tornado.ioloop.IOLoop.instance().start()

    insertBLOB(1, "Meter", "C:\Users\annaa\PycharmProjects\OCR_Project\Meter.png",
           "C:\Users\annaa\PycharmProjects\OCR_ProjectMeter_bioData.txt")


<hi>Due Date<input type="type" name="number" src="26-09-2020" autocomplete="off" formtarget="_blank" pattern="^[number]+$" autofocus="autofocus" content="" readonly></hi><br><br>
            <hi>Account No<input type="text" name="number" src="100124568" formtarget="_blank" pattern="^[number]+$" readonly></hi><br><br>
            <hi>Bill Amount<input type="text" name="number" src="66540.00" formtarget="_blank" pattern="^[number]+$" readonly></hi><br><br>

















import cv2

import tornado.web

import tornado.ioloop

from csv import writer

import pytesseract

import cgi
import os

def Extract_Data_From_Image():

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    '''
    fileitem = form('filename')
    if fileitem.filename:
        fname = os.path.basename(fileitem.filename)
        open('C:\\Users\\annaa\\PycharmProjects\\OCR_Project'+fname,'wb').write(fileitem.file.read())
        msg = 'File uploaded successfully'
    else:
        msg = 'File not uploaded successfully'


        form = cgi.FieldStorage()
        pn = str(form.getvalue('pname'))
        des = str(form.getvalue('des'))
        fileitem = form['filename']
        fn = os.path.basename(fileitem.filename)
        open('C:\\Users\\annaa\\PycharmProjects\\OCR_Project\\Meter.png'+fn,'wb').write(fileitem.file.read())
    '''

    img = cv2.imread("Meter.png", 0)

    Bill_Amount = img[685:705, 683:790]

    Due_Date = img[83:110, 660:800]

    CA_No = img[120:135, 775:900]

    cv2.imshow("Extract Data From Image", img)

    cv2.waitKey()

    print(pytesseract.image_to_string(Due_Date))

    print(pytesseract.image_to_string(CA_No))

    print(pytesseract.image_to_string(Bill_Amount))

class uploadHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("index.html")

    def post(self):

        files = self.request.files["img"]

        for f in files:

            fh = open(f"img/{f.bill_details}","wb")

            fh.write(f.body)                         # This is used when i used html process

            fh.close()

        self.write("<a href = 'http://localhost:5000/img/{f.Image}'")

if (__name__ == "__main__"):

    Extract_Data_From_Image()

    data = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler,{"path" : "C:\\Users\\annaa\\PycharmProjects\\OCR_Project\\Image"})
    ])

    data.listen(5000)
    print("Localhost 5000")
    tornado.ioloop.IOLoop.instance().start()