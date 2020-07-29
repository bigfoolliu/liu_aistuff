# angular使用

<!-- vim-markdown-toc Marked -->

* [1.安装](#1.安装)
* [2.目录介绍](#2.目录介绍)
* [3.命令介绍](#3.命令介绍)

<!-- vim-markdown-toc -->

## 1.安装

```sh
# 安装cnpm
npm install -g cnpm --registry=https://registry.npm.taobao.org

# 使用cnpm安装angular/cli
cnpm i -g @angular/cli

# 检查安装版本
ng version

# 创建和初始化一个项目,默认会使用npm来安装依赖包，可以打断
ng new project-name
cnpm install  # 使用cnpm来安装package.json中的依赖包

# 两条命令均可，启动该项目
ng serve
ng start

# 程序启动之后，自动检测代码更新
```

## 2.目录介绍

- main.ts，程序入口文件,加载app/中的组件
- app/，组件
- node_moudles/，安装的第三方包
- .editorconfig，编辑器配置
- angular.json，脚手架工具相关配置
- package.json，包说明文件，依赖信息
- karma.conf.js，单元测试

## 3.命令介绍

- ng serve，运行开发模式
- ng build --prod，运行项目打包构建用于生产上线
- ng test，运行karma单元测试
- ng lint，运行TypeScript代码校验
- ng e2e，运行protrator端到端测试


