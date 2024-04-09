import sys
from pathlib import Path
from PyInstaller.__main__ import run

if __name__ == '__main__':
    # 指定打包的主Python文件的绝对路径
    entry_point = Path(__file__).resolve().parent / 'main.py'

    # 打包配置，修改--name参数为您想要的新名称
    new_name = 'AHNU Campus Network Automatic Login'  # 指定新的名称
    opts = [
        '--onefile',              # 打包成一个单独的可执行文件
        '--noconsole',            # 不显示控制台窗口
        '--name', new_name       # 指定生成的可执行文件的新名称
    ]

    # 运行PyInstaller
    run(['-y', *opts, str(entry_point)])
