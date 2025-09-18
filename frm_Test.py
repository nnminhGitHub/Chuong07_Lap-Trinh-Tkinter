import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


# ===== Hàm canh giữa cửa sổ =====
def center_window(win, w=630, h=480):
    ws = win.winfo_screenwidth()
    hs = win.winfo_screenheight()
    x = (ws // 2) - (w // 2)
    y = (hs // 2) - (h // 2)
    win.geometry(f'{w}x{h}+{x}+{y}')


# ===== CỬA SỔ CHÍNH =====
root = tk.Tk()
root.title("Quản lý nhân viên")
center_window(root, 630, 480)
root.resizable(False, False)

# ===== TIÊU ĐỀ =====
lbl_title = tk.Label(root, text="QUẢN LÝ NHÂN VIÊN", font=("Arial", 18, "bold"))
lbl_title.pack(pady=10)

# ===== FRAME THÔNG TIN =====
frame_info = tk.Frame(root)
frame_info.pack(pady=5, padx=10, fill="x")

# ===== MAIN LOOP =====
root.mainloop()
