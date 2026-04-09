import tkinter as tk

# Lớp số phức
class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def cong(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    def tru(self, other):
        return SoPhuc(self.thuc - other.thuc, self.ao - other.ao)

    def nhan(self, other):
        return SoPhuc(
            self.thuc * other.thuc - self.ao * other.ao,
            self.thuc * other.ao + self.ao * other.thuc
        )

    def chia(self, other):
        mau = other.thuc**2 + other.ao**2
        return SoPhuc(
            (self.thuc * other.thuc + self.ao * other.ao) / mau,
            (self.ao * other.thuc - self.thuc * other.ao) / mau
        )

    def __str__(self):
        return f"{self.thuc:.2f} {'+' if self.ao >= 0 else '-'} {abs(self.ao):.2f}i"


# Xử lý khi bấm nút
def tinh():
    try:
        a = SoPhuc(float(a_real.get()), float(a_imag.get()))
        b = SoPhuc(float(b_real.get()), float(b_imag.get()))

        kq = ""
        kq += f"a + b = {a.cong(b)}\n"
        kq += f"a - b = {a.tru(b)}\n"
        kq += f"a * b = {a.nhan(b)}\n"
        kq += f"a / b = {a.chia(b)}\n"

        output.delete("1.0", tk.END)
        output.insert(tk.END, kq)

    except:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Lỗi dữ liệu!")

# Giao diện
root = tk.Tk()
root.title("Số phức")
root.geometry("500x400")
root.configure(bg="#f5f7fa")

label_style = {"bg": "#f5f7fa", "fg": "#2c3e50", "font": ("Arial", 12)}

# Nhập số a
tk.Label(root, text="Số phức a:", **label_style).pack()
a_real = tk.Entry(root)
a_real.pack()
a_imag = tk.Entry(root)
a_imag.pack()

# Nhập số b
tk.Label(root, text="Số phức b:", **label_style).pack()
b_real = tk.Entry(root)
b_real.pack()
b_imag = tk.Entry(root)
b_imag.pack()

# Nút tính
tk.Button(root, text="Tính toán",
          command=tinh,
          bg="#a8dadc", fg="#1d3557",
          font=("Arial", 11), bd=0).pack(pady=10)

# Kết quả
output = tk.Text(root, height=10, bg="#ffffff", font=("Consolas", 11))
output.pack(padx=10, fill="both", expand=True)

root.mainloop()