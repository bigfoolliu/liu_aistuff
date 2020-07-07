"""
rich 模块使用

可以在终端展示不同的颜色等 https://github.com/willmcgugan/rich

展示rich模块的使用
python -m rich
"""


from rich import print
from rich.progress import track
import time


print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals())


def do_step(step):
    time.sleep(1)


for step in track(range(100)):
    do_step(step)
