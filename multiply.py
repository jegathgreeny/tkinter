from tkinter import *


# perfomes multiplication
def multiply():
    first = int(first_num.get())
    second = int(second_num.get())
    output = first * second
    result.config(text=f"Result: {output}")


root = Tk()

welcome_message = Label(root, text="enter two numbers")
welcome_message.pack()

first_num = Entry(root)
first_num.pack()

second_num = Entry(root)
second_num.pack()

result = Label(root, text=f"Result:")
result.pack()

button = Button(root, text="calculate", command=multiply)
button.pack()

root.geometry("500x500")
root.mainloop()
