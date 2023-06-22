from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(bg="grey")
root.geometry("428x500")
reslt = StringVar()
operation = ""

top = Label(root,text="C A L C U L A T O R",font=('arial',18,'bold'),fg="blue",bg="grey").pack(pady=10)

def equal():
    global operation

    res = eval(operation)
    reslt.set(str(res))
    operation = ""

def clear():
    global operation
    reslt.set("")
    operation = ""

def btnclk(n):
    global operation
    operation = operation + str(n)
    reslt.set(operation)

def back():
    global operation
    operation = operation[0:-1]
    reslt.set(operation)
    

result = Entry(root,textvariable=reslt,width=34,bg="white",fg="Black",border=6,font=('calibri',16,'bold')).place(x=18,y=80)
btn1 = Button(root,text="9",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda:btnclk(9)).place(x=15,y=140)
btn2 = Button(root,text="6",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(6)).place(x=15,y=200)
btn3 = Button(root,text="3",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(3)).place(x=15,y=260)
btn4 = Button(root,text="0",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(0)).place(x=15,y=320)
btn5 = Button(root,text="AC",bg="red",border=5,width=8,font=('arial',10,'bold'),command= clear).place(x=70,y=380)
btn6 = Button(root,text="8",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(8)).place(x=120,y=140)
btn7 = Button(root,text="5",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(5)).place(x=120,y=200)
btn8 = Button(root,text="2",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(2)).place(x=120,y=260)
btn9 = Button(root,text=".",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(".")).place(x=120,y=320)
btn10 = Button(root,text="⬅️",bg="green",border=5,width=8,font=('arial',10,'bold'),command= back).place(x=175,y=380)
btn11 = Button(root,text="7",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(7)).place(x=225,y=140)
btn12 = Button(root,text="4",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(4)).place(x=225,y=200)
btn13 = Button(root,text="1",bg="orange",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk(1)).place(x=225,y=260)
btn14 = Button(root,text="-",fg="blue",bg="pink",border=5,width=8,font=('arial',10,'bold'),command=lambda:btnclk("-")).place(x=225,y=320)
btn15 = Button(root,text="Exit",bg="yellow",border=5,width=8,font=('arial',10,'bold'),command=lambda: root.destroy()).place(x=280,y=380)
btn16 = Button(root,text="+",fg="blue",bg="pink",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk("+")).place(x=330,y=140)
btn17 = Button(root,text="x",fg="blue",bg="pink",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk("*")).place(x=330,y=200)
btn18 = Button(root,text="/",fg="blue",bg="pink",border=5,width=8,font=('arial',10,'bold'),command=lambda: btnclk("/")).place(x=330,y=260)
btn19 = Button(root,text="=",fg="blue",bg="pink",border=5,width=8,font=('arial',10,'bold'),command= equal).place(x=330,y=320)

root.mainloop()