import tkinter as  tk

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("200x200")

l = tk.Label(window,text="",bg='yellow')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do'+str(counter)) # 改变label的参数
    counter+=1

menubar = tk.Menu(window)
filemenu =  tk.Menu(menubar,tearoff=0) # 定义在菜单栏中的menu,tearoff=0可以把虚线去除
menubar.add_cascade(label='File',menu=filemenu) # 显示在menubar上面
filemenu.add_command(label='New',command=do_job) # 定义选项功能
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)

filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

Editmenu =  tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=Editmenu)
Editmenu.add_command(label='Cut',command=do_job)
Editmenu.add_command(label='Copy',command=do_job)
Editmenu.add_command(label='Paste',command=do_job)

submenu = tk.Menu(filemenu,tearoff=0)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)
submenu.add_command(label='Submenu1',command=do_job)

window.config(menu=menubar) # 改变window的参数，把菜单栏放在window上    

window.mainloop() # 窗口不断刷新