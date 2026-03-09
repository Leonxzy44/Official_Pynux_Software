import tkinter as tk

# main desktop window
root = tk.Tk()
root.title("Learning Desktop")
root.geometry("800x500")
root.configure(bg="#40E0D0")  # turquoise

# --------- app functions ---------

def open_notepad():
    win = tk.Toplevel(root)
    win.title("Notepad")
    win.geometry("400x300")
    text = tk.Text(win)
    text.pack(expand=True, fill="both")

def open_calculator():
    win = tk.Toplevel(root)
    win.title("Calculator")
    win.geometry("250x300")

    entry = tk.Entry(win, font=("Arial", 18), justify="right")
    entry.pack(fill="x", padx=10, pady=10)

    def press(key):
        entry.insert("end", key)

    def calculate():
        try:
            entry.insert("end", "\n" + str(eval(entry.get())))
        except:
            entry.insert("end", "\nError")

    for sym in ("7 8 9 /", "4 5 6 *", "1 2 3 -", "0 . = +"):
        row = tk.Frame(win)
        row.pack()
        for ch in sym.split():
            if ch == "=":
                tk.Button(row, text=ch, width=5, command=calculate).pack(side="left")
            else:
                tk.Button(row, text=ch, width=5, command=lambda c=ch: press(c)).pack(side="left")

def open_about():
    win = tk.Toplevel(root)
    win.title("About")
    win.geometry("300x150")
    tk.Label(win, text="My Learning Desktop\nMade with Tkinter",
             font=("Arial", 12)).pack(expand=True)

# --------- desktop icons ---------

icon_style = {
    "bg": "#E0FFFF",
    "width": 10,
    "height": 3,
    "relief": "raised"
}

tk.Button(root, text="Notepad", command=open_notepad, **icon_style)\
    .place(x=40, y=40)

tk.Button(root, text="Calculator", command=open_calculator, **icon_style)\
    .place(x=40, y=110)

tk.Button(root, text="About", command=open_about, **icon_style)\
    .place(x=40, y=180)

root.mainloop()
