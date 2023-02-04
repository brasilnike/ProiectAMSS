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
        but = Button(self.root, text=curr_user._instance.first_name, bg="black", fg='white')
        # displaying button on the main display
        but.pack()
