#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


# print(2 ** 38)

# _text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

_text = "map"


def convert(s):
    codes = "abcdefghijklmnopqrstuvwxyz"
    for index, item in enumerate(codes):
        if s == item:
            _index = (index + 2) % 26
            return codes[_index]
    return s


if __name__ == "__main__":
    ret = ""
    for _s in _text:
        ret += convert(_s)

    print(ret)

