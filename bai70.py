import tkinter as tk
import random

# Hàm tạo mảng ngẫu nhiên
def tao_mang():
    try:
        n = int(entry_n.get())
        arr = [random.randint(-100, 100) for _ in range(n)]
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, " ".join(map(str, arr)))
    except:
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, "Nhập n hợp lệ!")

# Hàm xử lý
def xu_ly():
    try:
        arr = list(map(int, text_input.get("1.0", tk.END).strip().split()))
        
        le = [x for x in arr if x % 2 != 0]
        zero = [x for x in arr if x == 0]
        chan = [x for x in arr if x % 2 == 0 and x != 0]
        
        result = le + zero + chan
        
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, " ".join(map(str, result)))
    except:
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "Lỗi dữ liệu!")

# Giao diện
root = tk.Tk()
root.title("Xử lý mảng")

tk.Label(root, text="Nhập n:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tạo mảng", command=tao_mang).pack()

tk.Label(root, text="Mảng ban đầu:").pack()
text_input = tk.Text(root, height=3)
text_input.pack()

tk.Button(root, text="Xử lý", command=xu_ly).pack()

tk.Label(root, text="Kết quả:").pack()
text_output = tk.Text(root, height=3)
text_output.pack()

root.mainloop()