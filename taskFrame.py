import tkinter as tk

import sendemail
import task
from task import Task
from tkinter import *
from tkcalendar import Calendar
import mysql.connector

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


class TaskFrame():
    def callback(self):
        person_name = self.name_var.get()
        task_name = self.clicked.get()
        new_task = Task.create_task(1, 2, "Finish the report", "2023-02-05", False, task.Responsibilities.KID.name)
        #primele 2 ar trebui sa fie assignor/assignee, care sunt ID-uri care trebuiesc luate din baza de date
        self.email_singleton.send_email("calimandaniel5@gmail.com", new_task.description + " " +new_task.level_of_responsibility)
        #aici ar trebui sa pui emailul pe care il are assignee si toate detaliile loate in new)task
        print(person_name, task_name)

    def select_names(self):
        # Connect to the database
        cnx = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='admin')
        cursor = cnx.cursor()

        # Select all names from the Persons table
        query = "SELECT first_name, last_name FROM Person"
        cursor.execute(query)

        # Fetch all names from the result set
        names = cursor.fetchall()

        # Store the names in a list
        names_list = []
        for name in names:
            names_list.append(name[0] + " " + name[1])

        # Close the cursor and connection
        cursor.close()
        cnx.close()

        # Print the list of names
        return names_list

    def __init__(self, root):
        super().__init__()
        self.email_singleton = sendemail.SingletonEmail()
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

        self.options_list = ["Do the laundry", "Fold and put away clean clothes", "Vacuuming, sweeping, dusting",
                             "Wash and put away dishes", "Mop the floor", "Wash the family car", "Feed pet", "Walk pet",
                             "Do homework", "Take children to school", "Take children from school",
                             "Prepare breakfast ", "Prepare lunch", "Prepare dinner", "Clean the bathroom"]

        self.person_list = self.select_names()

        tkc = Calendar(self.root, selectmode="day", year=2022, month=1, date=1)
        # display on main window
        tkc.pack(pady=10)

        # getting date from the calendar
        def fetch_date():
            date.config(text="Selected Date is: " + tkc.get_date())

        but = Button(self.root, text="Select Date", command=fetch_date, bg="black", fg='white')
        # displaying button on the main display
        but.pack()
        # Label for showing date on main display
        date = Label(self.root, text="", bg='black', fg='white')
        date.pack(pady=20)

        self.select_names()

        self.username_label = tk.Label(self.root, text="Assign task:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.username_label.place(x=1, y=1)
        self.task_label = tk.Label(self.root, text="Select task:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.task_label.place(x=10, y=350)

        self.button = tk.Button(self.root, text="Demo Button", command=self.callback, font=FONT, bg=DARK_GREY, fg=WHITE)
        self.button.place(x=180, y=550)
        self.username_label.pack(side=tk.LEFT, padx=10)

        self.name_var = tk.StringVar()
        self.name_var.set("Pick a person!")

        self.username_drop = tk.OptionMenu(self.root, self.name_var, *self.person_list)
        self.username_drop.pack()
        self.username_drop.place(x=200, y=455)

        self.clicked = tk.StringVar()
        self.task = tk.Entry(self.root, textvariable=self.clicked, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
        self.task.pack()
        self.task.place(x=200, y=350)
