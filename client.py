# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 1234

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)
SEMI_BLUE = '#6C5B7B'
DARKER_BLUE = '#355C7D'

# Creating a socket object
# AF_INET: we are going to use IPv4 addresses
# SOCK_STREAM: we are using TCP packets for communication
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Client:
    def __init__(self, root, curr_user):
        super().__init__()
        self.curr_user = curr_user
        self.root = root
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=4)
        self.root.grid_rowconfigure(2, weight=1)

        self.top_frame = tk.Frame(self.root, width=600, height=100, bg=DARK_GREY)
        self.top_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.middle_frame = tk.Frame(self.root, width=600, height=400, bg=MEDIUM_GREY)
        self.middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.bottom_frame = tk.Frame(self.root, width=600, height=100, bg=DARK_GREY)
        self.bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

        self.username_label = tk.Label(self.top_frame, text="Logged as:", font=FONT, bg=DARK_GREY, fg=WHITE)
        self.username_label.pack(side=tk.LEFT, padx=10)

        self.username_textbox = tk.Label(self.top_frame, text=curr_user._instance.first_name, font=FONT, bg=DARK_GREY,
                                         fg=WHITE)
        self.username_textbox.pack(side=tk.LEFT)

        self.username_button = tk.Button(self.top_frame, text="Join", font=BUTTON_FONT, fg=DARKER_BLUE,
                                         command=self.connect)
        self.username_button.pack(side=tk.LEFT, padx=15)

        self.message_textbox = tk.Entry(self.bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=38)
        self.message_textbox.pack(side=tk.LEFT, padx=10)

        self.message_button = tk.Button(self.bottom_frame, text="Send", font=BUTTON_FONT, fg=DARKER_BLUE,
                                        command=self.send_message)
        self.message_button.pack(side=tk.LEFT, padx=10)

        self.message_box = scrolledtext.ScrolledText(self.middle_frame, font=SMALL_FONT, bg=MEDIUM_GREY, fg=WHITE,
                                                     width=67,
                                                     height=26.5)
        self.message_box.config(state=tk.DISABLED)
        self.message_box.pack(side=tk.TOP)

    def add_message(self, message):
        self.message_box.config(state=tk.NORMAL)
        self.message_box.insert(tk.END, message + '\n')
        self.message_box.config(state=tk.DISABLED)

    def connect(self):

        # try except block
        try:

            # Connect to the server
            clientSocket.connect((HOST, PORT))
            print("Successfully connected to server")
            self.add_message("[SERVER] Successfully connected to the server")
        except:
            messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

        username = self.username_textbox.cget("text")
        if username != '':
            clientSocket.sendall(username.encode())
        else:
            messagebox.showerror("Invalid username", "Username cannot be empty")

        threading.Thread(target=self.listen_for_messages_from_server, args=(clientSocket,)).start()

        self.username_textbox.config(state=tk.DISABLED)
        self.username_button.config(state=tk.DISABLED)

    def send_message(self):
        message = self.message_textbox.get()
        if message != '':
            clientSocket.sendall(message.encode())
            self.message_textbox.delete(0, len(message))
        else:
            messagebox.showerror("Empty message", "Message cannot be empty")

    def listen_for_messages_from_server(self, clientSocket):

        while 1:

            message = clientSocket.recv(2048).decode('utf-8')
            if message != '':
                self.username = message.split("~")[0]
                self.content = message.split('~')[1]

                self.add_message(f"[{self.username}] {self.content}")

            else:
                messagebox.showerror("Error", "Message recevied from client is empty")
