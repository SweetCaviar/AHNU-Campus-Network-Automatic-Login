import requests
from tkinter import messagebox


def send_get_request(url, params=None):
    try:
        response = requests.get(url, params=params)
        # 检查响应状态码
        if response.status_code == 200:
            # 返回响应内容
            return response.text
        else:
            messagebox.showerror("错误", f"请求失败，状态码：{response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("错误", f"请求发生异常：{e}")
        return None
