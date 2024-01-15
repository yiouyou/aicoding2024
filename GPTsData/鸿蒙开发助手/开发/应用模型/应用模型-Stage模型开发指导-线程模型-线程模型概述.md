# 线程模型概述

更新时间: 2024-01-15 12:17

HarmonyOS应用中每个进程都会有一个主线程，主线程有如下职责：

1. 执行UI绘制；
2. 管理主线程的ArkTS引擎实例，使多个UIAbility组件能够运行在其之上；
3. 管理其他线程（例如Worker线程）的ArkTS引擎实例，例如启动和终止其他线程；
4. 分发交互事件；
5. 处理应用代码的回调，包括事件处理和生命周期管理；
6. 接收Worker线程发送的消息；

除主线程外，还有一类与主线程并行的独立线程Worker，主要用于执行耗时操作，但不可以直接操作UI。Worker线程在主线程中创建，与主线程相互独立。最多可以创建8个Worker：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183829.84284400967280132653406303838080:50001231000000:2800:BE3E57C2B4D0144FDD76F3AB5F35C39C7F791AB7A3191D8E8433E58B105B04F8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

基于HarmonyOS的线程模型，不同的业务功能运行在不同的线程上，业务功能的交互就需要线程间通信。线程间通信目前主要有Emitter和Worker两种方式，其中Emitter主要适用于线程间的事件同步， Worker主要用于新开一个线程执行耗时任务。

说明：

* Stage模型只提供了主线程和Worker线程，Emitter主要用于主线程内或者主线程和Worker线程的事件同步。

