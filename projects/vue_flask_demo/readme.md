# vue.js加flask实现全栈单页面应用

<!-- TOC -->

- [vue.js加flask实现全栈单页面应用](#vuejs%e5%8a%a0flask%e5%ae%9e%e7%8e%b0%e5%85%a8%e6%a0%88%e5%8d%95%e9%a1%b5%e9%9d%a2%e5%ba%94%e7%94%a8)
  - [1.环境准备](#1%e7%8e%af%e5%a2%83%e5%87%86%e5%a4%87)

<!-- /TOC -->

- [使用vue.js和flask构建单页全栈应用](https://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649641385&idx=1&sn=51ae19d9c228c391e7de3aafbb5a6a7d&chksm=833db14fb44a38594b57bfb0b2e889d1bd5a0973e881f4a3d6e37624eab503bda1e98a869ce9&mpshare=1&scene=24&srcid=&sharer_sharetime=1573841659508&sharer_shareid=20ab6c09eef32b49dbe03904652b9eb2#rd)

## 1.环境准备

**前端命令：**

```shell
# 全局安装vue客户端
sudo npm install -g vue-cli

# 创建前端代码文件夹
mkdir flaskvue
cd flaskvue

# 创建vue项目文件夹
sudo vue init webpack frontend
cd frontend

# 安装项目依赖的的包文件
sudo npm install

# 利用本地的node服务器
sudo npm run dev

# 构建项目
sudo npm run build

# 使用axios库来连接后端
sudo npm install --save axios
```

**后端命令：**

```shell
# 执行后台服务，FLASK_APP指向服务启动文件，FLASK_DEUBG以调试模式运行
FLASK_APP=run.py FLASK_DEBUG=1 flask run

# 为访问API创建规则，解决cors问题
pip install -U flask-cors
```
