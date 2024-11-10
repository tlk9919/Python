#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/6 9:16
# @Author  : 刘宇
# @File    : pythonwork1_QQmusic.py
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json
import threading
from PIL import Image, ImageTk


def fetch_qq_music_singer_list_and_save(root, progress_window):
    try:
        # 发送GET请求获取歌手列表接口数据
        url = "https://y.qq.com/n/ryqq/singer_list"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查响应状态

        # 提取数据
        data = response.text

        # 将数据保存到文件中
        with open("QQ_music_singer_list.json", "w", encoding="utf-8") as file:
            json.dump(data, file)

        messagebox.showinfo("成功", "QQ音乐歌手列表接口数据保存成功！")

        # 关闭主窗口
        root.destroy()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("错误", f"获取数据失败: {e}")
        # 如果发生错误，关闭进度窗口
        progress_window.destroy()


def show_progress(root):
    progress_window = tk.Toplevel(root)
    progress_window.title("数据加载中")

    # 获取屏幕宽高
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置进度窗口位置为屏幕中间
    window_width = 300
    window_height = 150
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    progress_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    progress_label = tk.Label(progress_window, text="数据加载中，请稍候...")
    progress_label.pack(pady=10)

    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=5)

    # 在新线程中执行数据获取任务，并传入主窗口对象和标签对象
    threading.Thread(target=fetch_qq_music_singer_list_and_save, args=(root, progress_window)).start()

    # 更新加载百分比
    update_progress(progress_bar, progress_label)


def update_progress(progress_bar, progress_label):
    progress = 0
    while progress < 100:
        progress_bar["value"] = progress
        progress_label.config(text=f"加载进度：{progress}%")
        progress += 1
        progress_bar.update_idletasks()
        progress_label.update_idletasks()

        # 等待一段时间，模拟加载进度
        root.after(50)


# 创建主窗口
root = tk.Tk()
root.title("QQ音乐歌手列表接口数据获取与保存")

# 设置主窗口背景色为蓝色
root.configure(bg='green')

# 调整图标的大小
icon_size = (32, 32)  # 设置图标的目标大小
icon_image = Image.open('QQmusic_img.ico')  # 请替换为您的图标文件路径
icon_image = icon_image.resize(icon_size, resample=Image.BICUBIC)
icon_photo = ImageTk.PhotoImage(icon_image)

# 设置主窗口图标
root.iconphoto(True, icon_photo)

# 获取屏幕宽高
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置主窗口位置为屏幕中间
window_width = 300
window_height = 150
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 创建标签
label = tk.Label(root, text="点击下方按钮获取QQ音乐歌手列表接口数据", bg='blue', fg='white')
label.pack(pady=10)

# 创建按钮
button = tk.Button(root, text="获取并以json格式存储数据", command=lambda: show_progress(root))
button.pack(pady=5)

# 运行主循环
root.mainloop()

if __name__ == "__main__":
    run_code = 0
