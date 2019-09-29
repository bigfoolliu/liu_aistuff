# grpc介绍

[概念介绍](https://grpc.io/docs/guides/concepts/)

python使用：

1. 在`.proto`文件中定义服务
2. 使用协议缓冲区编译器生成服务端和客户端代码
3. 使用python grpc api编写简单的客户端和服务端

```shell
# 使用grpc生成RPC代码
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto
```
