# Importing necessary packages 
import tkinter as tk 
from pathlib import Path
from tkinter import ttk
import os
from tkinter import *
from tkinter import messagebox, filedialog 

#----------------------------------------------------------------------------------------------------------------

root = tk.Tk()
root.title('Random Password Generator')

#-----------------------------------------------------------------------------------------------------------------
# MenuBar
menubar = Menu(root)
root.config(menu=menubar)

def about_us():
    tk.messagebox.showinfo('About RPG', 'This is made using tkinter and ramdom-password-generator Module .Thankyou for using my app')

def Credits():
    tk.messagebox.showinfo('Credits', 'Developer Team -- Ashwin\n\nIdea for this app --Ashwin\n\nThankyou Siva for motivating supporting and helping me evertime')

## Sub menu
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Click Here!", menu=subMenu)
subMenu.add_command(label="About this app", command=about_us)
subMenu.add_command(label="Credits", command=Credits)
subMenu.add_command(label="Exit", command=root.destroy)
#----------------------------------------------------------------------------------------------------------------

# function
def pasgen():
	dirs = os.listdir("passwords")
	for file in dirs:
		global files
		files = file.replace('.txt', '')
	
	if files == name.get():
		tk.messagebox.showerror("Error","File with the same name already exists")
	elif len(name.get()) == 0:
		tk.messagebox.showerror("Warning","Enter name for the password file")

	else:
		a = name.get()
		from password_generator import PasswordGenerator
		pwo = PasswordGenerator()
		pwo.maxlen = 16
		pas = pwo.generate()
		button = tk.messagebox.askquestion("Message","Password generated, click yes to see")
		if button == "yes":
		    btn = tk.messagebox.askquestion("Password", " ' " + pas + " ' " + "is your password. Click Yes to continue")
		    if btn == "yes":
		        button2 = tk.messagebox.askquestion("Message", "Do you want to save the Password")
		        if button2 =="yes":
		            try:
		                import sys
		                text_file = open("passwords/"+a+".txt", "w")
		                n = text_file.write(str(pas))
		                text_file.close()
		                try:
		                    tk.messagebox.showinfo("Infomation", "Password Saved Successfully")
		                    tk.messagebox.showinfo("Message" , "Thankyou for using my App")
		                except:
		                    tk.messagebox.showerror("Error" ,"Sorry , An error occured")
		        

		            except:
		                tk.messagebox.showerror("Error" ,  "Sorry , An error occured")
		    else:
		        tk.messagebox.showinfo("Infomation" ,  "Try to generate a new password")
		else:
		        tk.messagebox.showinfo("Infomation" ,  "Try to generate a new password")


#----------------------------------------------------------------------------------------------------------------
# Vars
name = StringVar()

#Labels
file_name = Label(root,text="Enter a name for the password file :",bg="#E8D579").grid(row=1,column=0,pady=5,padx=5)

#Entry
entry_box = Entry(root, textvariable = name, exportselection = 2, width = 50 , bg = "lightgreen").grid(row=1,column=1,pady=5,padx=5)

#Button
work = Button(root, text="Generate",command=pasgen,width=20,bg="#05E8E0").grid(row=2,column=0,pady=3,padx=3) 

#-------------------------------------------------------------------------------------------------------------------
root.mainloop()