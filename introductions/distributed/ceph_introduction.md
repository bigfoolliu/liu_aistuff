# ceph介绍以及使用

<!-- TOC -->

- [ceph介绍以及使用](#ceph%e4%bb%8b%e7%bb%8d%e4%bb%a5%e5%8f%8a%e4%bd%bf%e7%94%a8)
  - [ceph FileSysterm文件系统](#ceph-filesysterm%e6%96%87%e4%bb%b6%e7%b3%bb%e7%bb%9f)
    - [使用fuse挂载cephfs](#%e4%bd%bf%e7%94%a8fuse%e6%8c%82%e8%bd%bdcephfs)

<!-- /TOC -->

## ceph FileSysterm文件系统

使用ceph文件系统在ceph存储集群上需要至少一个`Ceph Metadata Server(MDS)`，ceph元数据服务器。

### 使用fuse挂载cephfs

```shell
# 客户端的操作

# 创建配置文件夹
sudo mkdir -p /etc/ceph
# 将服务器端的配置文件拷贝至本地
sudo scp USER_NAME@REMOTE_SERVER:/etc/ceph.ceph.conf /etc/ceph/ceph.conf
# 将服务器端的keyring拷贝至本地
sudo scp USER_NAME@REMOTE_SERVER:/etc/ceph.ceph.keyring /etc/ceph/ceph.keyring
# 保证文件的权限正确
sudo chmod 644 ceph.conf
sudo chmod 644 ceph.keyring

# 将本地的文件夹挂载到ceph
# 如果有多个文件系统需要挂载，使用 --client_mds_namespace 命令行参数指定装入的文件系统，
# 将client_mds_namespace设置添加到ceph.conf中
sudo mkdir /home/tonyl/remote
sudo ceph-fuse -m REMOTE_SERVER:6789 /home/tonyl/remote
```
