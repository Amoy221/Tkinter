import tkinter as  tk

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("200x200")


l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection(v): # 拖动scale有个默认的传入值
    l.config(text='you have selectd ' + v) # 修改label的参数

s = tk.Scale(window,label="try me",from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=0,tickinterval=0,resolution=0.01,command=print_selection)
s.pack()

window.mainloop() # 窗口不断刷新