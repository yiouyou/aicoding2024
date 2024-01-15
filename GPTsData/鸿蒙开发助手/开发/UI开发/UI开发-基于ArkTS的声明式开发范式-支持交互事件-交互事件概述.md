# 交互事件概述

更新时间: 2024-01-15 11:54

交互事件按照触发类型来分类，包括触屏事件、键鼠事件和焦点事件。

* [触屏事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-touch-screen-event-0000001451076450-V3)：手指或手写笔在触屏上的单指或单笔操作。
* [键鼠事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-device-input-event-0000001529125201-V3)：包括外设鼠标或触控板的操作事件和外设键盘的按键事件。
  * 鼠标事件是指通过连接和使用外设鼠标/触控板操作时所响应的事件。
  * 按键事件是指通过连接和使用外设键盘操作时所响应的事件。
* [焦点事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3)：通过以上方式控制组件焦点的能力和响应的事件。

手势事件由绑定手势方法和绑定的手势组成，绑定的手势可以分为单一手势和组合手势两种类型，根据手势的复杂程度进行区分。

* [绑定手势方法](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-binding-0000001529037393-V3)：用于在组件上绑定单一手势或组合手势，并声明所绑定的手势的响应优先级。
* [单一手势](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-single-gesture-0000001450596854-V3)：手势的基本单元，是所有复杂手势的组成部分。
* [组合手势](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-combined-gestures-0000001500756325-V3)：由多个单一手势组合而成，可以根据声明的类型将多个单一手势按照一定规则组合成组合手势，并进行使用。

