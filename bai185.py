import tkinter as tk
from tkinter import filedialog, messagebox

# Đọc ma trận từ file
def doc_ma_tran(path):
    with open(path, "r") as f:
        lines = f.readlines()
    
    m, n = map(int, lines[0].split())
    matrix = [list(map(float, lines[i+1].split())) for i in range(m)]
    
    return matrix, m, n

# Nhân ma trận
def nhan(A, B, m, n, p):
    C = [[0]*p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Chọn file
def chon_file1():
    global file1
    file1 = filedialog.askopenfilename()
    lbl_file1.config(text=file1)

def chon_file2():
    global file2
    file2 = filedialog.askopenfilename()
    lbl_file2.config(text=file2)

# Xử lý
def tinh():
    try:
        A, m, n = doc_ma_tran(file1)
        B, n2, p = doc_ma_tran(file2)

        if n != n2:
            messagebox.showerror("Lỗi", "Không thể nhân ma trận!")
            return

        C = nhan(A, B, m, n, p)

        output.delete("1.0", tk.END)
        for row in C:
            output.insert(tk.END, " ".join(f"{x:.2f}" for x in row) + "\n")

    except:
        messagebox.showerror("Lỗi", "Chưa chọn file hoặc file sai định dạng!")

# Giao diện
root = tk.Tk()
root.title("Nhân ma trận")
root.geometry("550x400")
root.configure(bg="#f5f7fa")

label_style = {"bg": "#f5f7fa", "fg": "#2c3e50", "font": ("Arial", 12)}

tk.Label(root, text="Chọn file ma trận A:", **label_style).pack(pady=5)
tk.Button(root, text="Chọn file A", command=chon_file1,
          bg="#a8dadc", bd=0).pack()
lbl_file1 = tk.Label(root, text="", bg="#f5f7fa")
lbl_file1.pack()

tk.Label(root, text="Chọn file ma trận B:", **label_style).pack(pady=5)
tk.Button(root, text="Chọn file B", command=chon_file2,
          bg="#a8dadc", bd=0).pack()
lbl_file2 = tk.Label(root, text="", bg="#f5f7fa")
lbl_file2.pack()

tk.Button(root, text="Nhân ma trận",
          command=tinh,
          bg="#b7e4c7", bd=0, font=("Arial", 11)).pack(pady=10)

output = tk.Text(root, height=10, bg="#ffffff", font=("Consolas", 11))
output.pack(padx=10, fill="both", expand=True)

root.mainloop()