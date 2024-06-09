import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect("mydatabase.db")
cur = conn.cursor()
cur.execute("""

    CREATE TABLE IF NOT EXISTS customers (

        id INTEGER PRIMARY KEY,

        name TEXT,

        email TEXT,

        phone TEXT

    )

""")






def enter_data():
    firstname= first_name_entry.get()
    middlename= middle_name_entry.get()
    lastname= last_name_entry.get()
    age=age_spinbox.get()
    gender= gender_combobox.get()
    fathersname= fathersname_entry.get()
    mothersname= mothersname_entry.get()

    print("First Name: ",firstname, 'Middle Name: ',middlename,"Last Name:",lastname)
    print("Age: ",age,"Gender: ",gender)
    print("Father's Name:",fathersname,"Mother's Name: ", mothersname)
    print("---------------------------------------------")
    




  



window = tk.Tk()
window.title("Data Entry")


frame = tk.Frame(window, bg= "#ffe6f0")
frame.pack()


#saving user name
user_info_frame= tk.LabelFrame(frame, text='User Information',bg="#ADD8E6")
user_info_frame.grid(row=0,column=0, padx= 20 , pady=10)

first_name= tk.Label(user_info_frame,text= "First Name")
first_name.grid(row=0, column=0)

middle_name = tk.Label(user_info_frame, text="Middle Name")
middle_name.grid(row=0,column=1)

last_name= tk.Label(user_info_frame,text= "Last Name")
last_name.grid(row=0, column=2)

first_name_entry= tk.Entry(user_info_frame)
middle_name_entry= tk.Entry(user_info_frame)
last_name_entry= tk.Entry(user_info_frame)

first_name_entry.grid(row=1,column=0,padx=20, pady=10 )

middle_name_entry.grid(row=1,column=1,padx=20, pady=10 )

last_name_entry.grid(row=1,column=2,padx=20, pady=10 )

age= tk.Label(user_info_frame, text='Age')
age_spinbox = tk.Spinbox(user_info_frame, from_=15, to= 30)
age.grid(row=2, column= 0)
age_spinbox.grid(row=3,column=0, padx=20, pady=10)


gender= tk.Label(user_info_frame, text='Gender')
gender_combobox = ttk.Combobox(user_info_frame, value= ["male",'female','other'])
gender.grid(row=2, column= 1)
gender_combobox.grid(row=3,column=1,padx=20,pady=10)



#file menu
def nothing():
    print('*')
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New File", command= nothing)
file_menu.add_command(label="open",command= nothing)
file_menu.add_command(label="save",command= nothing)
file_menu.add_separator()
file_menu.add_command(label="exit",command = window.quit)

#parents info
parents_frame= tk.LabelFrame(frame, bg="#ADD8E6")
parents_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

fathersname = tk.Label(parents_frame,text=" Father's Name")
fathersname.grid(row=0,column=0)

mothersname = tk.Label(parents_frame,text=" Mother's Name")
mothersname.grid(row=0,column=1)

fathersname_entry= tk.Entry(parents_frame)
mothersname_entry= tk.Entry(parents_frame)
fathersname_entry.grid(row=1,column=0,padx=20, pady=10)
mothersname_entry.grid(row=1,column=1,padx=20,pady=10)



# button= tk.Button(frame, text= "RESET", command=lambda:first_name.config("First Name"))
# button.grid(row=3,column=0,sticky="news",padx=20, pady=10)

button= tk.Button(frame, text= "ENTER DATA", bg="#D1FFBD",command= enter_data)
button.grid(row=4,column=0,sticky="ns",padx=20, pady=10)





window.mainloop()


