import tkinter as tk
from tkinter import messagebox

# ===== Đệ quy =====
def hoan_vi(s, current, result):
    if len(s) == 0:
        result.append(current)
        return

    for i in range(len(s)):
        ch = s[i]
        con_lai = s[:i] + s[i+1:]
        hoan_vi(con_lai, current + ch, result)


# ===== Xử lý =====
def xu_ly():
    try:
        n = int(entry_n.get())

        if n <= 0 or n > 10:
            messagebox.showerror("Lỗi", "n phải từ 1 đến 10")
            return

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = alphabet[:n]

        result = []
        hoan_vi(s, "", result)

        text_kq.delete(1.0, tk.END)
        text_kq.insert(tk.END, "Các hoán vị:\n")

        for x in result:
            text_kq.insert(tk.END, x + " ")

        text_kq.insert(tk.END, f"\n\nTổng: {len(result)}")

    except:
        messagebox.showerror("Lỗi", "Nhập số hợp lệ!")


# ===== GUI =====
root = tk.Tk()
root.title("Hoán vị đệ quy")
root.geometry("500x400")

tk.Label(root, text="Nhập n:",
         font=("Arial", 12)).pack(pady=5)

entry_n = tk.Entry(root)
entry_n.pack(pady=5)

tk.Button(root, text="Tạo hoán vị",
          command=xu_ly).pack(pady=10)

text_kq = tk.Text(root, height=15)
text_kq.pack(padx=10, pady=10)

root.mainloop()
