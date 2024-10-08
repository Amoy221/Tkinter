import tkinter as  tk

window = tk.Tk() # 构造一个窗口对象 
window.title("my window")
window.geometry("800x600")

canvas = tk.Canvas(window,bg = 'blue',height=300,width=300)
canvas.pack()
image_file = tk.PhotoImage(file='D:\MyPython\Tkinter\dog.gif') # 打开image文件,tkinter支持gif格式的图片
image = canvas.create_image(10,10,anchor='nw',image=image_file) # 0,,0是是指画布中的哪个点，anchor是锚定点
x0,y0,x1,y1=50,50,80,80 # 自定义坐标
line = canvas.create_line(x0,y0,x1,y1) # 画一根黑线
oval = canvas.create_oval(x0,y0,x1,y1,fill='red') # 画圆形
arc = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start = 0,extent=180) # 画扇形，从0打开到180收回  
rect = canvas.create_rectangle(100,30,100+20,30+20) 

def moveit(): # 点击button，，正方形Y轴方向下移两个单位
    canvas.move(rect,0,2)  # 0是X坐标0个单位，2是Y坐标两个单位

b = tk.Button(window,text='move',command=moveit).pack()

                    
window.mainloop() # 窗口不断刷新