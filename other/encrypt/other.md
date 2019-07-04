## 2.MD5算法

### 2.1介绍

- 消息摘要算法，一种哈希算法，众多哈希算法中的一种，也可以用来加密
- `可以为任何文件（不管其大小，格式，数量）产生一个独一无二的数字指纹`
- 任意长度的数据算出的MD5值长度固定
- 抗修改，抗碰撞

### 2.2加密原理

1. 填充，对加密的二进制后面添加一个1和无数个0，使其位长对512求余数为448，其位长变为`n*512 + 448`，剩余的64位
2. 初始化变量，初始128位值用于第一轮计算，固定不变，为`A=0x01234567，B=0x89ABCDEF，C=0xFEDCBA98，D=0x76543210`
3. 处理分组数据

注意：

- 填充必须执行，即使余数已经为448

TODO:

## 3.AES加密（对称加密）