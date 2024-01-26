# import tkinter as tk
# from math import sqrt

# class Calculator:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Calculator")
        
#         self.result_var = tk.StringVar()
        
#         self.create_widgets()
        
#     def create_widgets(self):
#         # Entry widget to display the result
#         entry = tk.Entry(self.master, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=0, width=23, justify='right')
#         entry.grid(row=0, column=0, columnspan=4)
        
#         # Buttons
#         buttons = [
#             '%', 'CE', 'C', '<X',
#             '1/x', 'x^2', 'sqrt(x)', '÷',
#              '7', '8', '9', '*',
#             '4', '5', '6', '-',
#             '1', '2', '3', '+',
#             '+/-', '0', '.', '='
#         ]
        
#         row_val = 1
#         col_val = 0
#         for button in buttons:
#             tk.Button(self.master, text=button, font=('Arial', 14), height=3, width=7, command=lambda btn=button: self.on_button_click(btn)).grid(row=row_val, column=col_val)
#             col_val += 1
#             if col_val > 3:
#                 col_val = 0
#                 row_val += 1
    
#     def on_button_click(self, button):
#         current_text = self.result_var.get()
        
#         if button == '=':
#             try:
#                 result = eval(current_text)
#                 self.result_var.set(result)
#             except Exception as e:
#                 self.result_var.set("Error")
#         elif button == 'C':
#             self.result_var.set('')
#         elif button == 'CE':
#             self.result_var.set(current_text[:-1])
#         elif button == 'x^2':
#             self.result_var.set(str(float(current_text) ** 2))
#         elif button == '1/x':
#             try:
#                 result = 1 / float(current_text)
#                 self.result_var.set(result)
#             except ZeroDivisionError:
#                 self.result_var.set("Error")
#         elif button == '%':
#             try:
#                 result = float(current_text) / 100
#                 self.result_var.set(result)
#             except ZeroDivisionError:
#                 self.result_var.set("Error")
#         else:
#             self.result_var.set(current_text + button)

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("375x570")
#     root.resizable(0,0)
#     calculator = Calculator(root)
#     root.mainloop()



import tkinter as tk
from math import sqrt

def on_button_click(button, result_var):
    current_text = result_var.get()

    if button == '=':
        try:
            result = eval(current_text)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif button == 'C':
        result_var.set('')
    elif button == 'CE':
        result_var.set(current_text[:-1])
    elif button == 'x^2':
        result_var.set(str(float(current_text) ** 2))
    elif button == '1/x':
        try:
            result = 1 / float(current_text)
            result_var.set(result)
        except ZeroDivisionError:
            result_var.set("Error")
    elif button == '%':
        try:
            result = float(current_text) / 100
            result_var.set(result)
        except ZeroDivisionError:
            result_var.set("Error")
    else:
        result_var.set(current_text + button)

def create_widgets(root, result_var):
    # Entry widget to display the result
    entry = tk.Entry(root, textvariable=result_var, font=('Arial', 20), bd=10, insertwidth=0, width=23, justify='right')
    entry.grid(row=0, column=0, columnspan=4)

    # Buttons
    buttons = [
        "MC","MR","M+","M-","MS","M⋎",
        '%', 'CE', 'C', '<X',
        '1/x', 'x^2', 'sqrt(x)', '÷',
        '7', '8', '9', '*',
        '4', '5', '6', '-',
        '1', '2', '3', '+',
        '+/-', '0', '.', '='
    ]

    row_val = 1
    col_val = 0
    for button in buttons:
        tk.Button(root, text=button, font=('Arial', 14), height=3, width=7, command=lambda btn=button: on_button_click(btn, result_var)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1


root = tk.Tk()
root.geometry("375x570")
root.resizable(0, 0)

result_var = tk.StringVar()
create_widgets(root, result_var)

root.mainloop()


