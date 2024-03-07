import tkinter as tk

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

expression = ""

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input field
input_text = tk.StringVar()
input_field = tk.Entry(root, textvariable=input_text, justify='right', font=('Arial', 18))
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda item=text: button_click(item))
    button.grid(row=row, column=column, padx=5, pady=5)

# Create clear button
clear_button = tk.Button(root, text='Clear', padx=20, pady=20, font=('Arial', 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create calculate button
calculate_button = tk.Button(root, text='Calculate', padx=20, pady=20, font=('Arial', 14), command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
