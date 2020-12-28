#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Python 使用ftplib实现ftp服务器，实现文件的远程传输下载等

官方文档：https://docs.python.org/3/library/ftplib.html
代码：https://blog.csdn.net/ouyang_peng/article/details/79271113
"""

import os
import sys
import socket
import time
from ftplib import FTP


class SimpleFtp(object):
    """ftp自动上传，下载"""

    def __init__(self, host, port=21):
        """初始化端口，主机以及设置日志文件和编码"""
        self.host = host
        self.port = port
        self.ftp = FTP()
        self.ftp.encoding = "utf-8"
        self.log_file = open("ftp_log.log", "a")
        self.file_list = []

    def login(self, user_name, passward):
        """登录"""
        time_out = 60
        try:
            socket.setdefaulttimeout(time_out)
            self.ftp.set_pasv(True)  # 设置传输被动模式
            self.ftp.set_debuglevel(1)  # 设置debug的级别0,1,2

            self.debug_print("connect to {}".format(self.host))
            self.ftp.connect(self.host, self.port)
            self.debug_print("connect to {} success.".format(self.host))

            self.debug_print("login to {}".format(self.host))
            self.ftp.login(user_name, passward)
            self.debug_print("login to {} success.".format(self.host))

            self.debug_print(self.ftp.welcome)
        except Exception as e:
            self.deal_error("connect or login ftp error: {}".format(e))
            pass

    def is_same_size(self, local_file, remote_file):
        """检查本地与远程文件大小是否相同，即传输是否完整"""
        try:
            remote_file_size = self.ftp.size(remote_file)
        except Exception as e:
            remote_file_size = -1
            print(e)

        try:
            local_file_size = self.ftp.size(local_file)
        except Exception as e:
            local_file_size = -1
            print(e)

        self.debug_print("remote file size: {} local file size: {}".format(remote_file_size, local_file_size))
        if local_file_size == remote_file_size:
            return True
        return False

    def download_file(self, local_file, remote_file):
        """将远程单个文件下载到本地"""
        self.debug_print("begin to download file {} to {}".format(remote_file, local_file))
        if self.is_same_size(local_file, remote_file):
            self.debug_print("{} file not need to download".format(local_file))
            return
        try:
            self.debug_print("begin to download file {}".format(remote_file))
            buf_size = 1024
            file_handler = open(local_file, "wb")
            self.ftp.retrbinary("download remote file {}".format(remote_file), file_handler.write,
                                buf_size)  # ftp下载核心方法
            file_handler.close()
        except Exception as e:
            self.debug_print("download file error {}".format(e))
            return

    def download_file_tree(self, local_path, remote_path):
        """批量下载文件夹文件"""
        self.debug_print("begin to download path {} to {}".format(remote_path, local_path))
        try:
            self.ftp.cwd(remote_path)
        except Exception as e:
            self.debug_print("remote path {} not exist:{}".format(remote_path, e))
            return

        if not os.path.exists(local_path):
            self.debug_print("local path {} not exist".format(local_path))
            self.debug_print("begin to create dir {} not exist".format(local_path))
            os.makedirs(local_path)

        self.debug_print("switch to dir {}".format(self.ftp.pwd()))

        self.file_list = []
        self.ftp.dir(self.get_file_list)  # 方法回调

        remote_names = self.file_list
        self.debug_print("remote file names: {}".format(remote_names))

        for item in remote_names:
            file_type = item[0]
            file_name = item[1]

            local = os.path.join(local_path, file_name)
            if file_type == "d":  # 目录
                self.debug_print("download file tree {}".format(file_name))
                self.download_file_tree(local, file_name)
            elif file_type == "-":  # 文件
                self.debug_print("download file {}".format(file_name))
                self.download_file(local, file_name)
            self.ftp.cwd("..")
            self.debug_print("back to last dir {}".format(self.ftp.pwd()))
        return True

    def upload_file(self, local_file, remote_file):
        """上传本地文件"""
        if not os.path.isfile(local_file):
            self.debug_print("{} is not file".format(local_file))
            return
        if self.is_same_size(local_file, remote_file):
            self.debug_print("file {} already uploaded, skip".format(local_file))
            return

        buf_size = 1024
        file_handler = open(local_file, "rb")
        self.ftp.storbinary("store file {}".format(remote_file), file_handler, buf_size)
        file_handler.close()
        self.debug_print("file {} already uploaded".format(local_file))

    def upload_file_tree(self, local_path, remote_path):
        """上传本地文件夹"""
        if not os.path.isdir(local_path):
            self.debug_print("path {} not exist".format(local_path))
            return

        self.ftp.cwd(remote_path)
        self.debug_print("switch to remote dir {}".format(self.ftp.pwd()))

        local_name_list = os.listdir(local_path)
        for local_name in local_name_list:
            src = os.path.join(local_path, local_name)
            if os.path.isdir(src):
                try:
                    self.ftp.mkd(local_name)  # 远程创建文件夹
                except Exception as e:
                    self.debug_print("remote dir {} already exist: {}".format(src, e))
                self.debug_print("upload file tree {}".format(local_name))
                self.upload_file_tree(src, local_name)
            else:
                self.debug_print("upload file {}".format(src, local_name))
        self.ftp.cwd("..")  # 回到上层目录

    def get_file_list(self, line):
        """获取文件列表"""
        file_arr = self.get_file_name(line)
        # 去除 . 和 .. 两个文件
        if file_arr[1] not in [".", ".."]:
            self.file_list.append(file_arr)

    def get_file_name(self, line):
        """获取文件名"""
        pos = line.rfind(":")
        # 去除空格
        while line[pos] != " ":
            pos += 1
        while line[pos] == " ":
            pos += 1
        file_arr = [line[0], line[pos:]]
        return file_arr

    def debug_print(self, s):
        """debug输出"""
        self.write_log(s)

    def write_log(self, long_s):
        """设置日志格式，记录日志"""
        time_now = time.localtime()
        date_now = time.strftime("%Y-%m-%d", time_now)
        format_log_str = "{}: {}".format(date_now, long_s)
        print(format_log_str)
        self.log_file.write(format_log_str)

    def deal_error(self, e):
        """处理错误, 当发生严重错误时，程序终止"""
        log_str = "error: {}".format(e)
        self.write_log(log_str)
        sys.exit(1)

    def close(self):
        """退出ftp,关闭log"""
        self.debug_print("close ftp")
        self.ftp.quit()
        self.log_file.close()


if __name__ == "__main__":
    remote_host = None  # TODO:
    simple_ftp = SimpleFtp(remote_host)

    local_file = None
    remote_file = None
    simple_ftp.download_file(local_file, remote_file)
