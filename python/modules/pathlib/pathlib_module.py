#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pathlib模块更好的操作文件以及路径

使用：

http://c.biancheng.net/view/2541.html

https://www.dongwm.com/post/use-pathlib/

用法对比：

os and os.path          pathlib
os.path.abspath	        Path.resolve
os.chmod	            Path.chmod
os.mkdir	            Path.mkdir
os.rename	            Path.rename
os.replace	            Path.replace
os.rmdir	            Path.rmdir
os.remove, os.unlink	Path.unlink
os.getcwd	            Path.cwd
os.path.exists	        Path.exists
os.path.expanduser	    Path.expanduser and Path.home
os.path.isdir	        Path.is_dir
os.path.isfile	        Path.is_file
os.path.islink	        Path.is_symlink
os.stat	Path.stat,      Path.owner, Path.group
os.path.isabs	        PurePath.is_absolute
os.path.join	        PurePath.joinpath
os.path.basename	    PurePath.name
os.path.dirname	        PurePath.parent
os.path.samefile	    Path.samefile
os.path.splitext	    PurePath.suffix
"""


import pathlib


def basic_demo():
    # 路径不再是一个单纯的字符串，而是一个特殊的对象
    path = pathlib.Path("/home")
    print(path, type(path), str(path))

    # 获取当前的路径
    print(pathlib.Path.cwd())

    # 直接获取家目录
    print(pathlib.Path.home())

    # 判断当前路径是否为文件夹
    print(pathlib.Path.cwd().is_dir())

    # 更简易的路径拼接
    print(pathlib.Path("/").joinpath("a", "b", "c"))

    # 更简易的获得父级目录等
    print(pathlib.Path("/home/a/b/c").parents[0])
    print(pathlib.Path("/home/a/b/c").parents[1])
    print(pathlib.Path("/home/a/b/c").parent)
    print(pathlib.Path("/home/a/b/c").parent.parent)

    # 更简易的获取文件名以及后缀名
    print(pathlib.Path("/home/abc.txt").suffix)  # 获取文件后缀名
    print(pathlib.Path("/home/abc.txt.tar").suffixes)  # 获取文件后缀名,当有多个后缀的时候
    print(pathlib.Path("/home/abc.txt").stem)  # 获取文件名


    # 类似touch命令的创建文件
    pathlib.Path("./test.txt").touch(mode=0o766, exist_ok=True)
    # 对文件的操作
    p = pathlib.Path("./test.txt").expanduser()
    print(p, type(p))
    p.write_text("hello, pathlib")
    print(p.read_text())
    p.write_bytes(b"\nchina\n")
    print(p.read_bytes())

    # 获取文件的拥有者
    print(p.owner())

    # 创建目录以及多级目录
    pathlib.Path("./a/b/c").mkdir(parents=True, exist_ok=True)

    # 更简易的修改文件后缀名以及文件名
    p = pathlib.Path("./a.jpg")
    print(p)
    print(p.with_suffix(".png"))
    print(p.with_name(f"aa{p.suffix}"))


if __name__ == "__main__":
    basic_demo()
