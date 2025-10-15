#Download .ico file image
import tkinter as tk
from tkinter import ttk 
#create a window

def button_click_func():
    print("Button Clicked")
    user_input = entry.get()  #get text from entry box
    print(f"User Input: {user_input}")

root = tk.Tk()
root.title("Device Fault Tolerence system") #put a title to the window

width, height = 800, 700
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()

left = (display_width - width) // 2 #put the window openning location in to center
top = (display_height - height) // 2
root.geometry(f'{width}x{height}+{left}+{top}') #window size and position

root.resizable(False, False) #restrict window resizing

#create a button
button = tk.Button(root, text="Click Me", command=button_click_func())
button.pack(pady=20)

entry = tk.Entry(root)  #create an entry box
entry.pack(pady=10)


#Set icon for the window
#root.iconbitmap('icon.ico')

root.mainloop()
print("UI Loaded")
