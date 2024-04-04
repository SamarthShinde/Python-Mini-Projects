import tkinter as tk
def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)
def clear_entry():
    entry.delete(0, tk.END)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: click_button(x)
    if button == '=':
        action = evaluate
    elif button == 'C':
        action = clear_entry
    tk.Button(window, text=button, width=4, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
