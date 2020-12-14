---
title: React实战-从零开始
date: 2020-12-15 12:00:00
categories: 
- Web前端
tags:
- React
---

# 环境配置和脚手架使用
> 这些内容在上一篇文章中已经有提及，前提是已安装npm
## 工具安装
```
npm install webpack -g  # 安装webpack（全局）
npm install -g create-react-app # 安装react构建程序（全局）
```
## 应用创建
我们可以使用create-react-app快速构建一个react单页应用，更多关于create-react-app的信息可见其[官方网站](https://create-react-app.bootcss.com)。
```
create-react-app demo-app       # 创建一个名为demo-app的react单页应用（自动安装依赖工具），也可使用npm init react-app my-app
```
创建后得到名为demo-app的文件夹，文件结构如下
```
my-app/
  README.md
  node_modules/
  package.json
  public/
    index.html
    favicon.ico
  src/
    App.css
    App.js
    App.test.js
    index.css
    index.js
    logo.svg
```
上述文件中，除了`public/index.html`（page template）和`src/index.js`（JavaScript entry point）两个文件不能修改文件名和路径外（内容可修改），其余文件均可删除或重命名。

其中`node_modules`存储安装的模块（如npm install echarts --save），`package.json`管理本地安装的npm包，这两类文件都无需额外维护，使用npm安装模块后会自动修改。npm相关信息可详见[npm教程文档](https://cloud.tencent.com/developer/section/1490235)。

另外，只有 `src` 内部的文件由 webpack 处理，所有**所有Js和Css文件都应该放入 src中**，这些也是这次实战的主要要处理的文件；另外index.html仅能使用`public`目录中的文件。
## 代码分析

# 组件库的使用



