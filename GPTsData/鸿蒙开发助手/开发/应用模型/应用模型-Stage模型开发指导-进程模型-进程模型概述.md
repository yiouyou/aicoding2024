# 进程模型概述

更新时间: 2024-01-15 11:54

HarmonyOS的进程模型：

* 应用中（同一包名）的所有UIAbility运行在同一个独立进程中。
* WebView拥有独立的渲染进程。

基于HarmonyOS的进程模型，系统提供了[公共事件机制](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/common-event-overview-0000001427744568-V3)用于一对多的通信场景，公共事件发布者可能存在多个订阅者同时接收事件。

