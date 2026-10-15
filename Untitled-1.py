from tkinter import *

root = Tk()
root.title("GUI на Python")
root.geometry("250x200")

python_enabled = BooleanVar()
javascript_enabled = BooleanVar()

Checkbutton(text="Python", variable=python_enabled).pack(anchor="w", padx=6, pady=6)
Checkbutton(text="JavaScript", variable=javascript_enabled).pack(anchor="w", padx=6, pady=6)

root.mainloop()