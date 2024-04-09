import pickle


# def get_mac_address():
#     # 获取本机 MAC 地址
#     mac_address = hex(uuid.getnode()).replace("0x", "").upper()
#     mac_address = ":".join([mac_address[i:i + 2] for i in range(0, len(mac_address), 2)])
#     return mac_address


# def get_ip_address():
#     # 获取本机 IP 地址
#     ip_address = socket.gethostbyname(socket.gethostname())
#     return ip_address


def save_credentials(user_account, user_password, provider):
    # 保存凭据到本地文件
    credentials = {
        "user_account": user_account,
        "user_password": user_password,
        # "wlan_user_mac": wlan_user_mac,
        # "v_value": v_value,
        "provider": provider
    }
    with open("AHNUcredentials.pickle", "wb") as f:
        pickle.dump(credentials, f)


def load_credentials():
    # 从本地文件中加载凭据
    try:
        with open("AHNUcredentials.pickle", "rb") as f:
            credentials = pickle.load(f)
        return credentials["user_account"], \
            credentials["user_password"], \
            credentials["provider"]
    except (FileNotFoundError, pickle.UnpicklingError, TypeError):
        return None, None, None
