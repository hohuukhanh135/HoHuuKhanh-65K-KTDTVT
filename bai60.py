import tkinter as tk
from tkinter import messagebox
import random

# ===== Tạo mảng =====
def tao_mang(n):
    return [random.randint(-100, 100) for _ in range(n)]

# ===== Perfect Shuffle =====
def shuffle(arr):
    n = len(arr)
    half = n // 2
    result = []

    for i in range(half):
        result.append(arr[i])
        result.append(arr[i + half])

    return result

# ===== Xử lý =====
def xu_ly():
    try:
        n = int(entry_n.get())

        if n <= 0 or n % 2 != 0:
            messagebox.showerror("Lỗi", "n phải là số chẵn > 0")
            return

        arr = tao_mang(n)
        arr_goc = arr.copy()

        # Hiển thị mảng ban đầu
        text_kq.delete(1.0, tk.END)
        text_kq.insert(tk.END, f"Mảng ban đầu:\n{arr}\n\n")

        # Trộn 1 lần
        shuffled = shuffle(arr)
        text_kq.insert(tk.END, f"Sau 1 lần shuffle:\n{shuffled}\n\n")

        # Đếm số lần để quay lại ban đầu
        count = 1
        temp = shuffled.copy()

        while temp != arr_goc:
            temp = shuffle(temp)
            count += 1

        text_kq.insert(tk.END, f"Số lần trộn để quay lại ban đầu: {count}")

    except:
        messagebox.showerror("Lỗi", "Nhập số hợp lệ!")

# ===== Giao diện =====
root = tk.Tk()
root.title("Perfect Shuffle")
root.geometry("500x400")
root.configure(bg="#f0fff0")

# Tiêu đề
tk.Label(root,
         text="PERFECT SHUFFLE",
         font=("Arial", 14, "bold"),
         fg="darkblue",
         bg="#f0fff0").pack(pady=10)

# Nhập n
tk.Label(root,
         text="Nhập n (chẵn):",
         fg="green",
         bg="#f0fff0").pack()

entry_n = tk.Entry(root)
entry_n.pack(pady=5)

# Nút chạy
tk.Button(root,
          text="Thực hiện",
          bg="orange",
          fg="white",
          font=("Arial", 10, "bold"),
          command=xu_ly).pack(pady=10)

# Kết quả
text_kq = tk.Text(root, height=15)
text_kq.pack(padx=10, pady=10)

root.mainloop()