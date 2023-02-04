import tkinter as tk
import sendemail
import task
from task import Task

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

    def __init__(self, root):
        super().__init__()
        self.email_singleton = sendemail.SingletonEmail()
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=4)
        self.root.grid_rowconfigure(2, weight=1)

        self.options_list = ["Do the laundry", "Fold and put away clean clothes", "Vacuuming, sweeping, dusting",
                             "Wash and put away dishes", "Mop the floor", "Wash the family car", "Feed pet", "Walk pet",
                             "Do homework", "Take children to school", "Take children from school",
                             "Prepare breakfast ", "Prepare lunch", "Prepare dinner", "Clean the bathroom"]

        self.username_label = tk.Label(self.root, text="Assign task:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.username_label.place(x=1, y=1)
        self.task_label = tk.Label(self.root, text="Select task:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.task_label.place(x=10, y=350)

        self.button = tk.Button(self.root, text="Demo Button", command=self.callback, font=FONT, bg=DARK_GREY, fg=WHITE)
        self.button.place(x=180, y=450)
        self.username_label.pack(side=tk.LEFT, padx=10)

        self.name_var = tk.StringVar()
        self.username_textbox = tk.Entry(self.root, textvariable=self.name_var, font=FONT, bg=MEDIUM_GREY, fg=WHITE,
                                         width=23)
        self.username_textbox.pack(side=tk.LEFT)

        self.clicked = tk.StringVar()
        self.clicked.set("Pick a task!")
        self.drop = tk.OptionMenu(self.root, self.clicked, *self.options_list)
        self.drop.pack()
        self.drop.place(x=200, y=350)
