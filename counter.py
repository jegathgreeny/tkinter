from tkinter import *

count = 0

# to change any text
def increment():
    global count
    count += 1
    output.config(text=f'{count}')

# to change text styles
def decrement():
    global count
    count -= 1
    output.config(text=f'{count}')





root = Tk()

output = Label(text=0)
output.pack()

# this button increases the count
increase_button = Button(root, text='+', command=increment)
increase_button.pack()

# this button decreases the count
decrease_button = Button(root, text='-', command=decrement)
decrease_button.pack()

root.geometry("500x500")
root.mainloop()
