from tkinter import *

# # this outputs the text to std_out
# def print_something():
#     print('trying to fix it')

# to change any text
def change_text():
    welcome_message.config(text='still broken')

# to change text styles
def change_color():
    welcome_message.config(fg='white')

root = Tk()

welcome_message = Label(root, text="broken are the evolved", padx=200, pady=30, fg='red', bg='black')
welcome_message.pack()

button = Button(root, text="click me", command=change_color)
button.pack()

root.geometry("500x500")
root.mainloop()
