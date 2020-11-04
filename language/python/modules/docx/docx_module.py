#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python-docx模块使用

操作word文档: 
官方文档: https://python-docx.readthedocs.io/en/latest/index.html
知乎：https://zhuanlan.zhihu.com/p/61340025,  https://zhuanlan.zhihu.com/p/258763983
"""

import docx


def create_document_demo(text_dict):
    document = docx.Document()
    document.add_heading('试卷', 4)

    content = text_dict.get('content', '')
    choices = text_dict.get('choices', [])

    for i in range(30):
        p = document.add_paragraph(content)
        for choice in choices:
            p = document.add_paragraph(choice)

    document.save('test.docx')


def generate_exam_paper():
    ret = {'content': '这是一道选择题目()',
            'choices': ['A:a', 'B:b', 'C:c', 'D:d'],
            'type': 'choice'}
    return ret


def demo1():
    text_dict = generate_exam_paper()
    create_document_demo(text_dict)


if __name__ == '__main__':
    demo1()

