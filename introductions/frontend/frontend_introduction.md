# 前端相关知识

<!-- vim-markdown-toc Marked -->

* [1.基础知识](#1.基础知识)
        - [1.1web标准](#1.1web标准)
        - [1.2浏览器](#1.2浏览器)
* [2.前端流行的9大框架](#2.前端流行的9大框架)
        - [2.1Vue](#2.1vue)
        - [2.2React](#2.2react)
        - [2.3Angular](#2.3angular)
* [3.相关工具](#3.相关工具)
        - [3.1npm](#3.1npm)
        - [3.2yarn](#3.2yarn)
        - [3.3nvm](#3.3nvm)
        - [3.4webpack](#3.4webpack)
        - [3.5语法检查工具](#3.5语法检查工具)
* [4.前端工程化](#4.前端工程化)
        - [4.1脚手架](#4.1脚手架)
        - [4.2构建](#4.2构建)
                + [4.2.1基础介绍](#4.2.1基础介绍)
                + [4.2.2模块化开发](#4.2.2模块化开发)
                + [4.2.3覆盖更新和增量更新](#4.2.3覆盖更新和增量更新)
                + [4.4.4资源定位](#4.4.4资源定位)
        - [4.3本地开发服务器](#4.3本地开发服务器)
                + [4.3.1动态构建](#4.3.1动态构建)
                + [4.3.2Mock服务](#4.3.2mock服务)
        - [4.4部署](#4.4部署)
* [其他](#其他)

<!-- vim-markdown-toc -->

## 1.基础知识

### 1.1web标准

- 结构标准（HTML）：用于对网页元素进行整理和分类。
- 表现标准（CSS）：用于设置网页元素的版式、颜色、大小等外观样式。
- 行为标准（JS）：用于定义网页的交互和行为。

根据上面的三个标准，将web前端分为三层(HTML, CSS, JS)

### 1.2浏览器

- **渲染引擎(浏览器内核，rendering engine)** + **JS引擎** 组成
- 内核读取网页内容，计算显示方式并展示
- js引擎读取js代码并执行

## 2.前端流行的9大框架

- [前端流行的9大框架](https://zhuanlan.zhihu.com/p/76463271)

### 2.1Vue

- 可以自底向上逐层应用
- 便于上手和第三方库或项目整合

### 2.2React

- 主要用于构建ui
- 较高的性能

### 2.3Angular

- MVVM,模块化
- 自动化双向数据绑定
- 语义化标签

## 3.相关工具

### 3.1npm

- js包管理工具

```sh
npm config get registry  # 获取当前npm的版本
npm install -g npm  # 更新npm

# 安装源切换
npm config set registry=https://registry.npm.taobao.org  # 切换为淘宝源
npm config set registry=http://registry.npmjs.org  # 切换为官方源


npm init  # 初始化,生成package.json
npm install module_name -S  # 安装具体的模块, 生成node-modules文件夹

npm i webpack vue vue-loader  # 安装包示例
```

### 3.2yarn

- 一个包管理器
- [使用文档](https://yarn.bootcss.com/docs/)

```sh
# 安装升级
brew install yarn
brew upgrade yarn

yarn --version

# 1.初始化一个项目
yarn init

# 2.管理依赖
yarn add <package>  # 添加依赖包，自动添加至package.json
yarn add --dev  # 将依赖只添加到devDependencies
yarn add --optional  # 将依赖只添加到optionalDependencies中

yarn upgrade <package>  # 升级依赖，会修改package.json和yarn.lock

yarn remove <package>  # 删除依赖，会修改package,json和yarn.lock

# 3.安装依赖
yarn install  # 安装所有的依赖
```

### 3.3nvm

- `Node Version Manager`,管理不同版本node的工具
- 类似于pyenv

```sh
nvm ls  # 查看已经安装版本的node

nvm install 4.2.2  # 安装指定版本的node

nvm use 4.2.2  # 切换不同的版本
nvm use node  # 切换使用最新版本
```

### 3.4webpack

- [官网](https://www.webpackjs.com/)
- 静态模块打包器

```javascript
// webpack.config.js
// 该配置将输入index.js打包到指定文件夹dist

const path = require('path');  // 表明使用绝对路径

const config = {
    entry: path.join(__dirname, 'src/index.js'),  // 入口起点(entry point)指示 webpack 应该使用哪个模块，来作为构建其内部依赖图的开始,__dirname表示当前文件的路径
    output: {
        filename: 'bundle.js',
        path: path.join(__dirname, 'dist')
    }, // output 属性告诉 webpack 在哪里输出它所创建的 bundles，以及如何命名这些文件，默认值为 ./dist
    module: {
        rules: [
            {
                test: /\.vue$/,  // test 属性，用于标识出应该被对应的 loader 进行转换的某个或某些文件,此处指所有的.vue文件
                loader: 'vue-loader'  // use 属性，表示进行转换时，应该使用哪个 loader
            },
            {
                test: /\.css$/,
                use: [
                    'style-loader',  // css
                    'css-loader'
                ]
            },
            {
                test: /\.(gif|jpg|png)$/
                user: [
                    {
                        loader: 'url-loader',  // 将图片加载为base64格式，可以减少http请求
                        options: {
                            limit: 1024,
                            name: '[name].[ext]'  // 输出的图片的文件名为原始名+原始文件名的扩展名
                        }
                    }
                ]
            }
        ]
    },  // loader 让 webpack 能够去处理那些非 JavaScript 文件（webpack 自身只理解 JavaScript）
    plugins: [
        new HtmlWebpackPlugin({template: './src/index.html'})
    ]  // 插件则可以用于执行范围更广的任务。插件的范围包括，从打包优化和压缩，一直到重新定义环境中的变量
}

module.exports = config;
```

在package.json中配置使用该webpack配置:

```json
{
    "scripts": [
        "build": "webpack --config webpack.config.js"
    ]
}
```

### 3.5语法检查工具

- HTML去掉注析、换行符 - `HtmlMin`
- CSS文件压缩合并 – `CssMinify`
- JS代码风格检查 – `JsHint`
- JS代码压缩 – `Uglyfy`
- image压缩 - `imagemin`

## 4.前端工程化

- 前端工程化方案: `Boi`

### 4.1脚手架

脚手架是一种约定和规范：

- 相同的文件组织结构
- 相同的开发范式
- 相同的模块依赖
- 相同的工具配置
- 相同的基础代码
- 然后脚手架 将这些 重复性的东西全部都集成起来，减少这样无意义的操作
- 常用的有包括：`Yeoman`

### 4.2构建

#### 4.2.1基础介绍

- 即编译，不过针对的是整个项目，核心是资源(html,js,css)的管理
- 域名，路径，后缀，参数不同的URL会被浏览器视为全新的URL，浏览器就会发出触发新的请求

- 将领先于浏览器ECMAScript规范的js代码编译为符合ECMAScript规范的代码
- 将LESS/SCSS预编译语法写的CSS代码转译为CSS
- 将模板语法写的Html渲染

构建还包含以下功能：

- `依赖打包`，分析文件依赖关系，将同步依赖的文件打包到一起，减少http请求
- `资源嵌入`，比如将小于10kb的文件编译为base64嵌，减少请求
- `文件压缩`，通过各种方案减小文件体积
- `hash指纹`，给文件名增加hash指纹来应对浏览器的缓存策略

**前端中的模块和组件的差异体现在颗粒度的差异：比如一个button是一个模块，多个button组成的导航栏是一个组件。**

#### 4.2.2模块化开发

- `避免命名冲突`
- `便于依赖管理`
- `利于性能优化`
- `提高可维护性`
- `利于代码复用`

#### 4.2.3覆盖更新和增量更新

1. 本地存储，`LocalStorage`和`SessionStorage`
2. HTTP缓存策略, 包括`强制缓存`和`协商缓存`
3. `no-cache`不是禁止缓存，是先与服务器确认资源是否发生变化，没有变化则可以用缓存内容
4. `no-store`是真正的禁止缓存，每次用户发送请求都会下载完整的响应
5. `public`表示此响应可以被浏览器和其他中间缓存器无限期缓存
6. `private`表示此响应只可以被浏览器缓存
7. `max-age`表示从指定的时刻开始此响应的缓存副本有效的最长时间

**覆盖更新：***

- 在静态资源的url后面增加一个参数，而参数的值为这个文件内容的hash值，当文件内容发生变化，则hash值发生变化，url发生变化，则发出新请求
- 必须保证html文件和改动的静态文件同步更新否则会资源不同步；不利于版本回滚
- 使用较少，`基本被废弃`

**增量更新：**

- 相对于覆盖更新，将hash指纹作为文件名称的一部分
- 部署时候，将静态资源先部署先于html部署，静态资源没有引用路径，不影响线上环境，同时只是修改了文件名，不会覆盖已经存在的旧版文件

#### 4.4.4资源定位

1. 原始形态，直接定位路径
2. CDN,将静态资源缓存到距离用户较近的CDN节点上，属于一种`部署策略`,包括`分布式存储`，`负载均衡`，`内容管理`等
3. 使用webpack的`逆向注入模式`，将js文件视作一切的入口，与参与entry配置的js文件有引用关系的都会参与构建

### 4.3本地开发服务器

#### 4.3.1动态构建

**LiveLoad：**

- 在浏览器和服务器之间创建websocket连接，服务器端执行完动态编译之后会发送reload到浏览器，浏览器接收之后自动刷新
- 优点：保证动态构建的内容被浏览器即时获取
- 缺点：无法保存页面状态，调试时候可能对于操作好几步的调试要重复的调试好几步

**HMR：**

- 以局部刷新替换整体页面更新，弥补LivLoad无法保存状态的缺陷,主要为了本地的开发
- 开启`webpack-dev-server`时候，webpack向构建的输出文件中注入功能模块`HMR runtime`,向源文件注入服务模块`HMR server`,源文件更新之后两者通信进行热更新

#### 4.3.2Mock服务

- 为了前后端的协作，即`假数据`
- 直接在代码中构造假数据很方便，但是当接口过多的时候容易出错
- `客户端Mock`,Mock.js构造假数据，仍然涉及业务代码的修改,原理是`拦截js发出的Ajax请求并返回假数据`
- `服务端Mock Server`

### 4.4部署

- `速度`
- `安全`
- `协作`

## 其他

- `OpenSSL`组织。
- `W3C`组织。
