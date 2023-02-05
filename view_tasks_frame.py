from tkinter.ttk import Treeview, Combobox
from tkinter import *
import mysql.connector
import pandas as pd

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
                                       password='admin')
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
                                       password='admin')
        cursor = conn.cursor()
        query = "SELECT first_name FROM person WHERE PersonID = %s"
        cursor.execute(query, [user_id])
        person_id = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return person_id

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.tasks_list = self.get_tasks_list()
        self.tree = Treeview(self.root)

        self.task_id_list = []
        self.assignee_list = []
        self.assignor_list = []
        self.description_list = []
        self.due_date_list = []
        self.is_complete_list = []

        for item in self.tasks_list:
            self.task_id_list.append(item[0])
            self.assignor_list.append(self.get_user_by_id(item[1]))
            self.assignee_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])

        global df
        df = pd.DataFrame({"Task id": self.task_id_list,
                           "Assignor": self.assignor_list,
                           "Assignee": self.assignee_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           })

        columns = list(df.columns)
        values_list = list(df["Assignee"].unique())
        values_list.append("All assignees")

        self.Label1 = Label(self.root, text="   Select id of task you want to set as completed   ", bg='black',
                            fg='white',
                            font=SMALL_FONT)
        self.Label1.grid(row=0, column=0)
        self.Combo1 = Combobox(self.root, values=self.task_id_list, state="readonly", font=SMALL_FONT, width=24)
        self.Combo1.grid(row=0, column=1)
        self.Combo1.bind("<<ComboboxSelected>>", self.select_id)

        self.Label2 = Label(self.root, text="Select id of task you want to set as not completed", bg='black',
                            fg='white', font=SMALL_FONT)
        self.Label2.grid(row=1, column=0)
        self.Combo2 = Combobox(self.root, values=self.task_id_list, state="readonly", font=SMALL_FONT, width=24)
        self.Combo2.grid(row=1, column=1)
        self.Combo2.bind("<<ComboboxSelected>>", self.select_id_invers)

        self.Label = Label(self.root, text="                             Filter by:                              ",
                           bg='black', fg='white', font=SMALL_FONT)
        self.Label.grid(row=2, column=0)
        self.Combo = Combobox(self.root, values=values_list, state="readonly", font=SMALL_FONT, width=24)
        self.Combo.grid(row=2, column=1)
        self.Combo.bind("<<ComboboxSelected>>", self.select_assignee)

        self.tree["columns"] = columns
        self.tree.column("Task id", width=7)
        self.tree.column("Assignor", width=7)
        self.tree.column("Assignee", width=7)
        self.tree.column("Description", width=40)
        self.tree.column("Due date", width=7)
        self.tree.column("Is complete", width=7)
        self.tree.column("#0", width=2)
        # self.tree.pack(expand=TRUE, fill=BOTH)
        self.tree.grid(row=3, column=0, columnspan=2, sticky=NSEW)

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
                                       password='admin')
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

        self.tasks_list = self.get_tasks_list()

        for item in self.tasks_list:
            self.task_id_list.append(item[0])
            self.assignor_list.append(self.get_user_by_id(item[1]))
            self.assignee_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])

        global df
        df = df[0:0]
        df = pd.DataFrame({"Task id": self.task_id_list,
                           "Assignor": self.assignor_list,
                           "Assignee": self.assignee_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           })
        cursor.close()
        conn.close()

    def select_id_invers(self, event=None):
        id = self.Combo2.get()
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='admin')
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

        self.tasks_list = self.get_tasks_list()

        for item in self.tasks_list:
            self.task_id_list.append(item[0])
            self.assignor_list.append(self.get_user_by_id(item[1]))
            self.assignee_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])

        global df
        df = df[0:0]
        df = pd.DataFrame({"Task id": self.task_id_list,
                           "Assignor": self.assignor_list,
                           "Assignee": self.assignee_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           })
        cursor.close()
        conn.close()
