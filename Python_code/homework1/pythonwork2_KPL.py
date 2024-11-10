#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/4/8 16:32
# @Author  : 刘宇
# @File    : pythonwork2_KPL.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
from PIL import Image, ImageTk


def fetch_hero_data_and_save():
    try:
        # 发送GET请求获取网页内容
        url = "https://pvp.qq.com/web201605/herolist.shtml"
        response = requests.get(url)
        response.raise_for_status()  # 检查响应状态

        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # 找到英雄列表
        hero_list = soup.find("ul", class_="herolist clearfix").find_all("li")

        # 提取英雄信息
        hero_info = []
        for hero in hero_list:
            name = hero.find("img")["alt"]
            img_url = hero.find("img")["src"]
            hero_info.append({"name": name, "img_url": img_url})

        # 将数据保存到文件中
        with open("KPL_heroes.json", "w", encoding="utf-8") as file:
            json.dump(hero_info, file, ensure_ascii=False, indent=4)

        messagebox.showinfo("成功", "英雄数据保存成功！")
        open_time_window()  # 成功保存数据后打开新窗口显示系统时间和关闭按钮
    except requests.exceptions.RequestException as e:
        messagebox.showerror("错误", f"获取数据失败: {e}")


def open_time_window():
    # 创建新窗口
    time_window = tk.Toplevel(root)
    time_window.title("创建json文件时间")

    # 设置窗口大小
    time_window.geometry("300x300")

    # 居中显示
    window_width = time_window.winfo_reqwidth()
    window_height = time_window.winfo_reqheight()
    position_right = int(time_window.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(time_window.winfo_screenheight() / 2 - window_height / 2)
    time_window.geometry("+{}+{}".format(position_right, position_down))

    # 获取系统时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 创建标签，显示系统时间
    time_label = tk.Label(time_window, text=f"创建时间：{current_time}")
    time_label.pack(pady=10)

    # 加载图片并创建标签显示图片
    image_path = "wzry.jpg"  # 修改为你的图片文件路径
    img = Image.open(image_path)
    # 根据窗口大小调整图片大小
    time_window.update()
    window_width = time_window.winfo_width()
    window_height = time_window.winfo_height()


    if window_width > 0 and window_height > 0:
       resized_img = img.resize((window_width - 20, window_height - 100))
       img_tk = ImageTk.PhotoImage(resized_img)
       img_label = tk.Label(time_window, image=img_tk)
       img_label.image = img_tk  # 保持引用，否则图片显示不出来
       img_label.pack()

    # 创建关闭按钮
    close_button = tk.Button(time_window, text="关闭", command=lambda: close_windows(time_window))
    close_button.pack(pady=5)


def close_windows(window):
    window.destroy()
    root.destroy()


# 创建主窗口
root = tk.Tk()
root.title("王者荣耀英雄数据接口")

# 设置窗口大小
root.geometry("300x300")


# 调整图标的大小
icon_size = (35, 35)  # 设置图标的目标大小
icon_image = Image.open('wzry.jpg')  # 请替换为您的图标文件路径
icon_image = icon_image.resize(icon_size, resample=Image.BICUBIC)
icon_photo = ImageTk.PhotoImage(icon_image)

# 设置主窗口图标
root.iconphoto(True, icon_photo)

# 居中显示
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))


# 加载图片并创建标签显示图片
image_path = "wzry.jpg"  # 修改为你的图片文件路径
img = Image.open(image_path)
# 根据窗口大小调整图片大小
root.update()
window_width = root.winfo_width()
window_height = root.winfo_height()

if window_width > 0 and window_height > 0:
    resized_img = img.resize((window_width - 20, window_height - 100))
    img_tk = ImageTk.PhotoImage(resized_img)
    img_label = tk.Label(root, image=img_tk)
    img_label.image = img_tk  # 保持引用，否则图片显示不出来
    img_label.pack()

# 创建按钮
button = tk.Button(root, text="获取并以json格式存储数据", command=fetch_hero_data_and_save)
button.pack(pady=5)
# 运行主循环
root.mainloop()

if __name__ == "__main__":
    run_code = 0
