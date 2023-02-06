from tkinter import messagebox
from tkinter.ttk import Treeview, Combobox
from tkinter import *
import mysql.connector
import pandas as pd
import customtkinter

from connected_user import ConnectedUser
from task import Task

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)


class ViewTasksFrame():

    def get_tasks_list(self):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "SELECT * FROM task"
        cursor.execute(query)
        task_list = cursor.fetchall()
        cursor.close()
        conn.close()
        return task_list

    def get_user_by_id(self, user_id):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "SELECT first_name FROM person WHERE PersonID = %s"
        cursor.execute(query, [user_id])
        person_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return person_id

    def get_id_by_user(self, user_name):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "SELECT PersonId FROM person WHERE first_name = %s"
        cursor.execute(query, [user_name])
        person_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return person_id

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=20)

        self.tasks_list = self.get_tasks_list()
        self.tree = Treeview(self.root)

        self.task_id_list = []
        self.assignee_list = []
        self.assignor_list = []
        self.description_list = []
        self.due_date_list = []
        self.is_complete_list = []
        self.responsibility_level = []

        for item in self.tasks_list:
            self.task_id_list.append(str(item[0]))
            self.assignor_list.append(self.get_user_by_id(item[1]))
            self.assignee_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])
            self.responsibility_level.append(item[6])

        global df
        df = pd.DataFrame({"Task id": self.task_id_list,
                           "Assignor": self.assignor_list,
                           "Assignee": self.assignee_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           "Responsibility level": self.responsibility_level,
                           })

        columns = list(df.columns)
        values_list = list(df["Assignee"].unique())
        unique_persons_list = list(df["Assignee"].unique())
        values_list.append("All assignees")

        self.Label1 = customtkinter.CTkLabel(self.root, text="    Select id of task you want to set as completed    ",
                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.Label1.grid(row=0, column=0)
        self.optionmenu_var1 = customtkinter.StringVar(value="Pick an id!")
        self.Combo1 = customtkinter.CTkComboBox(master=self.root, values=self.task_id_list, command=self.select_id,
                                                variable=self.optionmenu_var1, width=260)
        self.Combo1.grid(row=0, column=1)

        self.Label2 = customtkinter.CTkLabel(self.root, text=" Select id of task you want to set as not completed ",
                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.Label2.grid(row=1, column=0)
        self.optionmenu_var2 = customtkinter.StringVar(value="Pick an id!")
        self.Combo2 = customtkinter.CTkComboBox(master=self.root, values=self.task_id_list,
                                                command=self.select_id_invers, variable=self.optionmenu_var2,
                                                width=260)
        self.Combo2.grid(row=1, column=1)

        self.Label3 = customtkinter.CTkLabel(self.root,
                                             text="Id of task for which you want to change assignee",
                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.Label3.grid(row=2, column=0)
        self.optionmenu_var3 = customtkinter.StringVar(value="Pick an id!")
        self.Combo3 = customtkinter.CTkComboBox(master=self.root, values=self.task_id_list,
                                                variable=self.optionmenu_var3,
                                                width=260)
        self.Combo3.grid(row=2, column=1)

        self.Label4 = customtkinter.CTkLabel(self.root,
                                             text="New assignee",
                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.Label4.grid(row=3, column=0)
        self.optionmenu_var4 = customtkinter.StringVar(value="Pick a new assignee!")
        self.Combo4 = customtkinter.CTkComboBox(master=self.root, values=unique_persons_list,
                                                command=self.new_assignee_to_task, variable=self.optionmenu_var4,
                                                width=260)
        self.Combo4.grid(row=3, column=1)

        self.Label = customtkinter.CTkLabel(self.root,
                                            text="                              Filter by:                               ",
                                            compound="left", font=customtkinter.CTkFont(size=15))
        self.Label.grid(row=4, column=0)
        self.optionmenu_var = customtkinter.StringVar(value="Pick an assignee!")
        self.Combo = customtkinter.CTkComboBox(master=self.root, values=values_list,
                                                 command=self.select_assignee, variable=self.optionmenu_var, width=260)
        self.Combo.grid(row=4, column=1)

        self.tree["columns"] = columns
        self.tree.column("Task id", width=7)
        self.tree.column("Assignor", width=7)
        self.tree.column("Assignee", width=7)
        self.tree.column("Description", width=40)
        self.tree.column("Due date", width=7)
        self.tree.column("Is complete", width=1)
        self.tree.column("Responsibility level", width=7)
        self.tree.column("#0", width=2)
        # self.tree.pack(expand=TRUE, fill=BOTH)
        self.tree.grid(row=5, column=0, columnspan=2, sticky=NSEW, rowspan=30)

        for i in columns:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor="w")

        for index, row in df.iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

    def select_assignee(self, event=None):
        if self.Combo.get() == "All assignees":
            self.tree.delete(*self.tree.get_children())
            for index, row in df.iterrows():
                self.tree.insert("", "end", text=index, values=list(row))
        else:
            self.tree.delete(*self.tree.get_children())
            for index, row in df.loc[df["Assignee"].eq(self.Combo.get())].iterrows():
                self.tree.insert("", "end", text=index, values=list(row))

    def select_id(self, event=None):
        id = self.Combo1.get()
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "UPDATE task SET is_Complete = true WHERE id = %s"
        cursor.execute(query, [id])
        conn.commit()
        self.tasks_list.clear()
        self.task_id_list.clear()
        self.assignor_list.clear()
        self.assignee_list.clear()
        self.description_list.clear()
        self.due_date_list.clear()
        self.is_complete_list.clear()
        self.responsibility_level.clear()

        self.tasks_list = self.get_tasks_list()

        for item in self.tasks_list:
            self.task_id_list.append(item[0])
            self.assignor_list.append(self.get_user_by_id(item[1]))
            self.assignee_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])
            self.responsibility_level.append(item[6])

        global df
        df = df[0:0]
        df = pd.DataFrame({"Task id": self.task_id_list,
                           "Assignor": self.assignor_list,
                           "Assignee": self.assignee_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           "Responsibility level": self.responsibility_level
                           })
        cursor.close()
        conn.close()

    def select_id_invers(self, event=None):
        id = self.Combo2.get()
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "UPDATE task SET is_Complete = false WHERE id = %s"
        cursor.execute(query, [id])
        conn.commit()
        self.tasks_list.clear()
        self.task_id_list.clear()
        self.assignor_list.clear()
        self.assignee_list.clear()
        self.description_list.clear()
        self.due_date_list.clear()
        self.is_complete_list.clear()
        self.responsibility_level.clear()

        self.tasks_list = self.get_tasks_list()

        for item in self.tasks_list:
            self.task_id_list.append(item[0])
            self.assignor_list.append(self.get_user_by_id(item[1]))
            self.assignee_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])
            self.responsibility_level.append(item[6])

        global df
        df = df[0:0]
        df = pd.DataFrame({"Task id": self.task_id_list,
                           "Assignor": self.assignor_list,
                           "Assignee": self.assignee_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           "Responsibility level": self.responsibility_level
                           })
        cursor.close()
        conn.close()

    def get_person(self, first_name):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "SELECT * FROM person WHERE first_name = %s"
        cursor.execute(query, [first_name])
        person = cursor.fetchall()
        curr_user = ConnectedUser(person[0][3], person[0][4], person[0][5], person[0][6], person[0][7],
                                  person[0][8], person[0][9])
        cursor.close()
        conn.close()
        return curr_user

    def get_task(self, task_id):
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
        cursor = conn.cursor()
        query = "SELECT * FROM task WHERE id = %s"
        cursor.execute(query, [task_id])
        person = cursor.fetchall()
        curr_task = Task(person[0][1], person[0][2], person[0][3], person[0][4], person[0][5],
                         person[0][6])
        cursor.close()
        conn.close()
        return curr_task

    def check_responbility(self, assignee_person, new_task):
        if assignee_person._instance.can_handle(new_task) == True:
            return True
        else:
            return False

    def new_assignee_to_task(self, event=None):
        assignee_person = self.get_person(event)
        curr_task = self.get_task(self.Combo3.get())
        if self.check_responbility(assignee_person, curr_task) == False:
            messagebox.showwarning("Warning", "Task is not compatible with the person you selected!")
        else:
            task_id = self.Combo3.get()
            person_name = self.Combo4.get()
            person_id = self.get_id_by_user(person_name)
            if task_id != "Pick an id!":
                conn = mysql.connector.connect(host='localhost',
                                               database='logindb',
                                               user='root',
                                               password='1q2w3e')
                cursor = conn.cursor()
                query = "UPDATE task SET assignee = %s WHERE id = %s"
                cursor.execute(query, [person_id, task_id])
                conn.commit()
                self.tasks_list.clear()
                self.task_id_list.clear()
                self.assignor_list.clear()
                self.assignee_list.clear()
                self.description_list.clear()
                self.due_date_list.clear()
                self.is_complete_list.clear()
                self.responsibility_level.clear()

                self.tasks_list = self.get_tasks_list()

                for item in self.tasks_list:
                    self.task_id_list.append(item[0])
                    self.assignor_list.append(self.get_user_by_id(item[1]))
                    self.assignee_list.append(self.get_user_by_id(item[2]))
                    self.description_list.append(item[3])
                    self.due_date_list.append(item[4])
                    self.is_complete_list.append(item[5])
                    self.responsibility_level.append(item[6])

                global df
                df = df[0:0]
                df = pd.DataFrame({"Task id": self.task_id_list,
                                   "Assignor": self.assignor_list,
                                   "Assignee": self.assignee_list,
                                   "Description": self.description_list,
                                   "Due date": self.due_date_list,
                                   "Is complete": self.is_complete_list,
                                   "Responsibility level": self.responsibility_level
                                   })
                cursor.close()
                conn.close()
