# PlaneGame

1. WebSpider3.py未完成

2. WebSpiderQQ.py和WebSiderToutiao未完成分析

---

## 打飞机游戏框架

1. 加载背景音乐
2. 播放背景音乐
3. 我方飞机诞生
4. 执行下列代码

```python
    while True:

        if 用户单击了退出按钮:
            退出程序
        interval(间隔) += 1

        if interval == 50:
            小飞机诞生
            小飞机移动一个位置
            屏幕刷新
            interval = 0

        if 用户鼠标产生移动:
            我方飞机中心位置 = 用户鼠标位置
            屏幕刷新

        if 我方飞机接触小飞机:
            我方失败
            播放失败背景音乐
            修改我方飞机图案
            打印“game over”
            停止背景音乐
```
