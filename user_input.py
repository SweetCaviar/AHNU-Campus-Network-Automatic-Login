import tkinter as tk
from tkinter import StringVar


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def get_user_input():
    root = tk.Tk()
    root.withdraw()

    dialog = tk.Toplevel(root)
    dialog.title("AHNU")

    center_window(dialog, 400, 250)

    tk.Label(dialog, text="账户:", font=("Helvetica", 14, "bold")).grid(row=0, column=0, padx=10, pady=5)
    account_entry = tk.Entry(dialog, font=("Helvetica", 12))
    account_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(dialog, text="密码:", font=("Helvetica", 14, "bold")).grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(dialog, show="*", font=("Helvetica", 12))
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(dialog, text="请选择您的网络运营商:", font=("Helvetica", 14, "bold")).grid(row=2, column=0, columnspan=2, pady=5)
    provider_var = StringVar()
    provider_var.set("telecom")
    providers = {"中国电信": "telecom", "中国联通": "unicom", "中国移动": "cmcc"}
    row_num = 3
    for text, value in providers.items():
        tk.Radiobutton(dialog, text=text, variable=provider_var, value=value, font=("Helvetica", 12)).grid(row=row_num, column=0, columnspan=2, padx=10, sticky=tk.W)
        row_num += 1

    user_input = [None, None, None]

    def submit():
        nonlocal user_input
        user_input[0] = account_entry.get()
        user_input[1] = password_entry.get()
        user_input[2] = provider_var.get()
        root.destroy()

    submit_button = tk.Button(dialog, text="提交", command=submit, font=("Helvetica", 14, "bold"))
    submit_button.grid(row=row_num, columnspan=2, pady=10)

    root.mainloop()

    return tuple(user_input)
