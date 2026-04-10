import tkinter as tk
from tkinter import messagebox
import random
import os

# --- LOGIC XỬ LÝ ---
def save_matrix(filename, rows, cols):
    try:
        with open(filename, 'w') as f:
            f.write(f"{rows} {cols}\n")
            matrix_data = ""
            for _ in range(rows):
                # Tạo số thực ngẫu nhiên từ 0.0 đến 10.0
                row_vals = [round(random.uniform(0, 10), 2) for _ in range(cols)]
                line = " ".join(map(str, row_vals))
                f.write(line + "\n")
                matrix_data += line + "\n"
        return matrix_data
    except Exception as e:
        return f"Lỗi: {str(e)}"

def read_matrix(filename):
    if not os.path.exists(filename): return None
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            rows, cols = map(int, lines[0].split())
            data = [list(map(float, line.split())) for line in lines[1:]]
            return {"rows": rows, "cols": cols, "data": data}
    except: return None

# --- GIAO DIỆN ĐỒ HỌA ---
class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chương Trình Ma Trận - Bài 185")
        self.root.geometry("550x650")
        
        # Tiêu đề chính
        tk.Label(root, text="QUẢN LÝ MA TRẬN TỪ FILE", font=("Arial", 14, "bold")).pack(pady=10)

        # KHU VỰC NHẬP KÍCH THƯỚC
        input_frame = tk.LabelFrame(root, text=" Nhập kích thước ma trận ", padx=20, pady=20)
        input_frame.pack(pady=10, fill="x", padx=20)

        # Ma trận 1
        tk.Label(input_frame, text="Ma trận 1: Số dòng (m)").grid(row=0, column=0, sticky="w")
        self.ent_m1 = tk.Entry(input_frame, width=10)
        self.ent_m1.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Số cột (n)").grid(row=0, column=2, sticky="w")
        self.ent_n1 = tk.Entry(input_frame, width=10)
        self.ent_n1.grid(row=0, column=3, padx=5, pady=5)

        # Ma trận 2
        tk.Label(input_frame, text="Ma trận 2: Số dòng (m)").grid(row=1, column=0, sticky="w")
        self.ent_m2 = tk.Entry(input_frame, width=10)
        self.ent_m2.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Số cột (n)").grid(row=1, column=2, sticky="w")
        self.ent_n2 = tk.Entry(input_frame, width=10)
        self.ent_n2.grid(row=1, column=3, padx=5, pady=5)

        # Tên file
        tk.Label(root, text="Tên file ma trận 1:").pack()
        self.file1 = tk.Entry(root, width=30); self.file1.insert(0, "MT1.txt"); self.file1.pack()
        
        tk.Label(root, text="Tên file ma trận 2:").pack()
        self.file2 = tk.Entry(root, width=30); self.file2.insert(0, "MT2.txt"); self.file2.pack()

        # NÚT BẤM
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="TẠO FILE MA TRẬN", command=self.handle_generate, 
                  bg="#2196F3", fg="white", font=("Arial", 10, "bold"), padx=10).pack(side="left", padx=10)
        
        tk.Button(btn_frame, text="NHÂN HAI MA TRẬN", command=self.handle_multiply, 
                  bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10).pack(side="left", padx=10)

        # KHU VỰC HIỂN THỊ
        tk.Label(root, text="Kết quả hiển thị:").pack()
        self.display = tk.Text(root, height=15, width=65, bg="#f9f9f9")
        self.display.pack(pady=5, padx=20)

    def handle_generate(self):
        try:
            # Lấy giá trị từ bàn phím (Entry)
            m1 = int(self.ent_m1.get())
            n1 = int(self.ent_n1.get())
            m2 = int(self.ent_m2.get())
            n2 = int(self.ent_n2.get())

            res1 = save_matrix(self.file1.get(), m1, n1)
            res2 = save_matrix(self.file2.get(), m2, n2)

            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, f"Đã tạo file {self.file1.get()}:\n{res1}\n")
            self.display.insert(tk.END, f"Đã tạo file {self.file2.get()}:\n{res2}")
            messagebox.showinfo("Thành công", "Đã tạo 2 file dựa trên kích thước bạn nhập!")
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập kích thước là các số nguyên!")

    def handle_multiply(self):
        f1, f2 = self.file1.get(), self.file2.get()
        f_res = "KETQUA.txt"
        
        m1_data = read_matrix(f1)
        m2_data = read_matrix(f2)

        if not m1_data or not m2_data:
            messagebox.showwarning("Lỗi", "Hãy nhấn nút Tạo File trước khi nhân!")
            return

        if m1_data['cols'] != m2_data['rows']:
            err = f"Không thể nhân: Cột ma trận 1 ({m1_data['cols']}) khác Dòng ma trận 2 ({m2_data['rows']})!"
            self.display.delete(1.0, tk.END)
            self.display.insert(tk.END, err)
            messagebox.showerror("Lỗi kích thước", err)
            return

        # Tính toán nhân
        res_rows, res_cols = m1_data['rows'], m2_data['cols']
        display_str = ""
        with open(f_res, 'w') as f:
            f.write(f"{res_rows} {res_cols}\n")
            for i in range(res_rows):
                row_vals = []
                for j in range(res_cols):
                    val = sum(m1_data['data'][i][k] * m2_data['data'][k][j] for k in range(m1_data['cols']))
                    row_vals.append(round(val, 2))
                line = " ".join(map(str, row_vals))
                f.write(line + "\n")
                display_str += line + "\n"

        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, f"KẾT QUẢ NHÂN MA TRẬN (Lưu tại {f_res}):\n{display_str}")
        messagebox.showinfo("Xong", "Đã nhân và lưu file KETQUA.txt")

if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()