#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import markdown

with open("./md_demo.md", "r") as md_file:
    html_content = markdown.markdown(md_file.read())

with open("./md_demo_ret.html", "w") as html_file:
    html_file.write(html_content)

