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
* [4.前端工程化](#4.前端工程化)
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

## 4.前端工程化



## 其他

- `OpenSSL`组织。
- `W3C`组织。
