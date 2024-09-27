import tkinter as  tk

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("200x200")


l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

def print_selection(): 
    if (var1.get()==1) & (var2.get()==0):
        l.config(text='I love only python ') # 修改label的参数
    elif (var1.get()==0) & (var2.get()==1):
        l.config(text='I love only C++ ')
    elif (var1.get()==0) & (var2.get()==0):
        l.config(text='I do not love either ')
    else:
        l.config(text='I love both ')

var1 = tk.IntVar()
var2 = tk.IntVar()
c1 = tk.Checkbutton(window,text='python',variable=var1,onvalue=1,offvalue=0,command=print_selection) # 选定时，把onvalue赋值给var1
c2 = tk.Checkbutton(window,text='c++',variable=var2,onvalue=1,offvalue=0,command=print_selection)
c1.pack()
c2.pack()
                    
window.mainloop() # 窗口不断刷新