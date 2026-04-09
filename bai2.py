import tkinter as tk
from tkinter import messagebox
import math

def tinh_khoang_cach():
    try:
        xA = float(entry_xA.get())
        yA = float(entry_yA.get())
        xB = float(entry_xB.get())
        yB = float(entry_yB.get())

        AB = math.sqrt((xB - xA)**2 + (yB - yA)**2)

        label_kq.config(text="Khoảng cách |AB| = " + str(round(AB, 4)), fg="blue")

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Tính khoảng cách 2 điểm")
root.geometry("400x320")
root.configure(bg="#f0f8ff")  # màu nền (xanh nhạt)

# Tiêu đề
tk.Label(root, text="TÍNH KHOẢNG CÁCH AB",
         font=("Arial", 14, "bold"),
         fg="darkred",
         bg="#f0f8ff").pack(pady=10)

# Điểm A
tk.Label(root, text="Điểm A (xA, yA)", fg="green", bg="#f0f8ff").pack()
entry_xA = tk.Entry(root)
entry_xA.pack()
entry_yA = tk.Entry(root)
entry_yA.pack()

# Điểm B
tk.Label(root, text="Điểm B (xB, yB)", fg="green", bg="#f0f8ff").pack()
entry_xB = tk.Entry(root)
entry_xB.pack()
entry_yB = tk.Entry(root)
entry_yB.pack()

# Nút bấm
tk.Button(root, text="Khoảng cách",
          bg="red",
          fg="white",
          font=("Arial", 10, "bold"),
          command=tinh_khoang_cach).pack(pady=10)

# Kết quả
label_kq = tk.Label(root, text="|AB| = ",
                    font=("Arial", 12, "bold"),
                    fg="purple",
                    bg="#f0f8ff")
label_kq.pack()

root.mainloop()