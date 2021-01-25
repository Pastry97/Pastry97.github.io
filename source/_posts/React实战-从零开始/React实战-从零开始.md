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
> 如果是复制的别人的项目，运行前一般需要`npm install`指令安装项目所依赖的模块

另外，只有 `src` 内部的文件由 webpack 处理，所有**所有Js和Css文件都应该放入 src中**，这些也是这次实战的主要要处理的文件；另外index.html仅能使用`public`目录中的文件。
# 代码分析
### index.js和index.html
index.js做渲染工作，通过ReactDOM提供的render函数将React元素转为HTML结构并插入DOM节点。需要注意的是，多个React元素需要用一个父标签全部包括才能算做一个元素。

> Javascript中的Document对象可见[教程](https://www.w3school.com.cn/jsref/dom_obj_document.asp)
```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';  // 自定义组件
import reportWebVitals from './reportWebVitals';

// ReactDOM.render(template,targetDOM)
ReactDOM.render(  // 将组件模板转为HTML语言，并插入指定的DOM节点
  // React.StrictMode组件 不会渲染任何可见的 UI。它为其后代元素触发额外的检查和警告
  // App组件 由App.js构建并导出
  <React.StrictMode>  
    <App />   
  </React.StrictMode>,
  // targetDOM 由getElementById在根节点下获取id为“root”的DOM节点，详见index.html
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();  // report信息
```
### App.js
App.js定义了一个名为App的组件（函数组件），需要注意的是，组件定义后为了其他js文件能import，需要在定以后导出（export），如果导出多个，可以用export {aaa, bbb}，如果是从一个文件中导出一个组件，那就需要用default。

```jsx
import logo from './logo.svg';
import './App.css'; // 样式

function App() {  // 函数组件
  return (  // 返回**一个**React元素
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;  // 导出该组件，如果导出多个，可以用export {aaa, bbb}，如果是从一个文件中导出一个组件，那就需要用default
```
总的来说，初始代码只是将App组件插入root节点，通过分析APP.js发现，该组件仅包含一个logo，一句提示和一条链接（当然也会有初始好的样式App.css），我们可以通过`npm start`指令运行代码，并在浏览器中进入`http://localhost:3000/`中进行查看，值得一提的是，我们可以一边运行一边修改代码，保存后修改会自动显示到页面上。
![Edited Page](/img/React实战_从零开始_editedPage.png)
# 组件库的使用
>React、Vue这类前端框架很方便的一点是有大量的成熟UI组件库供开发者使用。组件库顾名思义，也就是一个包含许多已经编写好的组件的库，我们这次使用[Antd UI组件库](https://ant.design/docs/react/introduce-cn)。

我们可以在Antd官网的[组件总览](https://ant.design/components/overview-cn/)中选取我们需要的组件

zheli


