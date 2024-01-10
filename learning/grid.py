import tkinter as tk

root = tk.Tk()
root.title("Text Config Example")

text_widget = tk.Text(root, width=40, height=10, wrap=tk.WORD, font=("Arial", 12))
text_widget.insert(tk.END, "Initial text\nLine 2\nLine 3")

scrollbar = tk.Scrollbar(root, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

text_widget.pack(pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


root.mainloop()