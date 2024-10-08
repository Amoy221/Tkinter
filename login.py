# -*- coding: utf-8 -*-
import tkinter as tk

window = tk.Tk()
window.title("Welcome to MyPython")
window.geometry('450x300')

# image
canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='dog.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

# Label
tk.Label(window,text='User name:').place(x=50,y=200)
tk.Label(window,text='Password:').place(x=50,y=240)

var_usr_name = tk.StringVar()
var_usr_name.set('1178445042') #  ‰≥ˆƒ¨»œ÷µ
entry_usr_name = tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=200)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=240)

# login and sign up button
def usr_login():
    pass

def usr_sign_up():
    pass

btn_login = tk.Button(window,text='Login',command=usr_login)
btn_login.place(x=150,y=270)
btn_sign_up = tk.Button(window,text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=220,y=270)



window.mainloop()