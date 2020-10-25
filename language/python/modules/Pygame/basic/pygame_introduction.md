# pygame介绍使用

<!-- vim-markdown-toc Marked -->

* [1.Display对象](#1.display对象)
* [2.Color对象](#2.color对象)
* [3.Rect对象](#3.rect对象)

<!-- vim-markdown-toc -->

## 1.Display对象

```python

"""
flags可选的类别
pygame.FULLSCREEN    create a fullscreen display
pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
pygame.OPENGL        create an OpenGL-renderable display
pygame.RESIZABLE     display window should be sizeable
pygame.NOFRAME       display window will have no border or controls
pygame.SCALED        resolution depends on desktop size and scale
                     graphics
"""

display = pygame.display.set_mode((10, 20, 30, 40), flags=0)
```

## 2.Color对象


## 3.Rect对象

