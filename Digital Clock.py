import tkinter as tk
from time import strftime

def time_update():
    string_time = strftime('%H:%M:%S %p')
    label_time.config(text=string_time)

    string_date = strftime('%B %d, %Y')
    label_date.config(text=string_date)

    string_day = strftime('%A')
    label_day.config(text=string_day)

    label_time.after(1000, time_update)

root = tk.Tk()
root.title("Stylish Digital Clock")
root.configure(bg='black')

frame_time = tk.Frame(root, bg='black')
frame_time.pack(pady=10)

# Use a custom font (you can replace this with your own font file)
font = ("Helvetica", 60, "bold")

label_time = tk.Label(frame_time, font=font, background='black', foreground='white')
label_time.pack(anchor='center')

frame_date_day = tk.Frame(root, bg='black')
frame_date_day.pack(pady=(0, 10))

font_small = ("Helvetica", 18)

label_date = tk.Label(frame_date_day, font=font_small, background='black', foreground='white')
label_date.grid(row=0, column=0, padx=(10, 0), sticky='w')

label_day = tk.Label(frame_date_day, font=font_small, background='black', foreground='white')
label_day.grid(row=0, column=1, padx=(0, 10), sticky='e')

time_update()

root.mainloop()
