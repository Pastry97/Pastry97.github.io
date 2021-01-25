---
title: React实战-基础讲解
date: 2020-12-11 12:00:00
categories: 
- Web前端
tags:
- React
---

> 课程demo，我负责的任务是demo前端，正好学习并总结一下React的使用，本文先对React的基础知识做一些介绍，在此之前，需要对html、css和javascript的相关知识有一定了解

*本文仅对一些React相关的基础知识进行讲解，系统学习可参考文末的参考链接*

### 相关背景知识与概述

#### WEB单页应用与多页应用

##### 多页应用（MPA）

每一次页面跳转的时候，后台服务器都会给返回一个新的`html`文档，这种类型的网站也就是多页网站，也叫做多页应用。多页应用首屏时间快，SEO (搜索引擎优化) 效果好，但页面切换慢。

##### 单页应用（SPA）

第一次进入页面的时候会请求一个`html`文件，刷新清除一下。切换到其他组件，此时路径`url`也相应变化，`js`会感知到`url`的变化，通过这一点可以用`js`动态地将当前页面的内容清除，然后将下一个页面的内容挂载到当前页面上。这个时候的路由不再是后端来做了，而是前端来做，判断页面显示相应的组件，清除不需要的。以这种方式，没有新的`html`文件请求，页面内容也变化了。SPA的页面跳转是js渲染，页面切换快，但首屏时间（html请求+js请求）稍慢，SEO差。


![React基础_MPA&SPA](/img/React基础_MPA&SPA.png)

#### React

React 是一个声明式，高效且灵活的用于构建用户界面的 JavaScript 库。使用 React 可以将一些简短、独立的代码片段组合成复杂的 UI 界面，这些代码片段被称作**“组件”**。



### 相关工具

#### webpack

webpack 是一个前端资源加载/打包工具。它将根据模块的依赖关系进行静态分析，然后将这些模块按照指定的规则生成对应的静态资源。webpack依赖nodejs和npm。

```
npm install webpack -g  # 全局安装
```

#### create-react-app

Create React App 是一个官方支持的创建 React **单页应用**程序的方法。它提供了一个零配置的现代构建设置。

```
npm install -g create-react-app # 利用npm全局安装
create-react-app demo-app       # 创建react单页应用（自动安装依赖工具）
cd demo-app

npm run eject					# 生成配置文件（运行后eject命令会在package.json中被移除）
npm start 						# 开发模式运行程序（内置命令），在http://localhost:3000查看
npm run build					# 将生产环境的应用程序构建到 build 目录
```



### 基本概念

#### JSX语法

建议在 React 中配合使用 JSX。JSX是JavaScript 的语法扩展，JSX 可以很好地描述 UI 应该呈现出它应有交互的本质形式。具体语法可见[JSX简介](https://react.docschina.org/docs/introducing-jsx.html)、[React JSX-菜鸟教程](https://www.runoob.com/react/react-jsx.html)。

#### React元素与组件

每一个 **React 元素**事实上都是一个 JavaScript 对象，可保存在**变量**中或者作为**参数**传递。React元素是一种对渲染内容的轻量级描述，大多数的 React 开发者使用了一种名为 “JSX” 的特殊语法，JSX 可以让你更轻松地书写这些结构。

```jsx
const element = <h1>Hello, world!</h1>;
var myDivElement = <div className="foo" />; //*<div />会被编译成 React.createElement('div')。
```

如果**React元素**对应**常量/变量**这一概念，**组件**则对应**函数/类**这一概念。如下所示，`ShoppingList` 是一个 **React 组件类**，或者说是一个 **React 组件类型**。一个组件接收一些参数，我们把这些参数叫做 `props`，然后通过 `render` 方法返回一个**React元素**（该组件需要展示在屏幕上的视图的层次结构）。组件名首字母必须大写。

```jsx
class ShoppingList extends React.Component {  // React.Component是React多种类型组件中的一种
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li> 
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// 用法示例: <ShoppingList name="Mark" />
```

#### DOM与ReactDOM

*浏览器代码解析与页面渲染：DOM构造 =>布局（文档流） =>页面绘制*

DOM (Document Object Model) 译为**文档对象模型**，是 W3C（万维网联盟）的标准，分为三个部分：

- 核心DOM：针对任何结构化文档的标准模型

- XML DOM：针对 XML 文档的标准模型，定义访问和操作XML文档的标准方法，即定义了所有 XML 元素的**对象**和**属性**，以及访问它们的**方法**。DOM 将 XML 文档作为一个树形结构，而树叶被定义为节点。

  > XML，可扩展标记语言，是一种很像HTML的**标记语言**，被设计用来传输和存储数据，需要自定义标签。

- HTML DOM：针对 HTML 文档的标准模型，定义了访问和操作 HTML 文档的标准，即定义了所有 HTML 元素的**对象和属性**，以及访问它们的**方法**（接口）。DOM同样以树结构表达 HTML 文档。

  > HTML，超文本标记语言，是一种用于创建网页的标准**标记语言**，包含了HTML **标签**及**文本**内容，HTML 运行在浏览器上，由浏览器来解析

React的DOM操作（**ReactDOM**）单独由react-dom包提供，常用其提供的`render`操作，如下，1）在提供的 `container` 里渲染一个**React 元素**，并返回对该组件的引用（或者针对无状态组件返回 `null`），2）如果 React 元素之前已经在 `container` 里渲染过，这将会对其执行更新操作，并仅会在必要时改变 DOM 以映射最新的 React 元素，3）如果提供了可选的回调函数，该回调将在组件被渲染或更新之后被执行。

```js
ReactDOM.render(element, container[, callback])  // 渲染、更新、回调
```



### 组件

#### 函数组件与class组件

组件的最终目的是返回一个React元素，定义组件最简单的方式就是编写 JavaScript 函数（函数组件）：

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

使用ES6的class来定义组件，两个组件在 React 里是等效的：

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

当使用自定义组件时，标签属性以及子组件会被转换成**props**对象传递给组件（class组件通过this.props访问）

```jsx
function Welcome(props) {  // 函数组件Welcome，接收props对象
  return <h1>Hello, {props.name}</h1>;  // 通过props.name获取name属性
}

const element = <Welcome name="Sara" />;  // 使用自定义组件Welcome，并设定属性name="Sara"
ReactDOM.render(  // 使用ReactDOM提供的render函数渲染元素
  element,
  document.getElementById('root')
);
```

**所有 React 组件都必须像纯函数一样保护它们的 props 不被更改。**

#### class组件中的state与生命周期

使用ES6的class来定义组件，class组件中存在状态state，通过this.state访问。需要注意的是，state是组件自己维护的一个javaScript对象，而props是传入的、不可修改的对象（可理解为形参）。在 React 中，`this.props` 和 `this.state` 都代表着**已经被渲染了的**值，即当前屏幕上显示的值。

```jsx
class Clock extends React.Component {
  constructor(props) { // 非必需
    super(props);
    this.state = {date: new Date()};   // 可在构造函数中对state进行初始化
  }

  render() { //必需
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>  // 通过this.state访问State
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

另外，除了初始化外，state并不能直接被修改，组件提供**this.setState()**方法更新组件的State，setState的调用会引发一次组件的更新（详见下文组件生命周期），从而引发重新绘制，即该组件重新渲染。

```
setState(updater[, callback]) // callback是state导致的页面重新渲染的回调
```

需要注意的是，setState是**异步且分批执行**的，连续多次setState函数调用产生的效果会合并。

```jsx
incrementCount() {
  // 注意：这样 *不会* 像预期的那样工作。
  this.setState({count: this.state.count + 1});
}

handleSomething() {
  // 假设 `this.state.count` 从 0 开始。
  this.incrementCount();
  this.incrementCount();
  this.incrementCount();
  // 当 React 重新渲染该组件时，`this.state.count` 会变为 1，而不是你期望的 3。

  // 这是因为上面的 `incrementCount()` 函数是从 `this.state.count` 中读取数据的，
  // 但是 React 不会更新 `this.state.count`，直到该组件被重新渲染（`this.props` 和 `this.state` 都代表着*已经被渲染了的*值）。
  // 所以最终 `incrementCount()` 每次读取 `this.state.count` 的值都是 0，并将它设为 1。
}
```

要修复上述问题，可以给 `setState` 传递一个函数，而不是一个对象，就可以确保每次的调用都是使用最新版的 state。当参数是函数的时候，setState() 会将上一个 setState() 的结果作为参数传入这个函数（链式地进行更新，并确保它们是一个建立在另一个之上的）。

```jsx
incrementCount() {
  this.setState((state) => {
    // 重要：在更新的时候读取 `state`（pre_state），而不是 `this.state`。
    return {count: state.count + 1}
  });
}

handleSomething() {
  // 假设 `this.state.count` 从 0 开始。
  this.incrementCount();
  this.incrementCount();
  this.incrementCount();

  // 如果你现在在这里读取 `this.state.count`，它还是会为 0。
  // 但是，当 React 重新渲染该组件时，它会变为 3。
}
```

**组件生命周期**可见[官方生命周期图谱![React基础_process](img/React基础_process.png)](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)

每个组件都包含 “生命周期方法”，可重写这些方法以便于在运行过程中特定的阶段执行特定操作，包括：

- constructor()，构造函数，React 组件挂载之前，会调用这个函数。一般重写该函数来给 `this.state` 赋初始值或为时间处理函数绑定实例。在为 React.Component 子类实现构造函数时，应在其他语句之前前调用`super(props)`，否则，`this.props` 在构造函数中可能会出现未定义的 bug
- getDriveredStateFromProps()
- render()，`render()` 方法是 class 组件中唯一必须实现的方法，它检查 `this.props` 和 `this.state` 的变化并返回React元素，在不修改组件 state 的情况下，每次调用时都返回相同的结果，并且它不会直接与浏览器交互。
- componentDidMount()，`componentDidMount()` 会在组件挂载后（插入 DOM 树中）立即调用。依赖于 DOM 节点的初始化应该放在这里，需要注意的是组件mount后，上层组件使其props更新后仅会update而不会重新mount。
- **componentDidUpdate()**，`componentDidUpdate()` 会在更新后会被立即调用。首次渲染不会执行此方法。
- **componentWillUnmount()**，`componentWillUnmount()` 会在组件卸载及销毁之前直接调用。在此方法中执行必要的清理操作，如清除 timer，取消网络请求或清除在 `componentDidMount()` 中创建的订阅等。

> 1. 当 `<Clock />` 被传递给 `ReactDOM.render()` 时，React 调用 `Clock` 组件的构造函数。 由于 `Clock` 需要显示当前时间，所以使用包含当前时间的对象来初始化 `this.state` 。 我们稍后会更新此状态。
> 2. React 然后调用 `Clock` 组件的 `render()` 方法。这是 React 了解屏幕上应该显示什么内容，然后 React 更新 DOM 以匹配 `Clock` 的渲染输出。
> 3. 当 `Clock` 的输出插入到 DOM 中时，React 调用 `componentDidMount()` 生命周期[钩子](#)。 在其中，`Clock` 组件要求浏览器设置一个定时器，每秒钟调用一次 `tick()`。
> 4. 浏览器每秒钟调用 `tick()` 方法。 在其中，`Clock` 组件通过使用包含当前时间的对象调用 `setState()` 来调度UI更新。 通过调用 `setState()` ，React 知道状态已经改变，并再次调用 `render()` 方法来确定屏幕上应当显示什么。 这一次，`render()` 方法中的 `this.state.date` 将不同，所以渲染输出将包含更新的时间，并相应地更新 DOM。
> 5. 一旦 `Clock` 组件被从 DOM 中移除，React 会调用 `componentWillUnmount()` 这个钩子函数，定时器也就会被清除。

#### 数据向下流动与状态提升

**组件复合**指通过创建多个组件合成一个组件，如下，下层组件`Welcome`接受上层组件`App`提供的数据构建组件。

```jsx
function Welcome(props) {  // 下层组件
  return <h1>Hello, {props.name}</h1>;  // 下层组件接受上层组件提供的props
}

function App() {  // 上层组件 ancestor.
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

通过上面关于`props`和`state`的介绍，我们知道`props`只能由上层级组件传入下层级组件，所以称为**向下流动的数据**，而`state`又只能在当前组件中记录状态，直接使用`props`和`state`似乎无法完成**下层级到上层级**或**同层级组件**间的数据传输，但结合回调函数，我们可以以一种名为**状态提升**的方式实现

以下层组件向上层组件传输数据为例，我们有上层组件`Base`，下层组件`Child`，通过用户输入我们在`Child`中获得数据`data`，我们的目标是将`data`从`Child`传入`Base`中。

首先我们在`Base`中设定一个修改/传递数据的函数`handleData`，将`handleData`这个函数通过`props`传入`Child`，当`Child`获得`data`后，通过一定的事件（如点击`onClick`事件）调用父级组件的`handleData`函数，将`data`传入`Base`。

如下是一个状态提升的示例，程序提供两个输入框分别显示华氏温度和摄氏温度，用户输入其中一个，另一个输入框根据输入自动更新，详细信息可见[状态提升-React中文文档](https://reactjs.bootcss.com/docs/lifting-state-up.html)。

```jsx
function tryConvert(temperature, convert) {
  const input = parseFloat(temperature);
  if (Number.isNaN(input)) {
    return '';
  }
  const output = convert(input);
  const rounded = Math.round(output * 1000) / 1000;
  return rounded.toString();
}

class Calculator extends React.Component { // 上层组件
  constructor(props) {
    super(props);
    this.handleCelsiusChange = this.handleCelsiusChange.bind(this);
    this.handleFahrenheitChange = this.handleFahrenheitChange.bind(this);
    this.state = {temperature: '', scale: 'c'};
  }

  handleCelsiusChange(temperature) {
    this.setState({scale: 'c', temperature});
  }

  handleFahrenheitChange(temperature) {
    this.setState({scale: 'f', temperature});
  }

  render() {
    const scale = this.state.scale;
    const temperature = this.state.temperature;
    const celsius = scale === 'f' ? tryConvert(temperature, toCelsius) : temperature;
    const fahrenheit = scale === 'c' ? tryConvert(temperature, toFahrenheit) : temperature;

    return (
      <div>
        <TemperatureInput
          scale="c"
          temperature={celsius}
          onTemperatureChange={this.handleCelsiusChange} />
        <TemperatureInput
          scale="f"
          temperature={fahrenheit}
          onTemperatureChange={this.handleFahrenheitChange} />
        <BoilingVerdict
          celsius={parseFloat(celsius)} />
      </div>
    );
  }
}

const scaleNames = {
  c: 'Celsius',
  f: 'Fahrenheit'
};

class TemperatureInput extends React.Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    this.props.onTemperatureChange(e.target.value);
  }

  render() {
    const temperature = this.props.temperature;
    const scale = this.props.scale;
    return (
      <fieldset>
        <legend>Enter temperature in {scaleNames[scale]}:</legend>
        <input value={temperature}
               onChange={this.handleChange} />
      </fieldset>
    );
  }
}
```







参考资料：

[SPA（单页面应用）和MPA（多页面应用）](https://www.jianshu.com/p/a02eb15d2d70)

[Create React App 中文文档](https://www.html.cn/create-react-app/)

[React教程-菜鸟教程](https://www.runoob.com/react/react-tutorial.html)

[HTML DOM 教程-菜鸟教程](https://www.runoob.com/htmldom/htmldom-tutorial.html)

[React学习：状态提升 实例](<https://blog.csdn.net/b954960630/article/details/80216160>)

[关于e.target](<https://segmentfault.com/q/1010000014782282>)

