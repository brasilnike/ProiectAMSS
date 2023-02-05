import customtkinter
import os
from PIL import Image

import client
import taskFrame
import journal_frame
import view_tasks_frame


class App(customtkinter.CTk):
    def __init__(self, curr_user):
        self.curr_user = curr_user
        super().__init__()

        self.title("Home management platform.py")
        self.geometry("900x680")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "theme_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")),
                                                 size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")),
                                                       size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                                       size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")),
                                                 size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")),
                                                 size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
            dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Home management platform",
                                                             image=self.logo_image,
                                                             compound="left",
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Your Details",
                                                   fg_color="transparent", text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Family chat",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w",
                                                      command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Create task",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      image=self.add_user_image, anchor="w",
                                                      command=self.frame_3_button_event)

        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.view_tasks_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                         border_spacing=10, text="View tasks",
                                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         anchor="w",
                                                         command=self.view_tasks_button_event)

        self.view_tasks_button.grid(row=4, column=0, sticky="ew")

        self.journal_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                                      border_spacing=10, text="Journal",
                                                      fg_color="transparent", text_color=("gray10", "gray90"),
                                                      hover_color=("gray70", "gray30"),
                                                      anchor="w",
                                                      command=self.journal_button_event)

        self.journal_button.grid(row=5, column=0, sticky="ew")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="",
                                                                   image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.label0 = customtkinter.CTkLabel(self.home_frame, text="First name:",
                                             font=("Arial", 20))
        self.label0.grid(row=1, column=0, padx=20, pady=10)

        self.label1 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.first_name,
                                             font=("Arial", 20))
        self.label1.grid(row=1, column=1, padx=20, pady=10)

        self.label2 = customtkinter.CTkLabel(self.home_frame, text="Last name:",
                                             font=("Arial", 20))
        self.label2.grid(row=2, column=0, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.last_name,
                                             font=("Arial", 20))
        self.label3.grid(row=2, column=1, padx=20, pady=10)

        self.label4 = customtkinter.CTkLabel(self.home_frame, text="Age:",
                                             font=("Arial", 20))
        self.label4.grid(row=3, column=0, padx=20, pady=10)

        self.label5 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.age,
                                             font=("Arial", 20))
        self.label5.grid(row=3, column=1, padx=20, pady=10)

        self.label6 = customtkinter.CTkLabel(self.home_frame, text="Email:",
                                             font=("Arial", 20))
        self.label6.grid(row=4, column=0, padx=20, pady=10)

        self.label7 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.email,
                                             font=("Arial", 20))
        self.label7.grid(row=4, column=1, padx=20, pady=10)

        self.label8 = customtkinter.CTkLabel(self.home_frame, text="Phone number:",
                                             font=("Arial", 20))
        self.label8.grid(row=5, column=0, padx=20, pady=10)

        self.label9 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.phone_number,
                                             font=("Arial", 20))
        self.label9.grid(row=5, column=1, padx=20, pady=10)

        self.label10 = customtkinter.CTkLabel(self.home_frame, text="Gender:",
                                              font=("Arial", 20))
        self.label10.grid(row=6, column=0, padx=20, pady=10)

        self.label11 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.gender,
                                              font=("Arial", 20))
        self.label11.grid(row=6, column=1, padx=20, pady=10)

        self.label12 = customtkinter.CTkLabel(self.home_frame, text="Responsibilities:",
                                              font=("Arial", 20))
        self.label12.grid(row=7, column=0, padx=20, pady=10)

        self.label13 = customtkinter.CTkLabel(self.home_frame, text=self.curr_user._instance.responsibilities,
                                              font=("Arial", 20))
        self.label13.grid(row=7, column=1, padx=20, pady=10)
        # self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        # self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
        #                                                    image=self.image_icon_image, compound="right")
        # self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
        #                                                    image=self.image_icon_image, compound="top")
        # self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        # self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton",
        #                                                    image=self.image_icon_image, compound="bottom", anchor="w")
        # self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        client.Client(self.second_frame, self.curr_user)
        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        taskFrame.TaskFrame(self.third_frame, self.curr_user)
        self.journal_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        journal_frame.JournalFrame(self.journal_frame, self.curr_user)
        self.view_tasks_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        view_tasks_frame.ViewTasksFrame(self.view_tasks_frame)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.journal_button.configure(fg_color=("gray75", "gray25") if name == "journal_frame" else "transparent")
        self.view_tasks_button.configure(fg_color=("gray75", "gray25") if name == "view_tasks" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()
        if name == "journal_frame":
            self.journal_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.journal_frame.grid_forget()
        if name == "view_tasks":
            self.view_tasks_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.view_tasks_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def journal_button_event(self):
        self.select_frame_by_name("journal_frame")

    def view_tasks_button_event(self):
        self.select_frame_by_name("view_tasks")
