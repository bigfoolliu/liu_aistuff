#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import time
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs51_v1_5


def generate_rsa_file(length):
    """generate master and ghost private_key files"""
    # only generate once so far
    random_generator = Random.new().read  # fake random number
    rsa = RSA.generate(length, random_generator)  # the bigger, the better

    public_key = rsa.publickey().exportKey()  # server keys pair
    private_key = rsa.exportKey()
    with open("./keys/public_key.pem", "w") as f:
        f.write(public_key.decode("utf-8"))
    with open("./keys/private_key.pem", "w") as f:
        f.write(private_key.decode("utf-8"))


def rsa_encrypt(message):
    """
    use public pem to encrypt
    :param message: str
    return: bytes
    """
    with open("./keys/public_key.pem", "r") as f:
        key = f.read()
        rsa_key = RSA.importKey(key)  # 导入读取的公钥
        cipher = Cipher_pkcs51_v1_5.new(rsa_key)  # 生成密码对象
        cipher_text = cipher.encrypt(message.encode(encoding="utf-8"))
        return cipher_text


def rsa_decrypt(cipher_text):
    """
    use private pem to decrypt
    :param cipher_text: bytes
    return: bytes
    """
    with open("./keys/private_key.pem", "r") as f:
        key = f.read()
        rsa_key = RSA.importKey(key)
        cipher = Cipher_pkcs51_v1_5.new(rsa_key)
        cipher_text = cipher.decrypt(cipher_text, b"error")
        return cipher_text


def main():
    start = time.time()

    generate_rsa_file(2048)
    
    message = "hello"
    encrypted_data = rsa_encrypt(message)
    print("message: {} \nencrypted_data: {}".format(message, encrypted_data))

    decrypted_data = rsa_decrypt(encrypted_data)
    print("decrypted_data: {}".format(decrypted_data))

    end = time.time()
    print("cost time: {} seconds".format(end - start))


if __name__ == "__main__":
    main()
