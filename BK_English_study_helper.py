import tkinter as tk
from tkinter import ttk, StringVar

def combobox_func(event):
    v = cb.get()
    print(v)

# Tkクラス生成
root = tk.Tk()
# 画面サイズ(Window位置)
root.geometry('1200x500+600+600')
# 画面タイトル
root.title('Study English Helper')

root.winfo_x = 200

# ラベル
lbl = tk.Label(root, text='url:',font=("MSゴシック", "14"),anchor=tk.W)
lbl.place(x=10, y =50)

fruits = ['Apple', 'Banana', 'Grape', 'orange', 'pinapure']

# Frame
frame = ttk.Frame(root, padding=100)
frame.grid()

v = StringVar()

style = ttk.Style()
style.theme_use('classic')
style.configure("office.TButton", anchor="w", font=20)

cb = ttk.Combobox(
        frame, textvariable=v, 
        values=fruits, width=10, height=10,font=("", 20, "underline"))
cb.set(fruits[0])
cb.bind('<<ComboboxSelected>>', combobox_func)
cb.grid(row=0, column=0)

# Button
button1 = ttk.Button(
    frame, text='OK',
    command=lambda: print('v=%s' % v.get()), style="office.TButton")
button1.grid(row=0, column=1)


# 表示
root.mainloop()