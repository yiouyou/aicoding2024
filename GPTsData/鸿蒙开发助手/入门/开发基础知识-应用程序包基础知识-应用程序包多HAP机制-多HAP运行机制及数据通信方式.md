# 多HAP运行机制及数据通信方式

更新时间: 2024-01-10 11:30

多HAP机制主要是为方便开发者进行模块化管理。HAP和应用运行时的进程并不是一一对应的，具体运行机制如下：

* 默认情况下，应用中（同一包名）的所有UIAbility、ServiceExtensionAbility、DataShareExtensionAbility运行在同一个独立进程中，其他同类型ExtensionAbility分别运行在单独的进程。
* HAP支持在module.json5（Stage模型）或者config.json（FA模型）中通过process标签配置单独的进程（仅系统应用支持，三方应用不支持）。配置了process的HAP，其组件运行在单独的process进程中，多个HAP可以配置相同的process，则这些HAP运行在相同进程中，process配置的详细说明请参见[module.json5配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/module-configuration-file-0000001427744540-V3)。
* 应用运行时，同一进程中的UIAbility组件被启动时，才加载对应HAP的资源和代码。

基于上述机制，多HAP数据通信方式如下：

* 同一进程内的数据通信，请参见[线程间通信](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/thread-model-stage-0000001428061492-V3)。
* 跨进程的数据通信，请参见[进程间通信](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/process-model-stage-0000001428061488-V3)。
* 多HAP如果运行在同一进程，则多HAP间组件的通信方式与同一HAP内组件的通信方式相同。

