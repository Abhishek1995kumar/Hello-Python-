import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
window =  tk.Tk()
window.title('NEWS_NATION')


name_label = ttk.Label(window, text='Enter your Name : ')
name_label.grid(row=0,column=0, sticky = tk.W) # W means West or left side
email_label = ttk.Label(window, text='Enter your Email : ')
email_label.grid(row=1,column=0, sticky = tk.W)
add_label = ttk.Label(window, text='Enter your Address : ')
add_label.grid(row=2,column=0, sticky = tk.W)
gender_label = ttk.Label(window, text='Confirm your Gender : ')
gender_label.grid(row=3,column=0, sticky = tk.W)


name_var = tk.StringVar()
name_entry = ttk.Entry(window,width=16, textvariable = name_var)
name_entry.grid(row=0,column=1)
name_entry.focus()
email_var = tk.StringVar()
email_entry = ttk.Entry(window,width=16, textvariable = email_var)
email_entry.grid(row=1,column=1)
add_var = tk.StringVar()
add_entry = ttk.Entry(window,width=16, textvariable = add_var)
add_entry.grid(row=2,column=1)


Gender_var = tk.StringVar()
Gender_combo = ttk.Combobox(window , width = 13, textvariable = Gender_var, state = 'readonly')
Gender_combo['value'] = ('Male','Female','Other')
Gender_combo.current(0)
Gender_combo.grid(row=3,column=1)


usertype = tk.StringVar()
Radiobtn1 = ttk.Radiobutton(window,text ='Businessman',value ='Businessman',variable =usertype)
Radiobtn1.grid(row=4,column=0)
Radiobtn2 = ttk.Radiobutton(window,text ='Employee',value ='Employee',variable =usertype)
Radiobtn2.grid(row=4,column=1)


check_var = tk.IntVar()
checkbtn = ttk.Checkbutton(window,text='Check if you are Used to New Nation Channel',variable= check_var)
checkbtn.grid(row=5,columnspan=3)


def action():
    username = name_var.get()
    useremail = email_var.get()
    useradd = add_var.get()
    usergender = Gender_var.get()
    useroccup = usertype.get()
    if check_var.get() == 0:
        Used = 'NO..'
    else:
        Used = 'YES..'

    with open('GUI.csv', 'a') as f:
        dictwriter = DictWriter(f,fieldnames= ['User Name ','User Email Address'
            ,'User Address','User Gender','User Occupation','Used'])

        if os.stat('GUI.csv').st_size == 0: 
            dictwriter.writeheader()

        dictwriter.writerow({

            'User Name ' : username,
            'User Email Address' : useremail,
            'User Address' : useradd,
            'User Gender' : usergender,
            'User Occupation' : useroccup,
            'Used' : Used
        })

    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    add_entry.delete(0, tk.END)

    name_label.configure(foreground='#2874A6')
    email_label.configure(foreground='#CB4335')
    add_label.configure(foreground='#F5B041')
    gender_label.configure(foreground='#7D3C98')
    Submit_Button.configure(foreground='#E6B0AA')

Submit_Button = tk.Button(window, text='Submit', command=action)
Submit_Button.grid(row=6, column=0)


window.mainloop()