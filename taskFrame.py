import tkinter as tk

import customtkinter

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
SEMI_BLUE = '#6C5B7B'
DARKER_BLUE = '#355C7D'

class TaskFrame():
    def callback(self):
        new_task = Task.create_task(self.get_person_id(self.curr_user._instance.first_name), self.get_person_id(self.optionmenu_var.get()), self.clicked.get(), datetime.strptime(self.tkc.get_date(), "%m/%d/%y").strftime("%Y-%m-%d"), False, self.resp_var.get())
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
            date.configure(text="Selected Date is: " + datetime.strptime(self.tkc.get_date(), "%m/%d/%y").strftime("%Y-%m-%d"))

        def optionmenu_callback(choice):
            return choice

        login_button = customtkinter.CTkButton(self.root, corner_radius=10,
                                               text="   Select Date",
                                               font=customtkinter.CTkFont(size=15, weight="bold"),
                                               fg_color="transparent", text_color=("gray10", "gray90"),
                                               hover_color=("gray70", "gray30"),
                                               anchor="w", command=fetch_date)
        login_button.pack()
        # but = Button(self.root, text="Select Date", command=fetch_date, fg=DARKER_BLUE)
        # but.pack()
        date = customtkinter.CTkLabel(self.root, text="Date selected:",
                                                compound="left",
                                                font=customtkinter.CTkFont(size=15))
        date.pack(pady=20)

        self.username_label = customtkinter.CTkLabel(self.root, text="Select person:",
                                                compound="left",
                                                font=customtkinter.CTkFont(size=15))
        self.username_label.place(x=10, y=400)

        self.task_label = customtkinter.CTkLabel(self.root, text="Assign task:",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=15))
        self.task_label.place(x=10, y=300)

        self.resp_label = customtkinter.CTkLabel(self.root, text="Select responsibility:",
                                                 compound="left",
                                                 font=customtkinter.CTkFont(size=15))
        self.resp_label.place(x=10, y=500)

        self.button = customtkinter.CTkButton(self.root, corner_radius=10, border_spacing=10,
                                               text="Add task!",
                                               font=customtkinter.CTkFont(size=25, weight="bold"),
                                               fg_color="transparent", text_color=("gray10", "gray90"),
                                               hover_color=("gray70", "gray30"),
                                               anchor="w", command=self.callback)
        self.button.place(x=250, y=600)

        self.optionmenu_var = customtkinter.StringVar(value="Pick a person!")  # set initial value

        self.username_drop = customtkinter.CTkOptionMenu(master=self.root,
                                               values=self.person_list,
                                               command=optionmenu_callback,
                                               variable=self.optionmenu_var)

        self.username_drop.pack()
        self.username_drop.place(x=250, y=400)

        self.resp_var = customtkinter.StringVar(value="Pick responsibility!")  # set initial value

        self.resp_drop = customtkinter.CTkOptionMenu(master=self.root,
                                                         values=self.responsibilities_list,
                                                         command=optionmenu_callback,
                                                         variable=self.resp_var)

        #self.resp_drop = tk.OptionMenu(self.root, self.resp_var, *self.responsibilities_list)
        self.resp_drop.pack()
        self.resp_drop.place(x=250, y=500)

        self.clicked = tk.StringVar()
        self.task = tk.Entry(self.root, textvariable=self.clicked, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
        self.task.pack()
        self.task.place(x=250, y=300)
