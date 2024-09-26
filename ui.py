import tkinter as  tk

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("200x100")

var = tk.StringVar() # 定义一个字符串变量

# l = tk.Label(window,text="va",bg='green',font=('Arial',12),width=15,height=2)
l = tk.Label(window,textvariable=var,bg='green',font=('Arial',12),width=15,height=2) # 构造一个window上的Label对象
l.pack()


on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")

b = tk.Button(window,text="hit me",width=15,height=2,command=hit_me)
b.pack()

window.mainloop() # 窗口不断刷新