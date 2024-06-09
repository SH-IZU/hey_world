#tkinter

import tkinter as tk
from tkinter import ttk

root= tk.Tk() #initialize and root is variable we can change it as our wish
root.title("tkinter window")
root.geometry("400x300") # here this is char x not multiplication sign
#adding lable

label= tk.Label(root, text="hello python")
label.pack()

#buttom click function 
def on_submit():
    print("button clicked")

    # adding button
button = tk.Button(root,text="submit", command= on_submit)
button.pack()

# adding input entry
entry = tk.Entry(root)
entry.pack()

#adding text area
text= tk.Text(root,height=5, width= 40)
text.pack()

frame=tk.Frame(root, bg="grey")

check = tk.IntVar()
check2= tk.IntVar() #checkbutton=multiple check
checkbutton= tk.Checkbutton(frame, text="check me",variable= check)
checkbutton2= tk.Checkbutton(frame, text="check me too",variable=check2)
checkbutton.pack()
checkbutton2.pack()

radio_var= tk.StringVar()
radiobutton1 = tk.Radiobutton(frame,text="male",variable = radio_var, value= "m")
radiobutton2 = tk.Radiobutton(frame,text="female",variable = radio_var, value= "m")
radiobutton1.pack()# pack make block
radiobutton2.pack()

frame.pack()
# menu used to make menu like save new open etc
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="new")
file_menu.add_command(label="open")
file_menu.add_command(label="save")
file_menu.add_separator()
file_menu.add_command(label="exit",command = root.quit)


tree= ttk.Treeview(root)
tree["columns"]=("name","age")
tree.column("#0",width=150)
tree.column("name")
root.mainloop()


#radiobutton.grid(row=1, column=1) it acts as matrix
