import logging
import sys
from tkinter import messagebox
import get_credentials
import user_input
import send_request
import auto_startup
import os


def setup_logging():
    # 设置日志记录器
    logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)


if __name__ == "__main__":
    # 获取当前脚本路径
    script_path = os.path.abspath(sys.argv[0])
    script_directory = os.path.dirname(script_path)

    # 获取脚本名称
    script_name = os.path.splitext(os.path.basename(script_path))[0]

    # 检查快捷方式是否已存在
    if not auto_startup.shortcut_exists(script_name):
        auto_startup.create_shortcut(script_path, script_name, script_directory)

    # 设置日志记录器
    setup_logging()

    # 尝试从本地文件中加载凭据
    user_account, user_password, provider = get_credentials.load_credentials()

    if user_account is None or user_password is None:
        # 如果本地文件中没有凭据，则获取用户输入
        user_account, user_password, provider = user_input.get_user_input()
        # 查询本机 MAC 地址
        # wlan_user_mac = get_credentials.get_mac_address()
        # 保存凭据到本地文件
        get_credentials.save_credentials(user_account, user_password, provider)

    # 获取本机 IP 地址
    # wlan_user_ip = get_credentials.get_ip_address()

    # 示例 URL
    base_url = "http://rz.ahnu.edu.cn:801/eportal/portal/login"

    # 构建查询参数字典
    params = {
        # "callback": "dr1003",
        # "login_method": "1",
        "user_account": f"{user_account}@{provider}",
        "user_password": user_password,
        # "wlan_user_ip": wlan_user_ip,
        # "wlan_user_ipv6": "",
        # "wlan_user_mac": wlan_user_mac,
        # "wlan_ac_ip": "100.64.4.10",
        # "wlan_ac_name": "bras1",
        # "jsVersion": "4.1.3",
        # "terminal_type": "1",
        # "lang": "zh-cn",
        # "v": v_value
    }

    # 发送 GET 请求并获取响应
    response = send_request.send_get_request(base_url, params)
    response = send_request.send_get_request(base_url, params)

    if response:
        logging.info("响应内容：" + response)
    else:
        logging.error("请求失败")

    # 退出程序
    sys.exit()
