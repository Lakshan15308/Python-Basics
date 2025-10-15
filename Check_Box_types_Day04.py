import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Check Box Example") #put a title to the window
root.geometry('800x600') #window size
root.resizable(False, False) #restrict window resizing
root.configure(bg='lightblue') #set background color
#root.iconbitmap('icon.ico') #set window icon

check1_var = tk.StringVar()
check2_var = tk.StringVar()
lebal_var = tk.StringVar() 

def checkbox_results():
    Output_string  = "You selected: " + check1_var.get() + check2_var.get()
    lebal_var.set(Output_string)

# Create check boxes    
check1 = ttk.Checkbutton(root, text="Meat", variable=check1_var, onvalue="Meat ", offvalue="")
check1.pack(pady=10)
check2 = ttk.Checkbutton(root, text="Vege", variable=check2_var, onvalue="Vege", offvalue="")
check2.pack(pady=10)

radio1 = ttk.Radiobutton(root, text="Male", value="Male", variable=lebal_var)
radio1.pack(pady=5)
radio2 = ttk.Radiobutton(root, text="Female", value="Female", variable=lebal_var)
radio2.pack(pady=5)

combobox = ttk.Combobox(root, values=["Python", "Java", "C++", "JavaScript"])
combobox.current(0)  #set default value
combobox.pack(pady=10)  

spinbox = ttk.Spinbox(root, from_=0, to=100)
spinbox.pack(pady=10)

button = ttk.Button(root, text="Submit", command=checkbox_results)  #create a button
button.pack(pady=20)    

#event binding for button selection 
button.bind("<Enter>", lambda e: button.config(text="Click to Submit")) 
button.bind("<Leave>", lambda e: button.config(text="Submit"))  
button.bind("<Motion>", lambda e: button.config(text="Submitted"))    

canvas = tk.Canvas(root, width=200, height=100, bg='green')
canvas.pack(pady=10)

label = ttk.Label(root, text="Select your Preference", textvariable=lebal_var, background='lightblue', font=('Arial', 14))
label.pack(pady=10)

root.mainloop()
print("Check Box UI Loaded")

#reference:
#https://www.youtube.com/watch?v=T8XwsQaTx9w&list=PL495mke12zYC-ZUbzd1Z0Y6WteuvsMf7Z&index=79
