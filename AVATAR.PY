from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=15)
frm.grid()
ttk.Label(frm, text="YEPPADI ERUKA NALLA ERUKIYA ").grid(column=1, row=0)
ttk.Button(frm, text="exit", command=root.destroy).grid(column=0, row=1),(frm, text="start",command=root.destroy)
root.mainloop()