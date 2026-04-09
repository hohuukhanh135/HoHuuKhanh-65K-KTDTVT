import tkinter as tk
from tkinter import messagebox

def tim_m():
    try:
        n = int(entry_n.get())

        tong = 0
        m = 0

        while tong + (m + 1) < n:
            m += 1
            tong += m

        label_kq.config(text="m lớn nhất = " + str(m), fg="blue")

    except:
        messagebox.showerror("Lỗi", "Nhập số nguyên hợp lệ!")

root = tk.Tk()
root.title("Tìm m")
root.geometry("300x200")
root.configure(bg="#e6f7ff")

tk.Label(root, text="Nhập n:",
         bg="#e6f7ff",
         fg="darkgreen").pack(pady=5)

entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tìm m",
          bg="orange",
          fg="white",
          command=tim_m).pack(pady=10)

label_kq = tk.Label(root, text="Kết quả:",
                    bg="#e6f7ff",
                    fg="purple",
                    font=("Arial", 12, "bold"))
label_kq.pack()

root.mainloop()