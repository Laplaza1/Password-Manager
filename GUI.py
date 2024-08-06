from _tkinter import *
import tkinter
import tkinter.filedialog

import PIL.Image
import ttkbootstrap as ttk
from Password_manager import Password_generator, image_pass_encode, clear_old_pass
import pyperclip
from PIL import Image,ImageTk

root = tkinter.Tk()
root.geometry("400x400")
root.title("Password Manager")

def set_var():
    test = Password_generator()
    Var.set(test)

def copy_var():
    pyperclip.copy(Var.get())



def set_password():
    root2 = tkinter.Tk()
    root2.title("Set your password")
    root2.geometry("200x200")
    entry_txt = tkinter.StringVar()
    label1 =tkinter.Label(root,text="Password:").pack(padx=7,pady=3)
    entry1 = tkinter.Entry(root,textvariable=entry_txt)
    entry1.pack(padx=7,pady=3)
    def test_return(p1):
        
        print( 'Got: ', entry_txt.get())
    entry1.bind('<Return>',test_return)

    select_img = tkinter.filedialog.askopenfilename(filetypes=(('png files', '*.png'),('png files', '*.png')))
    encode_button = tkinter.Button(root,text="Encode Img",command=lambda: image_pass_encode(image=select_img,password=entry_txt.get())).pack(padx=7,pady=3)
    clear_code_button = tkinter.Button(root,text="Clear Img",command=lambda: clear_old_pass(image=select_img)).pack(padx=7,pady=3)
    
    


Title = tkinter.Label(root,text="PassWord Manager")
Title.pack(pady=30)
Title.config(font=("Arial",22,"bold"))
Var = tkinter.StringVar()
Password_field_frame = tkinter.Frame(root)
Password_field_frame.pack(padx=15,pady=20,fill="x")

Password_label= tkinter.Label(Password_field_frame,text="Password").pack(side="left",padx=5)
Password_label2= tkinter.Label(Password_field_frame,textvariable=Var).pack(side="left",fill="x",expand=True,padx=5)

Password_button = tkinter.Button(Password_field_frame,command=set_var,text="Press me").pack(side="left",fill="x",padx=7)
Copy_button = tkinter.Button(Password_field_frame,text="Copy",command=copy_var).pack(side="left",fill="x",padx=9)
set_password_button = tkinter.Button(Password_field_frame,text="Set password",command=set_password).pack(side="bottom",pady=10,padx=10)


root.mainloop()




