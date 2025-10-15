import tkinter as tk
from tkinter import ttk
#create a window


root = tk.Tk()
root.title("Calculator") #put a title to the window
root.geometry('800x600') #window size
root.resizable(False, False) #restrict window resizing

def button_func(num1, num2):
    sum_result = num1 + num2
    result.set(f'Sum = {sum_result}')

number1 = tk.IntVar()
number2 = tk.IntVar()
result = tk.StringVar()

entry1 = ttk.Entry(root, textvariable=number1)  #create an entry box
entry1.pack(pady=10)    
entry2 = ttk.Entry(root, textvariable=number2)  #create an entry box
entry2.pack(pady=10)



buttom = ttk.Button(root, text="Calculate Sum", command=lambda: button_func(number1.get(), number2.get()))  #create a button
buttom.pack(pady=20)

label = ttk.Label(root, text="Result will be shown here", textvariable=result)  #create a label
label.pack(pady=10)

root.mainloop()

