#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import base64


def base64_encrypt(meg):
    """
    meg: str
    return: bytes
    """
    b64_meg = base64.b64encode(meg.encode("utf-8"))
    return b64_meg


def base64_decrypt(meg_data):
    """
    meg_data: bytes
    return: str
    """
    meg = base64.b64decode(meg_data)
    return meg.decode("utf-8")


def main():

    meg = "register_template (3).xlsx"
    # meg = "江行联"
    print(meg.encode("utf-8"))

    ret = base64_encrypt(meg)
    print("meg: {}\nmeg length: {}\nret: {}\nret length: {}".format(meg, len(meg), ret, len(ret)))

    ret = base64_decrypt(ret)
    print("decode ret: {}".format(ret))


if __name__ == "__main__":
    main()