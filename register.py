from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error

responsibilities_list = ["Parent", "Parent without driving license", "Over 18 with driving license",
                         "Over 18 without driving license", "Kid"]


def register_page(root):
    root_register = Toplevel(root)
    root_register.title("Python - Basic Register Form")

    width = 640
    height = 800
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
    RESPONSABILITIES = StringVar()

    # =======================================METHODS=======================================
    def Database():
        global conn, cursor
        conn = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
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
            cursor.execute("SELECT * FROM `usertable` WHERE `username` = %s", [USER.get()])
            if cursor.fetchone() is not None:
                lbl_result.config(text="Username is already taken", fg="red")
            else:
                cursor.execute(
                    "INSERT INTO `usertable` (username, pass_user, first_name, last_name, age, email, phone_number, gender, responsibilities) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
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
    TitleFrame = Frame(root_register, height=100, width=640, bd=1, relief=SOLID)
    TitleFrame.pack(side=TOP)
    RegisterFrame = Frame(root_register)
    RegisterFrame.pack(side=TOP, pady=20)

    # =====================================LABEL WIDGETS=============================
    lbl_title = Label(TitleFrame, text="Please enter your details", font=('arial', 18), bd=1, width=640)
    lbl_title.pack()
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="First name:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Last name:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_lastname = Label(RegisterFrame, text="Age:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=5)
    lbl_lastname = Label(RegisterFrame, text="Email:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=6)
    lbl_lastname = Label(RegisterFrame, text="Phone number:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=7)
    lbl_lastname = Label(RegisterFrame, text="Gender:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=8)
    lbl_lastname = Label(RegisterFrame, text="Responsibilities:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=9)
    lbl_result = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result.grid(row=10, columnspan=2)

    # =======================================ENTRY WIDGETS===========================
    user = Entry(RegisterFrame, font=('arial', 20), textvariable=USER, width=15)
    user.grid(row=1, column=1)
    pass1 = Entry(RegisterFrame, font=('arial', 20), textvariable=PASS, width=15, show="*")
    pass1.grid(row=2, column=1)
    first_name = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRST_NAME, width=15)
    first_name.grid(row=3, column=1)
    last_name = Entry(RegisterFrame, font=('arial', 20), textvariable=LAST_NAME, width=15)
    last_name.grid(row=4, column=1)
    age = Entry(RegisterFrame, font=('arial', 20), textvariable=AGE, width=15)
    age.grid(row=5, column=1)
    email = Entry(RegisterFrame, font=('arial', 20), textvariable=EMAIL, width=15)
    email.grid(row=6, column=1)
    phone_no = Entry(RegisterFrame, font=('arial', 20), textvariable=PHONE_NUMBER, width=15)
    phone_no.grid(row=7, column=1)
    gender = Entry(RegisterFrame, font=('arial', 20), textvariable=GENDER, width=15)
    gender.grid(row=8, column=1)
    responsibilities = OptionMenu(RegisterFrame, RESPONSABILITIES, *responsibilities_list)
    responsibilities.grid(row=9, column=1)
    # ========================================BUTTON WIDGETS=========================
    btn_register = Button(RegisterFrame, font=('arial', 20), text="Register", command=Register)
    btn_register.grid(row=11, columnspan=2)
    # ========================================MENUBAR WIDGETS==================================
    menubar = Menu(root_register)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", menu=filemenu)
    root_register.config(menu=menubar)
    root_register.mainloop()
