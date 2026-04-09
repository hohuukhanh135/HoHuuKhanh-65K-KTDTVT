import tkinter as tk
from tkinter import messagebox

# --- HÀM XỬ LÝ LOGIC ---

def nen_run_length(s):
    """Hàm nén chuỗi theo thuật toán Run-length"""
    if not s: return ""
    res = ""
    i = 0
    while i < len(s):
        count = 1
        # Đếm số lượng ký tự giống nhau liên tiếp
        while i + 1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        
        # Nếu count > 1 thì thêm số lượng trước ký tự (VD: 3a)
        # Nếu count = 1 thì chỉ thêm ký tự đó (VD: b)
        if count > 1:
            res += str(count) + s[i]
        else:
            res += s[i]
        i += 1
    return res

def giai_nen_run_length(s):
    """Hàm giải nén chuỗi"""
    res = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            # Nếu là số, ta cần lấy toàn bộ các chữ số liên tiếp (VD: '12')
            num_str = ""
            while i < len(s) and s[i].isdigit():
                num_str += s[i]
                i += 1
            # Sau số lượng chắc chắn là ký tự cần lặp
            res += s[i] * int(num_str)
        else:
            # Nếu không phải số, ký tự đó xuất hiện 1 lần
            res += s[i]
        i += 1
    return res

# --- HÀM XỬ LÝ GIAO DIỆN ---

def thuc_hien_nen():
    input_str = entry_input.get()
    # Kiểm tra xem chuỗi có chứa số không (theo đề bài)
    if any(char.isdigit() for char in input_str):
        messagebox.showwarning("Cảnh báo", "Chuỗi gốc không được chứa ký tự số!")
        return
    
    encoded = nen_run_length(input_str)
    # Tính toán tỷ lệ nén
    ratio = (len(encoded) / len(input_str)) * 100 if len(input_str) > 0 else 0
    
    label_nen.config(text=f"Nén: {encoded} [{ratio:.1f}%]")
    label_giai_nen.config(text=f"Giải nén: {giai_nen_run_length(encoded)}")

# --- THIẾT LẬP MÀN HÌNH ĐỒ HỌA ---

root = tk.Tk()
root.title("Chương trình Nén Run-length")
root.geometry("600x300")

# Thành phần nhập liệu
tk.Label(root, text="Nhập chuỗi gốc:", font=("Arial", 11)).pack(pady=10)
entry_input = tk.Entry(root, width=60, font=("Courier", 10))
entry_input.pack(pady=5)

# Nút bấm thực hiện
btn_run = tk.Button(root, text="Thực hiện Nén & Giải nén", command=thuc_hien_nen, bg="#4CAF50", fg="white")
btn_run.pack(pady=15)

# Vùng hiển thị kết quả (giả lập màn hình console trong ảnh)
frame_result = tk.Frame(root, bg="#d3d3d3", padx=10, pady=10)
frame_result.pack(fill="both", expand=True, padx=20, pady=10)

label_nen = tk.Label(frame_result, text="Nen: ", bg="#d3d3d3", font=("Courier", 10), anchor="w", justify="left")
label_nen.pack(fill="x")

label_giai_nen = tk.Label(frame_result, text="Giai nen: ", bg="#d3d3d3", font=("Courier", 10), anchor="w", justify="left")
label_giai_nen.pack(fill="x")

root.mainloop()