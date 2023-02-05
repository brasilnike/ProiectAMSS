from tkinter.ttk import Treeview, Combobox
from tkinter import *
import mysql.connector
import pandas as pd


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

        self.assignee_list = []
        self.assignor_list = []
        self.description_list = []
        self.due_date_list = []
        self.is_complete_list = []

        for item in self.tasks_list:
            self.assignee_list.append(self.get_user_by_id(item[1]))
            self.assignor_list.append(self.get_user_by_id(item[2]))
            self.description_list.append(item[3])
            self.due_date_list.append(item[4])
            self.is_complete_list.append(item[5])

        global df
        df = pd.DataFrame({"Assignor": self.assignee_list,
                           "Assignee": self.assignor_list,
                           "Description": self.description_list,
                           "Due date": self.due_date_list,
                           "Is complete": self.is_complete_list,
                           })

        columns = list(df.columns)
        values_list = list(df["Assignee"].unique())
        values_list.append("All assignees")
        self.Combo = Combobox(self.root, values=values_list, state="readonly")
        self.Combo.pack()
        self.Combo.bind("<<ComboboxSelected>>", self.select_assignee)
        self.tree["columns"] = columns
        self.tree.column("Assignor", width=7)
        self.tree.column("Assignee", width=7)
        self.tree.column("Description", width=40)
        self.tree.column("Due date", width=7)
        self.tree.column("Is complete", width=7)
        self.tree.column("#0", width=2)
        self.tree.pack(expand=TRUE, fill=BOTH)

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

        # assignor_text = Label(self.root, text="Assignor", bg='black', fg='white', font=("Arial", 15))
        # assignor_text.grid(row=0, column=0, sticky=NSEW)
        # assignee_text = Label(self.root, text="Assignee", bg='black', fg='white', font=("Arial", 15))
        # assignee_text.grid(row=0, column=1,sticky=NSEW)
        # task_description_text = Label(self.root, text="Task description", bg='black', fg='white', font=("Arial", 15))
        # task_description_text.grid(row=0, column=2, sticky=NSEW)
        # due_date_text = Label(self.root, text="Due date", bg='black', fg='white', font=("Arial", 15))
        # due_date_text.grid(row=0, column=3, sticky=NSEW)
        # is_complete_text = Label(self.root, text="Is complete", bg='black', fg='white', font=("Arial", 15))
        # is_complete_text.grid(row=0, column=4, sticky=NSEW)
        #
        # counter = 1
        # for item in self.tasks_list:
        #     assignor = self.get_user_by_id(item[1])
        #     assignee = self.get_user_by_id(item[2])
        #     task_description = item[3]
        #     due_date = item[4]
        #     is_complete = item[5]
        #     assignor_label = Label(self.root, text=assignor, bg='gray', fg='white', font=("Arial", 15))
        #     assignor_label.grid(row=counter, column=0, sticky=NSEW)
        #     assignee_label = Label(self.root, text=assignee, bg='gray', fg='white', font=("Arial", 15))
        #     assignee_label.grid(row=counter, column=1, sticky=NSEW)
        #     task_description_label = Label(self.root, text=task_description, bg='gray', fg='white', font=("Arial", 15))
        #     task_description_label.grid(row=counter, column=2, sticky=NSEW)
        #     due_date_label = Label(self.root, text=due_date, bg='gray', fg='white', font=("Arial", 15))
        #     due_date_label.grid(row=counter, column=3, sticky=NSEW)
        #     is_complete_label = Label(self.root, text=is_complete, bg='gray', fg='white', font=("Arial", 15))
        #     is_complete_label.grid(row=counter, column=4, sticky=NSEW)
        #     counter += 1
