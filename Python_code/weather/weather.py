#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/27 14:43
# @Author  : 刘宇
# @File    : weather.py
from urllib.request import urlretrieve
import requests
import tkinter as tk


class MainForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("天气查询")
        self.master.geometry("300x200")
        self.weather_label = tk.Label(self, text="天气情况")
        self.wweather_label.pack()
        self.weather_btn = tk.Button(self, text="获取天气", command=self.get_weather)
        self.weather_btn.pack()
        self.get_weather()
        self.after(1000 * 60, self.get_weather)

        def get_weather(self):
            url = "https://weather.cma.cn/api/now/56386"
            weather_data = requests.get(url).json()
            location = weather_data['data']['location']['name']
            temperature = weather_data['data']['now']['temperature']
            pressure = weather_data['data']['now']['pressure']
            humidity = weather_data['data']['now']['humidity']
            windDirection = weather_data['data']['now']['windDirection']
            windDirectionDegree = weather_data['data']['now']['windDirectionDegree']
            windSpeed = weather_data['data']['now']['windSpeed']
            windScale = weather_data['data']['now']['windScale']
            print(location, temperature, pressure, humidity, windDirection, windDirectionDegree, windSpeed, windScale)
            self.weather_label.config(
                text=f"地点：{location}  \n温度： {temperature}°C \n气压：{pressure}hPa \n湿度：{humidity}%\n风向： {windDirection} \n风向角度：{windDirectionDegree}°\n 风速: {windSpeed}m/s \n风力等级：{windScale}级")


if __name__ == "__main__":
    app = tk.Tk()
    mainform = MainForm(app)
    mainform.pack()
    app.mainloop()
    run_code = 0
