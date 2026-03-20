import tkinter as tk
from tkinter import messagebox

def tim_m():
    try:
        n = int(entry_n.get())

        if n <= 0:
            messagebox.showerror("Lỗi", "n phải > 0")
            return

        tong = 0
        m = 0

        while tong + (m + 1) < n:
            m += 1
            tong += m

        label_kq.config(
            text=f"m lớn nhất = {m}",
            fg="blue"
        )

    except:
        messagebox.showerror("Lỗi", "Nhập số nguyên hợp lệ!")

# ===== Giao diện =====
root = tk.Tk()
root.title("Tìm m lớn nhất")
root.geometry("350x250")
root.configure(bg="#eef7ff")

# Tiêu đề
tk.Label(root,
         text="TÌM m LỚN NHẤT",
         font=("Arial", 14, "bold"),
         fg="darkred",
         bg="#eef7ff").pack(pady=10)

# Nhập n
tk.Label(root,
         text="Nhập số n:",
         fg="green",
         bg="#eef7ff").pack()

entry_n = tk.Entry(root, font=("Arial", 11))
entry_n.pack(pady=5)

# Nút bấm
tk.Button(root,
          text="Tính",
          bg="orange",
          fg="white",
          font=("Arial", 10, "bold"),
          command=tim_m).pack(pady=10)

# Kết quả
label_kq = tk.Label(root,
                    text="Kết quả:",
                    font=("Arial", 12, "bold"),
                    fg="purple",
                    bg="#eef7ff")
label_kq.pack()

root.mainloop()