import tkinter as tk
from tkinter import messagebox

# ===== Node =====
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ===== Tạo danh sách =====
def create_list(arr):
    head = None
    tail = None

    for x in arr:
        new_node = Node(x)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


# ===== In danh sách =====
def list_to_string(head):
    result = []
    p = head
    while p:
        result.append(str(p.data))
        p = p.next
    return " ".join(f"[{x}]" for x in result)


# ===== Xóa giá trị =====
def delete_value(head, k):
    while head and head.data == k:
        head = head.next

    p = head
    while p and p.next:
        if p.next.data == k:
            p.next = p.next.next
        else:
            p = p.next

    return head


# ===== Xử lý khi bấm nút =====
def xu_ly():
    try:
        arr = list(map(int, entry_list.get().split()))
        k = int(entry_k.get())

        head = create_list(arr)

        list_goc.config(text="List gốc: " + list_to_string(head))

        head = delete_value(head, k)

        list_moi.config(text="List mới: " + list_to_string(head))

    except:
        messagebox.showerror("Lỗi", "Nhập sai định dạng!")


# ===== Giao diện =====
root = tk.Tk()
root.title("Danh sách liên kết")
root.geometry("500x300")
root.configure(bg="#eef7ff")

# Tiêu đề
tk.Label(root, text="XÓA NODE TRONG LINKED LIST",
         font=("Arial", 14, "bold"),
         fg="darkred", bg="#eef7ff").pack(pady=10)

# Nhập list
tk.Label(root, text="Nhập dãy (cách nhau bởi khoảng trắng):",
         bg="#eef7ff").pack()

entry_list = tk.Entry(root, width=40)
entry_list.pack(pady=5)

# Nhập k
tk.Label(root, text="Nhập giá trị cần xóa:",
         bg="#eef7ff").pack()

entry_k = tk.Entry(root)
entry_k.pack(pady=5)

# Nút
tk.Button(root, text="Thực hiện",
          bg="orange", fg="white",
          command=xu_ly).pack(pady=10)

# Kết quả
list_goc = tk.Label(root, text="List gốc:",
                    bg="#eef7ff", fg="blue")
list_goc.pack()

list_moi = tk.Label(root, text="List mới:",
                    bg="#eef7ff", fg="green")
list_moi.pack()

root.mainloop()