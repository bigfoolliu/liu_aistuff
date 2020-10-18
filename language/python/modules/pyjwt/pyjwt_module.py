#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyjwt模块的使用

用来编解码json web token

基本介绍：https://pyjwt.readthedocs.io/en/latest/
更多使用：https://pyjwt.readthedocs.io/en/latest/usage.html

- JSON Web Token通常简称为JWT，它是一种开放标准（RFC 7519）
- 随着RESTful架构的流行，越来越多的项目使用JWT作为用户身份认证的方式
- JWT相当于是三个JSON对象经过编码后，用.分隔并组合到一起，这三个JSON对象分别是头部（header）、载荷（payload）和签名.

头部:
{
  "alg": "HS256",
  "typ": "JWT"
}
其中，alg属性表示签名的算法，默认是HMAC SHA256（简写成HS256）；typ属性表示这个令牌的类型，JWT中都统一书写为JWT。

载荷:
载荷部分用来存放实际需要传递的数据。JWT官方文档中规定了7个可选的字段：
iss ：签发人
exp：过期时间
sub：主题
aud：受众
nbf：生效时间
iat：签发时间
jti：编号
除了官方定义的字典，我们可以根据应用的需要添加自定义的字段。

签名
签名部分是对前面两部分生成一个指纹，防止数据伪造和篡改。实现签名首先需要指定一个密钥。这个密钥只有服务器才知道，不能泄露给用户。
然后，使用头部指定的签名算法（默认是HS256）
按照下面的公式产生签名:
HS256(base64Encode(header) + '.' + base64Encode(payload), secret)

算出签名以后，把头部、载荷、签名三个部分拼接成一个字符串，每个部分用.进行分隔，这样一个JWT就生成好了。
"""

import jwt


def encode_demo():
    """编码示例"""
    # 需要声明待编码的信息，使用的密钥，使用的加密算法
    encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
    print(encoded_jwt, type(encoded_jwt))
    return encoded_jwt


def decode_demo():
    """解码示例"""
    encoded_jwt = encode_demo()
    decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
    print(decoded_jwt, type(decoded_jwt))


if __name__ == "__main__":
    # encode_demo()
    decode_demo()
