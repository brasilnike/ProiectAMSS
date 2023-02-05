from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error
import customtkinter

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)
SEMI_BLUE = '#6C5B7B'
DARKER_BLUE = '#355C7D'

responsibilities_list = ["Parent", "Parent without driving license", "Over 18 with driving license",
                         "Over 18 without driving license", "Kid"]


def register_page(root):
    root_register = Toplevel(root)
    root_register.config(bg=MEDIUM_GREY)
    root_register.title("Register page")

    width = 640
    height = 600
    screen_width = root_register.winfo_screenwidth()
    screen_height = root_register.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root_register.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root_register.resizable(0, 0)

    # =======================================VARIABLES=====================================
    USER = StringVar()
    PASS = StringVar()
    FIRST_NAME = StringVar()
    LAST_NAME = StringVar()
    AGE = StringVar()
    EMAIL = StringVar()
    PHONE_NUMBER = StringVar()
    GENDER = StringVar()
    RESPONSABILITIES = StringVar(value="Pick a responsibility level!")

    # =======================================METHODS=======================================
    def Database():
        global conn, cursor
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='admin')
        cursor = conn.cursor()

    def Exit():
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root_register.destroy()
            exit()

    def Register():
        Database()
        if USER.get() == "" or PASS.get() == "" or FIRST_NAME.get() == "" or LAST_NAME.get() == "" or AGE.get() == "" or EMAIL.get() == "" or PHONE_NUMBER.get() == "" or GENDER.get() == "" or RESPONSABILITIES.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `person` WHERE `username` = %s", [USER.get()])
            if cursor.fetchone() is not None:
                lbl_result.config(text="Username is already taken", fg="red")
            else:
                cursor.execute(
                    "INSERT INTO `person` (username, user_password, first_name, last_name, age, email, phone_number, gender, responsibilities) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (str(USER.get()), str(PASS.get()), str(FIRST_NAME.get()), str(LAST_NAME.get()), str(AGE.get()),
                     str(EMAIL.get()), str(PHONE_NUMBER.get()), str(GENDER.get()), str(RESPONSABILITIES.get())))
                conn.commit()
                USER.set("")
                PASS.set("")
                FIRST_NAME.set("")
                LAST_NAME.set("")
                AGE.set("")
                EMAIL.set("")
                PHONE_NUMBER.set("")
                GENDER.set("")
                RESPONSABILITIES.set("")
                lbl_result.config(text="Successfully Created!", fg="green")
            cursor.close()
            conn.close()

    # =====================================FRAMES====================================
    TitleFrame = Frame(root_register, height=100, width=640, bd=0, relief=SOLID)
    TitleFrame.pack(side=TOP)
    RegisterFrame = Frame(root_register)
    RegisterFrame.pack(side=TOP, pady=20)
    RegisterFrame.config(bg=MEDIUM_GREY)

    # =====================================LABEL WIDGETS=============================
    lbl_title = customtkinter.CTkLabel(TitleFrame, text="Please enter your details", compound="left",
                                       font=customtkinter.CTkFont(size=50), bg_color=MEDIUM_GREY)
    lbl_title.pack()
    lbl_username = customtkinter.CTkLabel(RegisterFrame, text="Username:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_username.grid(row=1)
    lbl_password = customtkinter.CTkLabel(RegisterFrame, text="Password:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_password.grid(row=2)
    lbl_firstname = customtkinter.CTkLabel(RegisterFrame, text="First name:", compound="left",
                                           font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_firstname.grid(row=3)
    lbl_lastname = customtkinter.CTkLabel(RegisterFrame, text="Last name:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_lastname.grid(row=4)
    lbl_lastname = customtkinter.CTkLabel(RegisterFrame, text="Age:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_lastname.grid(row=5)
    lbl_lastname = customtkinter.CTkLabel(RegisterFrame, text="Email:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_lastname.grid(row=6)
    lbl_lastname = customtkinter.CTkLabel(RegisterFrame, text="Phone number:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_lastname.grid(row=7)
    lbl_lastname = customtkinter.CTkLabel(RegisterFrame, text="Gender:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_lastname.grid(row=8)
    lbl_lastname = customtkinter.CTkLabel(RegisterFrame, text="Responsibilities:", compound="left",
                                          font=customtkinter.CTkFont(size=30), bg_color=MEDIUM_GREY)
    lbl_lastname.grid(row=9)
    lbl_result = Label(RegisterFrame, text="", compound="left", font=customtkinter.CTkFont(size=30), bg=MEDIUM_GREY)
    lbl_result.grid(row=10, columnspan=2)

    # =======================================ENTRY WIDGETS===========================
    user = Entry(RegisterFrame, textvariable=USER, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    user.grid(row=1, column=1)
    pass1 = Entry(RegisterFrame, textvariable=PASS, show="*", font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    pass1.grid(row=2, column=1)
    first_name = Entry(RegisterFrame, textvariable=FIRST_NAME, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    first_name.grid(row=3, column=1)
    last_name = Entry(RegisterFrame, textvariable=LAST_NAME, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    last_name.grid(row=4, column=1)
    age = Entry(RegisterFrame, textvariable=AGE, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    age.grid(row=5, column=1)
    email = Entry(RegisterFrame, textvariable=EMAIL, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    email.grid(row=6, column=1)
    phone_no = Entry(RegisterFrame, textvariable=PHONE_NUMBER, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    phone_no.grid(row=7, column=1)
    gender = Entry(RegisterFrame, textvariable=GENDER, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    gender.grid(row=8, column=1)
    responsibilities = customtkinter.CTkOptionMenu(master=RegisterFrame,
                                                   values=responsibilities_list,
                                                   variable=RESPONSABILITIES)
    responsibilities.grid(row=9, column=1)
    # ========================================BUTTON WIDGETS=========================
    btn_register = Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
    btn_register.grid(row=11, columnspan=2)
    # ========================================MENUBAR WIDGETS==================================
    menubar = Menu(root_register)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=Exit)
    root_register.config(menu=menubar)
    root_register.mainloop()
