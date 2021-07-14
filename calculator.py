from tkinter import *
import pyttsx3
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("450x685")

root.minsize(400,650) 
root.maxsize(500,700)
root.title("CALCULATOR--Made By BISWAMBHAR PAL--")
#root.wm_iconbitmap("calc.ico")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice",voices[0].id)

def pronouce():
    if dspvalue.get()=="":
        engine.say("Nothing to pronounce")
        engine.runAndWait()
    else:
        Message = dspvalue.get()
        engine.say(Message)
        engine.runAndWait()

def clr():
    dspvalue.set("")
    Display.update()

def click(event):
    text = str(event.widget.cget("text"))
    if text == "=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except:
                value = "ERROR"
        dspvalue.set(value)
        Display.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable = scvalue,font="Magneto 25",bg="light cyan",fg="midnight blue")
screen.pack(fill=X,ipadx=15,ipady=5,pady=20,padx=20)
root.configure(background="azure")

#Display Screen
dspvalue=StringVar()
dspvalue.set("")
f1 = Frame(root,bg="azure2")

f12=Frame(f1,bg="azure2")
Label(f1,text=" RESULT =",font="joan 20",fg="dark green").pack(side=LEFT)
f12.pack(side=LEFT)

f11=Frame(f1,bg="azure2")
clear=Button(f1,text="CLEAR",padx=17,font="Bahnschrift 15 bold",bg="alice blue",fg="red2",command=clr)
clear.pack(side=RIGHT)
f11.pack(side=RIGHT)

Display=Entry(f1,textvariable = dspvalue,font="Forte 30 bold",bg="mint cream",fg="green4")
Display.pack(ipadx=15,ipady=5,pady=5,padx=20)
Button(f1,text="PRONOUNCE",padx=10,font="Bahnschrift 15 bold",bg="brown4",fg="floral white",command=pronouce).pack()
f1.pack()


# / % =
f1 = Frame(root,bg="azure2")
b1=Button(f1,text="/",padx=17,font="Bahnschrift 25 bold",bg="alice blue",fg="purple4")
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="%",padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="purple4")
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="=",padx=15,font="Bahnschrift 25 bold",bg="alice blue",fg="green")
b1.pack(side=LEFT,padx=10,pady=5)
b1.bind("<Button-1>",click)
f1.pack(side=BOTTOM)

#  + - *
f1 = Frame(root,bg="azure2")
b1=Button(f1,text="+",padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="purple4")
b1.pack(side=LEFT,padx=15,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="-",padx=15,font="Bahnschrift 25 bold",bg="alice blue",fg="purple4")
b1.pack(side=LEFT,padx=15,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="*",padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="purple4")
b1.pack(side=LEFT,padx=15,pady=5)
b1.bind("<Button-1>",click)
f1.pack(side=BOTTOM)

# . 0 c
f1 = Frame(root,bg="azure2")
b1=Button(f1,text=".",padx=17,font="Bahnschrift 25 bold",bg="alice blue",fg="purple4")
b1.pack(side=LEFT,padx=14,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="0",padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="midnight blue")
b1.pack(side=LEFT,padx=14,pady=5)
b1.bind("<Button-1>",click)

b1=Button(f1,text="C",padx=9,font="Bahnschrift 25 bold",bg="alice blue",fg="red")
b1.pack(side=LEFT,padx=15,pady=5)
b1.bind("<Button-1>",click)
f1.pack(side=BOTTOM)

# 0 1 2 3 4 5 6 7 8 9
for i in range(1,10,3):
    f1 = Frame(root,bg="azure2")
    b1=Button(f1,text=i,padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="midnight blue")
    b1.pack(side=LEFT,padx=15,pady=5)
    b1.bind("<Button-1>",click)

    i=i+1
    b1=Button(f1,text=i,padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="midnight blue")
    b1.pack(side=LEFT,padx=15,pady=5)
    b1.bind("<Button-1>",click)

    i=i+1
    b1=Button(f1,text=i,padx=10,font="Bahnschrift 25 bold",bg="alice blue",fg="midnight blue")
    b1.pack(side=LEFT,padx=15,pady=5)
    b1.bind("<Button-1>",click)
    f1.pack(side=BOTTOM)




root.mainloop()
