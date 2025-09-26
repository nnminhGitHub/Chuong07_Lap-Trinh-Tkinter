'''
Tkinter là thư viên thiết kế giao diện tương tác người dùng Graphic User Interface (GUI)
Trình tự các bước để tạo ra một ứng dụng Tkinter gồm:
- import Tkinter module
- Tạo cửa sổ chính của ứng dụng GUI
- Thêm một hoặc nhiều widget vào ứng dụng GUI
- Gọi vòng lặp sự kiện chính để các hành động có thể diễn ra trên màn hình máy tính
  của người dùng
'''
# Nhập module tkinter để bạn có thể sử dụng các thành phần của nó, 
# thường được đặt tên viết tắt là tk để tiện sử dụng.
import tkinter as tk

# 1. root = tk.Tk(): Tạo một cửa sổ chính, đây là nơi tất cả các widget khác sẽ được đặt vào.
root = tk.Tk()
# Đặt tiêu đề hiển thị ở thanh tiêu đề của cửa sổ
root.title("Giao diện Tkinter đơn giản") # Đặt tiêu đề cho cửa sổ

# 2. Thêm một widget Label: Tạo một widget nhãn (label) để hiển thị văn bản trong cửa sổ.
label = tk.Label(root, text="Xin chào Tkinter!")
label.pack() # Đưa widget vào cửa sổ

# 3. Thêm một widget Button:
def nhan_nut():
    label.config(text="Bạn đã nhấn nút!")

button = tk.Button(root, text="Nhấn tôi", command=nhan_nut)
button.pack() # Đưa widget vào cửa sổ

# 4. Chạy vòng lặp sự kiện để cửa sổ hoạt động
root.mainloop()



