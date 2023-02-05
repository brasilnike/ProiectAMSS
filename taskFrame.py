import tkinter as tk

import sendemail
import task
from task import Task
from tkinter import *
from tkcalendar import Calendar
import mysql.connector
from datetime import datetime
import json

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

class TaskFrame():
    def callback(self):
        new_task = Task.create_task(self.get_person_id(self.curr_user._instance.first_name), self.get_person_id(self.name_var.get()), self.clicked.get(), datetime.strptime(self.tkc.get_date(), "%m/%d/%y").strftime("%Y-%m-%d"), False, self.resp_var.get())
        email_text = "You have a new task from: " + self.curr_user._instance.first_name + '. ' + "Task description: " + new_task.description + ". " + "Due date: " + new_task.due_date + ". " + "Level of responsibility: " + new_task.level_of_responsibility + "."
        self.email_singleton.send_email(self.get_person_email(new_task.assignee), email_text)

    def get_person_id(self, first_name):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='admin')
        cursor = conn.cursor()
        query = "SELECT PersonID FROM person WHERE first_name = %s"
        cursor.execute(query, [first_name])
        person_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return person_id

    def get_person_email(self, person_id):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='admin')
        cursor = conn.cursor()
        query = "SELECT email FROM Person WHERE PersonID = %s"
        cursor.execute(query, [person_id])
        email = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return email

    def select_names(self):
        # Connect to the database
        cnx = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='admin')
        cursor = cnx.cursor()

        # Select all names from the Persons table
        query = "SELECT first_name FROM person"
        cursor.execute(query)
        names = cursor.fetchall()
        names_list = []
        for name in names:
            names_list.append(name[0])
        cursor.close()
        cnx.close()
        return names_list

    def __init__(self, root, curr_user):
        super().__init__()
        self.email_singleton = sendemail.SingletonEmail()
        self.root = root
        self.curr_user = curr_user
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

        self.options_list = ["Do the laundry", "Fold and put away clean clothes", "Vacuuming, sweeping, dusting",
                             "Wash and put away dishes", "Mop the floor", "Wash the family car", "Feed pet", "Walk pet",
                             "Do homework", "Take children to school", "Take children from school",
                             "Prepare breakfast ", "Prepare lunch", "Prepare dinner", "Clean the bathroom"]

        self.person_list = self.select_names()
        self.responsibilities_list = ["Parent", "Parent without driving license", "Over 18 with driving license",
                         "Over 18 without driving license", "Kid"]
        self.tkc = Calendar(self.root, selectmode="day", year=2023, month=1, date=1)
        self.tkc.pack(pady=10)
        def fetch_date():
            date.config(text="Selected Date is: " + datetime.strptime(self.tkc.get_date(), "%m/%d/%y").strftime("%Y-%m-%d"))

        but = Button(self.root, text="Select Date", command=fetch_date, bg="black", fg='white')
        but.pack()
        date = Label(self.root, text="", bg='black', fg='white')
        date.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Select person:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.username_label.place(x=10, y=400)
        self.task_label = tk.Label(self.root, text="Assign task:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.task_label.place(x=10, y=300)
        self.resp_label = tk.Label(self.root, text="Select responsibility:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.resp_label.place(x=10, y=500)

        self.button = tk.Button(self.root, text="Demo Button", command=self.callback, font=FONT, bg=DARK_GREY, fg=WHITE)
        self.button.place(x=180, y=600)

        self.name_var = tk.StringVar()
        self.name_var.set("Pick a person!")

        self.username_drop = tk.OptionMenu(self.root, self.name_var, *self.person_list)
        self.username_drop.pack()
        self.username_drop.place(x=250, y=400)

        self.resp_var = tk.StringVar()
        self.resp_var.set("Pick responsibility!")

        self.resp_drop = tk.OptionMenu(self.root, self.resp_var, *self.responsibilities_list)
        self.resp_drop.pack()
        self.resp_drop.place(x=250, y=500)

        self.clicked = tk.StringVar()
        self.task = tk.Entry(self.root, textvariable=self.clicked, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
        self.task.pack()
        self.task.place(x=250, y=300)
