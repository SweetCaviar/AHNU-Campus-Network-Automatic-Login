import os
import sys
import winshell
from win32com.client import Dispatch
from tkinter import messagebox

def shortcut_exists(shortcut_name):
    startup_folder = winshell.startup()  # 获取启动目录
    shortcut_path = os.path.join(startup_folder, f"{shortcut_name}.lnk")  # 创建快捷方式路径
    return os.path.exists(shortcut_path)


def create_shortcut(target, shortcut_name, start_in=None):
    startup_folder = winshell.startup()  # 获取启动目录
    shortcut_path = os.path.join(startup_folder, f"{shortcut_name}.lnk")  # 创建快捷方式路径

    shell = Dispatch('WScript.Shell')  # 创建Shell对象
    shortcut = shell.CreateShortCut(shortcut_path)  # 创建快捷方式对象
    shortcut.TargetPath = target  # 设置目标路径
    if start_in:
        shortcut.WorkingDirectory = start_in  # 设置起始路径
    shortcut.save()  # 保存快捷方式
    messagebox.showinfo("提示", f"已成功将脚本添加到自启动文件夹！")