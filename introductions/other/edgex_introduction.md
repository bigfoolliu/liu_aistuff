# edgex相关介绍

<!-- TOC -->

- [edgex相关介绍](#edgex%e7%9b%b8%e5%85%b3%e4%bb%8b%e7%bb%8d)
  - [1.介绍](#1%e4%bb%8b%e7%bb%8d)
    - [1.1地址](#11%e5%9c%b0%e5%9d%80)
    - [1.2简介](#12%e7%ae%80%e4%bb%8b)
    - [1.3运行edgex](#13%e8%bf%90%e8%a1%8cedgex)
  - [go编写设备服务](#go%e7%bc%96%e5%86%99%e8%ae%be%e5%a4%87%e6%9c%8d%e5%8a%a1)
    - [configuration配置文件](#configuration%e9%85%8d%e7%bd%ae%e6%96%87%e4%bb%b6)
    - [Profile文件](#profile%e6%96%87%e4%bb%b6)
    - [main.go入口文件](#maingo%e5%85%a5%e5%8f%a3%e6%96%87%e4%bb%b6)

<!-- /TOC -->

## 1.介绍

### 1.1地址

- [edgex github地址](https://github.com/edgexfoundry)
- [官方介绍使用地址](https://docs.edgexfoundry.org/Ch-WalkthroughRunning.html)
- [edgex-device-service-requirements](https://docs.google.com/document/d/1aMIQ0kb46VE5eeCpDlaTg8PP29-DBSBTlgeWrv6LuYk/edit#heading=h.d3xiag9h4918)
- [edgex wiki页面](https://wiki.edgexfoundry.org/)

### 1.2简介

工业互联网边缘计算的通用框架。

### 1.3运行edgex

`下载最新的EdgeX Foundry docker并运行`

```shell
# 获取docker-compose文件至当前目录
wget https://raw.githubusercontent.com/edgexfoundry/developer-scripts/master/releases/edinburgh/compose-files/docker-compose-edinburgh-1.0.1.yml

# 获取所有镜像
docker-compose pull
# 启动所有EdgeX Foundry微服务
docker-compose up -d
# 验证EdgeX容器是否已全部启动
docker-compose ps

# 启动随机设备服务，设备服务将自动注册名为Random-Integer-Generator01的设备，该设备将开始将其随机数读数发送到EdgeX
docker-compose up -d device-random


# 用localhost替换了edgex-core-command。那是因为EdgeX Foundry服务在docker中运行，它识别内部主机名edgex-core-command，但是我从docker之外调用它，所以我必须使用locahost来访问它
# 查看查询EdgeX Logging服务来验证是否正在发送这些读数
curl http://localhost:48080/api/v1/event/device/Random-Integer-Generator01/10
# 询问您的设备来检查可以调用哪些命令
curl http://localhost:48082/api/v1/device/name/Random-Integer-Generator01
# 获取指定设备的信息，也可以使用put
curl http://localhost:48082/api/v1/device/5c0e8a259f8fc20001a5d230/command/5c0e8a259f8fc20001a5d22b
```

`运行一个带web ui界面的consul`

```shell
# 拉取consul的镜像并运行
docker pull edgexfoundry/docker-core-consul
docker login
docker network create edgex-network
docker run -it –name edgex-files –net=edgex-network -v /data/db -v /edgex/logs -v /consul/config -v /consul/data -d edgexfoundry/docker-edgex-volume
docker run -p 8400:8400 -p 8500:8500 -p 8600:8600 –name edgex-core-consul –hostname edgex-core-consul -d edgexfoundry/docker-core-consul
```

然后访问：[本地consul](http://localhost:8500/ui),即可看到consul界面

## go编写设备服务

[编写edgex device-service](https://wiki.edgexfoundry.org/display/FA/APIs--Device+Services--Virtual+Device+Service)
[核心服务core-data的api参考](https://github.com/edgexfoundry/edgex-go/blob/master/api/raml/core-metadata.raml)

1. 安装依赖项
2. 获取edgex device-service sdk
3. 修改sdk中的文件内容构建服务

```shell
sudo apt install build-essential
mkdir -p ~/go/src/github.com/edgexfoundry
cd ~/go/src/github.com/edgexfoundry
git clone https://github.com/edgexfoundry/device-sdk-go.git
mkdir device-simple
cp -rf ./device-sdk-go/example/* ./device-simple/
cp ./device-sdk-go/Makefile ./device-simple
cp ./device-sdk-go/Version ./device-simple/
cp ./device-sdk-go/version.go ./device-simple/

```

参考文档：

[编写设备服务文档](https://docs.edgexfoundry.org/Ch-GettingStartedSDK-Go.html)
[禅道编写设备服务文档](http://zentao.jiangxingai.com/zentao/doc-view-134.html)
[导航，编写设备服务](https://wiki.edgexfoundry.org/display/FA/EdgeX+Demonstration+API+Walk+Through)

### configuration配置文件

- `configuration.toml`, `/device-service/cmd/device-service/res`目录下的，是device-service 的配置文件
  - Service,描述本device-service对于edgex组件的访问地址，如果edgex使用docker运行，Host为172.17.0.1或者本机ip,127.0.0.1会报错
  - DeviceList,配置启动的时候自动添加的device，可以有多个（Name为设备名字，全局唯一；Profile为device对应的device profile名字）
  - Driver,device-service自定义的配置

### Profile文件

- `deviceType.yml`,提供一种device提供的资源
  - `deviceResources`,定义device 包含的属性，对应数据模型的DeviceObject
  - `deviceCommands`,定义device支持的get/set 控制指令
  - `coreCommands`,定义device-service 对外的控制命令

### main.go入口文件
