from tkinter import *

from click import command

sign = ''
window = Tk()
window.geometry("500x500")
window.title('Calculator')

# Label
inp = Label(window, text="Enter a number")
inp.pack(pady=10)


# Entry
entry_box = Entry(window, width=34, borderwidth=3 )
entry_box.place(x = 0, y = 0)
def click(num):
    input = entry_box.get()
    entry_box.delete(0,END)
    entry_box.insert(0,input+str(num))
b = Button(window , text=1 , width = 8, background="yellow", command=lambda:click(1))
b.place(x=0,y = 27)
b = Button(window , text=2 , width = 8, background="yellow" , command = lambda:click(2))
b.place(x=105,y = 27)
b = Button(window , text=3 , width = 8, background="yellow",command =lambda:click(3))
b.place(x=210,y = 27)
b = Button(window , text=4 , width = 8, background="yellow",command = lambda:click(4))
b.place(x=0,y = 57)
b = Button(window , text=5 , width = 8, background="yellow",command = lambda:click(5))
b.place(x=105,y = 57)
b = Button(window , text=6 , width = 8, background="yellow",command = lambda:click(6))
b.place(x=210,y = 57)
b = Button(window , text=7 , width = 8, background="yellow",command = lambda:click(7))
b.place(x=0,y = 87)
b = Button(window , text=8 , width = 8, background="yellow",command = lambda:click(8))
b.place(x=105,y = 87)
b = Button(window , text=9 , width = 8, background="yellow",command = lambda:click(9))
b.place(x=210,y = 87)
b = Button(window , text=0 , width = 8, background="yellow",command = lambda:click(0))
b.place(x=0,y = 117)
b = Button(window , text= '+' , width = 8, background="yellow",command = lambda:addition())
b.place(x=105,y = 117)
def addition():
    global a
    a = float(entry_box.get())
    entry_box.delete(0,END)
    global sign
    sign = "+"
b = Button(window , text='-', width = 8, background="yellow",command = lambda:minus())
b.place(x=210,y = 117)
def minus():
    global a
    global sign
    a = float(entry_box.get())
    entry_box.delete(0, END)
    sign = "-"
b = Button(window , text='/' , width = 8, background="yellow",command = lambda:divide())
b.place(x=0,y = 147)
def divide():
    global a
    global sign
    a = float(entry_box.get())
    entry_box.delete(0, END)
    sign = "/"
b = Button(window , text= '*' , width = 8, background="yellow" ,command = lambda:multiply())
b.place(x=105,y = 147)
def multiply():
    global a
    global sign
    a = float(entry_box.get())
    entry_box.delete(0, END)
    sign = "*"
b = Button(window , text='=', width = 8, background="yellow", command = lambda:equal())
def equal():
    value = float(entry_box.get())
    entry_box.delete(0, END)
    if(sign =="+"):
        entry_box.insert(0,int(value+a))
    elif(sign =="-"):
        entry_box.insert( 0,int(a-value))
    elif (sign == "/"):
        entry_box.insert( 0,int(a/value))
    elif (sign == "*"):
        entry_box.insert(0,int(value * a))
    else:
        entry_box.insert(0,'error')
b.place(x=210,y = 147)
b = Button(window , text='clear', width = 31, background="yellow" ,command = lambda:clear())
b.place(x=0,y = 177)
def clear():
    entry_box.delete(0,END)

window.mainloop()
