from tkinter import *
import tkinter.messagebox
import mysql.connector
import main_page
import register
from mysql.connector import Error
from parent import Parent
from kid import Kid
from connected_user import ConnectedUser

# connecting to the database
connectiondb = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
cursordb = connectiondb.cursor()

curr_user = None


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Account Details', bd=5, font=('arial', 12, 'bold'), relief="groove",
          fg="white",
          bg="blue", width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=login_verification).pack()
    Label(root2, text="")


def logged_destroy():
    logged_message.destroy()
    root2.destroy()
    root.destroy()
    global curr_user
    app = main_page.App(curr_user)
    app.mainloop()


def register_function():
    register.register_page(root)


def failed_destroy():
    failed_message.destroy()


def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green",
          font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Proceed to app", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=logged_destroy).pack()


def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from person where username = %s and user_password = %s"
    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()

    if results:
        for i in results:
            logged()
            break
        global curr_user
        curr_user = ConnectedUser(results[0][2], results[0][3], results[0][4], results[0][5], results[0][6],
                                  results[0][7], results[0][8])
    else:
        failed()


def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    Label(root, text='Welcome to Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
          bg="blue", width=300).pack()
    Label(root, text="").pack()
    Button(root, text='Log In', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=login).pack()
    Label(root, text="").pack()
    Button(root, text='Register', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=register_function).pack()
    Label(root, text="").pack()
    Button(root, text='Exit', height="1", width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
           bg="blue", command=Exit).pack()
    Label(root, text="").pack()


if __name__ == "__main__":
    main_display()
    root.mainloop()
