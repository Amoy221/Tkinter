import tkinter as  tk
from tkinter import messagebox

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("200x200")

def hit_me():
    # tk.messagebox.showinfo(title='Hi',message='hahahha')
    # tk.messagebox.showwarning(title='Hi',message='nononono') # 警告
    # tk.messagebox.showerror(title='Hi',message='NO! never')   # 报错
    # print(tk.messagebox.askquestion(title='Hi',message='hahahahh'))  # return 'yes','no'
    # print(tk.messagebox.askyesno(title='Hi',message='hahahaha')) # return 'true','false'
    # print(tk.messagebox.askretrycancel(title='Hi',message='hahahaha')) # return 'true','false'
    print(tk.messagebox.askokcancel(title='Hi',message='hahahaha')) # return 'true','false'


tk.Button(window,text='hit me',command=hit_me).pack()

window.mainloop() # 窗口不断刷新