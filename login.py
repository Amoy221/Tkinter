# -*- coding: utf-8 -*-
import tkinter as tk
import pickle
from tkinter import messagebox

window = tk.Tk()
window.title("Welcome to MyPython")
window.geometry('450x400')

# image
canvas = tk.Canvas(window,height=200,width=500)
image_file = tk.PhotoImage(file='dog.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack(side='top')

# Label
tk.Label(window,text='User name:').place(x=50,y=200)
tk.Label(window,text='Password:').place(x=50,y=240)

var_usr_name = tk.StringVar()
var_usr_name.set('1178445042') # 输出默认值
entry_usr_name = tk.Entry(window,textvariable=var_usr_name)
entry_usr_name.place(x=160,y=200)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window,textvariable=var_usr_pwd,show='*')
entry_usr_pwd.place(x=160,y=240)

# login and sign up button
def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('user_info.pickle','rb') as usr_file: # 打开文件读取信息
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('user_info.pickle','wb') as usr_file:
            usrs_info = {"admin":"admin"}
            pickle.dump(usrs_info,usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome',message='How are you?'+ usr_name)
        else:
            tk.messagebox.showerror(message='Error,your password is wrong,try again.')
    else:
        is_sign_up = tk.messagebox.askyesno('Welcome','You have not sign up yet.Sign up today?')
        if is_sign_up:
            usr_sign_up()

def usr_sign_up():

    def sign_to_Mofan_Python():
        np =  new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()

        with open('user_info.pickle','rb') as usr_file:
            exist_usrs_info = pickle.load(usr_file)

        if np != npf: # 输入的两次密码不一样
            tk.messagebox.showerror('Error','Password and confirm password must be the same!')
        elif nn in exist_usrs_info: # 已经注册过了
            tk.messagebox.showerror('Error','The user has already signed up!')
        else:
            exist_usrs_info[nn] = np
            with open('user_info.pickle','wb') as usr_file:
                pickle.dump(exist_usrs_info,usr_file)
            tk.messagebox.showinfo('Welcome','You have successfully signed up!')
            window_sign_up.destroy() # 关闭窗口


    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up,text='User name:').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    entry_usr_pwd = tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_usr_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text='Confirm password:').place(x=10,y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_usr_pwd_confirm.place(x=150,y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up,text='Sign up',command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=150,y=130)


btn_login = tk.Button(window,text='Login',command=usr_login)
btn_login.place(x=150,y=270)
btn_sign_up = tk.Button(window,text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=220,y=270)



window.mainloop()