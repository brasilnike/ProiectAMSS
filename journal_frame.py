import tkinter as tk
import customtkinter
from tkinter import *
import mysql.connector
from tkcalendar import Calendar

DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)

my_connect = mysql.connector.connect(host='localhost',
                                     database='amss',
                                     user='user',
                                     password='Password1!')
# ###### end of connection ######
my_conn = my_connect.cursor()


def update_desc(personid,title,new_desc):

    my_conn.execute("UPDATE Journal SET description='"+new_desc+"' where title='"+title+"'")
    print("New desc is"+new_desc)
    my_connect.commit()
def add_journal(personid,title,desc):
    print("title and desc of added journal")
    print(title,desc)
    my_conn.execute("INSERT INTO Journal (person_id,title,description) VALUES ("+str(personid[0])+" , ' "+title + "','"+desc+"');")
    
    my_connect.commit()
    

def popup(self,root,curr_user,title,desc):
        popup=Toplevel()
        popup.configure(bg="#242424")
        
        button=customtkinter.CTkButton(popup, corner_radius=0, height=80, border_spacing=10,
                                                    text=title,
                                                    font=("Arial",30),width=350,
                                                     text_color=("gray10", "gray90"),
                                                    
                                                    fg_color="#242424"
                                                    )
        button.pack()
        description=tk.Entry(popup,bg="#242424",width=100,fg="white")
        description.insert(0,desc)
      #  print("desc")
        description.pack(padx=20,pady=20)
       # print(description.get())
        update_button=customtkinter.CTkButton(popup, corner_radius=0, height=80, border_spacing=10,
                                                    text="Update description",
                                                    font=("Arial",20),width=150,
                                                     text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    fg_color="#242424",
                                                    command=lambda:update_desc(title,description.get()))
        update_button.pack()
        #print("popup")
        #print(title) 
        popup.mainloop()
def add_journal_popup(self,root,curr_user,personid):
        popup=Toplevel()
        popup.configure(bg="#242424")
        
        tk.Label(popup, text="Title",padx=10,pady=10,bg="#242424",fg="white").grid(row=0)
        tk.Label(popup, text="Description",padx=10,pady=10,bg="#242424",fg="white").grid(row=1)
        
        e1 = tk.Entry(popup)
        e2 = tk.Entry(popup)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        #
        addbutton =tk.Button(popup, text ="Add journal entry",bg="black",fg="white",command=lambda:add_journal(personid,e1.get(),e2.get())).grid(row=2,column=1)
        popup.mainloop()
   
class JournalFrame():
    
    def __init__(self, root, curr_user):
        super().__init__()
        self.root = root
        #print(curr_user._instance.first_name)
        
        
       
        my_conn.execute("SELECT PersonID from Person where first_name='"+curr_user._instance.first_name+"'")
        personid=my_conn.fetchone()
        my_conn.execute("SELECT COUNT(*) from Journal where person_id="+str(personid[0]))
        row_count=my_conn.fetchone()
       # print("Row count")
        row_count=row_count[0]
        #print(row_count)
        #print("--------")
        #print(personid[0])
        my_conn.execute("SELECT title,description from Journal WHERE person_id="+str(personid[0]))
        buttons=[]
        title=[]
        desc=[]
        addbutton =tk.Button(self.root, text ="Add journal entry",bg="black",fg="white",command=lambda:add_journal_popup(self,root,curr_user,personid))

        for i in range(row_count):
            
            entry=my_conn.fetchone()
            title.append(entry[0])
            desc.append(entry[1])
         #   print(title)
            def action(text=title[i],desctext=desc[i]):
                return popup(self,root,curr_user,text,desctext)
            buttonaux=customtkinter.CTkButton(self.root, corner_radius=0, height=40, border_spacing=10,
                                                    text=title[i],
                                                    fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),command=action) 
                                                    
          #  print("buttonaux cget"+buttonaux.cget("text"))
            buttons.append( buttonaux)
                                                    
            buttons[i].grid(row=i)
        buttons.append(addbutton)
        buttons[row_count].grid(row=row_count+1,column=0)
        #print(title)
       
           
        
    
