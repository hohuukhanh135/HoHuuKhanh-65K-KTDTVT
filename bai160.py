import tkinter as tk

# Hàm sinh hoán vị (đệ quy)
def hoan_vi(s, path, used, result):
    if len(path) == len(s):
        result.append("".join(path))
        return
    
    for i in range(len(s)):
        if not used[i]:
            used[i] = True
            path.append(s[i])
            
            hoan_vi(s, path, used, result)
            
            path.pop()
            used[i] = False

# Xử lý khi bấm nút
def xu_ly():
    s = entry.get().strip()
    result = []
    
    used = [False] * len(s)
    hoan_vi(s, [], used, result)
    
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, " ".join(result))

# Giao diện
root = tk.Tk()
root.title("Hoán vị chuỗi")
root.geometry("500x350")
root.configure(bg="#f5f7fa")  # nền nhẹ

label_style = {"bg": "#f5f7fa", "fg": "#2c3e50", "font": ("Arial", 12)}

tk.Label(root, text="Nhập chuỗi:", **label_style).pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

tk.Button(root, text="Tạo hoán vị",
          command=xu_ly,
          bg="#a8dadc", fg="#1d3557",
          font=("Arial", 11), padx=10, pady=5, bd=0).pack(pady=10)

tk.Label(root, text="Kết quả:", **label_style).pack(pady=5)

text_output = tk.Text(root, height=8, bg="#ffffff", font=("Consolas", 11))
text_output.pack(padx=10, fill="both", expand=True)

root.mainloop()