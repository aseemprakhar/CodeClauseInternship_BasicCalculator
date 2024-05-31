import tkinter as tk
from tkinter import messagebox

def press_key(key):
    current = entry.get()
    if key == '=':
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", str(e))
    elif key == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, key)

app = tk.Tk()
app.title("Calculator")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

entry = tk.Entry(app, width=30, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

row = 1
col = 0
for button_text in buttons:
    tk.Button(app, text=button_text, width=5, font=('Arial', 12),
              command=lambda text=button_text: press_key(text)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()
