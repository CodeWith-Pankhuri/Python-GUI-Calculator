from tkinter import *
root=Tk()
root.geometry("350x620")
root.title("My Calculator")
root.wm_iconbitmap("calculator.ico")

def click(event):
    global scvalue
    text=event.widget.cget("text") # cget-helps to get the value that is clicked through button(event)
    #print(text) show on output screen

    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(entry.get())
            except Exception as e:
                print(e)
                value="Error"

        scvalue.set(value)
        entry.update()
    elif text=="C":
        scvalue.set("")
        entry.update()

    else:
        scvalue.set(scvalue.get() + text)
        entry.update()

scvalue=StringVar()
scvalue.set("")
entry=Entry(root,textvariable=scvalue,font=("Arial",30,"bold"))
entry.pack(fill="x",ipadx=8,pady=10,padx=10)


list=[["C","/","*","="],
      ["7","8","9","+",],
      ["4","5","6","- "],
      ["1","2","3","%"],
      ["//","0",".","^"]]

for i in list:
    f = Frame(root)
    f.pack(fill="x")
    for j in i:
        b=Button(f,text=j,font=("Arial",25,"bold"))
        b.pack(side="left",padx=15,pady=15)
        b.bind("<Button-1>",click)



#Button(root,text="Close this Window",command=root.destroy,font="lucida 12 bold").pack(side="left",padx=15,pady=15)

root.mainloop()