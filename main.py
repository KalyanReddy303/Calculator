import tkinter as tk

def button_click(symbol):
    current = display_var.get()
    if symbol == 'C':
        display_var.set('')
    elif symbol == '=':
        try:
            result = eval(current)
            display_var.set(result)
        except Exception as e:
            display_var.set('Error')
    else:
        display_var.set(current + symbol)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a variable to hold the input
display_var = tk.StringVar()

# Create the display widget
display = tk.Entry(root, textvariable=display_var, font=('Arial', 20), justify='right')
display.grid(row=0, column=0, columnspan=4)

# Define button symbols
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

# Create and place the buttons
for i, symbol in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    button = tk.Button(root, text=symbol, width=5, height=2, command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=col)

# Run the main loop
root.mainloop()
