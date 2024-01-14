# 管理应用拥有的状态概述

更新时间: 2024-01-10 11:30

上一个章节中介绍的装饰器仅能在页面内，即一个组件树上共享状态变量。如果开发者要实现应用级的，或者多个页面的状态数据共享，就需要用到应用级别的状态管理的概念。ArkTS根据不同特性，提供了多种应用状态管理的能力：

* [LocalStorage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-localstorage-0000001524537149-V3)：页面级UI状态存储，通常用于[UIAbility](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-ability-uiability-0000001493584184-V3)内、页面间的状态共享。
* [AppStorage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-appstorage-0000001524417209-V3)：特殊的单例LocalStorage对象，由UI框架在应用程序启动时创建，为应用程序UI状态属性提供中央存储；
* [PersistentStorage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-persiststorage-0000001474017166-V3)：持久化存储UI状态，通常和AppStorage配合使用，选择AppStorage存储的数据写入磁盘，以确保这些属性在应用程序重新启动时的值与应用程序关闭时的值相同；
* [Environment](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-environment-0000001473537710-V3)：应用程序运行的设备的环境参数，环境参数会同步到AppStorage中，可以和AppStorage搭配使用。

