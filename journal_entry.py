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
                                     database='amss',
                                     user='user',
                                     password='Password1!')
# ###### end of connection ######
my_conn = my_connect.cursor()
def popup(curr_user,title):
    popup.Tk()
    print("popup")

class JournalEntry():
    def __init__(self, root, curr_user,title):
        super().__init__()
        self.root = root
        print(curr_user._instance.first_name)