from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I clicked a Button!!")
    myLabel.pack()

myButton =  Button(root, text="Click Me!", command=myClick, foreground="blue", background="purple")
# myButton =  Button(root, text="Click Me!", state=DISABLED)
myButton.pack()


root.mainloop()