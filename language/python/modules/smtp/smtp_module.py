#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
用来从消息队列中读取任务，发送验证邮件
"""
import email
import getpass
import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# from edge_box_api_gateway.settings import settings

# SMTP_HOST = settings["email"]["smtp_host"]
# SMTP_PORT = settings["email"]["smtp_server"]
# import unittest


class Email(object):

    def __init__(self, host, port=25):
        """
        :param host: str, 发件人的邮箱服务器(smtp.sina.com)
        """
        self.host = host
        self.port = port
        if "sina" in host.split("."):
            self.smtp_obj = smtplib.SMTP(host=self.host, port=self.port)
            self.smtp_obj.starttls()
        elif "qq" in host.split("."):
            self.port = 465
            self.smtp_obj = smtplib.SMTP_SSL(host=self.host, port=self.port)
        self.template_path = os.path.join("/mnt/d/pythonProjects/liu_aistuff/email_template.html")

    def login(self, user, pwd):
        """
        本地没有sendmail访问的时候，使用其他邮件服务商的SMTP访问
        :param pwd: str, 当使用sina的时候，为密码，当为qq时候，使用auth_code，生成的授权码
        """
        (code, resp) = self.smtp_obj.login(user, pwd)
        return (code, resp)

    def generate_msg(self, client, company, verify_link, image_path=None, image_name=None, sender=None, receiver=None,
                     subject=None):
        """
        生成邮件的内容,可以携带图片
        :param mail_body: str, 邮件的主体内容
        :param sender: str, 邮件显示的发送者
        :param receiver: str, 邮件显示的接收者
        :param subject: str, 邮件的主题
        :return msg: MIMEMultipart
        """
        msg = MIMEMultipart()

        with open(self.template_path, "r", encoding="utf-8") as f:
            content = f.read()
            print("content: {}".format(content))
            link_text = content.format(client, company, verify_link, verify_link, verify_link)

        link_msg = MIMEText(link_text, "html", "utf-8")
        msg.attach(link_msg)

        if image_path:
            with open(image_path, "rb") as f:
                if not image_name:
                    image_name = image_path.split("/")[-1]
                img_msg = MIMEBase("image", "jpg", filename=image_name)
                # 加上必要的头信息:
                img_msg.add_header("Content-Disposition", "attachment", filename=image_name)
                img_msg.add_header("Content-ID", "<0>")
                img_msg.add_header("X-Attachment-Id", "0")
                # 把附件的内容读进来:
                img_msg.set_payload(f.read())
                # 用Base64编码:
                encoders.encode_base64(img_msg)
                msg.attach(img_msg)

        if sender:
            msg["From"] = Header(sender)
        if receiver:
            msg["To"] = Header(receiver)
        if subject:
            msg["Subject"] = Header(subject, "utf-8")
        return msg

    def send_mail(self, from_addr, to_addrs, msg):
        """
        发送邮件
        :param: from_addr: str, 发送邮件的地址(xxx@sina.com)
        :param: to_addrs: list, 目标地址
        :param: msg: MIMEMultipart, 构建完成的邮件内容
        :return ret: dict,全部发送成功则返回空字典，出错则会返回错误码
        """
        ret = self.smtp_obj.sendmail(from_addr=from_addr, to_addrs=to_addrs, msg=msg.as_string())
        return ret


# class EmailTest(unittest.TestCase):

#     def setUp(self):
#         self.smtp_host = "smtp.sina.com"
#         self.smtp_port = 25
#         self.origin_addr = "liu15671677014@sina.com"
#         self.target_addrs = ["1365205439@qq.com", "2713281245@qq.com"]
#         self.pwd = "123456"
#         self.email_core = Email(host=self.smtp_host, port=self.smtp_port)

#     def test_login(self):
#         (code, resp) = self.email_core.login(self.origin_addr, self.pwd)
#         print("code: {}, resp: {}".format(code, resp))
#         self.assertEqual(code, 235)

#     def test_send_email(self):
#         # msg = self.email_core.generate_msg(text="你好，这是测试文件", sender="tonyliu", 
#                                     # receiver="evan", subject="email test", link="http://www.baidu.com")
#         msg = self.email_core.generate_msg(text="你好，这是测试文件")
#         self.email_core.login(self.origin_addr, self.pwd)
#         (code, resp) = self.email_core.send_mail(self.origin_addr, self.target_addrs, msg)
#         print("code: {}, resp: {}".format(code, resp))
#         self.assertEqual(code, 250)


def main():
    # 使用sina邮箱发送邮件的时候，需要用户名和密码
    # smtp_host = "smtp.sina.com"
    # smtp_port = 25
    # origin_addr = "liu15671677014@sina.com"
    # target_addrs = ["2713281245@qq.com"]
    # pwd = getpass.getpass("password:")  # 安全的输入用户密码

    # 使用qq邮箱发送邮件的时候，需要用户名以及生成的授权码
    # smtp_host = "smtp.qq.com"
    # smtp_port = 465
    # origin_addr = "2713281245@qq.com"
    # target_addrs = ["liu15671677014@sina.com"]
    # auth_code = "wepxpajolubkdhca"

    smtp_host = "smtp.exmail.qq.com"
    smtp_port = 25
    origin_addr = "jxzn@jiangxing.ai"
    target_addrs = ["2713281245@qq.com"]
    pwd = "e2wGaHbiHSRHXktF"

    email_core = Email(host=smtp_host, port=smtp_port)

    email_core.login(origin_addr, pwd)
    # email_core.login(origin_addr, auth_code)

    for targer_addr in target_addrs:
        msg = email_core.generate_msg(targer_addr.split("@")[0], "牛x公司", "https://www.baidu.com", sender=origin_addr,
                                      subject="【JX IoT Edge】操作员账户验证")
        # print("msg: {} {}".format(msg, type(msg)))
        email_core.send_mail(origin_addr, target_addrs, msg)


if __name__ == '__main__':
    main()
