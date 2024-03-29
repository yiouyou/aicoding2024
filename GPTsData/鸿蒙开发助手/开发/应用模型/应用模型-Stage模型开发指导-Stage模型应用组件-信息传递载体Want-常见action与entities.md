# 常见action与entities

更新时间: 2024-01-15 11:54

[action](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantaction)：表示调用方要执行的通用操作（如查看、分享、应用详情）。在隐式Want中，您可定义该字段，配合uri或parameters来表示对数据要执行的操作。如打开，查看该uri数据。例如，当uri为一段网址，action为ohos.want.action.viewData则表示匹配可查看该网址的Ability。在Want内声明action字段表示希望被调用方应用支持声明的操作。在被调用方应用配置文件skills字段内声明actions表示该应用支持声明操作。

常见action

* ACTION_HOME：启动应用入口组件的动作，需要和ENTITY_HOME配合使用；系统桌面应用图标就是显式的入口组件，点击也是启动入口组件；入口组件可以配置多个。
* ACTION_CHOOSE：选择本地资源数据，例如联系人、相册等；系统一般对不同类型的数据有对应的Picker应用，例如联系人和图库。
* ACTION_VIEW_DATA：查看数据，当使用网址uri时，则表示显示该网址对应的内容。
* ACTION_VIEW_MULTIPLE_DATA：发送多个数据记录的操作。

[entities](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-ability-wantconstant-0000001544583997-V3#ZH-CN_TOPIC_0000001574088649__wantconstantentity)：表示目标Ability的类别信息（如浏览器、视频播放器），在隐式Want中是对action的补充。在隐式Want中，开发者可定义该字段，来过滤匹配应用的类别，例如必须是浏览器。在Want内声明entities字段表示希望被调用方应用属于声明的类别。在被调用方应用配置文件skills字段内声明entites表示该应用支持的类别。

常用entities

* ENTITY_DEFAULT：默认类别无实际意义。
* ENTITY_HOME：主屏幕有图标点击入口类别。
* ENTITY_BROWSABLE：指示浏览器类别。

