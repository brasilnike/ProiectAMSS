import tkinter as tk

from tkinter import *
from tkcalendar import Calendar
DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


class CalendarFrame():

    def __init__(self, root):
        super().__init__()
        self.root = root
        # creating a calender object
        tkc = Calendar(self.root, selectmode="day", year=2022, month=1, date=1)
        # display on main window
        tkc.pack(pady=40)

        # getting date from the calendar
        def fetch_date():
            date.config(text="Selected Date is: " + tkc.get_date())

        # add button to load the date clicked on calendar
        but = Button(self.root, text="Select Date", command=fetch_date, bg="black", fg='white')
        # displaying button on the main display
        but.pack()
        # Label for showing date on main display
        date = Label(self.root, text="", bg='black', fg='white')
        date.pack(pady=20)
