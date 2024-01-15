# Stage模型开发概述

更新时间: 2024-01-15 12:17

## 基本概念

下图展示了Stage模型中的基本概念。

图1 Stage模型概念图

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183808.05512713618873359169037194692218:50001231000000:2800:D9354C1CE456CD407E4B4F43B82950F7BE0B6E19F6DA2D8B3A321DCF95F5615A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* [UIAbility组件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-overview-0000001477980929-V3)和ExtensionAbility组件
  Stage模型提供UIAbility和ExtensionAbility两种类型的组件，这两种组件都有具体的类承载，支持面向对象的开发方式。
  * UIAbility组件是一种包含UI界面的应用组件，主要用于和用户交互。例如，图库类应用可以在UIAbility组件中展示图片瀑布流，在用户选择某个图片后，在新的页面中展示图片的详细内容。同时用户可以通过返回键返回到瀑布流页面。UIAbility的生命周期只包含创建/销毁/前台/后台等状态，与显示相关的状态通过WindowStage的事件暴露给开发者。
  * ExtensionAbility组件是一种面向特定场景的应用组件。
* [WindowStage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-window-stage-0000001427584712-V3)
  每个UIAbility类实例都会与一个WindowStage类实例绑定，该类提供了应用进程内窗口管理器的作用。它包含一个主窗口。也就是说UIAbility通过WindowStage持有了一个窗口，该窗口为ArkUI提供了绘制区域。
* [Context](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3)
  在Stage模型上，Context及其派生类向开发者提供在运行期可以调用的各种能力。UIAbility组件和各种ExtensionAbility派生类都有各自不同的Context类，他们都继承自基类Context，但是各自又根据所属组件，提供不同的能力。
* [AbilityStage](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/abilitystage-0000001427584604-V3)
  每个Entry类型或者Feature类型的HAP在运行期都有一个AbilityStage类实例，当HAP中的代码首次被加载到进程中的时候，系统会先创建AbilityStage实例。每个在该HAP中定义的UIAbility类，在实例化后都会与该实例产生关联。开发者可以使用AbilityStage获取该HAP中UIAbility实例的运行时信息。

## 开发流程

基于Stage模型开发应用时，在应用模型部分，涉及如下开发过程。

表1 Stage模型开发流程

| 任务         | 简介                                                                         | 相关指导                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :----------- | :--------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 应用组件开发 | 本章节介绍了如何使用Stage模型的UIAbility组件和ExtensionAbility组件开发应用。 | -[应用/组件级配置](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-component-configuration-stage-0000001478340869-V3)- [UIAbility组件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/uiability-overview-0000001477980929-V3)- [ExtensionAbility组件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/4_3extensionability_u7ec4_u4ef6-0000001478340873-V3)- [AbilityStage组件容器](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/abilitystage-0000001427584604-V3)- [应用上下文Context](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3) |
| 了解进程模型 | 本章节介绍了Stage模型的进程模型以及几种常用的进程间通信方式。                | -[公共事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/common-event-overview-0000001427744568-V3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 了解线程模型 | 本章节介绍了Stage模型的线程模型以及几种常用的线程间通信方式。                | -[Emitter](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/itc-with-emitter-0000001427584616-V3)- [Worker](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/itc-with-worker-0000001427744572-V3)                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 应用配置文件 | 本章节介绍Stage模型中应用配置文件的开发要求。                                | [Stage模型应用配置文件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-configuration-file-overview-stage-0000001428061460-V3)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

