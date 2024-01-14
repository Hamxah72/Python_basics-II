from tkinter import *

root = Tk()

# e = Entry(root, width=50, background="pink", foreground="yellow")
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name ")

def myClick():
    hello = "Assalam " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton =  Button(root, text="Enter Your Name", command=myClick)
# myButton =  Button(root, text="Click Me!", state=DISABLED)
myButton.pack()


root.mainloop()