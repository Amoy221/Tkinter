import tkinter as  tk

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("200x200")

var = tk.StringVar()
l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    l.config(text='you have selectd ' + var.get()) # 修改label的参数

r1 = tk.Radiobutton(window,text='Option A',variable=var,value='A',command=print_selection) # 选中时把 ’Option A‘改为’A‘ 
r1.pack()
r2 = tk.Radiobutton(window,text='Option B',variable=var,value='B',command=print_selection) # 选中时把 ’Option A‘改为’A‘ 
r2.pack()
r3 = tk.Radiobutton(window,text='Option C',variable=var,value='C',command=print_selection) # 选中时把 ’Option A‘改为’A‘ 
r3.pack()

window.mainloop() # 窗口不断刷新