import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar
# from tkcalendar import DateEntry

def print_sel():
    global cal
    val = cal.entry.get()
    print(val)

def combobox_func(event):
    v = cb.get()
    print(v)

root = ttk.Window(themename="darkly")
# 画面サイズ(Window位置)
root.geometry('1200x500+600+600')

fruits = ['Apple', 'Banana', 'Grape', 'orange', 'pinapure']

v = StringVar()

cb = ttk.Combobox(values=fruits, style="primary")
cb.set(fruits[0])
cb.bind('<<ComboboxSelected>>', combobox_func)
cb.pack()

cal = ttk.DateEntry(bootstyle='darkly', dateformat='%Y/%m/%d')
cal.bind("<<DateEntrySelected>>", print_sel)
cal.pack()

b1 = ttk.Button(root, text="Submit", bootstyle="dark")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text='日付を選択', bootstyle="info", command=print_sel)
b2.pack(padx=5, pady=10)

root.mainloop()