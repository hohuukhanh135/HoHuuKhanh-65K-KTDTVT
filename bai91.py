import tkinter as tk
import random
from tkinter import messagebox

# ===== Tạo ma trận ngẫu nhiên n x m =====
def tao_ma_tran(n, m):
    # Tạo ma trận gồm n dòng, mỗi dòng m phần tử (0 hoặc 1)
    return [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

# ===== Lấy ma trận con =====
def lay_ma_tran_con(A, start_row, start_col, rows, cols):
    # Lấy từ dòng start_row đến start_row + rows
    # Và từ cột start_col đến start_col + cols
    return [row[start_col:start_col+cols] for row in A[start_row:start_row+rows]]

# ===== Chuyển ma trận thành chuỗi để in ra màn hình =====
def hien_thi(matrix):
    s = ""
    for row in matrix:
        # nối các phần tử trong 1 dòng thành chuỗi
        s += " ".join(map(str, row)) + "\n"
    return s

# ===== Xử lý khi bấm nút =====
def xu_ly():
    try:
        # Tạo ma trận A 20x20
        A = tao_ma_tran(20, 20)

        # Lấy ma trận con B:
        # bắt đầu tại A[3][4], kích thước 8x12
        B = lay_ma_tran_con(A, 3, 4, 8, 12)

        # Xóa nội dung cũ trong ô hiển thị
        text_kq.delete(1.0, tk.END)

        # Hiển thị ma trận A
        text_kq.insert(tk.END, "Ma trận A (20x20):\n")
        text_kq.insert(tk.END, hien_thi(A) + "\n")

        # Hiển thị ma trận con B
        text_kq.insert(tk.END, "Ma trận con B (8x12):\n")
        text_kq.insert(tk.END, hien_thi(B))

    except:
        # Báo lỗi nếu có vấn đề
        messagebox.showerror("Lỗi", "Có lỗi xảy ra!")

# ===== Tạo cửa sổ =====
root = tk.Tk()
root.title("Bài 91 - Ma trận con")
root.geometry("600x500")

# Đặt màu nền
root.configure(bg="#f5f5ff")

# ===== Tiêu đề =====
tk.Label(root,
         text="TRÍCH MA TRẬN CON",
         font=("Arial", 14, "bold"),
         fg="darkblue",
         bg="#f5f5ff").pack(pady=10)

# ===== Nút bấm =====
tk.Button(root,
          text="Tạo và trích ma trận",
          bg="orange",
          fg="white",
          font=("Arial", 10, "bold"),
          command=xu_ly).pack(pady=10)

# ===== Ô hiển thị kết quả =====
text_kq = tk.Text(root, height=25)
text_kq.pack(padx=10, pady=10)

# ===== Chạy chương trình =====
root.mainloop()