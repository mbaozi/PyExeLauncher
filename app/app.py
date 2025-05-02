# PyExeLauncher 示例程序
# author: mbaozi
# date: 2025.05.02

import tkinter as tk

print("Hello, PyExeLauncher!")

def exit_program():
    print("Exiting program...")
    # 关闭窗口并退出程序
    root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("PyExeLauncher")

# 设置窗口大小
root.geometry("300x160")

# 设置窗口图标
root.iconbitmap('app/icon.ico')

# 创建一个标签
label = tk.Label(root, text="PyExeLauncher DEMO", font=("Arial", 14))
label.pack(pady=20)  # 使用pack布局，添加一些垂直间距

# 创建一个按钮，点击后调用exit_program函数
button = tk.Button(root, text="退出程序", command=exit_program, font=("Arial", 14))
button.pack(pady=20)

# 启动主循环，让窗口保持打开状态
root.mainloop()