# 公共事件订阅概述

更新时间: 2024-01-15 11:54

公共事件服务提供了动态订阅和静态订阅两种订阅方式。动态订阅与静态订阅最大的区别在于，动态订阅是应用运行时行为，而静态订阅是后台服务无需处于运行状态。

* 动态订阅：指订阅方在运行时调用公共事件订阅的API实现对公共事件的订阅，详见[动态订阅公共事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/common-event-subscription-0000001544583897-V3)。
* 静态订阅：订阅方通过配置文件声明和实现继承自StaticSubscriberExtensionAbility的类实现对公共事件的订阅，详见[静态订阅公共事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/common-event-static-subscription-0000001544703825-V3)。

