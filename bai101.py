import tkinter as tk
from tkinter import messagebox

# ===== Tạo ô nhập ma trận =====
def tao_ma_tran():
    try:
        global entries, n
        n = int(entry_n.get())

        if n <= 0:
            raise ValueError

        # Xóa ma trận cũ
        for widget in frame_matrix.winfo_children():
            widget.destroy()

        entries = []

        # Tạo lưới nhập
        for i in range(n):
            row = []
            for j in range(n):
                e = tk.Entry(frame_matrix, width=5, justify='center')
                e.grid(row=i, column=j, padx=2, pady=2)
                row.append(e)
            entries.append(row)

    except:
        messagebox.showerror("Lỗi", "Nhập n hợp lệ!")

# ===== Xử lý =====
def xu_ly():
    try:
        matrix = []

        # Lấy dữ liệu
        for i in range(n):
            row = []
            for j in range(n):
                val = int(entries[i][j].get())
                row.append(val)
            matrix.append(row)

        # Tổng hàng
        tong_hang = [sum(row) for row in matrix]

        # Tổng cột
        tong_cot = [sum(matrix[i][j] for i in range(n)) for j in range(n)]

        # Tổng đường chéo
        cheo1 = sum(matrix[i][i] for i in range(n))
        cheo2 = sum(matrix[i][n-i-1] for i in range(n))

        # Hiển thị
        text_kq.delete("1.0", tk.END)

        for i in range(n):
            text_kq.insert(tk.END, f"Tổng hàng {i}: {tong_hang[i]}\n")

        for j in range(n):
            text_kq.insert(tk.END, f"Tổng cột {j}: {tong_cot[j]}\n")

        text_kq.insert(tk.END, f"Chéo chính: {cheo1}\n")
        text_kq.insert(tk.END, f"Chéo phụ: {cheo2}\n")

        # Kiểm tra ma phương
        if (len(set(tong_hang)) == 1 and
            len(set(tong_cot)) == 1 and
            cheo1 == cheo2 == tong_hang[0]):

            text_kq.insert(tk.END, "\n=> Đây là MA PHƯƠNG ✅")
        else:
            text_kq.insert(tk.END, "\n=> KHÔNG phải ma phương ❌")

    except:
        messagebox.showerror("Lỗi", "Nhập đầy đủ số!")

# ===== GUI =====
root = tk.Tk()
root.title("Kiểm tra ma phương")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Nhập n
tk.Label(root, text="Nhập n:",
         bg="#f0f8ff").pack()

entry_n = tk.Entry(root)
entry_n.pack()

tk.Button(root, text="Tạo ma trận",
          command=tao_ma_tran).pack(pady=5)

# Frame ma trận
frame_matrix = tk.Frame(root, bg="#f0f8ff")
frame_matrix.pack()

# Nút xử lý
tk.Button(root, text="Kiểm tra",
          bg="green", fg="white",
          command=xu_ly).pack(pady=10)

# Kết quả
text_kq = tk.Text(root, height=12, width=50)
text_kq.pack()

root.mainloop()