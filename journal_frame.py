import tkinter as tk
import customtkinter
from tkinter import *
import mysql.connector
from tkcalendar import Calendar

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

my_connect = mysql.connector.connect(host='localhost',
                                     database='logindb',
                                     user='root',
                                     password='1q2w3e')
# ###### end of connection ######
my_conn = my_connect.cursor()


class JournalFrame():

    def __init__(self, root, curr_user):
        super().__init__()
        self.root = root
        print(curr_user._instance.first_name)
       
        my_conn.execute("SELECT PersonID from Person where first_name='"+curr_user._instance.first_name+"'")
        personid=my_conn.fetchone()
       
        print(personid[0])
        my_conn.execute("SELECT title,description from Journal WHERE person_id="+str(personid[0]))
        entry=my_conn.fetchone()
        title=entry[0]
        desc=entry[1]
        tk.Label(self.root, bg="#242424", fg='white',
		 text=title,
		 
         height=2,
		 font = ("Times", 33)).pack()
        tk.Label(self.root, bg="#242424", fg='white',
		 text=desc,
		 
         height=2,
         pady=15,
		 font = ("Times", 20)).place(y=500)
    
#
