"""
colorama模块使用

可以跨多终端，显示字体不同的颜色和背景
https://www.cnblogs.com/xiao-apple36/p/9151883.html

Fore: 针对字体颜色
Back: 针对背景颜色
Style: 针对字体格式

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""


from colorama import Fore, Back, Style, init 


def basic_demo():
    init(autoreset=True)
    
    # 注意这些风格是累加的效果
    print(Fore.RED + 'red color')  # 对字体增加颜色
    print(Back.YELLOW + 'back color yellow')  # 增加背景颜色
    print(Style.DIM + 'dim text')  # 使用dim风格
    
    # 如果没有 init 则需要手动将风格全部取消
    # print(Fore.RESET + Back.RESET + Style.RESET_ALL)

    print('normal style')


if __name__ == "__main__":
    basic_demo()

