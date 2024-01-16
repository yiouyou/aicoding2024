# 方舟开发框架（ArkUI）概述

更新时间: 2024-01-15 12:16

方舟开发框架（简称ArkUI）为HarmonyOS应用的UI开发提供了完整的基础设施，包括简洁的UI语法、丰富的UI功能（组件、布局、动画以及交互事件），以及实时界面预览工具等，可以支持开发者进行可视化界面开发。

## 基本概念

* UI： 即用户界面。开发者可以将应用的用户界面设计为多个功能页面，每个页面进行单独的文件管理，并通过[页面路由](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3)API完成页面间的调度管理如跳转、回退等操作，以实现应用内的功能解耦。
* 组件： UI构建与显示的最小单位，如列表、网格、按钮、单选框、进度条、文本等。开发者通过多种组件的组合，构建出满足自身应用诉求的完整界面。

## 两种开发范式

针对不同的应用场景及技术背景，方舟开发框架提供了两种开发范式，分别是[基于ArkTS的声明式开发范式](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-development-overview-0000001438467628-V3)（简称“声明式开发范式”）和[兼容JS的类Web开发范式](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/ui-js-overview-0000001428061548-V3)（简称“类Web开发范式”）。

* 声明式开发范式 ：采用基于TypeScript声明式UI语法扩展而来的[ArkTS语言](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-get-started-0000001504769321-V3)，从组件、动画和状态管理三个维度提供UI绘制能力。
* 类Web开发范式 ：采用经典的HML、CSS、JavaScript三段式开发方式，即使用HML标签文件搭建布局、使用CSS文件描述样式、使用JavaScript文件处理逻辑。该范式更符合于Web前端开发者的使用习惯，便于快速将已有的Web应用改造成方舟开发框架应用。

在开发一款新应用时，推荐采用声明式开发范式来构建UI，主要基于以下几点考虑：

* 开发效率： 声明式开发范式更接近自然语义的编程方式，开发者可以直观地描述UI，无需关心如何实现UI绘制和渲染，开发高效简洁。
* 应用性能： 如下图所示，两种开发范式的UI后端引擎和语言运行时是共用的，但是相比类Web开发范式，声明式开发范式无需JS框架进行页面DOM管理，渲染更新链路更为精简，占用内存更少，应用性能更佳。
* 发展趋势 ：声明式开发范式后续会作为主推的开发范式持续演进，为开发者提供更丰富、更强大的能力。

图1 方舟开发框架示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183835.03366751673772256616095400007738:50001231000000:2800:C84BBC2EA8BE63DEF6B997C2D37A613DAF3D4CFDBF754020D01326A2D9E9C269.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 不同应用类型支持的开发范式

根据所选用HarmonyOS[应用模型](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-model-composition-0000001544384013-V3)（Stage模型、FA模型）和页面形态（应用或服务的普通页面、卡片）的不同，对应支持的UI开发范式也有所差异，详见下表。

表1 支持的UI开发范式

| 应用模型          | 页面形态         | 支持的UI开发范式                    |
| :---------------- | :--------------- | :---------------------------------- |
| Stage模型（推荐） | 应用或服务的页面 | 声明式开发范式（推荐）              |
|                   | 卡片             | 声明式开发范式（推荐）类Web开发范式 |
| FA模型            | 应用或服务的页面 | 声明式开发范式类Web开发范式         |
|                   | 卡片             | 类Web开发范式                       |



# UI开发（ArkTS声明式开发范式）概述

更新时间: 2024-01-15 12:17

基于ArkTS的声明式开发范式的方舟开发框架是一套开发极简、高性能、支持跨设备的UI开发框架，提供了构建HarmonyOS应用UI所必需的能力，主要包括：

* ArkTS
  ArkTS是HarmonyOS优选的主力应用开发语言，围绕应用开发在[TypeScript](https://gitee.com/link?target=https://www.typescriptlang.org/)（简称TS）生态基础上做了进一步扩展。扩展能力包含声明式UI描述、自定义组件、动态扩展UI元素、状态管理和渲染控制。状态管理作为基于ArkTS的声明式开发范式的特色，通过功能不同的装饰器给开发者提供了清晰的页面更新渲染流程和管道。状态管理包括UI组件状态和应用程序状态，两者协作可以使开发者完整地构建整个应用的数据更新和UI渲染。ArkTS语言的基础知识请参考[学习ArkTS语言](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-get-started-0000001504769321-V3)。
* 布局
  布局是UI的必要元素，它定义了组件在界面中的位置。ArkUI框架提供了多种布局方式，除了基础的线性布局、层叠布局、弹性布局、相对布局、栅格布局外，也提供了相对复杂的列表、宫格、轮播。
* 组件
  组件是UI的必要元素，形成了在界面中的样子，由框架直接提供的称为 系统组件 ，由开发者定义的称为 自定义组件 。系统内置组件包括按钮、单选框、进度条、文本等。开发者可以通过链式调用的方式设置系统内置组件的渲染效果。开发者可以将系统内置组件组合为自定义组件，通过这种方式将页面组件化为一个个独立的UI单元，实现页面不同单元的独立创建、开发和复用，具有更强的工程性。
* 页面路由和组件导航
  应用可能包含多个页面，可通过页面路由实现页面间的跳转。一个页面内可能存在组件间的导航如典型的分栏，可通过导航组件实现组件间的导航。
* 图形
  方舟开发框架提供了多种类型图片的显示能力和多种自定义绘制的能力，以满足开发者的自定义绘图需求，支持绘制形状、填充颜色、绘制文本、变形与裁剪、嵌入图片等。
* 动画
  动画是UI的重要元素之一。优秀的动画设计能够极大地提升用户体验，框架提供了丰富的动画能力，除了组件内置动画效果外，还包括属性动画、显式动画、自定义转场动画以及动画API等，开发者可以通过封装的物理模型或者调用动画能力API来实现自定义动画轨迹。
* 交互事件
  交互事件是UI和用户交互的必要元素。方舟开发框架提供了多种交互事件，除了触摸事件、鼠标事件、键盘按键事件、焦点事件等通用事件外，还包括基于通用事件进行进一步识别的手势事件。手势事件有单一手势如点击手势、长按手势、拖动手势、捏合手势、旋转手势、滑动手势，以及通过单一手势事件进行组合的组合手势事件。

## 特点

* 开发效率高，开发体验好
* 代码简洁：通过接近自然语义的方式描述UI，不必关心框架如何实现UI绘制和渲染。
* 数据驱动UI变化：让开发者更专注自身业务逻辑的处理。当UI发生变化时，开发者无需编写在不同的UI之间进行切换的UI代码， 开发人员仅需要编写引起界面变化的数据，具体UI如何变化交给框架。
* 开发体验好：界面也是代码，让开发者的编程体验得到提升。
* 性能优越
  * 声明式UI前端和UI后端分层：UI后端采用C++语言构建，提供对应前端的基础组件、布局、动效、交互事件、组件状态管理和渲染管线。
  * 语言编译器和运行时的优化：统一字节码、高效FFI-Foreign Function Interface、AOT-Ahead Of Time、引擎极小化、类型优化等。
* 生态容易快速推进能够借力主流语言生态快速推进，语言相对中立友好，有相应的标准组织可以逐步演进。

## 整体架构

图1 整体架构图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183835.55416990424641061066031010287574:50001231000000:2800:72C8299F2C597AEB3953F8A5E5D31D3C1927137D8452D5686181BE4D668AD46C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 声明式UI前端
  提供了UI开发范式的基础语言规范，并提供内置的UI组件、布局和动画，提供了多种状态管理机制，为应用开发者提供一系列接口支持。
* 语言运行时
  选用方舟语言运行时，提供了针对UI范式语法的解析能力、跨语言调用支持的能力和TS语言高性能运行环境。
* 声明式UI后端引擎
  后端引擎提供了兼容不同开发范式的UI渲染管线，提供多种基础组件、布局计算、动效、交互事件，提供了状态管理和绘制能力。
* 渲染引擎
  提供了高效的绘制能力，将渲染管线收集的渲染指令，绘制到屏幕的能力。
* 平台适配层
  提供了对系统平台的抽象接口，具备接入不同系统的能力，如系统渲染管线、生命周期调度等。

## 开发流程

使用UI开发框架开发应用时，主要涉及如下开发过程。开发者可以先通过[第一个入门](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/start-with-ets-stage-0000001477980905-V3)实例了解整个应用的UI开发过程。

| 任务                   | 简介                                                                | 相关指导                                                                                                                                                                                                                                                                                                                                                                                                      |
| :--------------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 学习ArkTS              | 介绍了ArkTS的基本语法、状态管理和渲染控制的场景。                   | *[基本语法](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-basic-syntax-overview-0000001531611153-V3)* [状态管理](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-state-management-overview-0000001524537145-V3)* [渲染控制](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-overview-0000001543911149-V3)            |
| 开发布局               | 介绍了几种常用的布局方式以及如何提升布局性能。                      | *[常用布局](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-overview-0000001450866508-V3)* [布局性能](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-performance-boost-0000001450914106-V3)                                                                                                                              |
| 添加组件               | 介绍了几种常用的内置组件、自定义组件以及通过API方式支持的界面元素。 | *[常用组件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-components-button-0000001450914110-V3)* [自定义组件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-create-custom-components-0000001473537046-V3)* [气泡和菜单](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-popup-and-menu-components-popup-0000001500753909-V3) |
| 设置页面路由和组件导航 | 介绍了如何设置页面路由以及组件间的导航。                            | *[页面路由](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3)* [组件导航](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-navigation-navigation-0000001453365116-V3)                                                                                                                                                                 |
| 显示图形               | 介绍了如何显示图片、绘制自定义几何图形以及使用画布绘制自定义图形。  | *[图片](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-graphics-display-0000001451075174-V3)* [几何图形](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-geometric-shape-drawing-0000001503484809-V3)* [画布](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-drawing-customization-on-canvas-0000001453684976-V3)                      |
| 使用动画               | 介绍了组件和页面使用动画的典型场景。                                | *[页面内的动画](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-update-animation-0000001500356349-V3)* [页面间的动画](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-zoom-animation-0000001500515609-V3)                                                                                                                                                |
| 绑定事件               | 介绍了事件的基本概念和如何使用通用事件和手势事件。                  | *[通用事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-touch-screen-event-0000001451076450-V3)* [手势事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-binding-0000001529037393-V3)                                                                                                                                       |



# 布局概述

更新时间: 2024-01-15 12:17

组件按照布局的要求依次排列，构成应用的页面。在声明式UI中，所有的页面都是由自定义组件构成，开发者可以根据自己的需求，选择合适的布局进行页面开发。

布局指用特定的组件或者属性来管理用户页面所放置UI组件的大小和位置。在实际的开发过程中，需要遵守以下流程保证整体的布局效果：

* 确定页面的布局结构。
* 分析页面中的元素构成。
* 选用适合的布局容器组件或属性控制页面中各个元素的位置和大小约束。

## 布局结构

布局的结构通常是分层级的，代表了用户界面中的整体架构。一个常见的页面结构如下所示：

图1 常见页面结构图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103816.48715349484013210532094168148068:50001231000000:2800:C606FA6FEA2FE4B4192AE39FAA6140B6882A44E25F117B593A499C923E540562.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

为实现上述效果，开发者需要在页面中声明对应的元素。其中，Page表示页面的根节点，Column/Row等元素为系统组件。针对不同的页面结构，ArkUI提供了不同的布局组件来帮助开发者实现对应布局的效果，例如Row用于实现线性布局。

## 布局元素的组成

布局相关的容器组件可形成对应的布局效果。例如，List组件可构成线性布局。

图2 布局元素组成图

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103816.24200095737901364536591001243773:50001231000000:2800:5FD7BAAFB684932B448182A93FB7F4CBC39E23335E58FBBAC44D74736764ABE7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 组件区域（蓝区方块）：组件区域表明组件的大小，width、height属性设置该区域的大小。
* 组件内容区（黄色方块）：组件区域大小减去组件的border值，组件内容区大小会作为组件内容（或者子组件）进行大小测算时的布局测算限制。
* 组件内容（绿色方块）：组件内容本身占用的大小，比如文本内容占用的大小。组件内容和组件内容区不一定匹配，比如设置了固定的width和height，此时组件内容的大小就是设置的width和height减去padding和border值，但文本内容则是通过文本布局引擎测算后得到的大小，可能出现文本真实大小小于设置的组件内容区大小。当组件内容和组件内容区大小不一致时，align属性生效，定义组件内容在组件内容区的对齐方式，如居中对齐。
* 组件布局边界（虚线部分）：组件通过margin属性设置外边距时，组件布局边界就是组件区域加上margin的大小。

## 如何选择布局

声明式UI提供了以下8种常见布局，开发者可根据实际应用场景选择合适的布局进行页面开发。

| 布局                                                                                                                                                           | 应用场景                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [线性布局](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-linear-0000001504125349-V3)（Row、Column）                | 如果布局内子元素超过1个，且能够以某种方式线性排列时优先考虑此布局。                                                                                                                                                                                                                                                                                                  |
| [层叠布局](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-stack-layout-0000001454605342-V3)（Stack）                | 组件需要有堆叠效果时优先考虑此布局，层叠布局的堆叠效果不会占用或影响其他同容器内子组件的布局空间。例如[Panel](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-panel-0000001427744836-V3)作为子组件弹出时将其他组件覆盖更为合理，则优先考虑在外层使用堆叠布局。                                                                     |
| [弹性布局](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-flex-layout-0000001504525013-V3)（Flex）                  | 弹性布局是与线性布局类似的布局方式。区别在于弹性布局默认能够使子组件压缩或拉伸。在子组件需要计算拉伸或压缩比例时优先使用此布局，可使得多个容器内子组件能有更好的视觉上的填充容器效果。                                                                                                                                                                               |
| [相对布局](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-relative-layout-0000001455042516-V3)（RelativeContainer） | 相对布局是在二维空间中的布局方式，不需要遵循线性布局的规则，布局方式更为自由。通过在子组件上设置锚点规则（AlignRules）使子组件能够将自己在横轴、纵轴中的位置与容器或容器内其他子组件的位置对齐。设置的锚点规则可以天然支持子元素压缩、拉伸，堆叠或形成多行效果。在页面元素分布复杂或通过线性布局会使容器嵌套层数过深时推荐使用。                                     |
| [栅格布局](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-grid-layout-0000001454765270-V3)（GridRow、GridCol）      | 栅格是多设备场景下通用的辅助定位工具，通过将空间分割为有规律的栅格。栅格不同于网格布局固定的空间划分，它可以实现不同设备下不同的布局，空间划分更随心所欲，从而显著降低适配不同屏幕尺寸的设计及开发成本，使得整体设计和开发流程更有秩序和节奏感，同时也保证多设备上应用显示的协调性和一致性，提升用户体验。推荐手机、大屏、平板等不同设备，内容相同但布局不同时使用。 |
| [媒体查询](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-media-query-0000001454445606-V3)（@ohos.mediaquery）      | 媒体查询可根据不同设备类型或同设备不同状态修改应用的样式。例如根据设备和应用的不同属性信息设计不同的布局，以及屏幕发生动态改变时更新应用的页面布局。                                                                                                                                                                                                                 |
| [列表](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3)（List）                      | 使用列表可以轻松高效地显示结构化、可滚动的信息。在ArkUI中，列表具有垂直和水平布局能力和自适应交叉轴方向上排列个数的布局能力，超出屏幕时可以滚动。列表适合用于呈现同类数据类型或数据类型集，例如图片和文本。                                                                                                                                                          |
| [网格](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-grid-0000001504486057-V3)（Grid）                      | 网格布局具有较强的页面均分能力，子组件占比控制能力，是一种重要自适应布局。网格布局可以控制元素所占的网格数量、设置子组件横跨几行或者几列，当网格容器尺寸发生变化时，所有子组件以及间距等比例调整。推荐在需要按照固定比例或者均匀分配空间的布局场景下使用，例如计算器、相册、日历等。                                                                                 |
| [轮播](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-looping-0000001454931830-V3)（Swiper）                 | 轮播组件通常用于实现广告轮播、图片预览、可滚动应用等。                                                                                                                                                                                                                                                                                                               |

## 布局位置

position、offset等属性影响了布局容器相对于自身或其他组件的位置。

| 定位能力 | 使用场景                                                                               | 实现方式                                                                                                                                                                                                                                                            |
| :------- | :------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 绝对定位 | 对于不同尺寸的设备，使用绝对定位的适应性会比较差，在屏幕的适配上有缺陷。               | 使用[position](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-location-0000001427584824-V3)实现绝对定位，设置元素左上角相对于父容器左上角偏移位置。在布局容器中，设置该属性不影响父容器布局，仅在绘制时进行位置调整。 |
| 相对定位 | 相对定位不脱离文档流，即原位置依然保留，不影响元素本身的特性，仅相对于原位置进行偏移。 | 使用[offset](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-location-0000001427584824-V3)可以实现相对定位，设置元素相对于自身的偏移量。设置该属性，不影响父容器布局，仅在绘制时进行位置调整。                         |

## 对子元素的约束

| 对子元素的约束能力 | 使用场景                                                                                                                         | 实现方式                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 拉伸               | 容器组件尺寸发生变化时，增加或减小的空间全部分配给容器组件内指定区域。                                                           | [flexGrow](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)和[flexShrink](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性：1. flexGrow基于父容器的剩余空间分配来控制组件拉伸。1. flexShrink设置父容器的压缩尺寸来控制组件压缩。 |
| 缩放               | 子组件的宽高按照预设的比例，随容器组件发生变化，且变化过程中子组件的宽高比不变。                                                 | [aspectRatio](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-layout-constraints-0000001427744784-V3)属性指定当前组件的宽高比来控制缩放，公式为：aspectRatio=width/height。                                                                                                                                                                       |
| 占比               | 占比能力是指子组件的宽高按照预设的比例，随父容器组件发生变化。                                                                   | 基于通用属性的两种实现方式：1. 将子组件的宽高设置为父组件宽高的百分比。2. [layoutWeight](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-size-0000001428061700-V3)属性，使得子元素自适应占满剩余空间。                                                                                                                                            |
| 隐藏               | 隐藏能力是指容器组件内的子组件，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏，其中相同显示优先级的子组件同时显示或隐藏。 | 通过[displayPriority](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-layout-constraints-0000001427744784-V3)属性来控制页面的显示和隐藏。                                                                                                                                                                                                         |



# 线性布局（Row/Column）

更新时间: 2024-01-15 12:17

## 概述

线性布局（LinearLayout）是开发中最常用的布局，通过线性容器[Row](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-row-0000001478061717-V3)和[Column](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-column-0000001478341157-V3)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Column容器内子元素按照垂直方向排列，Row容器内子元素按照水平方向排列。根据不同的排列方向，开发者可选择使用Row或Column容器创建线性布局。

图1 Column容器内子元素排列示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.10408821819796528460105427538245:50001231000000:2800:7020D904725885BBB8DFA97F7000B1169B0F03A003752ADCC599FFA926F9231B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

图2 Row容器内子元素排列示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.67453062900729220136229791216409:50001231000000:2800:97A61FC171EA973D934D73CFA99CAF2A23088CCAB0CFC76AAFB236A93EFA5920.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 基本概念

* 布局容器：具有布局能力的容器组件，可以承载其他元素作为其子元素，布局容器会对其子元素进行尺寸计算和布局排列。

* 布局子元素：布局容器内部的元素。
* 主轴：线性布局容器在布局方向上的轴线，子元素默认沿主轴排列。Row容器主轴为水平方向，Column容器主轴为垂直方向。
* 交叉轴：垂直于主轴方向的轴线。Row容器交叉轴为垂直方向，Column容器交叉轴为水平方向。
* 间距：布局子元素的间距。

## 布局子元素在排列方向上的间距

在布局容器内，可以通过space属性设置排列方向上子元素的间距，使各子元素在排列方向上有等间距效果。

### Column容器内排列方向上的间距

图3 Column容器内排列方向的间距图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.57122332191520882936947620133261:50001231000000:2800:9331A877C0A83673D9B660E76C57559C7890E1BF63C740D4EE5E39DADEB52C17.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
Column({ space: 20 }) {
  Text('space: 20').fontSize(15).fontColor(Color.Gray).width('90%')
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
  Row().width('90%').height(50).backgroundColor(0xD2B48C)
  Row().width('90%').height(50).backgroundColor(0xF5DEB3)
}.width('100%')
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.26566956029801473769458710622477:50001231000000:2800:08C7FC016BE6A1C0D87C8E0FE34A7E020F1A292CF78C805F5EF7AC94A2DC3DB0.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### Row容器内排列方向上的间距

图4 Row容器内排列方向的间距图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.14653192204704273583449566542332:50001231000000:2800:006412CCDC5303BB7D1F7CF111C2315C0F38128C09A89554D1F1A6B50FAFF103.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
Row({ space: 35 }) {
  Text('space: 35').fontSize(15).fontColor(Color.Gray)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
  Row().width('10%').height(150).backgroundColor(0xD2B48C)
  Row().width('10%').height(150).backgroundColor(0xF5DEB3)
}.width('90%')
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.60008031670206980167100142966498:50001231000000:2800:6FA78A91778FA4BC90D79C2F36B4A81482D4DCD58F0CA8470890ECF25EA8386E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 布局子元素在交叉轴上的对齐方式

在布局容器内，可以通过alignItems属性设置子元素在交叉轴（排列方向的垂直方向）上的对齐方式。且在各类尺寸屏幕中，表现一致。其中，交叉轴为垂直方向时，取值为[VerticalAlign类型](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__verticalalign)，水平方向取值为[HorizontalAlign](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__horizontalalign)。

alignSelf属性用于控制单个子元素在容器交叉轴上的对齐方式，其优先级高于alignItems属性，如果设置了alignSelf属性，则在单个子元素上会覆盖alignItems属性。

### Column容器内子元素在水平方向上的排列

图5 Column容器内子元素在水平方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.85069341221009462031012466664099:50001231000000:2800:5D8175B50CA5F4B3D234CB0BB2A81B30AB6EB90B6863F910FCB3F716AA8446FA.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* HorizontalAlign.Start：子元素在水平方向左对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.Start).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142809.60951629222264030433705976305174:50001231000000:2800:9E9A896D07D7E19C07B4137A0AB249AAF4AB7BFB0842EB583FAC6A3823DEBF16.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* HorizontalAlign.Center：子元素在水平方向居中对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.Center).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.02134079336841605583329835444114:50001231000000:2800:6D5DAA3F87B85B51042B8EBA041A1FD6702B10D4D4E596A7822D337868DAC3B4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* HorizontalAlign.End：子元素在水平方向右对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').alignItems(HorizontalAlign.End).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.45977768659527231097394444575888:50001231000000:2800:C067AC79F73961F45A5860428F3596B2814A102962D336BA7D6035A46E9C3165.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### Row容器内子元素在垂直方向上的排列

图6 Row容器内子元素在垂直方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.11789049186891385222200526959821:50001231000000:2800:C166B0BF4B4CEF0453196C4D650D763AAC5C92B44CEC87359F987B90A7C8183D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* VerticalAlign.Top：子元素在垂直方向顶部对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Top).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.16676977917735074478869270523658:50001231000000:2800:A6A23DBCC69D796D458C94696CBCA7BC4BBB7BCDCF601CC0BF9AF95ED30D385F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* VerticalAlign.Center：子元素在垂直方向居中对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Center).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.19153990809444775569322940073601:50001231000000:2800:119E759DFF1B6AD6D63037EBCDA276D71885FF1D70F67AE60DD1B7D5F9E64D0D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* VerticalAlign.Bottom：子元素在垂直方向底部对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).alignItems(VerticalAlign.Bottom).backgroundColor('rgb(242,242,242)')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.61859652681513152160987592817819:50001231000000:2800:AAA223331C500D69E20D4A9EC86D0752851E16DE89ADB01FE229A2CDE3532668.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 布局子元素在主轴上的排列方式

在布局容器内，可以通过justifyContent属性设置子元素在容器主轴上的排列方式。可以从主轴起始位置开始排布，也可以从主轴结束位置开始排布，或者均匀分割主轴的空间。

### Column容器内子元素在垂直方向上的排列

图7 Column容器内子元素在垂直方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.26654709287413811372252601970942:50001231000000:2800:B3BFBA1BC5E0BE898C885784C1F112810D4D96439358BA8A9BDA1BCB9962EE10.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* justifyContent(FlexAlign.Start)：元素在垂直方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.16919978921459680606731764702340:50001231000000:2800:089440C547E1C002A54FE208B6D4F704AF7D29C788A18E1CE52740954C05F1C2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Center)：元素在垂直方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.94226725638737143810610474432326:50001231000000:2800:295AAE1FDDCB4E46A01F1F71B7E8792AE0238218BD120AC6DB998AD6FEA359F7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.End)：元素在垂直方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.02730687251544179186517905762202:50001231000000:2800:749AD10E32BF7D0A9698730FD175222030C52D1E8F8DBA3D716399B45C1B53FC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Spacebetween)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.65545086411708198430241459937849:50001231000000:2800:9DDE9E6951ADA63CBD806CDF9A1DD6727C74A40F3820D19FF55CF5CB16D452E1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceAround)：垂直方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.77447620657285171184570238222776:50001231000000:2800:DB8B19E25F12C92F6BB7D08FF5992D6D2EA9440AA307D38FBA35987BC357B97B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceEvenly)：垂直方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

```
Column({}) {
  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)

  Column() {
  }.width('80%').height(50).backgroundColor(0xD2B48C)

  Column() {
  }.width('80%').height(50).backgroundColor(0xF5DEB3)
}.width('100%').height(300).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.76673581595146875257832359880967:50001231000000:2800:5B83349842D8821502294DF4FABA5829502AF57D4C1010AC27194C7A54EAFB6F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### Row容器内子元素在水平方向上的排列

图8 Row容器内子元素在水平方向上的排列图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.46416226973241546619287224558714:50001231000000:2800:B435DD840998053EE65DE53DAF76825218D215205E5CDBA96B2969986231DA62.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* justifyContent(FlexAlign.Start)：元素在水平方向方向首端对齐，第一个元素与行首对齐，同时后续的元素与前一个对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Start)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.27302699606028731415014500799823:50001231000000:2800:1FC38B85067630BEAFB1C15B48BDA2DF6B5C7686C6AB86300D0E9F024669E158.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Center)：元素在水平方向方向中心对齐，第一个元素与行首的距离与最后一个元素与行尾距离相同。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.Center)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.36573290726626741597352920096217:50001231000000:2800:A05EE09C326620F5A77296033B1467E6F7141E2C38CAEAF639E93DE632652AD1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.End)：元素在水平方向方向尾部对齐，最后一个元素与行尾对齐，其他元素与后一个对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.End)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.71669053867342696874701662628156:50001231000000:2800:7F1173B64AE71324570E63610750FEC453D3D3FB459EA8A31565F489C7B4DCA6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.Spacebetween)：水平方向方向均匀分配元素，相邻元素之间距离相同。第一个元素与行首对齐，最后一个元素与行尾对齐。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceBetween)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.14665410400511619407800357179280:50001231000000:2800:1DA244465B28A4934DF2A242CE95FC76CC68E02D0DE8C5F17A8F7C2A848610A1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceAround)：水平方向方向均匀分配元素，相邻元素之间距离相同。第一个元素到行首的距离和最后一个元素到行尾的距离是相邻元素之间距离的一半。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceAround)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.04812205397561032060805302466837:50001231000000:2800:5AABC9F08188AAA041A750B701E89C49C30BAE6A0EA5ED3D4F4B788BF515DDA5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* justifyContent(FlexAlign.SpaceEvenly)：水平方向方向均匀分配元素，相邻元素之间的距离、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

```
Row({}) {
  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)

  Column() {
  }.width('20%').height(30).backgroundColor(0xD2B48C)

  Column() {
  }.width('20%').height(30).backgroundColor(0xF5DEB3)
}.width('100%').height(200).backgroundColor('rgb(242,242,242)').justifyContent(FlexAlign.SpaceEvenly)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.41653287622649410605452468673100:50001231000000:2800:8A68DE795AE9E835393A604A42CFD711B8D68B1C73E0BF9C64156113B0523BA4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自适应拉伸

在线性布局下，常用空白填充组件[Blank](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-blank-0000001428061724-V3)，在容器主轴方向自动填充空白空间，达到自适应拉伸效果。Row和Column作为容器，只需要添加宽高为百分比，当屏幕宽高发生变化时，会产生自适应效果。

```
@Entry
@Component
struct BlankExample {
  build() {
    Column() {
      Row() {
        Text('Bluetooth').fontSize(18)
        Blank()
        Toggle({ type: ToggleType.Switch, isOn: true })
      }.backgroundColor(0xFFFFFF).borderRadius(15).padding({ left: 12 }).width('100%')
    }.backgroundColor(0xEFEFEF).padding(20).width('100%')
  }
}
```

图9 竖屏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.52760781496991050161589218676053:50001231000000:2800:C79F70E4EEE5129F738431C4C9F4C76268107F4F5D43797AA93C209E0EBDF559.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

图10 横屏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142810.86168917853442316155687297983039:50001231000000:2800:002F0960889940584D82C0CE483EA03FE63ACF6E38C83AC04EF6B9FDA535D82E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自适应缩放

自适应缩放是指子组件随容器尺寸的变化而按照预设的比例自动调整尺寸，适应各种不同大小的设备。在线性布局中，可以使用以下两种方法实现自适应缩放。

* 父容器尺寸确定时，使用layoutWeight属性设置子组件和兄弟元素在主轴上的权重，忽略元素本身尺寸设置，使它们在任意尺寸的设备下自适应占满剩余空间。

```
@Entry
@Component
struct layoutWeightExample {
  build() {
    Column() {
      Text('1:2:3').width('100%')
      Row() {
        Column() {
          Text('layoutWeight(1)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(1).backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('layoutWeight(2)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(2).backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('layoutWeight(3)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')

      }.backgroundColor(0xffd306).height('30%')

      Text('2:5:3').width('100%')
      Row() {
        Column() {
          Text('layoutWeight(2)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(2).backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('layoutWeight(5)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(5).backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('layoutWeight(3)')
            .textAlign(TextAlign.Center)
        }.layoutWeight(3).backgroundColor(0xF5DEB3).height('100%')
      }.backgroundColor(0xffd306).height('30%')
    }
  }
}
```

  图11 横屏![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.49888199209215082288559229745576:50001231000000:2800:D06F04BDEDBA457CAFA43E0F8F060DC4143A59EBDDAAA4CBC79227363ED51678.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

  图12 竖屏![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.29623377163851288313519380242426:50001231000000:2800:C5034AB85E841274A2585BA9501B039AAE0EEAA24DB24CDBB363FBD14A6951BF.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 父容器尺寸确定时，使用百分比设置子组件和兄弟元素的宽度，使他们在任意尺寸的设备下保持固定的自适应占比。

```
@Entry
@Component
struct WidthExample {
  build() {
    Column() {
      Row() {
        Column() {
          Text('left width 20%')
            .textAlign(TextAlign.Center)
        }.width('20%').backgroundColor(0xF5DEB3).height('100%')

        Column() {
          Text('center width 50%')
            .textAlign(TextAlign.Center)
        }.width('50%').backgroundColor(0xD2B48C).height('100%')

        Column() {
          Text('right width 30%')
            .textAlign(TextAlign.Center)
        }.width('30%').backgroundColor(0xF5DEB3).height('100%')
      }.backgroundColor(0xffd306).height('30%')
    }
  }
}
```

  图13 横屏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.62776757713572784142451637775733:50001231000000:2800:A969A4D1E3C2AFFCF6C6FCFE751F1FD2099237032C147806BA010DAC14074997.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  图14 竖屏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.16464389118435932158162742955810:50001231000000:2800:6764773A441B7AECD50CBE2395B251AC9769925AD642A4359D0EEA0D08351569.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 自适应延伸

自适应延伸是指在不同尺寸设备下，当页面的内容超出屏幕大小而无法完全显示时，可以通过滚动条进行拖动展示。这种方法适用于线性布局中内容无法一屏展示的场景。通常有以下两种实现方式。

* [在List中添加滚动条](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section1958410178617)：当List子项过多一屏放不下时，可以将每一项子元素放置在不同的组件中，通过滚动条进行拖动展示。可以通过scrollBar属性设置滚动条的常驻状态，edgeEffect属性设置拖动到内容最末端的回弹效果。
* 使用Scroll组件：在线性布局中，开发者可以进行垂直方向或者水平方向的布局。当一屏无法完全显示时，可以在Column或Row组件的外层包裹一个可滚动的容器组件Scroll来实现可滑动的线性布局。
  垂直方向布局中使用Scroll组件：

```
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Scroll(this.scroller) {
      Column() {
        ForEach(this.arr, (item) => {
          Text(item.toString())
            .width('90%')
            .height(150)
            .backgroundColor(0xFFFFFF)
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .margin({ top: 10 })
        }, item => item)
      }.width('100%')
    }
    .backgroundColor(0xDCDCDC)
    .scrollable(ScrollDirection.Vertical) // 滚动方向为垂直方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.56030495400687142568072148103673:50001231000000:2800:29AA3194299D769D928177D9112ED779950C517E9F6EF3DC5B540978C4A9E054.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
  水平方向布局中使用Scroll组件：

```
@Entry
@Component
struct ScrollExample {
  scroller: Scroller = new Scroller();
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  build() {
    Scroll(this.scroller) {
      Row() {
        ForEach(this.arr, (item) => {
          Text(item.toString())
            .height('90%')
            .width(150)
            .backgroundColor(0xFFFFFF)
            .borderRadius(15)
            .fontSize(16)
            .textAlign(TextAlign.Center)
            .margin({ left: 10 })
        })
      }.height('100%')
    }
    .backgroundColor(0xDCDCDC)
    .scrollable(ScrollDirection.Horizontal) // 滚动方向为水平方向
    .scrollBar(BarState.On) // 滚动条常驻显示
    .scrollBarColor(Color.Gray) // 滚动条颜色
    .scrollBarWidth(10) // 滚动条宽度
    .edgeEffect(EdgeEffect.Spring) // 滚动到边沿后回弹
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142811.06286462041112147965873459754906:50001231000000:2800:044EDFB9E3AF3665D6C4682B9D58ADE5C80652A386FED2ABAFD30F211E38E56B.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 层叠布局（Stack）

更新时间: 2024-01-15 12:18

## 概述

层叠布局（StackLayout）用于在屏幕上预留一块区域来显示组件中的元素，提供元素可以重叠的布局。层叠布局通过[Stack](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-stack-0000001427584888-V3)容器组件实现位置的固定定位与层叠，容器中的子元素（子组件）依次入栈，后一个子元素覆盖前一个子元素，子元素可以叠加，也可以设置位置。

层叠布局具有较强的页面层叠、位置定位能力，其使用场景有广告、卡片层叠效果等。

如图1，Stack作为容器，容器内的子元素（子组件）的顺序为Item1->Item2->Item3。

图1 层叠布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.74169199830606561229130479303704:50001231000000:2800:C900AE70985C74FE2C4847C2C4CDD3B0F47E262CBE9652711016626E2D1CC15C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 开发布局

Stack组件为容器组件，容器内可包含各种子组件。其中子组件默认进行居中堆叠。子元素被约束在Stack下，进行自己的样式定义以及排列。

```
Column(){
  Stack({ }) {
    Column(){}.width('90%').height('100%').backgroundColor('#ff58b87c')
    Text('text').width('60%').height('60%').backgroundColor('#ffc3f6aa')
    Button('button').width('30%').height('30%').backgroundColor('#ff8ff3eb').fontColor('#000')
  }.width('100%').height(150).margin({ top: 50 })
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.65811578815629624853158685265382:50001231000000:2800:14CAEC331AE003730B810F2AFDEAFA93427D441B6DF0C40EDB814D8E9F0BA8B7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 对齐方式

Stack组件通过[alignContent参数](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__alignment)实现位置的相对移动。如图2所示，支持九种对齐方式。

图2 Stack容器内元素的对齐方式
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.52776776731691091772205695450275:50001231000000:2800:C57F38D5D8DA5A8A80731A4B990E99CA43F207986AD0BE87D6D71C54080E6A03.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## Z序控制

Stack容器中兄弟组件显示层级关系可以通过[Z序控制](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-z-order-0000001478181381-V3)的zIndex属性改变。zIndex值越大，显示层级越高，即zIndex值大的组件会覆盖在zIndex值小的组件上方。

在层叠布局中，如果后面子元素尺寸大于前面子元素尺寸，则前面子元素完全隐藏。

```
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    Text('Stack子元素1').textAlign(TextAlign.End).fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306)

  Column() {
    Text('Stack子元素2').fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink)

  Column() {
    Text('Stack子元素3').fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.margin({ top: 100 }).width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.98205936597258763776022376443932:50001231000000:2800:19C8CAF25BEA6524187F43FF1046FA981440B61C42D9895800FF6FE2987C7300.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

上图中，最后的子元素3的尺寸大于前面的所有子元素，所以，前面两个元素完全隐藏。改变子元素1，子元素2的zIndex属性后，可以将元素展示出来。

```
Stack({ alignContent: Alignment.BottomStart }) {
  Column() {
    Text('Stack子元素1').fontSize(20)
  }.width(100).height(100).backgroundColor(0xffd306).zIndex(2)

  Column() {
    Text('Stack子元素2').fontSize(20)
  }.width(150).height(150).backgroundColor(Color.Pink).zIndex(1)

  Column() {
    Text('Stack子元素3').fontSize(20)
  }.width(200).height(200).backgroundColor(Color.Grey)
}.margin({ top: 100 }).width(350).height(350).backgroundColor(0xe0e0e0)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.84274098820616013062971574976199:50001231000000:2800:7579D8D488EF68035F60CCBC9511CD19ADF4C8A6111471E643E635F968E1924E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 场景示例

使用层叠布局快速搭建手机页面显示模型。

```
@Entry
@Component
struct StackSample {
  private arr: string[] = ['APP1', 'APP2', 'APP3', 'APP4', 'APP5', 'APP6', 'APP7', 'APP8'];

  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Flex({ wrap: FlexWrap.Wrap }) {
        ForEach(this.arr, (item) => {
          Text(item)
            .width(100)
            .height(100)
            .fontSize(16)
            .margin(10)
            .textAlign(TextAlign.Center)
            .borderRadius(10)
            .backgroundColor(0xFFFFFF)
        }, item => item)
      }.width('100%').height('100%')

      Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
        Text('联系人').fontSize(16)
        Text('设置').fontSize(16)
        Text('短信').fontSize(16)
      }
      .width('50%')
      .height(50)
      .backgroundColor('#16302e2e')
      .margin({ bottom: 15 })
      .borderRadius(15)
    }.width('100%').height('100%').backgroundColor('#CFD0CF')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142812.28766386625006672473341686670243:50001231000000:2800:6FE6D3838EF2565CE7D4DF01CF03B6B1C22B99A8F9BF9ED945549BAFF9CA870D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 弹性布局（Flex）

更新时间: 2024-01-15 12:18

## 概述

弹性布局（[Flex](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-flex-0000001427902472-V3)）提供更加有效的方式对容器中的子元素进行排列、对齐和分配剩余空间。容器默认存在主轴与交叉轴，子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸，在交叉轴方向的尺寸称为交叉轴尺寸。弹性布局在开发场景中用例特别多，比如页面头部导航栏的均匀分布、页面框架的搭建、多行数据的排列等等。

图1 主轴为水平方向的Flex容器示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.41098908374020862675743668937095:50001231000000:2800:274648DD02D0CC3CB745723ADDCE77D55DCEE14C135B7F80D0E092329503EE65.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 基本概念

* 主轴：Flex组件布局方向的轴线，子元素默认沿着主轴排列。主轴开始的位置称为主轴起始点，结束位置称为主轴结束点。

* 交叉轴：垂直于主轴方向的轴线。交叉轴开始的位置称为交叉轴起始点，结束位置称为交叉轴结束点。

## 布局方向

在弹性布局中，容器的子元素可以按照任意方向排列。通过设置参数direction，可以决定主轴的方向，从而控制子组件的排列方向。

图2 弹性布局方向图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.60021406997536400704277300397495:50001231000000:2800:86A3B13B0D090964887A285B96967660DC266825B93ED1F81F03924998F1ECEE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* FlexDirection.Row（默认值）：主轴为水平方向，子组件从起始端沿着水平方向开始排布。

```
Flex({ direction: FlexDirection.Row }) {
  Text('1').width('33%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('33%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.46970331529008185416727905484219:50001231000000:2800:93D85884A880BA799E89414B897F2BBF540715BD5ECC421E667D89B4BB3638AA.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexDirection.RowReverse：主轴为水平方向，子组件从终点端沿着FlexDirection. Row相反的方向开始排布。

```
Flex({ direction: FlexDirection.RowReverse }) {
  Text('1').width('33%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('33%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.91834465828141973882040833489017:50001231000000:2800:1DAEA2C0D2D3CD3C0829080E96EFB0568F09E9EC087767F1273622B37DC9F445.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexDirection.Column：主轴为垂直方向，子组件从起始端沿着垂直方向开始排布。

```
Flex({ direction: FlexDirection.Column }) {
  Text('1').width('100%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('100%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('100%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.08016024279592011872238833420256:50001231000000:2800:81A6377ABC081A2AD2AF9E1903A10457580EDC8F718343399A05EA782A86E9EC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexDirection.ColumnReverse：主轴为垂直方向，子组件从终点端沿着FlexDirection. Column相反的方向开始排布。

```
Flex({ direction: FlexDirection.ColumnReverse }) {
  Text('1').width('100%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('100%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('100%').height(50).backgroundColor(0xF5DEB3)
}
.height(70)
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.09309466297851093339936954889449:50001231000000:2800:6A6F90B157CC72C44DCBD503E2E5A744C36C032C68281B7A067E3C10B236D65D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 布局换行

弹性布局分为单行布局和多行布局。默认情况下，Flex容器中的子元素都排在一条线（又称“轴线”）上。wrap属性控制当子元素主轴尺寸之和大于容器主轴尺寸时，Flex是单行布局还是多行布局。在多行布局时，通过交叉轴方向，确认新行堆叠方向。

* FlexWrap. NoWrap（默认值）：不换行。如果子组件的宽度总和大于父元素的宽度，则子组件会被压缩宽度。

```
Flex({ wrap: FlexWrap.NoWrap }) {
  Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
} 
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.28261167876429188617788866218985:50001231000000:2800:AA9C91A65A0D79C6486619765C5CAD10C8184C93C60FDBBC25E43401810A63E8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexWrap. Wrap：换行，每一行子组件按照主轴方向排列。

```
Flex({ wrap: FlexWrap.Wrap }) {
  Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('50%').height(50).backgroundColor(0xD2B48C)
} 
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.63161945379946973975327620051755:50001231000000:2800:5440EF940795E7AB146CF99B60457809D47A08A200446DAA61CC7E615475C40C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexWrap. WrapReverse：换行，每一行子组件按照主轴反方向排列。

```
Flex({ wrap: FlexWrap.WrapReverse}) {
  Text('1').width('50%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('50%').height(50).backgroundColor(0xD2B48C)
  Text('3').width('50%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.79558311872469624950014388902696:50001231000000:2800:7E97BCBB041CFEB6F958422BDE143BCCC7CAAC0E725BDC66612AC832890AA6C4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 主轴对齐方式

通过justifyContent参数设置在主轴方向的对齐方式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.06974291234020504015090768435272:50001231000000:2800:563A7A66126DB6094173B36EC56735E0A8A0A881FEE8B2C083A669E6E9C73D65.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* FlexAlign.Start（默认值）：子组件在主轴方向起始端对齐， 第一个子组件与父元素边沿对齐，其他元素与前一个元素对齐。

```
Flex({ justifyContent: FlexAlign.Start }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)    
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.95464514466420734294902746063409:50001231000000:2800:AA67B5B8BB01D720F8C2382CB5C9BEEC32B5BB3398787EBAD3B9548E0961DD47.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.Center：子组件在主轴方向居中对齐。

```
Flex({ justifyContent: FlexAlign.Center }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.97028034996780382958321313386590:50001231000000:2800:905CA05A65754598A3D887C11921FE629EAED1B57A1C34B1C9C224C82103745A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.End：子组件在主轴方向终点端对齐, 最后一个子组件与父元素边沿对齐，其他元素与后一个元素对齐。

```
Flex({ justifyContent: FlexAlign.End }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103820.76833920579798885135580709349469:50001231000000:2800:FFE63B7800379C9E624D2658629EB16F363319C9064612C7B1AFBF260B6C5CD8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceBetween：Flex主轴方向均匀分配弹性元素，相邻子组件之间距离相同。第一个子组件和最后一个子组件与父元素边沿对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.95963156913340983848797451470535:50001231000000:2800:F53A7B3348FEFDB5EE27DAB3E6D915AF55F140DAA35DF44245975BBB75F0D3E3.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceAround：Flex主轴方向均匀分配弹性元素，相邻子组件之间距离相同。第一个子组件到主轴起始端的距离和最后一个子组件到主轴终点端的距离是相邻元素之间距离的一半。

```
Flex({ justifyContent: FlexAlign.SpaceAround }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.87592983601492168352144706875584:50001231000000:2800:5BE887DE026F8B2663A78AD33B4529C2320ABC30608B3EFFCC0C551EF6965868.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceEvenly：Flex主轴方向元素等间距布局，相邻子组件之间的间距、第一个子组件与主轴起始端的间距、最后一个子组件到主轴终点端的间距均相等。

```
Flex({ justifyContent: FlexAlign.SpaceEvenly }) {  
  Text('1').width('20%').height(50).backgroundColor(0xF5DEB3)  
  Text('2').width('20%').height(50).backgroundColor(0xD2B48C)   
  Text('3').width('20%').height(50).backgroundColor(0xF5DEB3)
}
.width('90%')
.padding({ top: 10, bottom: 10 })
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.77728741360322784810337463378001:50001231000000:2800:023FE36E02E5F21B701D7C234171D823B9A6DAD1DC3C4AB56BED27A81C59AF19.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 交叉轴对齐方式

容器和子元素都可以设置交叉轴对齐方式，且子元素设置的对齐方式优先级较高。

### 容器组件设置交叉轴对齐

可以通过Flex组件的alignItems参数设置子组件在交叉轴的对齐方式。

* ItemAlign.Auto：使用Flex容器中默认配置。

```
Flex({ alignItems: ItemAlign.Auto }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.23278915116746187733363571948310:50001231000000:2800:667743AFC513819C5832ECE23877FD96A62B35A5A9FC8F1A1680A1F2A0B1DFBD.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.Start：交叉轴方向首部对齐。

```
Flex({ alignItems: ItemAlign.Start }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.70694756306687989087245254218698:50001231000000:2800:7D60EC9F000F32B414A5401A39E258D82CDACC1A37164AA514B8C164417475E6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.Center：交叉轴方向居中对齐。

```
Flex({ alignItems: ItemAlign.Center }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.87592845340755307375145954416047:50001231000000:2800:D76322476A52968D1CAFAEF87BBD9487B11EF132DF030CBFEE198D31F73B7C44.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.End：交叉轴方向底部对齐。

```
Flex({ alignItems: ItemAlign.End }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.88133592144840009949703573338443:50001231000000:2800:909307D8227E921FA69D1D861610FCCBE7785A4E52E162FA116F7B0363D4FAAD.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign.Stretch：交叉轴方向拉伸填充，在未设置尺寸时，拉伸到容器尺寸。

```
Flex({ alignItems: ItemAlign.Stretch }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.04897240815671459005780517393137:50001231000000:2800:8578B4F8A137BAD24B2626BD29D10703EF2EBDD6849E84ECAF72E6E78118A962.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* ItemAlign. Baseline：交叉轴方向文本基线对齐。

```
Flex({ alignItems: ItemAlign.Baseline }) {  
  Text('1').width('33%').height(30).backgroundColor(0xF5DEB3)  
  Text('2').width('33%').height(40).backgroundColor(0xD2B48C)  
  Text('3').width('33%').height(50).backgroundColor(0xF5DEB3)
}
.size({ width: '90%', height: 80 })
.padding(10)
.backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.44901746859068267151276034528449:50001231000000:2800:3A8AD1EEE2658A9C2649EF801910A864A2A9E33B2F6E4C2026E96F484024CE53.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 子组件设置交叉轴对齐

子组件的[alignSelf](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性也可以设置子组件在父容器交叉轴的对齐格式，且会覆盖Flex布局容器中alignItems配置。如下例所示：

```
Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center }) { // 容器组件设置子组件居中
  Text('alignSelf Start').width('25%').height(80)
    .alignSelf(ItemAlign.Start)
    .backgroundColor(0xF5DEB3)
  Text('alignSelf Baseline')
    .alignSelf(ItemAlign.Baseline)
    .width('25%')
    .height(80)
    .backgroundColor(0xD2B48C)
  Text('alignSelf Baseline').width('25%').height(100)
    .backgroundColor(0xF5DEB3)
    .alignSelf(ItemAlign.Baseline)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor(0xD2B48C)
  Text('no alignSelf').width('25%').height(100)
    .backgroundColor(0xF5DEB3)

}.width('90%').height(220).backgroundColor(0xAFEEEE)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.58967021566928478019773387587842:50001231000000:2800:6DCA546B2F15254EBB9C4114A56C48D6AE24F2E341C1677D9B3F20BD9CB65C3D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

上例中，Flex容器中alignItems设置交叉轴子组件的对齐方式为居中，子组件自身设置了alignSelf属性的情况，覆盖父组件的alignItems值，表现为alignSelf的定义。

### 内容对齐

可以通过[alignContent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-flex-0000001427902472-V3)参数设置子组件各行在交叉轴剩余空间内的对齐方式，只在多行的flex布局中生效，可选值有：

* FlexAlign.Start：子组件各行与交叉轴起点对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Start }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.33300533070591199790569141830855:50001231000000:2800:BF393B0052EE1884EFDCF373BDF79F51020A74DFCD80E5460DC6C1DC2D336940.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.Center：子组件各行在交叉轴方向居中对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.Center }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.05882808582582916152351736660192:50001231000000:2800:EBB4F6194AED80E5F11CC4CA1ED1ADA1309BDC55CD2592C9C722BBC1E987306F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.End：子组件各行与交叉轴终点对齐。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.End }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.01807846917610542985277911102807:50001231000000:2800:C405840577DC6137F465C964CB95546A58EFC2B4EAF229B9A269D9F65C138775.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceBetween：子组件各行与交叉轴两端对齐，各行间垂直间距平均分布。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceBetween }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.53014585466231773856389118137867:50001231000000:2800:F359070A9EECCDB4D737E69A73D2B871C24721AE2B58CAD16D7EAB270B49BF7A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceAround：子组件各行间距相等，是元素首尾行与交叉轴两端距离的两倍。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceAround }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.64742442774703922888861312312600:50001231000000:2800:2703BB9CD03E5AF471AA69842B3D1FAD791661D8A5F45C30AFED42E11AD16F91.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* FlexAlign.SpaceEvenly: 子组件各行间距，子组件首尾行与交叉轴两端距离都相等。

```
Flex({ justifyContent: FlexAlign.SpaceBetween, wrap: FlexWrap.Wrap, alignContent: FlexAlign.SpaceEvenly }) {
  Text('1').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('2').width('60%').height(20).backgroundColor(0xD2B48C)
  Text('3').width('40%').height(20).backgroundColor(0xD2B48C)
  Text('4').width('30%').height(20).backgroundColor(0xF5DEB3)
  Text('5').width('20%').height(20).backgroundColor(0xD2B48C)
}
.width('90%')
.height(100)
.backgroundColor(0xAFEEEE)          
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.75219968475760655489964056165598:50001231000000:2800:F77B3D6DD0A2A6DA646BC7726D5D2A25AE4C7ECF43BDB310E7A7C816A3D75AEF.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自适应拉伸

在弹性布局父组件尺寸不够大的时候，通过子组件的下面几个属性设置其在父容器的占比，达到自适应布局能力。

* flexBasis：设置子组件在父容器主轴方向上的基准尺寸。如果设置了该值，则子项占用的空间为设置的值；如果没设置该属性，那子项的空间为width/height的值。

```
Flex() {
  Text('flexBasis("auto")')
    .flexBasis('auto') // 未设置width以及flexBasis值为auto，内容自身宽松
    .height(100)
    .backgroundColor(0xF5DEB3)
  Text('flexBasis("auto")' + ' width("40%")')
    .width('40%')
    .flexBasis('auto') //设置width以及flexBasis值auto，使用width的值
    .height(100)
    .backgroundColor(0xD2B48C)

  Text('flexBasis(100)') // 未设置width以及flexBasis值为100，宽度为100vp
    .fontSize(15)
    .flexBasis(100)
    .height(100)
    .backgroundColor(0xF5DEB3)

  Text('flexBasis(100)')
    .fontSize(15)
    .flexBasis(100)
    .width(200) // flexBasis值为100，覆盖width的设置值，宽度为100vp
    .height(100)
    .backgroundColor(0xD2B48C)
}.width('90%').height(120).padding(10).backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.45892628655925830306481185553379:50001231000000:2800:E2F7F28D3BD23DA61E8CDED03604250C06DA5EB49CBA6FBF86CB2DF0719A7857.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* flexGrow：设置父容器的剩余空间分配给此属性所在组件的比例。用于“瓜分”父组件的剩余空间。

```
Flex() {
Text('flexGrow(2)')
  .flexGrow(2) 
  .width(100)
  .height(100)
  .backgroundColor(0xF5DEB3)

Text('flexGrow(3)')
  .flexGrow(3)
  .width(100)
  .height(100)
  .backgroundColor(0xD2B48C)

Text('no flexGrow')
  .width(100) 
  .height(100)
  .backgroundColor(0xF5DEB3)
}.width(420).height(120).padding(10).backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.83092017588361824585277293797023:50001231000000:2800:09DA40E437B3BF6BF0983D0B0E87105BE802DC17A72F3DCC2487797C2D430F20.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
  父容器宽度420vp，三个子元素原始宽度为100vp，左右padding为20vp，总和320vp，剩余空间100vp根据flexGrow值的占比分配给子元素，未设置flexGrow的子元素不参与“瓜分”。
  第一个元素以及第二个元素以2:3分配剩下的100vp。第一个元素为100vp+100vp*2/5=140vp，第二个元素为100vp+100vp*3/5=160vp。
* flexShrink: 当父容器空间不足时，子组件的压缩比例。

```
Flex({ direction: FlexDirection.Row }) {
  Text('flexShrink(3)')
    .fontSize(15)
    .flexShrink(3)
    .width(200)
    .height(100)
    .backgroundColor(0xF5DEB3)

  Text('no flexShrink')
    .width(200)
    .height(100)
    .backgroundColor(0xD2B48C)

  Text('flexShrink(2)')
    .flexShrink(2)
    .width(200)
    .height(100)
    .backgroundColor(0xF5DEB3)
}.width(400).height(120).padding(10).backgroundColor(0xAFEEEE)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.55220725202123017979460093498862:50001231000000:2800:FDD3112C7D4C61F0DDB3BE38F0E7B82AAF634277559CDB63E1FBEC807C0AC5C2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 相关实例

使用弹性布局，可以实现子组件沿水平方向排列，两端对齐，子组件间距平分，竖直方向上子组件居中的效果。

```
@Entry  
@Component
struct FlexExample {
  build() {
    Column() {
      Column({ space: 5 }) {
        Flex({ direction: FlexDirection.Row, wrap: FlexWrap.NoWrap, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
          Text('1').width('30%').height(50).backgroundColor(0xF5DEB3)
          Text('2').width('30%').height(50).backgroundColor(0xD2B48C)
          Text('3').width('30%').height(50).backgroundColor(0xF5DEB3)
        }
        .height(70)
        .width('90%')
        .backgroundColor(0xAFEEEE)
      }.width('100%').margin({ top: 5 })
    }.width('100%') 
 }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103821.06523227728508759286492936853514:50001231000000:2800:50F78944F7006F0EC88A1C03E6663CC53A8F35459D176004DAC80B492D143137.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 相对布局（RelativeContainer）

更新时间: 2024-01-15 12:19

## 概述

[RelativeContainer](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-relativecontainer-0000001478341165-V3)为采用相对布局的容器，支持容器内部的子元素设置相对位置关系。子元素支持指定兄弟元素作为锚点，也支持指定父容器作为锚点，基于锚点做相对位置布局。下图是一个RelativeContainer的概念图，图中的虚线表示位置的依赖关系。

图1 相对布局示意图

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231123162444.52003353321971216275516898511961:50001231000000:2800:ADDD5DAC0A04A5E6BF869973210DE494474C0C90ED8C0AE480DDC2D96B27CD5F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

子元素并不完全是上图中的依赖关系。比如，Item4可以以Item2为依赖锚点，也可以以RelativeContainer父容器为依赖锚点。

## 基本概念

* 锚点：通过锚点设置当前元素基于哪个元素确定位置。

* 对齐方式：通过对齐方式，设置当前元素是基于锚点的上中下对齐，还是基于锚点的左中右对齐。

## 设置依赖关系



### 锚点设置

锚点设置是指设置子元素相对于父元素或兄弟元素的位置依赖关系。在水平方向上，可以设置left、middle、right的锚点。在竖直方向上，可以设置top、center、bottom的锚点。为了明确定义锚点，必须为RelativeContainer及其子元素设置ID，用于指定锚点信息。ID默认为“__container__”，其余子元素的ID通过id属性设置。未设置ID的子元素在RelativeContainer中不会显示。

说明

在使用锚点时要注意子元素的相对位置关系，避免出现错位或遮挡的情况。

* RelativeContainer父组件为锚点，__container__代表父容器的id。

```
RelativeContainer() {
  Row()
    // 添加其他属性
    .alignRules({
      top: { anchor: '__container__', align: VerticalAlign.Top },
      left: { anchor: '__container__', align: HorizontalAlign.Start }
    })
    .id("row1")

  Row()
    ...
    .alignRules({
      top: { anchor: '__container__', align: VerticalAlign.Top },
      right: { anchor: '__container__', align: HorizontalAlign.End }
    })
    .id("row2")
}
...
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231123162444.56688651314571707096842415117357:50001231000000:2800:BDC9A0586CA598EC42B891685A8801968822AC98D008BCD840B6B97E52FBFD3A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 以子元素为锚点。

```
RelativeContainer() {
  ...
  top: { anchor: 'row1', align: VerticalAlign.Bottom },
  ...
}
.width(300).height(300)
.margin({ left: 20 })
.border({ width: 2, color: '#6699FF' })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231123162444.63674341652629099505262390473441:50001231000000:2800:431F658282BC581429811DD2579B1C1F2E304F681B2C5827E77CC8D1D5DA62EC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 设置相对于锚点的对齐位置

设置了锚点之后，可以通过align设置相对于锚点的对齐位置。

在水平方向上，对齐位置可以设置为HorizontalAlign.Start、HorizontalAlign.Center、HorizontalAlign.End。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231123162444.48983724806411090915530960282308:50001231000000:2800:06449111B267B7346FA1390C77804A819FF892AE7E9D413EE828EBDC5DD9FC09.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在竖直方向上，对齐位置可以设置为VerticalAlign.Top、VerticalAlign.Center、VerticalAlign.Bottom。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231123162444.22049522820287855628130531867497:50001231000000:2800:AE8E32805EA07C268C481CDB1F9EB96D4D5D54C23BC095C0B22F7C4560BB17DB.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景实例

相对布局内的子元素相对灵活，只要在RelativeContainer容器内，均可以通过alignRules进行相应的位置移动。

```
@Entry
@Component
struct Index {
  build() {
    Row() {
      RelativeContainer() {
        Row()
          .width(100)
          .height(100)
          .backgroundColor('#FF3333')
          .alignRules({
            top: { anchor: '__container__', align: VerticalAlign.Top },  //以父容器为锚点，竖直方向顶头对齐
            middle: { anchor: '__container__', align: HorizontalAlign.Center }  //以父容器为锚点，水平方向居中对齐
          })
          .id('row1')  //设置锚点为row1

        Row() {
          Image($r('app.media.icon'))
        }
        .height(100).width(100)
        .alignRules({
          top: { anchor: 'row1', align: VerticalAlign.Bottom },  //以row1组件为锚点，竖直方向低端对齐
          left: { anchor: 'row1', align: HorizontalAlign.Start }  //以row1组件为锚点，水平方向开头对齐
        })
        .id('row2')  //设置锚点为row2

        Row()
          .width(100)
          .height(100)
          .backgroundColor('#FFCC00')
          .alignRules({
            top: { anchor: 'row2', align: VerticalAlign.Top }
          })
          .id('row3')  //设置锚点为row3

        Row()
          .width(100)
          .height(100)
          .backgroundColor('#FF9966')
          .alignRules({
            top: { anchor: 'row2', align: VerticalAlign.Top },
            left: { anchor: 'row2', align: HorizontalAlign.End },
          })
          .id('row4')  //设置锚点为row4

        Row()
          .width(100)
          .height(100)
          .backgroundColor('#FF66FF')
          .alignRules({
            top: { anchor: 'row2', align: VerticalAlign.Bottom },
            middle: { anchor: 'row2', align: HorizontalAlign.Center }
          })
          .id('row5')  //设置锚点为row5
      }
      .width(300).height(300)
      .border({ width: 2, color: '#6699FF' })
    }
    .height('100%').margin({ left: 30 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231123162445.00811888831816538276716065274006:50001231000000:2800:B7DA4E6D14C473156468CC6BF490F5D389700A7044071B4F2CD717ED0169FD0A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 栅格布局（GridRow/GridCol）

更新时间: 2024-01-10 11:33

## 概述

栅格布局是一种通用的辅助定位工具，对移动设备的界面设计有较好的借鉴作用。主要优势包括：

1. 提供可循的规律：栅格布局可以为布局提供规律性的结构，解决多尺寸多设备的动态布局问题。通过将页面划分为等宽的列数和行数，可以方便地对页面元素进行定位和排版。
2. 统一的定位标注：栅格布局可以为系统提供一种统一的定位标注，保证不同设备上各个模块的布局一致性。这可以减少设计和开发的复杂度，提高工作效率。
3. 灵活的间距调整方法：栅格布局可以提供一种灵活的间距调整方法，满足特殊场景布局调整的需求。通过调整列与列之间和行与行之间的间距，可以控制整个页面的排版效果。
4. 自动换行和自适应：栅格布局可以完成一对多布局的自动换行和自适应。当页面元素的数量超出了一行或一列的容量时，他们会自动换到下一行或下一列，并且在不同的设备上自适应排版，使得页面布局更加灵活和适应性强。

[GridRow](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-gridrow-0000001478181425-V3)为栅格容器组件，需与栅格子组件[GridCol](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-gridcol-0000001427744832-V3)在栅格布局场景中联合使用。

## 栅格容器GridRow

### 栅格系统断点

栅格系统以设备的水平宽度（[屏幕密度像素值](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-pixel-units-0000001478341189-V3)，单位vp）作为断点依据，定义设备的宽度类型，形成了一套断点规则。开发者可根据需求在不同的断点区间实现不同的页面布局效果。

栅格系统默认断点将设备宽度分为xs、sm、md、lg四类，尺寸范围如下：

| 断点名称 | 取值范围（vp） | 设备描述           |
| :------- | :------------- | :----------------- |
| xs       | [0, 320）      | 最小宽度类型设备。 |
| sm       | [320, 520)     | 小宽度类型设备。   |
| md       | [520, 840)     | 中等宽度类型设备。 |
| lg       | [840, +∞)     | 大宽度类型设备。   |

在GridRow栅格组件中，允许开发者使用breakpoints自定义修改断点的取值范围，最多支持6个断点，除了默认的四个断点外，还可以启用xl，xxl两个断点，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备的布局设置。

| 断点名称 | 设备描述           |
| :------- | :----------------- |
| xs       | 最小宽度类型设备。 |
| sm       | 小宽度类型设备。   |
| md       | 中等宽度类型设备。 |
| lg       | 大宽度类型设备。   |
| xl       | 特大宽度类型设备。 |
| xxl      | 超大宽度类型设备。 |

* 针对断点位置，开发者根据实际使用场景，通过一个单调递增数组设置。由于breakpoints最多支持六个断点，单调递增数组长度最大为5。

```
breakpoints: {value: ['100vp', '200vp']}
```

  表示启用xs、sm、md共3个断点，小于100vp为xs，100vp-200vp为sm，大于200vp为md。

```
breakpoints: {value: ['320vp', '520vp', '840vp', '1080vp']}
```

  表示启用xs、sm、md、lg、xl共5个断点，小于320vp为xs，320vp-520vp为sm，520vp-840vp为md，840vp-1080vp为lg，大于1080vp为xl。
* 栅格系统通过监听窗口或容器的尺寸变化进行断点，通过reference设置断点切换参考物。 考虑到应用可能以非全屏窗口的形式显示，以应用窗口宽度为参照物更为通用。

例如，使用栅格的默认列数12列，通过断点设置将应用宽度分成六个区间，在各区间中，每个栅格子元素占用的列数均不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow({
  breakpoints: {
    value: ['200vp', '300vp', '400vp', '500vp', '600vp'],
    reference: BreakpointsReference.WindowSize
  }
}) {
   ForEach(this.bgColors, (color, index) => {
     GridCol({
       span: {
         xs: 2, // 在最小宽度类型设备上，栅格子组件占据的栅格容器2列。
         sm: 3, // 在小宽度类型设备上，栅格子组件占据的栅格容器3列。
         md: 4, // 在中等宽度类型设备上，栅格子组件占据的栅格容器4列。
         lg: 6, // 在大宽度类型设备上，栅格子组件占据的栅格容器6列。
         xl: 8, // 在特大宽度类型设备上，栅格子组件占据的栅格容器8列。
         xxl: 12 // 在超大宽度类型设备上，栅格子组件占据的栅格容器12列。
       }
     }) {
       Row() {
         Text(`${index}`)
       }.width("100%").height('50vp')
     }.backgroundColor(color)
   })
}                                                                     
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.47257113918867463806512134720145:50001231000000:2800:149B0F881763D6D6ED10FA321724669A5A5A8EC181B55286ADE3831A74725314.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### 布局的总列数

GridRow中通过columns设置栅格布局的总列数。

* columns默认值为12，即在未设置columns时，任何断点下，栅格布局被分成12列。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown,Color.Red, Color.Orange, Color.Yellow, Color.Green];
...
GridRow() {
  ForEach(this.bgColors, (item, index) => {
    GridCol() {
      Row() {
        Text(`${index + 1}`)
      }.width('100%').height('50')
    }.backgroundColor(item)
  })
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.00410689426142383404918933116451:50001231000000:2800:502E73ABEBF9416768903341512CF895F5851E7D7F6C4B7F82160931AB51011B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当columns为自定义值，栅格布局在任何尺寸设备下都被分为columns列。下面分别设置栅格布局列数为4和8，子元素默认占一列，效果如下：

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
@State currentBp: string = 'unknown';
...
Row() {
  GridRow({ columns: 4 }) {
    ForEach(this.bgColors, (item, index) => {
      GridCol() {
        Row() {
          Text(`${index + 1}`)
        }.width('100%').height('50')
      }.backgroundColor(item)
    })
  }
  .width('100%').height('100%')
  .onBreakpointChange((breakpoint) => {
    this.currentBp = breakpoint
  })
}
.height(160)
.border({ color: Color.Blue, width: 2 })
.width('90%')

Row() {
  GridRow({ columns: 8 }) {
    ForEach(this.bgColors, (item, index) => {
      GridCol() {
        Row() {
          Text(`${index + 1}`)
        }.width('100%').height('50')
      }.backgroundColor(item)
    })
  }
  .width('100%').height('100%')
  .onBreakpointChange((breakpoint) => {
    this.currentBp = breakpoint
  })
}
.height(160)
.border({ color: Color.Blue, width: 2 })
.width('90%')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.90921119564142117547384004964985:50001231000000:2800:D942D1007F7D92F14F60D046C374D00EB60B0D08544727A3EEFA8FE5C7634433.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当columns类型为GridRowColumnOption时，支持下面六种不同尺寸（xs, sm, md, lg, xl, xxl）设备的总列数设置，各个尺寸下数值可不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown]
GridRow({ columns: { sm: 4, md: 8 }, breakpoints: { value: ['200vp', '300vp', '400vp', '500vp', '600vp'] } }) {
  ForEach(this.bgColors, (item, index) => {
    GridCol() {
      Row() {
        Text(`${index + 1}`)
      }.width('100%').height('50')
    }.backgroundColor(item)
  })
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.62184789942767538067176035049534:50001231000000:2800:495B27BE74C81A17C454EB2902D2FA839491C445EDA6DB86CDC0C600E6653C02.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

  若只设置sm, md的栅格总列数，则较小的尺寸使用默认columns值12，较大的尺寸使用前一个尺寸的columns。这里只设置sm:4, md:8，则较小尺寸的xs:12，较大尺寸的参照md的设置，lg:8, xl:8, xxl:8。

### 排列方向

栅格布局中，可以通过设置GridRow的direction属性来指定栅格子组件在栅格容器中的排列方向。该属性可以设置为GridRowDirection.Row（从左往右排列）或GridRowDirection.RowReverse（从右往左排列），以满足不同的布局需求。通过合理的direction属性设置，可以使得页面布局更加灵活和符合设计要求。

* 子组件默认从左往右排列。

```
GridRow({ direction: GridRowDirection.Row }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.60471278343580648315078478778372:50001231000000:2800:033FFA9031A400CC64AFB03C84BAA79148AA9F9D7703CEA488F8263EE44EA463.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 子组件从右往左排列。

```
GridRow({ direction: GridRowDirection.RowReverse }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.60393311084538399996696648905407:50001231000000:2800:E941ADDFADE115A0217544381C84CEE2C44FE1CAAC9CD9819D26CE0D02D57797.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 子组件间距

GridRow中通过gutter属性设置子元素在水平和垂直方向的间距。

* 当gutter类型为number时，同时设置栅格子组件间水平和垂直方向边距且相等。下例中，设置子组件水平与垂直方向距离相邻元素的间距为10。

```
GridRow({ gutter: 10 }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.20323338812210863272015753595221:50001231000000:2800:18868826C939EF2E4F4BE06C3E8B28C4A96286968929C182A51528E233FF6A24.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当gutter类型为GutterOption时，单独设置栅格子组件水平垂直边距，x属性为水平方向间距，y为垂直方向间距。

```
GridRow({ gutter: { x: 20, y: 50 } }){}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.99405762733586829804400600801889:50001231000000:2800:4BA972814D5CD4631A80281097BB7F3E113CBCF5F2057D410EA03FF5A3106D36.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 子组件GridCol

GridCol组件作为GridRow组件的子组件，通过给GridCol传参或者设置属性两种方式，设置span（占用列数），offset（偏移列数），order（元素序号）的值。

* 设置span。
```
GridCol({ span: 2 }){}
GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }){}
GridCol(){}.span(2)
GridCol(){}.span({ xs: 1, sm: 2, md: 3, lg: 4 })
```
* 设置offset。
```
GridCol({ offset: 2 }){}
GridCol({ offset: { xs: 2, sm: 2, md: 2, lg: 2 } }){}
GridCol(){}.offset(2)
GridCol(){}.offset({ xs: 1, sm: 2, md: 3, lg: 4 }) 
```
* 设置order。
```
GridCol({ order: 2 }){}
GridCol({ order: { xs: 1, sm: 2, md: 3, lg: 4 } }){}
GridCol(){}.order(2)
GridCol(){}.order({ xs: 1, sm: 2, md: 3, lg: 4 })
```

### span

子组件占栅格布局的列数，决定了子组件的宽度，默认为1。

* 当类型为number时，子组件在所有尺寸设备下占用的列数相同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow({ columns: 8 }) {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ span: 2 }) {      
      Row() {
        Text(`${index}`)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.63830234683969399106860496900929:50001231000000:2800:8AAB1FC0FCBD19AF83A61CE3B68EBEA972A34F16D695DED3BD9CEFD5F693E684.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件所占列数设置,各个尺寸下数值可不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow({ columns: 8 }) {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ span: { xs: 1, sm: 2, md: 3, lg: 4 } }) {      
      Row() {
        Text(`${index}`)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.84333160929084705655923710553369:50001231000000:2800:6BDA024E3EF190B6C7FD5535B494C7AD506693BA690395792316693628C38E8C.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### offset

栅格子组件相对于前一个子组件的偏移列数，默认为0。

* 当类型为number时，子组件偏移相同列数。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...
GridRow() {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ offset: 2 }) {      
      Row() {
        Text('' + index)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.89795367088709185858383045251957:50001231000000:2800:B64F82890C87A03CBEED0E4BBBE8E9DE0E5D63B9D9C293C2271AD22387B26B2D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  栅格默认分成12列，每一个子组件默认占1列，偏移2列，每个子组件及间距共占3列，一行放四个子组件。
* 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件所占列数设置,各个尺寸下数值可不同。

```
@State bgColors: Color[] = [Color.Red, Color.Orange, Color.Yellow, Color.Green, Color.Pink, Color.Grey, Color.Blue, Color.Brown];
...

GridRow() {
  ForEach(this.bgColors, (color, index) => {
    GridCol({ offset: { xs: 1, sm: 2, md: 3, lg: 4 } }) {      
      Row() {
        Text('' + index)
      }.width('100%').height('50vp')          
    }
    .backgroundColor(color)
  })
}                 
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.62895421863468669487381498262473:50001231000000:2800:943CDB13414B821BAA206AED9B2EB6BA4ACD2F7458B3600BAB2E8864A9D452C2.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### order

栅格子组件的序号，决定子组件排列次序。当子组件不设置order或者设置相同的order, 子组件按照代码顺序展示。当子组件设置不同的order时，order较小的组件在前，较大的在后。

当子组件部分设置order，部分不设置order时，未设置order的子组件依次排序靠前，设置了order的子组件按照数值从小到大排列。

* 当类型为number时，子组件在任何尺寸下排序次序一致。

```
GridRow() {
  GridCol({ order: 4 }) {
    Row() {
      Text('1')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Red)
  GridCol({ order: 3 }) {
    Row() {
      Text('2')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Orange)
  GridCol({ order: 2 }) {
    Row() {
      Text('3')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Yellow)
  GridCol({ order: 1 }) {
    Row() {
      Text('4')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Green)
}            
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.22437510525828855543769750680122:50001231000000:2800:327F9EFE39A8948A729D70874049A46A8F28B1F1DBC08B675DF2FC6F5848EDA2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 当类型为GridColColumnOption时，支持六种不同尺寸（xs, sm, md, lg, xl, xxl）设备中子组件排序次序设置。在xs设备中，子组件排列顺序为1234；sm为2341，md为3412，lg为2431。

```
GridRow() {
  GridCol({ order: { xs:1, sm:5, md:3, lg:7}}) {
    Row() {
      Text('1')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Red)
  GridCol({ order: { xs:2, sm:2, md:6, lg:1} }) {
    Row() {
      Text('2')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Orange)
  GridCol({ order: { xs:3, sm:3, md:1, lg:6} }) {
    Row() {
      Text('3')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Yellow)
  GridCol({ order: { xs:4, sm:4, md:2, lg:5} }) {
    Row() {
      Text('4')
    }.width('100%').height('50vp')
  }.backgroundColor(Color.Green)
} 
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.63400501599078180678215127730409:50001231000000:2800:A886B3584A007541EF13E2878C2A2DCBA20378267616FDE824CA6D496271C7E4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 栅格组件的嵌套使用

栅格组件也可以嵌套使用，完成一些复杂的布局。

以下示例中，栅格把整个空间分为12份。第一层GridRow嵌套GridCol，分为中间大区域以及“footer”区域。第二层GridRow嵌套GridCol，分为“left”和“right”区域。子组件空间按照上一层父组件的空间划分，粉色的区域是屏幕空间的12列，绿色和蓝色的区域是父组件GridCol的12列，依次进行空间的划分。

```
@Entry
@Component
struct GridRowExample {
  build() {
    GridRow() {
      GridCol({ span: { sm: 12 } }) {
        GridRow() {
          GridCol({ span: { sm: 2 } }) {
            Row() {
              Text('left').fontSize(24)
            }
            .justifyContent(FlexAlign.Center)
            .height('90%')
          }.backgroundColor('#ff41dbaa')

          GridCol({ span: { sm: 10 } }) {
            Row() {
              Text('right').fontSize(24)
            }
            .justifyContent(FlexAlign.Center)
            .height('90%')
          }.backgroundColor('#ff4168db')
        }
        .backgroundColor('#19000000')
        .height('100%')
      }

      GridCol({ span: { sm: 12 } }) {
        Row() {
          Text('footer').width('100%').textAlign(TextAlign.Center)
        }.width('100%').height('10%').backgroundColor(Color.Pink)
      }
    }.width('100%').height(300)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103822.32228766180311627932140020469160:50001231000000:2800:E46CE96D120781EA9CB8529FDDD2F12C097F46C3E3360DD41746F8BF616DC685.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

综上所述，栅格组件提供了丰富的自定义能力，功能异常灵活和强大。只需要明确栅格在不同断点下的Columns、Margin、Gutter及span等参数，即可确定最终布局，无需关心具体的设备类型及设备状态（如横竖屏）等。



# 媒体查询（mediaquery）

更新时间: 2024-01-15 12:21

## 概述

[媒体查询](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-mediaquery-0000001478181613-V3)作为响应式设计的核心，在移动设备上应用十分广泛。媒体查询可根据不同设备类型或同设备不同状态修改应用的样式。媒体查询常用于下面两种场景：

1. 针对设备和应用的属性信息（比如显示区域、深浅色、分辨率），设计出相匹配的布局。
2. 当屏幕发生动态改变时（比如分屏、横竖屏切换），同步更新应用的页面布局。

## 引入与使用流程

媒体查询通过mediaquery模块接口，设置查询条件并绑定回调函数，在对应的条件的回调函数里更改页面布局或者实现业务逻辑，实现页面的响应式设计。具体步骤如下：

首先导入媒体查询模块。

```
import mediaquery from '@ohos.mediaquery';
```

通过matchMediaSync接口设置媒体查询条件，保存返回的条件监听句柄listener。例如监听横屏事件：

```
let listener = mediaquery.matchMediaSync('(orientation: landscape)');
```

给条件监听句柄listener绑定回调函数onPortrait，当listener检测设备状态变化时执行回调函数。在回调函数内，根据不同设备状态更改页面布局或者实现业务逻辑。

```
onPortrait(mediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}

listener.on('change', onPortrait);
```

## 媒体查询条件

媒体查询条件由媒体类型、逻辑操作符、媒体特征组成，其中媒体类型可省略，逻辑操作符用于连接不同媒体类型与媒体特征，其中，媒体特征要使用“()”包裹且可以有多个。具体规则如下：

### 语法规则

语法规则包括[媒体类型（media-type）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-media-query-0000001454445606-V3#section861273217318)、[媒体逻辑操作（media-logic-operations）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-media-query-0000001454445606-V3#section1538871014512)和[媒体特征（media-feature）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-media-query-0000001454445606-V3#section347144245014)。

```
[media-type] [media-logic-operations] [(media-feature)]
```

例如：

* screen and (round-screen: true) ：表示当设备屏幕是圆形时条件成立。
* (max-height: 800) ：表示当高度小于等于800vp时条件成立。
* (height <= 800) ：表示当高度小于等于800vp时条件成立。
* screen and (device-type: tv) or (resolution < 2) ：表示包含多个媒体特征的多条件复杂语句查询，当设备类型为tv或设备分辨率小于2时条件成立。

### 媒体类型（media-type）

| 类型 | 说明               |
| :--------------- | :----------------------------- |
| screen         | 按屏幕相关参数进行媒体查询。 |

### 媒体逻辑操作（media-logic-operations）

媒体逻辑操作符：and、or、not、only用于构成复杂媒体查询，也可以通过comma（, ）将其组合起来，详细解释说明如下表。

表1 媒体逻辑操作符| 类型 | 说明 |
| :- | :- |
| -------------- |

| and         | 将多个媒体特征（Media Feature）以“与”的方式连接成一个媒体查询，只有当所有媒体特征都为true，查询条件成立。另外，它还可以将媒体类型和媒体功能结合起来。例如：screen and (device-type: wearable) and (max-height: 600) 表示当设备类型是智能穿戴且应用的最大高度小于等于600个像素单位时成立。                                                                       |
| :---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| or          | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。例如：screen and (max-height: 1000) or (round-screen: true) 表示当应用高度小于等于1000个像素单位或者设备屏幕是圆形时，条件成立。                                                                                                                                    |
| not         | 取反媒体查询结果，媒体查询结果不成立时返回true，否则返回false。例如：not screen and (min-height: 50) and (max-height: 600) 表示当应用高度小于50个像素单位或者大于600个像素单位时成立。使用not运算符时必须指定媒体类型。                                                                                                                                           |
| only        | 当整个表达式都匹配时，才会应用选择的样式，可以应用在防止某些较早的版本的浏览器上产生歧义的场景。一些较早版本的浏览器对于同时包含了媒体类型和媒体特征的语句会产生歧义，比如：screen and (min-height: 50)。老版本浏览器会将这句话理解成screen，从而导致仅仅匹配到媒体类型（screen），就应用了指定样式，使用only可以很好地规避这种情况。使用only时必须指定媒体类型。 |
| comma（, ） | 将多个媒体特征以“或”的方式连接成一个媒体查询，如果存在结果为true的媒体特征，则查询条件成立。其效果等同于or运算符。例如：screen and (min-height: 1000), (round-screen: true) 表示当应用高度大于等于1000个像素单位或者设备屏幕是圆形时，条件成立。                                                                                                                |

媒体范围操作符包括<=，>=，<，>，详细解释说明如下表。

表2 媒体逻辑范围操作符| 类型 | 说明 |
| :- | :- |
| -------------- |

| <= | 小于等于，例如：screen and (height <= 50)。  |
| :- | -------------------------------------------- |
| >= | 大于等于，例如：screen and (height >= 600)。 |
| <  | 小于，例如：screen and (height < 50)。       |
| >  | 大于，例如：screen and (height > 600)。      |

### 媒体特征（media-feature）

媒体特征包括应用显示区域的宽高、设备分辨率以及设备的宽高等属性，详细说明如下表。

表3 媒体特征说明表| 类型 | 说明 |
| :- | :- |
| -------------- |

| height            | 应用页面可绘制区域的高度。                                                                                                                                                                                                                                    |
| :---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| min-height        | 应用页面可绘制区域的最小高度。                                                                                                                                                                                                                                |
| max-height        | 应用页面可绘制区域的最大高度。                                                                                                                                                                                                                                |
| width             | 应用页面可绘制区域的宽度。                                                                                                                                                                                                                                    |
| min-width         | 应用页面可绘制区域的最小宽度。                                                                                                                                                                                                                                |
| max-width         | 应用页面可绘制区域的最大宽度。                                                                                                                                                                                                                                |
| resolution        | 设备的分辨率，支持dpi，dppx和dpcm单位。其中：- dpi表示每英寸中物理像素个数，1dpi ≈ 0.39dpcm；- dpcm表示每厘米上的物理像素个数，1dpcm ≈ 2.54dpi；- dppx表示每个px中的物理像素数（此单位按96px = 1英寸为基准，与页面中的px单位计算方式不同），1dppx = 96dpi。 |
| min-resolution    | 设备的最小分辨率。                                                                                                                                                                                                                                            |
| max-resolution    | 设备的最大分辨率。                                                                                                                                                                                                                                            |
| orientation       | 屏幕的方向。可选值：- orientation: portrait（设备竖屏）；- orientation: landscape（设备横屏）。                                                                                                                                                               |
| device-height     | 设备的高度。                                                                                                                                                                                                                                                  |
| min-device-height | 设备的最小高度。                                                                                                                                                                                                                                              |
| max-device-height | 设备的最大高度。                                                                                                                                                                                                                                              |
| device-width      | 设备的宽度。                                                                                                                                                                                                                                                  |
| device-type       | 设备的类型。可选值：default、tablet。                                                                                                                                                                                                                         |
| min-device-width  | 设备的最小宽度。                                                                                                                                                                                                                                              |
| max-device-width  | 设备的最大宽度。                                                                                                                                                                                                                                              |
| round-screen      | 屏幕类型，圆形屏幕为true，非圆形屏幕为false。                                                                                                                                                                                                                 |
| dark-mode         | 系统为深色模式时为true，否则为false。                                                                                                                                                                                                                         |

## 场景示例

下例中使用媒体查询，实现屏幕横竖屏切换时，给页面文本应用添加不同的内容和样式。

Stage模型下的示例：

```
import mediaquery from '@ohos.mediaquery';
import window from '@ohos.window';
import common from '@ohos.app.ability.common';

let portraitFunc = null;

@Entry
@Component
struct MediaQueryExample {
  @State color: string = '#DB7093';
  @State text: string = 'Portrait';
  // 当设备横屏时条件成立
  listener = mediaquery.matchMediaSync('(orientation: landscape)');

  // 当满足媒体查询条件时，触发回调
  onPortrait(mediaQueryResult) {
    if (mediaQueryResult.matches) { // 若设备为横屏状态，更改相应的页面布局
      this.color = '#FFD700';
      this.text = 'Landscape';
    } else {
      this.color = '#DB7093';
      this.text = 'Portrait';
    }
  }

  aboutToAppear() {
    // 绑定当前应用实例
    portraitFunc = this.onPortrait.bind(this);
    // 绑定回调函数
    this.listener.on('change', portraitFunc);
  }

  // 改变设备横竖屏状态函数
  private changeOrientation(isLandscape: boolean) {
    // 获取UIAbility实例的上下文信息
    let context = getContext(this) as common.UIAbilityContext;
    // 调用该接口手动改变设备横竖屏状态
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT)
    });
  }

  build() {
    Column({ space: 50 }) {
      Text(this.text).fontSize(50).fontColor(this.color)
      Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          this.changeOrientation(true);
        })
      Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          this.changeOrientation(false);
        })
    }
    .width('100%').height('100%')
  }
}
```

FA模型下的示例：

```
import mediaquery from '@ohos.mediaquery';
import featureAbility from '@ohos.ability.featureAbility';

let portraitFunc = null;

@Entry
@Component
struct MediaQueryExample {
  @State color: string = '#DB7093';
  @State text: string = 'Portrait';
  listener = mediaquery.matchMediaSync('(orientation: landscape)'); // 当设备横屏时条件成立

  onPortrait(mediaQueryResult) { // 当满足媒体查询条件时，触发回调
    if (mediaQueryResult.matches) { // 若设备为横屏状态，更改相应的页面布局
      this.color = '#FFD700';
      this.text = 'Landscape';
    } else {
      this.color = '#DB7093';
      this.text = 'Portrait';
    }
  }

  aboutToAppear() {
    portraitFunc = this.onPortrait.bind(this); // 绑定当前应用实例
    this.listener.on('change', portraitFunc); //绑定回调函数
  }

  build() {
    Column({ space: 50 }) {
      Text(this.text).fontSize(50).fontColor(this.color)
      Text('Landscape').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          let context = featureAbility.getContext();
          context.setDisplayOrientation(0); //调用该接口手动改变设备横竖屏状态
        })
      Text('Portrait').fontSize(50).fontColor(this.color).backgroundColor(Color.Orange)
        .onClick(() => {
          let context = featureAbility.getContext();
          context.setDisplayOrientation(1); //调用该接口手动改变设备横竖屏状态
        })
    }
    .width('100%').height('100%')
  }
}
```

图1 竖屏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214113214.67208492160144478632396023012257:50001231000000:2800:E74FE7C9C399DFC442E82BF47161195639ACF89F687B85DB9799273213780664.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

图2 横屏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214113214.75273283847924910396153356085082:50001231000000:2800:CE59982DD489EE9CF713E65D721F5F1E5F393E3C3C4EAABFC24209B5DB37BABE.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")



# 创建列表（List）

更新时间: 2024-01-15 12:20

## 概述

列表是一种复杂的容器，当列表项达到一定数量，内容超过屏幕大小时，可以自动提供滚动功能。它适合用于呈现同类数据类型或数据类型集，例如图片和文本。在列表中显示数据集合是许多应用程序中的常见要求（如通讯录、音乐列表、购物清单等）。

使用列表可以轻松高效地显示结构化、可滚动的信息。通过在[List](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-list-0000001477981213-V3)组件中按垂直或者水平方向线性排列子组件[ListItemGroup](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-listitemgroup-0000001428061756-V3)或[ListItem](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-listitem-0000001427902476-V3)，为列表中的行或列提供单个视图，或使用[ForEach](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)迭代一组行或列，或混合任意数量的单个视图和ForEach结构，构建一个列表。List组件支持使用条件渲染、循环渲染、懒加载等[渲染控制](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-overview-0000001543911149-V3)方式生成子组件。

## 布局与约束

列表作为一种容器，会自动按其滚动方向排列子组件，向列表中添加组件或从列表中移除组件会重新排列子组件。

如下图所示，在垂直列表中，List按垂直方向自动排列ListItemGroup或ListItem。

ListItemGroup用于列表数据的分组展示，其子组件也是ListItem。ListItem表示单个列表项，可以包含单个子组件。

图1 List、ListItemGroup和ListItem组件关系
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.51481375244221331182921591197577:50001231000000:2800:EBE759F8717E84D74E76A9F75FEE56A20A70E9BC313F88F1F46C18121833133C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

说明

List的子组件必须是ListItemGroup或ListItem，ListItem和ListItemGroup必须配合List来使用。

### 布局

List除了提供垂直和水平布局能力、超出屏幕时可以滚动的自适应延伸能力之外，还提供了自适应交叉轴方向上排列个数的布局能力。

利用垂直布局能力可以构建单列或者多列垂直滚动列表，如下图所示。

图2 垂直滚动列表（左：单列；右：多列）
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.29234831842502016656623830026470:50001231000000:2800:25B9CB6BB6FC6D636CE94F735961AFFD90DE0A3283B2F637AB9CC3BBB8135AC0.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

利用水平布局能力可以是构建单行或多行水平滚动列表，如下图所示。

图3 水平滚动列表（左：单行；右：多行）
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.96762754362954204048191417722942:50001231000000:2800:CEF9E1ED1648B563420E4864509F1111D795283D1ACADDF130553048BD633DE1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### 约束

列表的主轴方向是指子组件列的排列方向，也是列表的滚动方向。垂直于主轴的轴称为交叉轴，其方向与主轴方向相互垂直。

如下图所示，垂直列表的主轴是垂直方向，交叉轴是水平方向。水平列表的主轴是水平方向，交叉轴是垂直方向。

图4 列表的主轴与交叉轴
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.45782886804855090237583609855763:50001231000000:2800:16BDC727200933BBB5DE1020104832528CDC2D97E9EFDE1864A8A92A150B3857.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果List组件主轴或交叉轴方向设置了尺寸，则其对应方向上的尺寸为设置值。

如果List组件主轴方向没有设置尺寸，当List子组件主轴方向总尺寸小于List的父组件尺寸时，List主轴方向尺寸自动适应子组件的总尺寸。

如下图所示，一个垂直列表B没有设置高度时，其父组件A高度为200vp，若其所有子组件C的高度总和为150vp，则此时列表B的高度为150vp。

图5 列表主轴高度约束示例1（ A : List的父组件;  B : List组件;  C : List的所有子组件）
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.45063832871857678506354067837041:50001231000000:2800:E90D37BEFBD83414E3A8645FC5348A2A816DB8032A198A9FB7A44A440B89298F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果子组件主轴方向总尺寸超过List父组件尺寸时，List主轴方向尺寸适应List的父组件尺寸。

如下图所示，同样是没有设置高度的垂直列表B，其父组件A高度为200vp，若其所有子组件C的高度总和为300vp，则此时列表B的高度为200vp。

图6 列表主轴高度约束示例2（ A : List的父组件;  B : List组件;  C : List的所有子组件）
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.78309702915872005125143692932677:50001231000000:2800:37FCA42049CD4F5B959F9EDE035E86D3FD34524F290F1B4ED07967639378C44F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

List组件交叉轴方向在没有设置尺寸时，其尺寸默认自适应父组件尺寸。

## 开发布局

### 设置主轴方向

List组件主轴默认是垂直方向，即默认情况下不需要手动设置List方向，就可以构建一个垂直滚动列表。

若是水平滚动列表场景，将List的listDirection属性设置为Axis.Horizontal即可实现。listDirection默认为Axis.Vertical，即主轴默认是垂直方向。

```
List() {
  ...
}
.listDirection(Axis.Horizontal)
```

### 设置交叉轴布局

List组件的交叉轴布局可以通过lanes和alignListItem属性进行设置，lanes属性用于确定交叉轴排列的列表项数量，alignListItem用于设置子组件在交叉轴方向的对齐方式。

List组件的lanes属性通常用于在不同尺寸的设备自适应构建不同行数或列数的列表。lanes属性的取值类型是"number | [LengthConstrain](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-types-0000001477981241-V3#ZH-CN_TOPIC_0000001573928889__lengthconstrain)"，即整数或者LengthConstrain类型。以垂直列表为例，如果将lanes属性设为2，表示构建的是一个两列的垂直列表，如图2中右图所示。lanes的默认值为1，即默认情况下，垂直列表的列数是1。

```
List() {
  ...
}
.lanes(2)
```

当其取值为LengthConstrain类型时，表示会根据LengthConstrain与List组件的尺寸自适应决定行或列数。

```
List() {
  ...
}
.lanes({ minLength: 200, maxLength: 300 })
```

例如，假设在垂直列表中设置了lanes的值为{ minLength: 200, maxLength: 300 }。此时，

* 当List组件宽度为300vp时，由于minLength为200vp，此时列表为一列。
* 当List组件宽度变化至400vp时，符合两倍的minLength，则此时列表自适应为两列。

同样以垂直列表为例，当alignListItem属性设置为ListItemAlign.Center表示列表项在水平方向上居中对齐。alignListItem的默认值是ListItemAlign.Start，即列表项在列表交叉轴方向上默认按首部对齐。

```
List() {
  ...
}
.alignListItem(ListItemAlign.Center)
```

## 在列表中显示数据

列表视图垂直或水平显示项目集合，在行或列超出屏幕时提供滚动功能，使其适合显示大型数据集合。在最简单的列表形式中，List静态地创建其列表项ListItem的内容。

图7 城市列表
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.94181413223185390842956610030401:50001231000000:2800:235035BD491E93FE569050CD26E7EDD726FB3E612F947038CE9ADD6A92F406F9.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
@Component
struct CityList {
  build() {
    List() {
      ListItem() {
        Text('北京').fontSize(24)
      }

      ListItem() {
        Text('杭州').fontSize(24)
      }

      ListItem() {
        Text('上海').fontSize(24)
      }
    }
    .backgroundColor('#FFF1F3F5')
    .alignListItem(ListItemAlign.Center)
  }
}
```

由于在ListItem中只能有一个根节点组件，不支持以平铺形式使用多个组件。因此，若列表项是由多个组件元素组成的，则需要将这多个元素组合到一个容器组件内或组成一个自定义组件。

图8 联系人列表项示例
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.70545124132830242245512230521305:50001231000000:2800:48830F5AB16B74D3A3A20AA0750E9D3A757B4D2A831EE754EAC4C6B18F0CEB6A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如上图所示，联系人列表的列表项中，每个联系人都有头像和名称。此时，需要将Image和Text封装到一个Row容器内。

```
List() {
  ListItem() {
    Row() {
      Image($r('app.media.iconE'))
        .width(40)
        .height(40)
        .margin(10)

      Text('小明')
        .fontSize(20)
    }
  }

  ListItem() {
    Row() {
      Image($r('app.media.iconF'))
        .width(40)
        .height(40)
        .margin(10)

      Text('小红')
        .fontSize(20)
    }
  }
}
```

## 迭代列表内容

通常更常见的是，应用通过数据集合动态地创建列表。使用[循环渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)可从数据源中迭代获取数据，并在每次迭代过程中创建相应的组件，降低代码复杂度。

ArkTS通过[ForEach](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)提供了组件的循环渲染能力。以简单形式的联系人列表为例，将联系人名称和头像数据以Contact类结构存储到contacts数组，使用ForEach中嵌套ListItem的形式来代替多个平铺的、内容相似的ListItem，从而减少重复代码。

```
import util from '@ohos.util';

class Contact {
  key: string = util.generateRandomUUID(true);
  name: string;
  icon: Resource;

  constructor(name: string, icon: Resource) {
    this.name = name;
    this.icon = icon;
  }
}

@Entry
@Component
struct SimpleContacts {
  private contacts = [
    new Contact('小明', $r("app.media.iconA")),
    new Contact('小红', $r("app.media.iconB")),
    ...
  ]

  build() {
    List() {
      ForEach(this.contacts, (item: Contact) => {
        ListItem() {
          Row() {
            Image(item.icon)
              .width(40)
              .height(40)
              .margin(10)
            Text(item.name).fontSize(20)
          }
          .width('100%')
          .justifyContent(FlexAlign.Start)
        }
      }, item => item.key)
    }
    .width('100%')
  }
}
```

在List组件中，ForEach除了可以用来循环渲染ListItem，也可以用来循环渲染ListItemGroup。ListItemGroup的循环渲染详细使用请参见[支持分组列表](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section1246111713018)。

## 自定义列表样式

### 设置内容间距

在初始化列表时，如需在列表项之间添加间距，可以使用space参数。例如，在每个列表项之间沿主轴方向添加10vp的间距：

```
List({ space: 10 }) {
  ...
}
```

### 添加分隔线

分隔线用来将界面元素隔开，使单个元素更加容易识别。如下图所示，当列表项左边有图标（如蓝牙图标），由于图标本身就能很好的区分，此时分隔线从图标之后开始显示即可。

图9 设置列表分隔线样式
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.39778774982686676926644431939001:50001231000000:2800:5B08320B00996446612FB0E66D593CB79118AC7793D5CE8F6148348924E6EF09.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

List提供了divider属性用于给列表项之间添加分隔线。在设置divider属性时，可以通过strokeWidth和color属性设置分隔线的粗细和颜色。

startMargin和endMargin属性分别用于设置分隔线距离列表侧边起始端的距离和距离列表侧边结束端的距离。

```
List() {
  ...
}
.divider({
  strokeWidth: 1,
  startMargin: 60,
  endMargin: 10,
  color: '#ffe9f0f0'
})
```

此示例表示从距离列表侧边起始端60vp开始到距离结束端10vp的位置，画一条粗细为1vp的分割线，可以实现图8设置列表分隔线的样式。

说明

1. 分隔线的宽度会使ListItem之间存在一定间隔，当List设置的内容间距小于分隔线宽度时，ListItem之间的间隔会使用分隔线的宽度。
2. 当List存在多列时，分割线的startMargin和endMargin作用于每一列上。
3. List组件的分隔线画在两个ListItem之间，第一个ListItem上方和最后一个ListItem下方不会绘制分隔线。

### 添加滚动条

当列表项高度（宽度）超出屏幕高度（宽度）时，列表可以沿垂直（水平)方向滚动。在页面内容很多时，若用户需快速定位，可拖拽滚动条，如下图所示。

图10 列表的滚动条
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.61975514652070940682373689919063:50001231000000:2800:80786507D8511990584BEDC948AC3D6D99112B31832105F4C206532A340D47D4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在使用List组件时，可通过scrollBar属性控制列表滚动条的显示。scrollBar的取值类型为[BarState](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__barstate)，当取值为BarState.Auto表示按需显示滚动条。此时，当触摸到滚动条区域时显示控件，可上下拖拽滚动条快速浏览内容，拖拽时会变粗。若不进行任何操作，2秒后滚动条自动消失。

```
List() {
  ...
}
.scrollBar(BarState.Auto)
```

## 支持分组列表

在列表中支持数据的分组展示，可以使列表显示结构清晰，查找方便，从而提高使用效率。分组列表在实际应用中十分常见，如下图所示联系人列表。

图11 联系人分组列表
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.72058413690973133961067873714929:50001231000000:2800:B8EF2517DFD12784C3F5D5C5C72396B3A74D74D4D445BD00A8F22358307A8318.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在List组件中使用ListItemGroup对项目进行分组，可以构建二维列表。

在List组件中可以直接使用一个或者多个ListItemGroup组件，ListItemGroup的宽度默认充满List组件。在初始化ListItemGroup时，可通过header参数设置列表分组的头部组件。

```
@Component
struct ContactsList {
  ...
  
  @Builder itemHead(text: string) {
    // 列表分组的头部组件，对应联系人分组A、B等位置的组件
    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {
    List() {
      ListItemGroup({ header: this.itemHead('A') }) {
        // 循环渲染分组A的ListItem
        ...
      }
      ...

      ListItemGroup({ header: this.itemHead('B') }) {
        // 循环渲染分组B的ListItem
        ...
      }
      ...
    }
  }
}
```

如果多个ListItemGroup结构类似，可以将多个分组的数据组成数组，然后使用ForEach对多个分组进行循环渲染。例如在联系人列表中，将每个分组的联系人数据contacts（可参考[迭代列表内容](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section574912673615)章节）和对应分组的标题title数据进行组合，定义为数组contactsGroups。

```
contactsGroups: object[] = [
  {
    title: 'A',
    contacts: [
      new Contact('艾佳', $r('app.media.iconA')),
      new Contact('安安', $r('app.media.iconB')),
      new Contact('Angela', $r('app.media.iconC')),
    ],
  },
  {
    title: 'B',
    contacts: [
      new Contact('白叶', $r('app.media.iconD')),
      new Contact('伯明', $r('app.media.iconE')),
    ],
  },
  ...
]
```

然后在ForEach中对contactsGroups进行循环渲染，即可实现多个分组的联系人列表。

```
List() {
  // 循环渲染ListItemGroup，contactsGroups为多个分组联系人contacts和标题title的数据集合
  ForEach(this.contactsGroups, item => {
    ListItemGroup({ header: this.itemHead(item.title) }) {
      // 循环渲染ListItem
      ForEach(item.contacts, contact => {
        ListItem() {
          ...
        }
      }, item => item.key)
    }
    ...
  })
}
```

## 添加粘性标题

粘性标题是一种常见的标题模式，常用于定位字母列表的头部元素。如下图所示，在联系人列表中滚动A部分时，B部分开始的头部元素始终处于A的下方。而在开始滚动B部分时，B的头部会固定在屏幕顶部，直到所有B的项均完成滚动后，才被后面的头部替代。

粘性标题不仅有助于阐明列表中数据的表示形式和用途，还可以帮助用户在大量信息中进行数据定位，从而避免用户在标题所在的表的顶部与感兴趣区域之间反复滚动。

图12 粘性标题
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.31029249535448930732930531007404:50001231000000:2800:F2ED462DA18EBB340C38136DEB839A7843E26C1295177D26DB3BF15EA1C2FC31.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

List组件的sticky属性配合ListItemGroup组件使用，用于设置ListItemGroup中的头部组件是否呈现吸顶效果或者尾部组件是否呈现吸底效果。

通过给List组件设置sticky属性为StickyStyle.Header，即可实现列表的粘性标题效果。如果需要支持吸底效果，可以通过footer参数初始化ListItemGroup的底部组件，并将sticky属性设置为StickyStyle.Footer。

```
@Component
struct ContactsList {
  // 定义分组联系人数据集合contactsGroups数组
  ...
 
  @Builder itemHead(text: string) {
    // 列表分组的头部组件，对应联系人分组A、B等位置的组件
    Text(text)
      .fontSize(20)
      .backgroundColor('#fff1f3f5')
      .width('100%')
      .padding(5)
  }

  build() {
    List() {
      // 循环渲染ListItemGroup，contactsGroups为多个分组联系人contacts和标题title的数据集合
      ForEach(this.contactsGroups, item => {
        ListItemGroup({ header: this.itemHead(item.title) }) {
          // 循环渲染ListItem
          ForEach(item.contacts, contact => {
            ListItem() {
              ...
            }
          }, item => item.key)
        }
        ...
      })
    }
    .sticky(StickyStyle.Header)  // 设置吸顶，实现粘性标题效果
  }
}
```

## 控制滚动位置

控制滚动位置在实际应用中十分常见，例如当新闻页列表项数量庞大，用户滚动列表到一定位置时，希望快速滚动到列表底部或返回列表顶部。此时，可以通过控制滚动位置来实现列表的快速定位，如下图所示。

图13 返回列表顶部
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.05594662022925476029693659819366:50001231000000:2800:E2468EF838F84FE9DE54187BEF7E4B6BD20D9BBD183E15AE7634E64C1528DD81.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

List组件初始化时，可以通过scroller参数绑定一个[Scroller](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-scroll-0000001427902480-V3#ZH-CN_TOPIC_0000001523648790__scroller)对象，进行列表的滚动控制。例如，用户在新闻应用中，点击新闻页面底部的返回顶部按钮时，就可以通过Scroller对象的scrollToIndex方法使列表滚动到指定的列表项索引位置。

首先，需要创建一个Scroller的对象listScroller。

```
private listScroller: Scroller = new Scroller();
```

然后，通过将listScroller用于初始化List组件的scroller参数，完成listScroller与列表的绑定。在需要跳转的位置指定scrollToIndex的参数为0，表示返回列表顶部。

```
Stack({ alignContent: Alignment.BottomEnd }) {
  // 将listScroller用于初始化List组件的scroller参数，完成listScroller与列表的绑定。
  List({ space: 20, scroller: this.listScroller }) {
    ...
  }
  ...

  Button() {
    ...
  }
  .onClick(() => {
    // 点击按钮时，指定跳转位置，返回列表顶部
    this.listScroller.scrollToIndex(0)
  })
  ...
}
```

## 响应滚动位置

许多应用需要监听列表的滚动位置变化并作出响应。例如，在联系人列表滚动时，如果跨越了不同字母开头的分组，则侧边字母索引栏也需要更新到对应的字母位置。

除了字母索引之外，滚动列表结合多级分类索引在应用开发过程中也很常见，例如购物应用的商品分类页面，多级分类也需要监听列表的滚动位置。

图14 字母索引响应联系人列表滚动
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.06102859857063327290872324181164:50001231000000:2800:9244C46536544EC49589B793DE24D854B73D5143DF881CC424678A2A00535C2C.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如上图所示，当联系人列表从A滚动到B时，右侧索引栏也需要同步从选中A状态变成选中B状态。此场景可以通过监听List组件的onScrollIndex事件来实现，右侧索引栏需要使用字母表索引组件[AlphabetIndexer](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-alphabet-indexer-0000001427744828-V3)。

在列表滚动时，根据列表此时所在的索引值位置firstIndex，重新计算字母索引栏对应字母的位置selectedIndex。由于AlphabetIndexer组件通过selected属性设置了选中项索引值，当selectedIndex变化时会触发AlphabetIndexer组件重新渲染，从而显示为选中对应字母的状态。

```
...
const alphabets = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

@Entry
@Component
struct ContactsList {
  @State selectedIndex: number = 0;
  private listScroller: Scroller = new Scroller();
  ...

  build() {
    Stack({ alignContent: Alignment.End }) {
      List({ scroller: this.listScroller }) {
        ...
      }
      .onScrollIndex((firstIndex: number) => {
          this.selectedIndex = firstIndex
        // 根据列表滚动到的索引值，重新计算对应联系人索引栏的位置this.selectedIndex
        ...
      })
      ...

      // 字母表索引组件
      AlphabetIndexer({ arrayValue: alphabets, selected: 0 })
        .selected(this.selectedIndex)
      ...
    }
  }
}
```

说明

计算索引值时，ListItemGroup作为一个整体占一个索引值，不计算ListItemGroup内部ListItem的索引值。

## 响应列表项侧滑

侧滑菜单在许多应用中都很常见。例如，通讯类应用通常会给消息列表提供侧滑删除功能，即用户可以通过向左侧滑列表的某一项，再点击删除按钮删除消息，如下图所示。

图15 侧滑删除列表项
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.88038935355399957651603772045203:50001231000000:2800:3477D019BEE56E88F0776BA89F664D6C2C815BA88F198A902C80B061725A6FD2.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")ListItem的swipeAction属性可用于实现列表项的左右滑动功能。swipeAction属性方法初始化时有必填参数SwipeActionOptions，其中，start参数表示设置列表项右滑时起始端滑出的组件，end参数表示设置列表项左滑时尾端滑出的组件。

在消息列表中，end参数表示设置ListItem左滑时尾端划出自定义组件，即删除按钮。在初始化end方法时，将滑动列表项的索引传入删除按钮组件，当用户点击删除按钮时，可以根据索引值来删除列表项对应的数据，从而实现侧滑删除功能。

```
@Entry
@Component
struct MessageList {
  @State messages: object[] = [
    // 初始化消息列表数据
    ...
  ];

  @Builder itemEnd(index: number) {
    // 侧滑后尾端出现的组件
    Button({ type: ButtonType.Circle }) {
      Image($r('app.media.ic_public_delete_filled'))
        .width(20)
        .height(20)
    }
    .onClick(() => {
      this.messages.splice(index, 1);
    })
    ...
  }

  build() {
    ...
      List() {
        ForEach(this.messages, (item, index) => {
          ListItem() {
            ...
          }
          .swipeAction({ end: this.itemEnd.bind(this, index) }) // 设置侧滑属性
        }, item => item.id.toString())
      }
    ...
  }
}
```

## 给列表项添加标记

添加标记是一种无干扰性且直观的方法，用于显示通知或将注意力集中到应用内的某个区域。例如，当消息列表接收到新消息时，通常对应的联系人头像的右上方会出现标记，提示有若干条未读消息，如下图所示。

图16 给列表项添加标记
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183848.63982640310795711716641451070904:50001231000000:2800:AAC23FCE95A6F8412DDB090B0DD92037353E8486E73FBCB36200B8AD8D63FEB5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在ListItem中使用[Badge](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-badge-0000001478181417-V3)组件可实现给列表项添加标记功能。Badge是可以附加在单个组件上用于信息标记的容器组件。

在消息列表中，若希望在联系人头像右上角添加标记，可在实现消息列表项ListItem的联系人头像时，将头像Image组件作为Badge的子组件。

在Badge组件中，count和position参数用于设置需要展示的消息数量和提示点显示位置，还可以通过style参数灵活设置标记的样式。

```
Badge({
  count: 1,
  position: BadgePosition.RightTop,
  style: { badgeSize: 16, badgeColor: '#FA2A2D' }
}) {
  // Image组件实现消息联系人头像
  ...
}
...
```

## 下拉刷新与上拉加载

页面的下拉刷新与上拉加载功能在移动应用中十分常见，例如，新闻页面的内容刷新和加载。这两种操作的原理都是通过响应用户的[触摸事件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-touch-0000001427902424-V3)，在顶部或者底部显示一个刷新或加载视图，完成后再将此视图隐藏。

以下拉刷新为例，其实现主要分成三步：

1. 监听手指按下事件，记录其初始位置的值。
2. 监听手指按压移动事件，记录并计算当前移动的位置与初始值的差值，大于0表示向下移动，同时设置一个允许移动的最大值。
3. 监听手指抬起事件，若此时移动达到最大值，则触发数据加载并显示刷新视图，加载完成后将此视图隐藏。

下拉刷新与上拉加载的具体实现可参考[相关实例](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section18857174610218)中新闻数据加载。若开发者希望快速实现此功能，也可使用三方组件[PullToRefresh](https://gitee.com/openharmony-sig/PullToRefresh)。

## 编辑列表

列表的编辑模式用途十分广泛，常见于待办事项管理、文件管理、备忘录的记录管理等应用场景。在列表的编辑模式下，新增和删除列表项是最基础的功能，其核心是对列表项对应的数据集合进行数据添加和删除。

下面以待办事项管理为例，介绍如何快速实现新增和删除列表项功能。

### 新增列表项

如下图所示，当用户点击添加按钮时，提供用户新增列表项内容选择或填写的交互界面，用户点击确定后，列表中新增对应的项目。

图17 新增待办
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183849.64358874222378847536107442462663:50001231000000:2800:1A62CE7465B8EAF05C35100F6DEB72B318F05F1C50F7210EF6AE7A1BDFED79AF.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

添加列表项功能实现主要流程如下：

1. 定义列表项数据结构和初始化列表数据，构建列表整体布局和列表项。
  以待办事项管理为例，首先定义待办数据结构：

```
import util from '@ohos.util';

export class ToDo {
  key: string = util.generateRandomUUID(true);
  name: string;

  constructor(name: string) {
    this.name = name;
  }
}
```

  然后，初始化待办列表数据和可选事项：

```
@State toDoData: ToDo[] = [];
private availableThings: string[] = ['读书', '运动', '旅游', '听音乐', '看电影', '唱歌'];
```

  最后，构建列表布局和列表项：

```
List({ space: 10 }) {
  ForEach(this.toDoData, (toDoItem) => {
    ListItem() {
      ...
    }
  }, toDoItem => toDoItem.key)
}
```
2. 提供新增列表项入口，即给新增按钮添加点击事件。
3. 响应用户确定新增事件，更新列表数据。
  待办事项管理示例的步骤2和步骤3功能实现如下：

```
Text('+')
  .onClick(() => {
    TextPickerDialog.show({
      range: this.availableThings,
      onAccept: (value: TextPickerResult) => {
         this.toDoData.push(new ToDo(this.availableThings[value.index])); // 新增列表项数据toDoData
      },
    })
  })
```

### 删除列表项

如下图所示，当用户长按列表项进入删除模式时，提供用户删除列表项选择的交互界面，用户勾选完成后点击删除按钮，列表中删除对应的项目。

图18 长按删除待办事项
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183849.35602437479744579621096206612477:50001231000000:2800:B419F06EF41660BC06D3630DABB0ECFA2FB2126559971CD1E16FD9CBCB383DA4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

删除列表项功能实现主要流程如下：

1. 列表的删除功能一般进入编辑模式后才可使用，所以需要提供编辑模式的入口。
  以待办列表为例，通过监听列表项的长按事件，当用户长按列表项时，进入编辑模式。
```
// ToDoListItem.ets

Flex({ justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
  ...
}
.gesture(
GestureGroup(GestureMode.Exclusive,
  LongPressGesture()
    .onAction(() => {
      if (!this.isEditMode) {
        this.isEditMode = true; //进入编辑模式
        this.selectedItems.push(this.toDoItem); // 记录长按时选中的列表项
      }
    })
  )
)
```
2. 需要响应用户的选择交互，记录要删除的列表项数据。
  在待办列表中，通过勾选框的勾选或取消勾选，响应用户勾选列表项变化，记录所有选择的列表项。
```
// ToDoListItem.ets

if (this.isEditMode) {
  Checkbox()
    .onChange((isSelected) => {
      if (isSelected) {
        this.selectedItems.push(this.toDoItem) // 勾选时，记录选中的列表项
      } else {
        let index = this.selectedItems.indexOf(this.toDoItem)
        if (index !== -1) {
          this.selectedItems.splice(index, 1) // 取消勾选时，则将此项从selectedItems中删除
        }
      }
    })
    ...
}
```
3. 需要响应用户点击删除按钮事件，删除列表中对应的选项。
```
// ToDoList.ets

Button('删除')
  .onClick(() => {
    // 删除选中的列表项对应的toDoData数据
    let leftData = this.toDoData.filter((item) => {
      return this.selectedItems.find((selectedItem) => selectedItem !== item);
    })

    this.toDoData = leftData;
    this.isEditMode = false;
  })
  ...
```

## 长列表的处理

[循环渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)适用于短列表，当构建具有大量列表项的长列表时，如果直接采用循环渲染方式，会一次性加载所有的列表元素，会导致页面启动时间过长，影响用户体验。因此，推荐使用[数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)（LazyForEach）方式实现按需迭代加载数据，从而提升列表性能。

关于长列表按需加载优化的具体实现可参考[数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)章节中的示例。

当使用懒加载方式渲染列表时，为了更好的列表滚动体验，减少列表滑动时出现白块，List组件提供了cachedCount参数用于设置列表项缓存数，只在懒加载LazyForEach中生效。

```
List() {
  LazyForEach(this.dataSource, item => {
    ListItem() {
      ...
    }
  })
}.cachedCount(3)
```

以垂直列表为例：

* 若懒加载是用于ListItem，当列表为单列模式时，会在List显示的ListItem前后各缓存cachedCount个ListItem；若是多列模式下，会在List显示的ListItem前后各缓存cachedCount*列数个ListItem。
* 若懒加载是用于ListItemGroup，无论单列模式还是多列模式，都是在List显示的ListItem前后各缓存cachedCount个ListItemGroup。

说明

1. cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。
2. 列表使用数据懒加载时，除了显示区域的列表项和前后缓存的列表项，其他列表项会被销毁。

## 相关实例

如需详细了解ArkUI中列表的创建与使用，请参考以下示例：

* [新闻数据加载](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NewsDataLoad)



# 创建网格（Grid/GridItem）

更新时间: 2024-01-15 12:21

## 概述

网格布局是由“行”和“列”分割的单元格所组成，通过指定“项目”所在的单元格做出各种各样的布局。网格布局具有较强的页面均分能力，子组件占比控制能力，是一种重要自适应布局，其使用场景有九宫格图片展示、日历、计算器等。

ArkUI提供了[Grid](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-grid-0000001478341161-V3)容器组件和子组件[GridItem](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-griditem-0000001478061713-V3)，用于构建网格布局。Grid用于设置网格布局相关参数，GridItem定义子组件相关特征。Grid组件支持使用条件渲染、循环渲染、懒加载等[渲染控制](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-overview-0000001543911149-V3)方式生成子组件。

## 布局与约束

Grid组件为网格容器，其中容器内每一个条目对应一个GridItem组件，如下图所示。

图1 Grid与GridItem组件关系
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.75534080997090101453601173782938:50001231000000:2800:792F9AB0800C826E903DF641CA1DB79809DAB5FFB9E0234F818968028617C045.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

说明

Grid的子组件必须是GridItem组件。

网格布局是一种二维布局。Grid组件支持自定义行列数和每行每列尺寸占比、设置子组件横跨几行或者几列，同时提供了垂直和水平布局能力。当网格容器组件尺寸发生变化时，所有子组件以及间距会等比例调整，从而实现网格布局的自适应能力。根据Grid的这些布局能力，可以构建出不同样式的网格布局，如下图所示。

图2 网格布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.89903509019269690386990147418336:50001231000000:2800:EF1D47CF147D5862D2B384210F38F264AB94CCEA0BE10DA0154C9FFD1AAAC935.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果Grid组件设置了宽高属性，则其尺寸为设置值。如果没有设置宽高属性，Grid组件的尺寸默认适应其父组件的尺寸。

Grid组件根据行列数量与占比属性的设置，可以分为三种布局情况：

* 行、列数量与占比同时设置：Grid只展示固定行列数的元素，其余元素不展示，且Grid不可滚动。（推荐使用该种布局方式）
* 只设置行、列数量与占比中的一个：元素按照设置的方向进行排布，超出的元素可通过滚动的方式展示。
* 行列数量与占比都不设置：元素在布局方向上排布，其行列数由布局方向、单个网格的宽高等多个属性共同决定。超出行列容纳范围的元素不展示，且Grid不可滚动。

## 设置排列方式



### 设置行列数量与占比

通过设置行列数量与尺寸占比可以确定网格布局的整体排列方式。Grid组件提供了rowsTemplate和columnsTemplate属性用于设置网格布局行列数量与尺寸占比。

rowsTemplate和columnsTemplate属性值是一个由多个空格和'数字+fr'间隔拼接的字符串，fr的个数即网格布局的行或列数，fr前面的数值大小，用于计算该行或列在网格布局宽度上的占比，最终决定该行或列的宽度。

图3 行列数量占比示例
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.04327925987458971666528865187345:50001231000000:2800:E55F6F6727F1DC8D505DFD9E31C0FFEA0BA776B3C6CD485D8917460CD008D69E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如上图所示，构建的是一个三行三列的的网格布局，其在垂直方向上分为三等份，每行占一份；在水平方向上分为四等份，第一列占一份，第二列占两份，第三列占一份。

只要将rowsTemplate的值为'1fr 1fr 1fr'，同时将columnsTemplate的值为'1fr 2fr 1fr'，即可实现上述网格布局。

```
Grid() {
  ...
}
.rowsTemplate('1fr 1fr 1fr')
.columnsTemplate('1fr 2fr 1fr')
```

说明

当Grid组件设置了rowsTemplate或columnsTemplate时，Grid的layoutDirection、maxCount、minCount、cellLength属性不生效，属性说明可参考[Grid-属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-grid-0000001478341161-V3#ZH-CN_TOPIC_0000001574128969__%E5%B1%9E%E6%80%A7)。

### 设置子组件所占行列数

除了大小相同的等比例网格布局，由不同大小的网格组成不均匀分布的网格布局场景在实际应用中十分常见，如下图所示。在Grid组件中，通过设置GridItem的rowStart、rowEnd、columnStart和columnEnd可以实现如图所示的单个网格横跨多行或多列的场景。

图4 不均匀网格布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.73808496517871292442533164851382:50001231000000:2800:DEA0A7406A2D9C497F7F9B97749FBACF75F3B7301992F6AC4FE9C22AECE86147.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

例如计算器的按键布局就是常见的不均匀网格布局场景。如下图，计算器中的按键“0”和“=”，按键“0”横跨第一、二两列，按键“=”横跨第五、六两行。使用Grid构建的网格布局，其行列标号从1开始，依次编号。

图5 计算器
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.96743220453375348691778926410350:50001231000000:2800:72F02A9B70149EFFD0CFC33EC2BEF8D6AB5108E89BFE0B159B9F200C919E9EFC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在单个网格单元中，rowStart和rowEnd属性表示指定当前元素起始行号和终点行号，columnStart和columnEnd属性表示指定当前元素的起始列号和终点列号。

所以“0”按键横跨第一列和第二列，只要将“0”对应GridItem的columnStart和columnEnd设为1和2，将“=”对应GridItem的的rowStart和rowEnd设为5和6即可。

```
GridItem() {
  Text(key)
    ...
}
.columnStart(1)
.columnEnd(2)
```

“=”按键横跨第五行和第六行，只要将将“=”对应GridItem的的rowStart和rowEnd设为5和6即可。

```
GridItem() {
  Text(key)
    ...
}
.rowStart(5)
.rowEnd(6)
```

### 设置主轴方向

使用Grid构建网格布局时，若没有设置行列数量与占比，可以通过layoutDirection可以设置网格布局的主轴方向，决定子组件的排列方式。此时可以结合minCount和maxCount属性来约束主轴方向上的网格数量。

图6 主轴方向示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.75504242616292487682681940935036:50001231000000:2800:09E52DFFB119F35607E2862605D091084E01A261666F588BABFB95B126D023D6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

当前layoutDirection设置为Row时，先从左到右排列，排满一行再排一下一行。当前layoutDirection设置为Column时，先从上到下排列，排满一列再排一下一列，如上图所示。此时，将maxCount属性设为3，表示主轴方向上最大显示的网格单元数量为3。

```
Grid() {
  ...
}
.maxCount(3)
.layoutDirection(GridDirection.Row)
```

说明

1. layoutDirection属性仅在不设置rowsTemplate和columnsTemplate时生效，此时元素在layoutDirection方向上排列。
2. 仅设置rowsTemplate时，Grid主轴为水平方向，交叉轴为垂直方向。
3. 仅设置columnsTemplate时，Grid主轴为垂直方向，交叉轴为水平方向。

## 在网格布局中显示数据

网格布局采用二维布局的方式组织其内部元素，如下图所示。

图7 通用办公服务
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.17529420672506068665163981444203:50001231000000:2800:A919C273AAE96440BCE7B595156D9BCBF4A63481A3822B13607FB0AB139DBE96.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

Grid组件可以通过二维布局的方式显示一组GridItem子组件。

```
Grid() {
  GridItem() {
    Text('会议')
      ...
  }

  GridItem() {
    Text('签到')
      ...
  }

  GridItem() {
    Text('投票')
      ...
  }

  GridItem() {
    Text('打印')
      ...
  }
}
.rowsTemplate('1fr 1fr')
.columnsTemplate('1fr 1fr')
```

对于内容结构相似的多个GridItem，通常更推荐使用[循环渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)ForEach语句中嵌套GridItem的形式，来减少重复代码。

```
@Component
struct OfficeService {
  @State services: Array<string> = ['会议', '投票', '签到', '打印']
  ...

  build() {
    Column() {
      Grid() {
        ForEach(this.services, service => {
          GridItem() {
            Text(service)
              ...
          }
        }, service => service)
      }
      .rowsTemplate('1fr 1fr')
      .columnsTemplate('1fr 1fr')
      ...
    }
    ...
  }
}
```

## 设置行列间距

在两个网格单元之间的网格横向间距称为行间距，网格纵向间距称为列间距，如下图所示。

图8 网格的行列间距
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.11661572535337771444048654269564:50001231000000:2800:1A025E6381CCD84D0886F5919535895BD5BFDDE5F1EC2AA61834BA665DB16F1B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")通过Grid的rowsGap和columnsGap可以设置网格布局的行列间距。在图5所示的计算器中，行间距为15vp，列间距为10vp。

```
Grid() {
  ...
}
.columnsGap(10)
.rowsGap(15)
```

## 构建可滚动的网格布局

可滚动的网格布局常用在文件管理、购物或视频列表等页面中，如下图所示。在设置Grid的行列数量与占比时，如果仅设置行、列数量与占比中的一个，即仅设置rowsTemplate或仅设置columnsTemplate属性，网格单元按照设置的方向排列，超出Grid显示区域后，Grid拥有可滚动能力。

图9 横向可滚动网格布局
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.76180846287498201880108753731669:50001231000000:2800:0FDAB20AB6E4CAF3603B5A9A82ED96ABEC786200721EACED5CA3B2CF679843BD.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

如果设置的是columnsTemplate，Grid的滚动方向为垂直方向；如果设置的是rowsTemplate，Grid的滚动方向为水平方向。

如上图所示的横向可滚动网格布局，只要设置rowsTemplate属性的值且不设置columnsTemplate属性，当内容超出Grid组件宽度时，Grid可横向滚动进行内容展示。

```
@Component
struct Shopping {
  @State services: Array<string> = ['直播', '进口', ...]
  ...

  build() {
    Column({ space: 5 }) {
      Grid() {
        ForEach(this.services, (service: string, index) => {
          GridItem() {
            ...
          }
          .width('25%')
        }, service => service)
      }
      .rowsTemplate('1fr 1fr') // 只设置rowsTemplate属性，当内容超出Grid区域时，可水平滚动。
      .rowsGap(15)
      ...
    }
    ...
  }
}
```

## 控制滚动位置

与新闻列表的返回顶部场景类似，控制滚动位置功能在网格布局中也很常用，例如下图所示日历的翻页功能。

图10 日历翻页
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183852.82949552411824461323389842112811:50001231000000:2800:48DE205FBF1D60BF6E86739C50AAA5090F8D64F1E885AC4B4D741B8F8B2B6BEB.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

Grid组件初始化时，可以绑定一个[Scroller](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-scroll-0000001427902480-V3#ZH-CN_TOPIC_0000001523648790__scroller)对象，用于进行滚动控制，例如通过Scroller对象的[scrollPage](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-scroll-0000001427902480-V3#ZH-CN_TOPIC_0000001523648790__scrollpage)方法进行翻页。

```
private scroller: Scroller = new Scroller()
```

在日历页面中，用户在点击“下一页”按钮时，应用响应点击事件，通过指定scrollPage方法的参数next为true，滚动到下一页。

```
Column({ space: 5 }) {
  Grid(this.scroller) {
    ...
  }
  .columnsTemplate('1fr 1fr 1fr 1fr 1fr 1fr 1fr')
  ...
 
 Row({space: 20}) {
   Button('上一页')
     .onClick(() => {
       this.scroller.scrollPage({
         next: false
       })
     })

   Button('下一页')
     .onClick(() => {
       this.scroller.scrollPage({
         next: true
       })
     })
 }
}
...
```

## 性能优化

与[长列表的处理](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-development-create-list-0000001451074018-V3#section94148431926)类似，[循环渲染](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)适用于数据量较小的布局场景，当构建具有大量网格项的可滚动网格布局时，推荐使用[数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)方式实现按需迭代加载数据，从而提升列表性能。

关于按需加载优化的具体实现可参考[数据懒加载](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)章节中的示例。

当使用懒加载方式渲染网格时，为了更好的滚动体验，减少滑动时出现白块，Grid组件中也可通过cachedCount属性设置GridItem的预加载数量，只在懒加载LazyForEach中生效。

设置预加载数量后，会在Grid显示区域前后各缓存cachedCount*列数个GridItem，超出显示和缓存范围的GridItem会被释放。

```
Grid() {
  LazyForEach(this.dataSource, item => {
    GridItem() {
      ...
    }
  })
}
.cachedCount(3)
```

说明

cachedCount的增加会增大UI的CPU、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。



# 创建轮播（Swiper）

更新时间: 2024-01-15 12:23

[Swiper](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-swiper-0000001427744844-V3)组件提供滑动轮播显示的能力。Swiper本身是一个容器组件，当设置了多个子组件后，可以对这些子组件进行轮播显示。通常，在一些应用首页显示推荐的内容时，需要用到轮播显示的能力。

## 布局与约束

Swiper作为一个容器组件，在自身尺寸属性未被设置时，会自动根据子组件的大小设置自身的尺寸。如果开发者对Swiper组件设置了固定的尺寸，则在轮播显示过程中均以该尺寸生效；否则，在轮播过程中，会根据子组件的大小自动调整自身的尺寸。

## 循环播放

通过loop属性控制是否循环播放，该属性默认值为true。

当loop为true时，在显示第一页或最后一页时，可以继续往前切换到前一页或者往后切换到后一页。如果loop为false，则在第一页或最后一页时，无法继续向前或者向后切换页面。

loop为true：

```
...
private swiperController: SwiperController = new SwiperController()
...
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Blue)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.loop(true)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.31642353669443233164328904499980:50001231000000:2800:52B054264F875BE2A556116825910CB57C3213F1355110ED8F9D7D390851A28D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

loop为false：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Blue)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.loop(false)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.91103852937824746641345124342516:50001231000000:2800:D192C4557FFB0F67A2192FFD6E8CC125053F68FF7790518990ECC401954C100E.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自动轮播

Swiper通过设置autoPlay属性，控制是否自动轮播子组件。该属性默认值为false。

autoPlay为true时，会自动切换播放子组件，子组件与子组件之间的播放间隔通过interval属性设置。interval属性默认值为3000，单位毫秒。

autoPlay为true：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.loop(true)
.autoPlay(true)
.interval(1000)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.81202262964629428224310900061593:50001231000000:2800:50FD16A3116BB34A04A3206ADA0CB1C61C9729B889B044EF5685A315E44A9D5A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 导航点样式

Swiper提供了默认的导航点样式，导航点默认显示在Swiper下方居中位置，开发者也可以通过indicatorStyle属性自定义导航点的位置和样式。

通过indicatorStyle属性，开发者可以设置导航点相对于Swiper组件上下左右四个方位的位置，同时也可以设置每个导航点的尺寸、颜色、蒙层和被选中导航点的颜色。

导航点使用默认样式：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.09650938221009313693657688266528:50001231000000:2800:2DA6BFFC441F36B340CA027DA81DB27DD986F7ED4E3B1E8068BACFFB46CDEE11.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

自定义导航点样式（示例：导航点直径设为30VP，左边距为0，导航点颜色设为红色）：

```
Swiper(this.swiperController) {
  Text("0")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("1")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)

  Text("2")
    .width('90%')
    .height('100%')
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.indicatorStyle({
  size: 30,
  left: 0,
  color: Color.Red
})
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.50494487807687429218644629228349:50001231000000:2800:21DE4742102A1274E852B52D9C32215D3C8EF59617379BD8FC6727B9512A015F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 页面切换方式

Swiper支持三种页面切换方式：手指滑动、点击导航点和通过控制器。

通过控制器切换页面：

```
@Entry
@Component
struct SwiperDemo {
  private swiperController: SwiperController = new SwiperController();

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        Text("0")
          .width(250)
          .height(250)
          .backgroundColor(Color.Gray)
          .textAlign(TextAlign.Center)
          .fontSize(30)
        Text("1")
          .width(250)
          .height(250)
          .backgroundColor(Color.Green)
          .textAlign(TextAlign.Center)
          .fontSize(30)
        Text("2")
          .width(250)
          .height(250)
          .backgroundColor(Color.Pink)
          .textAlign(TextAlign.Center)
          .fontSize(30)
      }
      .indicator(true)

      Row({ space: 12 }) {
        Button('showNext')
          .onClick(() => {
            this.swiperController.showNext(); // 通过controller切换到后一页
          })
        Button('showPrevious')
          .onClick(() => {
            this.swiperController.showPrevious(); // 通过controller切换到前一页
          })
      }.margin(5)
    }.width('100%')
    .margin({ top: 5 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.93289871911183688478456436794437:50001231000000:2800:DDCD6EBB3EE0C1081E411ADF35C8D1009510396C157DB505FA1DEBA7E61EA734.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 轮播方向

Swiper支持水平和垂直方向上进行轮播，主要通过vertical属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

设置水平方向上轮播：

```
Swiper(this.swiperController) {
  ...
}
.indicator(true)
.vertical(false)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183854.48512939215655935695074689242255:50001231000000:2800:CE932C0858A2F8E260CECBAAA31B0A9FD192FA4834A8057890874709052C13A8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

设置垂直方向轮播：

```
Swiper(this.swiperController) {
  ...
}
.indicator(true)
.vertical(true)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.38349886946585687700614295700064:50001231000000:2800:7AB2C0ABDC9621973880C97F95232A143B93ABCDA0D617BA45A361374C582E2A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 每页显示多个子页面

Swiper支持在一个页面内同时显示多个子组件，通过[displayCount](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-swiper-0000001427744844-V3)属性设置。

设置一个页面内显示两个子组件：

```
Swiper(this.swiperController) {
  Text("0")
    .width(250)
    .height(250)
    .backgroundColor(Color.Gray)
    .textAlign(TextAlign.Center)
    .fontSize(30)
  Text("1")
    .width(250)
    .height(250)
    .backgroundColor(Color.Green)
    .textAlign(TextAlign.Center)
    .fontSize(30)
  Text("2")
    .width(250)
    .height(250)
    .backgroundColor(Color.Pink)
    .textAlign(TextAlign.Center)
    .fontSize(30)
  Text("3")
    .width(250)
    .height(250)
    .backgroundColor(Color.Blue)
    .textAlign(TextAlign.Center)
    .fontSize(30)
}
.indicator(true)
.displayCount(2)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.65234031092017077969679844708564:50001231000000:2800:014BF58C5F6550A5F2AEDD767DA591482F8C8B75B9B391B4A3FC82D70F5F52DF.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 改善布局性能

更新时间: 2024-01-15 12:17

Flex为采用弹性布局的容器。容器内部的所有子元素，会自动参与弹性布局。子元素默认沿主轴排列，子元素在主轴方向的尺寸称为主轴尺寸。

在单行布局场景下，容器里子组件的主轴尺寸长度总和可能存在不等于容器主轴尺寸长度的情况。例如，三个子组件的宽均为200px，容器宽为500px，当第一个子组件和第二个子组件布局完成后，为了显示第三个子组件，需要给第二个子组件和第三个子组件设置压缩属性[flexShrink](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)，此时第二个子组件会被再布局一次，导致布局效率下降。

## 场景一

所有子组件未设置[displayPriority](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-layout-constraints-0000001427744784-V3)属性（或displayPriority设置为默认值1）和[layoutWeight](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性（或layoutWeight设置为默认值0）时，所有子组件先按序布局一次。

* 第一次布局子组件主轴尺寸长度总和等于容器主轴尺寸长度，不需要二次布局。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.46818115426235369052238484386518:50001231000000:2800:BB38D3872369CD73B20DFC078BB6968C3F64A05DC2995C18CE3E440C2DDD5203.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 第一次布局子组件主轴尺寸长度总和小于容器主轴尺寸长度，且包含设置有效的[flexGrow](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-flex-layout-0000001478181377-V3)属性的子组件，设置有效的flexGrow属性的子组件会触发二次布局，拉伸布局填满容器。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.56485760498246700612123109539472:50001231000000:2800:4BF2FC641B7366877F6DBCC59AE91CC38DB06CDA296A74EABF236F0196D0EEB4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 第一次布局子组件主轴尺寸长度总和大于容器主轴尺寸长度，且包含设置有效的flexShrink属性（flex子组件默认值为1，为有效值）的子组件，设置有效的flexShrink属性的子组件会触发二次布局，压缩布局填满容器。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.08424079892667659624461236971158:50001231000000:2800:0C9DB66D3FD61E2CF4A754592AAA6F5E47B55B5DD9D41AF60CE5972EDB968E3D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景二

子组件存在设置displayPriority属性，不存在设置layoutWeight属性。

根据displayPriority从大到小顺序，布局每组同displayPriority值的子组件，直到子组件主轴尺寸长度总和最大且不超过容器主轴尺寸长度，舍弃未布局的低优先级displayPriority（可能存在一组临界displayPriority值的子组件布局但未使用的情况）。

* 第一次布局子组件主轴尺寸长度总和等于容器主轴尺寸长度，不需要二次布局。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.79492943016652148945301873629113:50001231000000:2800:59F0E90C21F19340234CEDE653882BC2D4DBB9CDE0BB71B9E36230A2D9E01A49.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 第一次布局子组件主轴尺寸长度总和小于容器主轴尺寸长度，且包含设置有效的flexGrow属性的子组件，设置有效的flexGrow属性的子组件会触发二次布局，拉伸布局填满容器。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.33065224215722752937991080435094:50001231000000:2800:704CFB4261724AEB0D61A9AC7F0C70364655D8011972C9760BE390EE1F01E197.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景三

子组件中存在设置layoutWeight属性。

根据displayPriority从大到小顺序，对设置displayPriority相同值的子组件且不设置layoutWeight属性的子组件进行布局，直到子组件主轴尺寸长度的总和最大且不超过容器主轴尺寸长度。如果子组件主轴尺寸长度的总和超过了容器主轴尺寸长度，舍弃未布局的低优先级displayPriority，可能存在一组临界displayPriority值的子组件布局但未使用的情况。

剩余空间按设置layoutWeight属性的子组件的layoutWeight比例填满容器。

* 两次遍历都只布局一次组件，不会触发二次布局。![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183855.71664618830295189729587921575867:50001231000000:2800:AD9EA72B2E9FAB79F930BEDF2B9094F1B365D57A840031D2A2B4F5FACF0D4446.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 如何优化Flex的布局性能

* 使用Column/Row代替Flex。
* 大小不需要变更的子组件主动设置flexShrink属性值为0。
* 优先使用layoutWeight属性替代flexGrow属性和flexShrink属性。
* 子组件主轴长度分配设置为最常用场景的布局结果，使子组件主轴长度总和等于Flex容器主轴长度。



# 按钮（Button）

更新时间: 2024-01-15 12:18

Button是按钮组件，通常用于响应用户的点击操作，其类型包括胶囊按钮、圆形按钮、普通按钮。Button当做为容器使用时可以通过添加子组件实现包含文字、图片等元素的按钮。具体用法请参考[Button](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-button-0000001427584848-V3)。

## 创建按钮

Button通过调用接口来创建，接口调用有以下两种形式：

* 创建不包含子组件的按钮。

```
Button(label?: string, options?: { type?: ButtonType, stateEffect?: boolean })
```

  该接口用于创建不包含子组件的按钮，其中label用来设置按钮文字，type用于设置Button类型，stateEffect属性设置Button是否开启点击效果。

```
Button('Ok', { type: ButtonType.Normal, stateEffect: true }) 
  .borderRadius(8) 
  .backgroundColor(0x317aff) 
  .width(90)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.68709774846202841087444365394519:50001231000000:2800:52B7059DCCF7E6AC85F1A1450D47C6A9F9506D66C1CB248674F496E72F4B4E01.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 创建包含子组件的按钮。

```
Button(options?: {type?: ButtonType, stateEffect?: boolean})
```

  该接口用于创建包含子组件的按钮，只支持包含一个子组件，子组件可以是[基础组件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-alphabet-indexer-0000001427744828-V3)或者[容器组件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-badge-0000001478181417-V3)。

```
Button({ type: ButtonType.Normal, stateEffect: true }) {
  Row() {
    Image($r('app.media.loading')).width(20).height(40).margin({ left: 12 })
    Text('loading').fontSize(12).fontColor(0xffffff).margin({ left: 5, right: 12 })
  }.alignItems(VerticalAlign.Center)
}.borderRadius(8).backgroundColor(0x317aff).width(90).height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.77462936499010173006258252660667:50001231000000:2800:4A9785EA34DCB7AD0D001BB08AEE9C0FAC35B900422E282D14F92F105457D38B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 设置按钮类型

Button有三种可选类型，分别为Capsule（胶囊类型）、Circle（圆形按钮）和Normal（普通按钮），通过type进行设置。

* 胶囊按钮（默认类型）此类型按钮的圆角自动设置为高度的一半，不支持通过borderRadius属性重新设置圆角。

```
Button('Disable', { type: ButtonType.Capsule, stateEffect: false }) 
  .backgroundColor(0x317aff) 
  .width(90)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.43897344296160030375834797868039:50001231000000:2800:7065BBC85FAC39DE3A102338F066768B717D92837B8D25286A644874478E9EF5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 圆形按钮此类型按钮为圆形，不支持通过borderRadius属性重新设置圆角。

```
Button('Circle', { type: ButtonType.Circle, stateEffect: false }) 
  .backgroundColor(0x317aff) 
  .width(90) 
  .height(90)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.39309621427301997008480624930043:50001231000000:2800:2AE57915B2B6D8085A360A45529881F85C8CEC9A32910FFD5779911498212BFD.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 普通按钮此类型的按钮默认圆角为0，支持通过borderRadius属性重新设置圆角。

```
Button('Ok', { type: ButtonType.Normal, stateEffect: true }) 
  .borderRadius(8) 
  .backgroundColor(0x317aff) 
  .width(90)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.04967863439339643038556997288712:50001231000000:2800:3BEEDA76DFDDA1E8795CA716E6A16DEC3962AFB455A146F1ACDFFB0B01440D4A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

* 设置边框弧度。
  一般使用通用属性来自定义按钮样式。例如通过borderRadius属性设置按钮的边框弧度。

```
Button('circle border', { type: ButtonType.Normal }) 
  .borderRadius(20)
  .height(40)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.86691812017673344410264576273998:50001231000000:2800:6A38C8F8A5E6E1E9ACCF6FCCE08306003E09B653A60986CE52FFA4E7FF871909.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 设置文本样式。通过添加文本样式设置按钮文本的展示样式。

```
Button('font style', { type: ButtonType.Normal }) 
  .fontSize(20) 
  .fontColor(Color.Pink) 
  .fontWeight(800)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.98642942182022718477123684670093:50001231000000:2800:EEA589743B581A9582014D8F79EF90C4CA1C57550A917AC5E073F31902E69CB1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 设置背景颜色。添加backgroundColor属性设置按钮的背景颜色。

```
Button('background color').backgroundColor(0xF55A42)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.06644360513315284049135432917299:50001231000000:2800:D847B7366DA4A974CD4FF5F0FC6424A81C83769D53567E88A1ED40350C97F29E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 用作功能型按钮。为删除操作创建一个按钮。

```
Button({ type: ButtonType.Circle, stateEffect: true }) { 
  Image($r('app.media.ic_public_delete_filled')).width(30).height(30) 
}.width(55).height(55).margin({ left: 20 }).backgroundColor(0xF55A42)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.96215170762646281150232692214340:50001231000000:2800:4D303C5C92F9821D74C388B8BDBF5FABDEC706475E41585268644ADDE0CF289E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

Button组件通常用于触发某些操作，可以绑定onClick事件来响应点击操作后的自定义行为。

```
Button('Ok', { type: ButtonType.Normal, stateEffect: true }) 
  .onClick(()=>{ 
    console.info('Button onClick') 
  })
```

## 场景示例

* 用于启动操作。可以用按钮启动任何用户界面元素，按钮会根据用户的操作触发相应的事件。例如，在List容器里通过点击按钮进行页面跳转。

```
// xxx.ets
import router from '@ohos.router';
@Entry
@Component
struct ButtonCase1 {
  build() {
    List({ space: 4 }) {
      ListItem() {
        Button("First").onClick(() => {
          router.pushUrl({ url: 'pages/first_page' })
        })
          .width('100%')
      }
      ListItem() {
        Button("Second").onClick(() => {
          router.pushUrl({ url: 'pages/second_page' })
        })
          .width('100%')
      }
      ListItem() {
        Button("Third").onClick(() => {
          router.pushUrl({ url: 'pages/third_page' })
        })
          .width('100%')
      }
    }
    .listDirection(Axis.Vertical)
    .backgroundColor(0xDCDCDC).padding(20)
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.73825096193515558546306278881215:50001231000000:2800:BE8B7E861DA9EC2C7FC4068AF6ADEECF5C9D965A64F77639CF0D7A9B08FECD96.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* 用于表单的提交。在用户登录/注册页面，使用按钮进行登录或注册操作。

```
// xxx.ets
@Entry
@Component
struct ButtonCase2 {
  build() {
    Column() {
      TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
      TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
      Button('Register').width(300).margin({ top: 20 })
        .onClick(() => {
          // 需要执行的操作
        })
    }.padding(20)
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.37608849491344976073238734219957:50001231000000:2800:E00B577B162EBF780613216DDFCEAD650CA916DC5373E5685917DAA91D195055.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 悬浮按钮在可以滑动的界面，滑动时按钮始终保持悬浮状态。

```
// xxx.ets
@Entry
@Component
struct HoverButtonExample {
  private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  build() {
    Stack() {
      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.arr, (item) => {
          ListItem() {
            Text('' + item)
              .width('100%').height(100).fontSize(16)
              .textAlign(TextAlign.Center).borderRadius(10).backgroundColor(0xFFFFFF)
          }
        }, item => item)
      }.width('90%')
      Button() {
        Image($r('app.media.ic_public_add'))
          .width(50)
          .height(50)
      }
      .width(60)
      .height(60)
      .position({x: '80%', y: 600})
      .shadow({radius: 10})
      .onClick(() => {
        // 需要执行的操作
      })
    }
    .width('100%')
    .height('100%')
    .backgroundColor(0xDCDCDC)
    .padding({ top: 5 })
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183856.77706157243493821898075978653236:50001231000000:2800:78066818C07B509664B6B8730518F7A78630302F1CD2236056FEC004AA0AC3C7.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 单选框（Radio）

更新时间: 2024-01-15 12:18

Radio是单选框组件，通常用于提供相应的用户交互选择项，同一组的Radio中只有一个可以被选中。具体用法请参考[Radio](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-radio-0000001478181405-V3)。

## 创建单选框

Radio通过调用接口来创建，接口调用形式如下：

```
Radio(options: {value: string, group: string})
```

该接口用于创建一个单选框，其中value是单选框的名称，group是单选框的所属群组名称。checked属性可以设置单选框的状态，状态分别为false和true时，设置为true时表示单选框被选中。Radio仅支持选中和未选中两种样式，不支持自定义颜色和形状。

```
Radio({ value: 'Radio1', group: 'radioGroup' })
  .checked(false)
Radio({ value: 'Radio2', group: 'radioGroup' })
  .checked(true)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183857.58125840987137090703903969184716:50001231000000:2800:7C721A6C327398CB6AA26F14C26160E1ED66471CDBE0C2A994EE72645C95E066.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

除支持[通用事件](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-click-0000001477981153-V3)外，Radio通常用于选中后触发某些操作，可以绑定onChange事件来响应选中操作后的自定义行为。

```
  Radio({ value: 'Radio1', group: 'radioGroup' })
    .onChange((isChecked: boolean) => {
      if(isChecked) {
        //需要执行的操作
      }
    })
  Radio({ value: 'Radio2', group: 'radioGroup' })
    .onChange((isChecked: boolean) => {
      if(isChecked) {
        //需要执行的操作
      }
    })
```

## 场景示例

通过点击Radio切换声音模式。

```
// xxx.ets
import promptAction from '@ohos.promptAction';
@Entry
@Component
struct RadioExample {
  build() {
    Row() {
      Column() {
        Radio({ value: 'Radio1', group: 'radioGroup' }).checked(true)
          .height(50)
          .width(50)
          .onChange((isChecked: boolean) => {
            if(isChecked) {
              // 切换为响铃模式
              promptAction.showToast({ message: 'Ringing mode.' })
            }
          })
        Text('Ringing')
      }
      Column() {
        Radio({ value: 'Radio2', group: 'radioGroup' })
          .height(50)
          .width(50)
          .onChange((isChecked: boolean) => {
            if(isChecked) {
              // 切换为振动模式
              promptAction.showToast({ message: 'Vibration mode.' })
            }
          })
        Text('Vibration')
      }
      Column() {
        Radio({ value: 'Radio3', group: 'radioGroup' })
          .height(50)
          .width(50)
          .onChange((isChecked: boolean) => {
            if(isChecked) {
              // 切换为静音模式
              promptAction.showToast({ message: 'Silent mode.' })
            }
          })
        Text('Silent')
      }
    }.height('100%').width('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183857.83967246863091138556907506453041:50001231000000:2800:64F3902EF615FAD09B39A767C4AAF5FDB514A82C9DB1454C5CA8ED2A255BBB16.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 切换按钮（Toggle）

更新时间: 2024-01-15 12:19

Toggle组件提供状态按钮样式，勾选框样式及开关样式，一般用于两种状态之间的切换。具体用法请参考[Toggle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-toggle-0000001478061705-V3)。

## 创建切换按钮

Toggle通过调用接口来创建，接口调用形式如下：

```
Toggle(options: { type: ToggleType, isOn?: boolean })
```

该接口用于创建切换按钮，其中ToggleType为开关类型，包括Button、Checkbox和Switch，isOn为切换按钮的状态，接口调用有以下两种形式：

* 创建不包含子组件的Toggle。当ToggleType为Checkbox或者Switch时，用于创建不包含子组件的Toggle：

```
Toggle({ type: ToggleType.Checkbox, isOn: false })
Toggle({ type: ToggleType.Checkbox, isOn: true })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.63359999959084338946341552977337:50001231000000:2800:E269DE4D840B020037BD611A278806471C97F7656CC06FF1214C5D1CAA004731.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
Toggle({ type: ToggleType.Switch, isOn: false })
Toggle({ type: ToggleType.Switch, isOn: true })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.69258225389488419026499656703181:50001231000000:2800:E73F64436F7EA6516A9D7EECBCE43DE3F5FC18B313B391B7197D4DD9497D4AA2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 创建包含子组件的Toggle。当ToggleType为Button时，只能包含一个子组件，如果子组件有文本设置，则相应的文本内容会显示在按钮内部。

```
Toggle({ type: ToggleType.Button, isOn: false }) {
  Text('status button')
  .fontColor('#182431')
  .fontSize(12)
}.width(100)
Toggle({ type: ToggleType.Button, isOn: true }) {
  Text('status button')
  .fontColor('#182431')
  .fontSize(12)
}.width(100)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.88367328583453750101839410377391:50001231000000:2800:26B356CAFCBC3D87CE7A3F05096D693E435D14D5AEDF9426FE60F77EECF12955.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

* 通过selectedColor属性设置Toggle打开选中后的背景颜色。

```
Toggle({ type: ToggleType.Button, isOn: true }) {
  Text('status button')
  .fontColor('#182431')
  .fontSize(12)
}.width(100).selectedColor(Color.Pink)
Toggle({ type: ToggleType.Checkbox, isOn: true })
  .selectedColor(Color.Pink)
Toggle({ type: ToggleType.Switch, isOn: true })
  .selectedColor(Color.Pink)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.67975277303320854612047822255134:50001231000000:2800:A7BA0E5642706178AAF7C49DC342187ECCC44149170D30DE17C4D4134B8DBE95.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 通过switchPointColor属性设置Switch类型的圆形滑块颜色，仅对type为ToggleType.Switch生效。

```
Toggle({ type: ToggleType.Switch, isOn: false })
  .switchPointColor(Color.Pink)
Toggle({ type: ToggleType.Switch, isOn: true })
  .switchPointColor(Color.Pink)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.96429584369034224847932645394359:50001231000000:2800:489F4A053400A329AC1CAEECB9AE0677E4FF2E3F7CDBC43E897B5B94265AC219.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

除支持通用事件外，Toggle通常用于选中和取消选中后触发某些操作，可以绑定onChange事件来响应操作后的自定义行为。

```
Toggle({ type: ToggleType.Switch, isOn: false })
  .onChange((isOn: boolean) => {
      if(isOn) {
        // 需要执行的操作
      }
  })
```

## 场景示例

Toggle可用于切换蓝牙开关状态。

```
// xxx.ets
import promptAction from '@ohos.promptAction';
@Entry
@Component
struct ToggleExample {
  build() {
    Column() {
      Row() {
        Text("Bluetooth Mode")
        .height(50)
        .fontSize(16)
      }
      Row() {
        Text("Bluetooth")
          .height(50)
          .padding({left: 10})
          .fontSize(16)
          .textAlign(TextAlign.Start)
          .backgroundColor(0xFFFFFF)
        Toggle({ type: ToggleType.Switch })
          .margin({left: 200, right: 10})
          .onChange((isOn: boolean) => {
            if(isOn) {
              promptAction.showToast({ message: 'Bluetooth is on.' })
            } else {
              promptAction.showToast({ message: 'Bluetooth is off.' })
            }
          })
      }
      .backgroundColor(0xFFFFFF)
    }
    .padding(10)
    .backgroundColor(0xDCDCDC)
    .width('100%')
    .height('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.24657703002271897332137543889719:50001231000000:2800:2BBA9EF7681A4DAA6451E9E6AC0BFE2158CFDDBF6BC2BD8BCEF0C984D68B0C9C.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 进度条（Progress）

更新时间: 2024-01-15 12:19

Progress是进度条显示组件，显示内容通常为某次目标操作的当前进度。具体用法请参考[Progress](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-progress-0000001427584856-V3)。

## 创建进度条

Progress通过调用接口来创建，接口调用形式如下：

```
Progress(options: {value: number, total?: number, type?: ProgressType})
```

该接口用于创建type样式的进度条，其中value用于设置初始进度值，total用于设置进度总长度，type决定Progress样式。

```
Progress({ value: 24, total: 100, type: ProgressType.Linear }) // 创建一个进度总长为100，初始进度值为24的线性进度条
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183858.57769289555107438405777389064934:50001231000000:2800:CA6C35423CD14C282D0B8D26E5E8766975294EA2559B0A25A096110707658F4E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 设置进度条样式

Progress有5种可选类型，在创建时通过设置ProgressType枚举类型给type可选项指定Progress类型。其分别为：ProgressType.Linear（线性样式）、 ProgressType.Ring（环形无刻度样式）、ProgressType.ScaleRing（环形有刻度样式）、ProgressType.Eclipse（圆形样式）和ProgressType.Capsule（胶囊样式）。

* 线性样式进度条（默认类型）

  说明

  从API version9开始，组件高度大于宽度的时候自适应垂直显示，相等时仍然保持水平显示。

```
Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(200).height(50)
Progress({ value: 20, total: 100, type: ProgressType.Linear }).width(50).height(200)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.74892607344261232461461445128449:50001231000000:2800:77BD4029B78561D799A8AEC8CB253DCBE111238D03F054E9B99C23F3B2AB5924.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 环形无刻度样式进度条

```
// 从左往右，1号环形进度条，默认前景色为蓝色，默认strokeWidth进度条宽度为2.0vp
Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
// 从左往右，2号环形进度条
Progress({ value: 40, total: 150, type: ProgressType.Ring }).width(100).height(100)
    .color(Color.Grey)    // 进度条前景色为灰色
    .style({ strokeWidth: 15})    // 设置strokeWidth进度条宽度为15.0vp
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.05153981671267527681468405862277:50001231000000:2800:8EAFA559C2977E3DE2A27DD98D34E0E3E1B03CBBFFEE81253914D00DA5F57C49.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 环形有刻度样式进度条

```
Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条总刻度数为20，刻度宽度为5vp
Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 5 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为5vp
Progress({ value: 20, total: 150, type: ProgressType.ScaleRing }).width(100).height(100)
    .backgroundColor(Color.Black)
    .style({ strokeWidth: 15, scaleCount: 20, scaleWidth: 3 })    // 设置环形有刻度进度条宽度15，总刻度数为20，刻度宽度为3vp
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.62226786515688842004266218036776:50001231000000:2800:08FD48609931EBFD68704428B0F0C5EA19C2F6FCEB7D630226817D85BC67D80F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 圆形样式进度条

```
// 从左往右，1号圆形进度条，默认前景色为蓝色
Progress({ value: 10, total: 150, type: ProgressType.Eclipse }).width(100).height(100)
// 从左往右，2号圆形进度条，指定前景色为灰色
Progress({ value: 20, total: 150, type: ProgressType.Eclipse }).color(Color.Grey).width(100).height(100)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.42477033744202250277186171981344:50001231000000:2800:99E9AAA81186258DD6DA435581AA4BBE072B996992F990A56FD8026D53F04764.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 胶囊样式进度条

  说明

  1、头尾两端圆弧处的进度展示效果与ProgressType.Eclipse样式相同；

  2、中段处的进度展示效果为矩形状长条，与ProgressType.Linear线性样式相似；

  3、组件高度大于宽度的时候自适应垂直显示。

```
Progress({ value: 10, total: 150, type: ProgressType.Capsule }).width(100).height(50)
Progress({ value: 20, total: 150, type: ProgressType.Capsule }).width(50).height(100).color(Color.Grey)
Progress({ value: 50, total: 150, type: ProgressType.Capsule }).width(50).height(100).backgroundColor(Color.Black)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.30662222812426085183035503353677:50001231000000:2800:3D27D44D9226D65700ED5AE4221B3E322A1245C8D8ED86018638A15DCD098392.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 场景示例

更新当前进度值，如应用安装进度条。可通过点击Button增加progressValue，.value()属性将progressValue设置给Progress组件，进度条组件即会触发刷新，更新当前进度。

```
@Entry
@Component
struct ProgressCase1 { 
  @State progressValue: number = 0    // 设置进度条初始值为0
  build() {
    Column() {
      Column() {
        Progress({value:0, total:100, type:ProgressType.Capsule}).width(200).height(50)
          .style({strokeWidth:50}).value(this.progressValue)
        Row().width('100%').height(5)
        Button("进度条+5")
          .onClick(()=>{
            this.progressValue += 5
            if (this.progressValue > 100){
              this.progressValue = 0
            }
          })
      }
    }.width('100%').height('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.42706131621390699036153271157395:50001231000000:2800:59293A225861A9C56E69F3E2A45FF061413BBD81E14411621B3491E9280CCD4D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 文本显示（Text/Span）

更新时间: 2024-01-10 11:33

Text是文本组件，通常用于展示用户的视图，如显示文章的文字。具体用法可参考[Text](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-text-0000001477981201-V3)。

## 创建文本

Text可通过以下两种方式来创建：

* string字符串
```
Text('我是一段文本')
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.93429348121794113363964533464803:50001231000000:2800:B4F99044A8271D5DB3D1B709634820972A5708BBCEC3F89DDF8C71F0C9ECBAE9.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 引用Resource资源资源引用类型可以通过$r创建Resource类型对象，文件位置为/resources/base/element/string.json。

```
Text($r('app.string.module_desc'))
  .baselineOffset(0)
  .fontSize(30)
  .border({ width: 1 })
  .padding(10)
  .width(300)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.92424685450543855036200257527709:50001231000000:2800:D7406C178FB04D518025FFE8A1888357FBB8F1D245C14E089E0FD96009B01AE2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 添加子组件

[Span](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-span-0000001478181409-V3)只能作为Text组件的子组件显示文本内容。可以在一个Text内添加多个Span来显示一段信息，例如产品说明书、承诺书等。

* 创建Span。Span组件需要写到Text组件内，单独写Span组件不会显示信息，Text与Span同时配置文本内容内容时，Span内容覆盖Text内容。

```
Text('我是Text') {
  Span('我是Span')
}
.padding(10)
.borderWidth(1)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.77919587967963993642568719202596:50001231000000:2800:CA7CE04AFD390D4E64E90980D0FA79FBF57933B423A91F3D3DFD31FB3937F697.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 设置文本装饰线及颜色。通过decoration设置文本装饰线及颜色。

```
Text() {
  Span('我是Span1，').fontSize(16).fontColor(Color.Grey)
    .decoration({ type: TextDecorationType.LineThrough, color: Color.Red })
  Span('我是Span2').fontColor(Color.Blue).fontSize(16)
    .fontStyle(FontStyle.Italic)
    .decoration({ type: TextDecorationType.Underline, color: Color.Black })
  Span('，我是Span3').fontSize(16).fontColor(Color.Grey)
    .decoration({ type: TextDecorationType.Overline, color: Color.Green })
}
.borderWidth(1)
.padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.48233267578523794365253382904643:50001231000000:2800:44DA649656316086B06CA1E2B32B273CE08C88A112C30CA6B2E17651475395BE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过textCase设置文字一直保持大写或者小写状态。

```
Text() {
  Span('I am Upper-span').fontSize(12)
    .textCase(TextCase.UpperCase)
}
.borderWidth(1)
.padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.68306206760767372955690251208521:50001231000000:2800:727D4C08C59BF816C431335D12E3FE4BAA3B158DCF2E322228175492BA3ACB20.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 添加事件。由于Span组件无尺寸信息，事件仅支持点击事件onClick。

```
Text() {
  Span('I am Upper-span').fontSize(12)
    .textCase(TextCase.UpperCase)
    .onClick(()=>{
      console.info('我是Span——onClick')
    })
}
```

## 自定义文本样式

* 通过textAlign属性设置文本对齐样式。

```
Text('左对齐')
  .width(300)
  .textAlign(TextAlign.Start)
  .border({ width: 1 })
  .padding(10)
Text('中间对齐')
  .width(300)
  .textAlign(TextAlign.Center)
  .border({ width: 1 })
  .padding(10)
Text('右对齐')
  .width(300)
  .textAlign(TextAlign.End)
  .border({ width: 1 })
  .padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183859.35461854621184576358902865027043:50001231000000:2800:2760D979D312DF05111B44C58913A2FD720AB681D0C680072ACCB1E71FB8D682.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 通过textOverflow属性控制文本超长处理，textOverflow需配合maxLines一起使用（默认情况下文本自动折行）。

```
Text('This is the setting of textOverflow to Clip text content This is the setting of textOverflow to None text content. This is the setting of textOverflow to Clip text content This is the setting of textOverflow to None text content.')
  .width(250)
  .textOverflow({ overflow: TextOverflow.None })
  .maxLines(1)
  .fontSize(12)
  .border({ width: 1 }).padding(10)
Text('我是超长文本，超出的部分显示省略号。I am an extra long text, with ellipses displayed for any excess。')
  .width(250)
  .textOverflow({ overflow: TextOverflow.Ellipsis })
  .maxLines(1)
  .fontSize(12)
  .border({ width: 1 }).padding(10)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.25244512426491378048069280903281:50001231000000:2800:2A9D2E3374CD402343DA71815EBEF1715E6D9F08CAF35B104EC1266D99B449CE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过lineHeight属性设置文本行高。

```
Text('This is the text with the line height set. This is the text with the line height set.')
  .width(300).fontSize(12).border({ width: 1 }).padding(10)
Text('This is the text with the line height set. This is the text with the line height set.')
  .width(300).fontSize(12).border({ width: 1 }).padding(10)
  .lineHeight(20)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.80508978597073240927005799174452:50001231000000:2800:655722990AAD035FD5EA5D4A1BC978D65DA28536E957F18306102669975AA1DB.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过decoration属性设置文本装饰线样式及其颜色。

```
Text('This is the text')
  .decoration({
    type: TextDecorationType.LineThrough,
    color: Color.Red
  })
  .borderWidth(1).padding(10).margin(5)
Text('This is the text')
  .decoration({
    type: TextDecorationType.Overline,
    color: Color.Red
  })
  .borderWidth(1).padding(10).margin(5)
Text('This is the text')
  .decoration({
    type: TextDecorationType.Underline,
    color: Color.Red
  })
  .borderWidth(1).padding(10).margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.81035767760278503071548795344886:50001231000000:2800:6D37F0D3C776D2D5777736A852E765D49F632BFC971F76A4CBA8C53998600BA5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过baselineOffset属性设置文本基线的偏移量。

```
Text('This is the text content with baselineOffset 0.')
  .baselineOffset(0)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
Text('This is the text content with baselineOffset 30.')
  .baselineOffset(30)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)

Text('This is the text content with baselineOffset -20.')
  .baselineOffset(-20)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.36220935520643711697530009641168:50001231000000:2800:B13C408A1DC0166D585ED91796EC154D6427AA0893B4E15E4ED13CCA2381CDEB.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过letterSpacing属性设置文本字符间距。

```
Text('This is the text content with letterSpacing 0.')
  .letterSpacing(0)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
Text('This is the text content with letterSpacing 3.')
  .letterSpacing(3)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
Text('This is the text content with letterSpacing -1.')
  .letterSpacing(-1)
  .fontSize(12)
  .border({ width: 1 })
  .padding(10)
  .width('100%')
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.25095992223348752830318534501455:50001231000000:2800:A01CC27BFAF1251220687B8756B1581F3351171D1DBBA0EAEC339FE492AE73C1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过minFontSize与maxFontSize自适应字体大小，minFontSize设置文本最小显示字号，maxFontSize设置文本最大显示字号，minFontSize与maxFontSize必须搭配同时使用，以及需配合maxline或布局大小限制一起使用，单独设置不生效。

```
Text('我的最大字号为30，最小字号为5，宽度为250，maxLines为1')
  .width(250)
  .maxLines(1)
  .maxFontSize(30)
  .minFontSize(5)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
Text('我的最大字号为30，最小字号为5，宽度为250，maxLines为2')
  .width(250)
  .maxLines(2)
  .maxFontSize(30)
  .minFontSize(5)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
Text('我的最大字号为30，最小字号为15，宽度为250,高度为50')
  .width(250)
  .height(50)
  .maxFontSize(30)
  .minFontSize(15)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
Text('我的最大字号为30，最小字号为15，宽度为250,高度为100')
  .width(250)
  .height(100)
  .maxFontSize(30)
  .minFontSize(15)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.92952318650253509979306874741004:50001231000000:2800:1CC189B1B255B57B4989089BBCE8DE00E7EB56A7CD751980B1A525E1DE2B6B37.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过textCase属性设置文本大小写。

```
Text('This is the text content with textCase set to Normal.')
  .textCase(TextCase.Normal)
  .padding(10)
  .border({ width: 1 })
  .padding(10)
  .margin(5)

// 文本全小写展示
Text('This is the text content with textCase set to LowerCase.')
  .textCase(TextCase.LowerCase)
  .border({ width: 1 })
  .padding(10)
  .margin(5)

// 文本全大写展示
Text('This is the text content with textCase set to UpperCase.')
  .textCase(TextCase.UpperCase)
  .border({ width: 1 })
  .padding(10)
  .margin(5)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.67046622923529261862633076150055:50001231000000:2800:5B3667382BD88B6F0B8F50CC02B390B97929222314B4547AB6A0BDCEDA1FED26.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过copyOption属性设置文本是否可复制粘贴。

```
Text("这是一段可复制文本")
  .fontSize(30)
  .copyOption(CopyOptions.InApp)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.75275001077786483108250391280735:50001231000000:2800:52AE3A08C98393E8F50998FE780B7C763E77839AAE5CCEEFA78FC585A68C12D2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 添加事件

Text组件可以添加通用事件，可以绑定onClick、onTouch等事件来响应操作。

```
Text('点我')
  .onClick(()=>{
      console.info('我是Text的点击响应事件');
   })
```

## 场景示例

```
// xxx.ets
@Entry
@Component
struct TextExample {
  build() {
    Column() {
      Row() {
        Text("1").fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
        Text("我是热搜词条1")
          .fontSize(12)
          .fontColor(Color.Blue)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .fontWeight(300)
        Text("爆")
          .margin({ left: 6 })
          .textAlign(TextAlign.Center)
          .fontSize(10)
          .fontColor(Color.White)
          .fontWeight(600)
          .backgroundColor(0x770100)
          .borderRadius(5)
          .width(15)
          .height(14)
      }.width('100%').margin(5)

      Row() {
        Text("2").fontSize(14).fontColor(Color.Red).margin({ left: 10, right: 10 })
        Text("我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2 我是热搜词条2")
          .fontSize(12)
          .fontColor(Color.Blue)
          .fontWeight(300)
          .constraintSize({ maxWidth: 200 })
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        Text("热")
          .margin({ left: 6 })
          .textAlign(TextAlign.Center)
          .fontSize(10)
          .fontColor(Color.White)
          .fontWeight(600)
          .backgroundColor(0xCC5500)
          .borderRadius(5)
          .width(15)
          .height(14)
      }.width('100%').margin(5)

      Row() {
        Text("3").fontSize(14).fontColor(Color.Orange).margin({ left: 10, right: 10 })
        Text("我是热搜词条3")
          .fontSize(12)
          .fontColor(Color.Blue)
          .fontWeight(300)
          .maxLines(1)
          .constraintSize({ maxWidth: 200 })
          .textOverflow({ overflow: TextOverflow.Ellipsis })
        Text("热")
          .margin({ left: 6 })
          .textAlign(TextAlign.Center)
          .fontSize(10)
          .fontColor(Color.White)
          .fontWeight(600)
          .backgroundColor(0xCC5500)
          .borderRadius(5)
          .width(15)
          .height(14)
      }.width('100%').margin(5)

      Row() {
        Text("4").fontSize(14).fontColor(Color.Grey).margin({ left: 10, right: 10 })
        Text("我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4 我是热搜词条4")
          .fontSize(12)
          .fontColor(Color.Blue)
          .fontWeight(300)
          .constraintSize({ maxWidth: 200 })
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
      }.width('100%').margin(5)
    }.width('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.37405728115610030654692687321589:50001231000000:2800:FF6B1ACE7E8394703159D8A972464EC920589B6378E4FEBD1AC95B65A49AB5B2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 文本输入（TextInput/TextArea）

更新时间: 2024-01-15 12:20

TextInput、TextArea是输入框组件，通常用于响应用户的输入操作，比如评论区的输入、聊天框的输入、表格的输入等，也可以结合其它组件构建功能页面，例如登录注册页面。具体用法参考[TextInput](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-textinput-0000001427584864-V3)、[TextArea](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-textarea-0000001427902464-V3)。

## 创建输入框

TextInput为单行输入框、TextArea为多行输入框。通过以下接口来创建。

```
TextArea(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextAreaController})
```

```
TextInput(value?:{placeholder?: ResourceStr, text?: ResourceStr, controller?: TextInputController})
```

* 单行输入框

```
TextInput()
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183900.60105743670591572432693151922254:50001231000000:2800:D34F5E468BE91ABB83F0D8B7667CBE833F826C653032986F1B35ADE9F70255B2.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 多行输入框

```
TextArea()
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.18787163973979756192018624158969:50001231000000:2800:4EDAF7C46C1E024009A883976D7BA7D1D411DDE3824046878082CF6B0B1A5192.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  多行输入框文字超出一行时会自动折行。

```
TextArea({text:"我是TextArea我是TextArea我是TextArea我是TextArea"}).width(300)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.54124870910132494382915045969135:50001231000000:2800:342C3C6EAA62875216855A64AFA7E9D81E4ADAAA306171634F3EAB0390673209.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 设置输入框类型

TextInput有5种可选类型，分别为Normal基本输入模式、Password密码输入模式、Email邮箱地址输入模式、Number纯数字输入模式、PhoneNumber电话号码输入模式。通过type属性进行设置：

* 基本输入模式（默认类型）

```
TextInput()
  .type(InputType.Normal)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.88243555708157205155533778486989:50001231000000:2800:B54E79DB74C92AA39BC0DB90EA9D008F7987DF67D4AB76A4A366F056A51A31C5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 密码输入模式

```
TextInput()
  .type(InputType.Password)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.57353881986755179431735971058548:50001231000000:2800:C8CD01FF872720462A5501DD6A796FA948BD73512E5C1B66730179A1DF07DA06.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

* 设置无输入时的提示文本。TextInput({placeholder:'我是提示文本'})

```
TextInput({placeholder:'我是提示文本'})
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.71449742475743655727732278465084:50001231000000:2800:14D0F29F147212DF3B3FB5E791F6C6587154148AC2B07FA8AF2526E5E6224DEE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 设置输入框当前的文本内容。

```
TextInput({placeholder:'我是提示文本',text:'我是当前文本内容'})
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.58953168371699324434886289553484:50001231000000:2800:B5B67240785653DB4E60A7FDEA8FF095246F844F1E3C148A458D543D413B7BD6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 添加backgroundColor改变输入框的背景颜色。

```
TextInput({placeholder:'我是提示文本',text:'我是当前文本内容'})
  .backgroundColor(Color.Pink)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.46258544254859938677826376725522:50001231000000:2800:6207A8927B48EEDE7F058FA8BDC4AD955F8840679E89D12CA93B8175916958F1.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  更丰富的样式可以结合[通用属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-size-0000001428061700-V3)实现。

## 添加事件

文本框主要用于获取用户输入的信息，把信息处理成数据进行上传，绑定onChange事件可以获取输入框内改变的内容。用户也可以使用通用事件来进行相应的交互操作。

```
TextInput()
  .onChange((value: string) => {
    console.info(value);
  })
  .onFocus(() => {
    console.info('获取焦点');
  })
```

## 场景示例

用于表单的提交，在用户登录/注册页面，用户的登录或注册的输入操作。

```
@Entry
@Component
struct TextInputSample {
  build() {
    Column() {
      TextInput({ placeholder: 'input your username' }).margin({ top: 20 })
        .onSubmit((EnterKeyType)=>{
          console.info(EnterKeyType+'输入法回车键的类型值')
        })
      TextInput({ placeholder: 'input your password' }).type(InputType.Password).margin({ top: 20 })
        .onSubmit((EnterKeyType)=>{
          console.info(EnterKeyType+'输入法回车键的类型值')
        })
      Button('Sign in').width(150).margin({ top: 20 })
    }.padding(20)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183901.49165210017560003257249200742946:50001231000000:2800:7ACF303A0C57C6E852CA461278472AD4CD6B436183351B664B31195D6261B87F.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 自定义弹窗（CustomDialog）

更新时间: 2024-01-15 12:21

自定义弹窗（CustomDialog）可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹窗。具体用法请参考[自定义弹窗](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-methods-custom-dialog-box-0000001477981237-V3)。

## 创建自定义弹窗

1. 使用@CustomDialog装饰器装饰自定义弹窗。
2. @CustomDialog装饰器用于装饰自定义弹框，此装饰器内进行自定义内容（也就是弹框内容）。

```
@CustomDialog
struct CustomDialogExample {
  controller: CustomDialogController
  build() {
    Column() {
      Text('我是内容')
      .fontSize(20)
      .margin({ top: 10, bottom: 10 })
    }
  }
}
```
3. 创建构造器，与装饰器呼应相连。

```
dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({}),
})
```
4. 点击与onClick事件绑定的组件使弹窗弹出

```
Flex({justifyContent:FlexAlign.Center}){
  Button('click me')
    .onClick(() => {
      this.dialogController.open()
    })
}.width('100%')
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183902.69528997104534762488785087406715:50001231000000:2800:35B794BB3FC0E5DA8F723B4BD4280A9BA976D4F4B209FA2B6633A1BF60032FA7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 弹窗的交互

弹窗可用于数据交互，完成用户一系列响应操作。

1. 在@CustomDialog装饰器内添加按钮操作，同时添加数据函数的创建。

```
@CustomDialog
struct CustomDialogExample {
  controller: CustomDialogController
  cancel: () => void
  confirm: () => void
  build() {
    Column() {
      Text('我是内容').fontSize(20).margin({ top: 10, bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('cancel')
          .onClick(() => {
            this.controller.close()
            this.cancel()
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('confirm')
          .onClick(() => {
            this.controller.close()
            this.confirm()
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })
    }
  }
}
```
2. 页面内需要在构造器内进行接收，同时创建相应的函数操作。

```
dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: this.onCancel,
      confirm: this.onAccept,
    }),
    alignment: DialogAlignment.Default,  // 可设置dialog的对齐方式，设定显示在底部或中间等，默认为底部显示
  })
  onCancel() {
    console.info('Callback when the first button is clicked')
  }
  onAccept() {
    console.info('Callback when the second button is clicked')
  }
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183902.96524827102640941630508613075326:50001231000000:2800:6AE3B260C8CCA829912585271DA7449E69368B0C895CADEBF2FE7BBB04CA52A4.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 完整示例

```
// xxx.ets
@CustomDialog
struct CustomDialogExample {
  controller: CustomDialogController
  cancel: () => void
  confirm: () => void
  build() {
    Column() {
      Text('我是内容').fontSize(20).margin({ top: 10, bottom: 10 })
      Flex({ justifyContent: FlexAlign.SpaceAround }) {
        Button('cancel')
          .onClick(() => {
            this.controller.close()
            this.cancel()
          }).backgroundColor(0xffffff).fontColor(Color.Black)
        Button('confirm')
          .onClick(() => {
            this.controller.close()
            this.confirm()
          }).backgroundColor(0xffffff).fontColor(Color.Red)
      }.margin({ bottom: 10 })
    }
  }
}

@Entry
@Component
struct DialogExample {
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomDialogExample({
      cancel: this.onCancel,
      confirm: this.onAccept,
    }),
    alignment: DialogAlignment.Default,  // 可设置dialog的对齐方式，设定显示在底部或中间等，默认为底部显示
  })
  onCancel() {
    console.info('Callback when the first button is clicked')
  }
  onAccept() {
    console.info('Callback when the second button is clicked')
  }

  build() {
    Flex({ justifyContent: FlexAlign.Center }) {
      Button('click me')
        .onClick(() => {
          this.dialogController.open()
        })
    }.width('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183902.83747573693038569605266854152733:50001231000000:2800:E05CDF2157727C20FB3D70861D78CD5F0E71C8831A67CC03F80D94CCF735370B.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 视频播放（Video）

更新时间: 2024-01-10 11:35

Video组件用于播放视频文件并控制其播放状态，常用于为短视频应用和应用内部视频的列表页面。当视频完整出现时会自动播放，用户点击视频区域则会暂停播放，同时显示播放进度条，通过拖动播放进度条指定视频播放到具体位置。具体用法请参考[Video](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-media-components-video-0000001427902484-V3)。

## 创建视频组件

Video通过调用接口来创建，接口调用形式如下：

```
Video(value: {src?: string | Resource, currentProgressRate?: number | string | PlaybackSpeed, previewUri?: string | PixelMap | Resource, controller?: VideoController})
```

该接口用于创建视频播放组件。其中，src指定视频播放源的路径，加载方式请参考[加载视频资源](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-components-video-player-0000001450594438-V3#section1375516161615)，currentProgressRate用于设置视频播放倍速，previewUri指定视频未播放时的预览图片路径，controller设置视频控制器，用于自定义控制视频。

## 加载视频资源

Video组件支持加载本地视频和网络视频。

### 加载本地视频

* 普通本地视频。加载本地视频时，首先在本地rawfile目录指定对应的文件，如下图所示。

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183902.53066616043652085736172111218107:50001231000000:2800:8531B77925C8D228AA44CEDBA9B415029A0E33E0E21D3E68AAB11639FB72E5F3.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  再使用资源访问符$rawfile()引用视频资源。

```
@Component
export struct VideoPlayer{
   private controller:VideoController;
   private previewUris: Resource = $r ('app.media.preview');
   private innerResource: Resource = $rawfile('videoTest.mp4');
   build(){
     Column() {
       Video({
         src: this.innerResource,
         previewUri: this.previewUris,
         controller: this.controller
       })
   }
 }
}
```

* [Data Ability](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/dataability-overview-0000001428061508-V3)提供的视频路径带有dataability://前缀，使用时确保对应视频资源存在即可。
```
@Component
export struct VideoPlayer{
   private controller:VideoController;
   private previewUris: Resource = $r ('app.media.preview');
   private videosrc: string= 'dataability://device_id/com.domainname.dataability.videodata/video/10'
   build(){
     Column() {
       Video({
         src: this.videosrc,
         previewUri: this.previewUris,
         controller: this.controller
       })
   }
 }
}
```

### 加载沙箱路径视频

支持file:///data/storage路径前缀的字符串，用于读取应用沙箱路径内的资源。需要保证应用沙箱目录路径下的文件存在并且有可读权限。

```
@Component
export struct VideoPlayer {
  private controller: VideoController;
  private videosrc: string = 'file:///data/storage/el2/base/haps/entry/files/show.mp4'

  build() {
    Column() {
      Video({
        src: this.videosrc,
        controller: this.controller
      })
    }
  }
}
```

### 加载网络视频

加载网络视频时，需要申请权限ohos.permission.INTERNET，具体申请方式请参考[权限申请声明](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/accesstoken-guidelines-0000001493744016-V3)。此时，Video的src属性为网络视频的链接。

```
@Component
export struct VideoPlayer{
   private controller:VideoController;
   private previewUris: Resource = $r ('app.media.preview');
   private videosrc: string= 'https://www.example.com/example.mp4' // 使用时请替换为实际视频加载网址
   build(){
     Column() {
       Video({
         src: this.videosrc,
         previewUri: this.previewUris,
         controller: this.controller
       })
   }
 }
}
```

## 添加属性

Video组件[属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-media-components-video-0000001427902484-V3#ZH-CN_TOPIC_0000001573929037__%E5%B1%9E%E6%80%A7)主要用于设置视频的播放形式。例如设置视频播放是否静音、播放时是否显示控制条等。

```
@Component
export struct VideoPlayer {
  private controller: VideoController;

  build() {
    Column() {
      Video({
        controller: this.controller
      })
        .muted(false) //设置是否静音
        .controls(false) //设置是否显示默认控制条
        .autoPlay(false) //设置是否自动播放
        .loop(false) //设置是否循环播放
        .objectFit(ImageFit.Contain) //设置视频适配模式
    }
  }
}
```

## 事件调用

Video组件回调事件主要为播放开始、暂停结束、播放失败、视频准备和操作进度条等事件，除此之外，Video组件也支持通用事件的调用，如点击、触摸等事件的调用。详细的事件请参考[事件说明](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-media-components-video-0000001427902484-V3#ZH-CN_TOPIC_0000001573929037__%E4%BA%8B%E4%BB%B6)。

```
@Entry
@Component
struct VideoPlayer{
  private controller:VideoController;
  private previewUris: Resource = $r ('app.media.preview');
  private innerResource: Resource = $rawfile('videoTest.mp4');
  build(){
    Column() {
      Video({
        src: this.innerResource,
        previewUri: this.previewUris,
        controller: this.controller
      })
        .onUpdate((event) => {   //更新事件回调
          console.info("Video update.");
        })
        .onPrepared((event) => {  //准备事件回调
          console.info("Video prepared.");
        })
        .onError(() => {          //失败事件回调
          console.info("Video error.");
        })
    }
  }
}
```

## Video控制器使用

Video控制器主要用于控制视频的状态，包括播放、暂停、停止以及设置进度等，详细的使用请参考[VideoController使用说明](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-media-components-video-0000001427902484-V3#ZH-CN_TOPIC_0000001573929037__videocontroller)。

* 默认控制器默认的控制器支持视频的开始、暂停、进度调整、全屏显示四项基本功能。

```
@Entry
@Component
struct VideoGuide {
  @State videoSrc: Resource = $rawfile('videoTest.mp4')
  @State previewUri: string = 'common/videoIcon.png'
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X
    build() {
    Row() {
      Column() {
        Video({
          src: this.videoSrc,
          previewUri: this.previewUri,
          currentProgressRate: this.curRate
        })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
* 自定义控制器
  使用自定义的控制器，先将默认控制器关闭掉，之后可以使用button以及slider等组件进行自定义的控制与显示，适合自定义较强的场景下使用。

```
@Entry
@Component
struct VideoGuide {
  @State videoSrc: Resource = $rawfile('videoTest.mp4')
  @State previewUri: string = 'common/videoIcon.png'
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X
  @State isAutoPlay: boolean = false
  @State showControls: boolean = true
  @State sliderStartTime: string = '';
  @State currentTime: number = 0;
  @State durationTime: number = 0;
  @State durationStringTime: string ='';
  controller: VideoController = new VideoController()

  build() {
    Row() {
      Column() {
        Video({
          src: this.videoSrc,
          previewUri: this.previewUri,
          currentProgressRate: this.curRate,
          controller: this.controller
        }).controls(false).autoPlay(true)
        .onPrepared((event)=>{
          this.durationTime = event.duration
        })
        .onUpdate((event)=>{
          this.currentTime =event.time
        })
        Row() {
          Text(JSON.stringify(this.currentTime) + 's')
          Slider({
            value: this.currentTime,
            min: 0,
            max: this.durationTime
          })
          .onChange((value: number, mode: SliderChangeMode) => {
              this.controller.setCurrentTime(value);
            }).width("90%")
          Text(JSON.stringify(this.durationTime) + 's')
        }
        .opacity(0.8)
        .width("100%")
      }
      .width('100%')
    }
    .height('40%')
  }
}
```

## 其他说明

Video组件已经封装好了视频播放的基础能力，开发者无需进行视频实例的创建，视频信息的设置获取，只需要设置数据源以及基础信息即可播放视频，相对扩展能力较弱。如果开发者想自定义视频播放，还请参考[媒体系统播放音视频](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/av-overview-0000001488951497-V3)。



# XComponent

更新时间: 2024-01-15 12:21

[XComponent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-xcomponent-0000001427902468-V3)组件作为一种绘制组件，通常用于满足开发者较为复杂的自定义绘制需求，例如相机预览流的显示和游戏画面的绘制。

其可通过指定其type字段来实现不同的功能，主要有两个"surface"和"component"字段可供选择。

对于"surface"类型，开发者可将相关数据传入XComponent单独拥有的"[NativeWindow](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/native-window-guidelines-0000001493584172-V3)"来渲染画面。

对于"component"类型则主要用于实现动态加载显示内容的目的。

## surface类型

XComponent设置为surface类型时通常用于EGL/OpenGLES和媒体数据写入，并将其显示在XComponent组件上。

设置为"surface"类型时XComponent组件可以和其他组件一起进行布局和渲染。

同时XComponent又拥有单独的"NativeWindow"，可以为开发者在native侧提供native window用来创建EGL/OpenGLES环境，进而使用标准的OpenGL ES开发。

除此之外，媒体相关应用（视频、相机等）也可以将相关数据写入XComponent所提供的NativeWindow，从而实现呈现相应画面。

## 使用EGL/OpenGLES渲染

### native侧代码开发要点

HarmonyOS的应用如果要通过js来桥接native，一般需要使用napi接口来处理js交互，XComponent同样不例外，具体使用请参考[Native API在应用工程中的使用指导](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/napi-guidelines-0000001493903956-V3)。

Native侧处理js逻辑的文件类型为so：

* 每个模块对应一个so
* so的命名规则为 lib{模块名}.so

对于使用XComponent进行标准OpenGL ES开发的场景，CMAKELists.txt文件内容大致如下：

```
cmake_minimum_required(VERSION 3.4.1)
project(XComponent) # 项目名称

set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})
# 头文件查找路径
include_directories(${NATIVERENDER_ROOT_PATH}
                    ${NATIVERENDER_ROOT_PATH}/include
                    )

# 编译目标so，SHARED表示动态库
add_library(nativerender SHARED
            xxx.cpp
            )

# 查找相关库 (包括OpenGL ES相关库和XComponent提供的ndk接口)
find_library( EGL-lib
              EGL )

find_library( GLES-lib
              GLESv3 )

find_library( libace-lib
              ace_ndk.z )

# 编译so所需要的依赖
target_link_libraries(nativerender PUBLIC ${EGL-lib} ${GLES-lib} ${libace-lib} libace_napi.z.so libc++.a)
```

### Napi模块注册

```
static napi_value Init(napi_env env, napi_value exports)
{
    // 定义暴露在模块上的方法
    napi_property_descriptor desc[] ={
        DECLARE_NAPI_FUNCTION("changeColor", PluginRender::NapiChangeColor),
    };
    // 通过此接口开发者可在exports上挂载native方法（即上面的PluginRender::NapiChangeColor），exports会通过js引擎绑定到js层的一个js对象
    NAPI_CALL(env, napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc));
    return exports;
}

static napi_module nativerenderModule = {
    .nm_version = 1,
    .nm_flags = 0,
    .nm_filename = nullptr,
    .nm_register_func = Init, // 指定加载对应模块时的回调函数
    .nm_modname = "nativerender", // 指定模块名称，对于XComponent相关开发，这个名称必须和ArkTS侧XComponent中libraryname的值保持一致
    .nm_priv = ((void*)0),
    .reserved = { 0 },
};

extern "C" __attribute__((constructor)) void RegisterModule(void)
{
    // 注册so模块
    napi_module_register(&nativerenderModule);
}
```

### 解析XComponent组件的NativeXComponent实例

NativeXComponent为XComponent提供了在native层的实例，可作为js层和native层XComponent绑定的桥梁。XComponent所提供的的NDK接口都依赖于该实例。具体NDK接口可参考[Native XComponent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/_o_h___native_x_component-0000001497210885-V3)。

可以在模块被加载时的回调内（即[Napi模块注册](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-components-xcomponent-0000001504835025-V3#section58354181516)中的Init函数）解析获得NativeXComponent实例

```
{
    // ...
    napi_status status;
    napi_value exportInstance = nullptr;
    OH_NativeXComponent *nativeXComponent = nullptr;
    // 用来解析出被wrap了NativeXComponent指针的属性
    status = napi_get_named_property(env, exports, OH_NATIVE_XCOMPONENT_OBJ, &exportInstance);
    if (status != napi_ok) {
        return false;
    }
    // 通过napi_unwrap接口，解析出NativeXComponent的实例指针
    status = napi_unwrap(env, exportInstance, reinterpret_cast<void**>(&nativeXComponent));
    // ...
}
```

### 注册XComponent事件回调

依赖[解析XComponent组件的NativeXComponent实例](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-components-xcomponent-0000001504835025-V3#section109791557151518)拿到的NativeXComponent指针，通过OH_NativeXComponent_RegisterCallback接口进行回调注册

```
{
    ...
    OH_NativeXComponent *nativeXComponent = nullptr;
    // 解析出NativeXComponent实例

    OH_NativeXComponent_Callback callback;
    callback->OnSurfaceCreated = OnSurfaceCreatedCB; // surface创建成功后触发，开发者可以从中获取native window的句柄
    callback->OnSurfaceChanged = OnSurfaceChangedCB; // surface发生变化后触发，开发者可以从中获取native window的句柄以及XComponent的变更信息
    callback->OnSurfaceDestroyed = OnSurfaceDestroyedCB; // surface销毁时触发，开发者可以在此释放资源
    callback->DispatchTouchEvent = DispatchTouchEventCB; // XComponent的touch事件回调接口，开发者可以从中获得此次touch事件的信息

    OH_NativeXComponent_RegisterCallback(nativeXComponent, callback);
    ...
}
```

### 创建EGL/OpenGLES环境

在注册的OnSurfaceCreated回调中开发者能拿到native window的句柄（其本质就是XComponent所单独拥有的NativeWindow），因此可以在这里创建应用自己的EGL/OpenGLES开发环境，由此开始具体渲染逻辑的开发。

```
EGLCore* eglCore_; // EGLCore为封装了OpenGL相关接口的类
uint64_t width_;
uint64_t height_;
void OnSurfaceCreatedCB(OH_NativeXComponent* component, void* window)
{
    int32_t ret = OH_NativeXComponent_GetXComponentSize(component, window, &width_, &height_);
    if (ret === OH_NATIVEXCOMPONENT_RESULT_SUCCESS) {
        eglCore_->GLContextInit(window, width_, height_); // 初始化OpenGL环境
    }
}
```

### ArkTS侧语法介绍

开发者在ArkTS侧使用如下代码即可用XComponent组件进行利用EGL/OpenGLES渲染的开发。

```
XComponent({ id: 'xcomponentId1', type: 'surface', libraryname: 'nativerender' })
  .onLoad((context) => {})
  .onDestroy(() => {})
```

* id : 与XComponent组件为一一对应关系，不可重复。通常开发者可以在native侧通过OH_NativeXComponent_GetXComponentId接口来获取对应的id从而绑定对应的XComponent。
* libraryname：加载模块的名称，必须与在native侧Napi模块注册时nm_modname的名字一致。

  说明

  应用加载模块实现跨语言调用有两种方式：1. 使用NAPI的import方式加载：

  <pre class="screen prettyprint linenums hljs coffeescript"><div class="sun"></div><div class="copybtn"></div><ol class="linenums"><li><p>import nativerender from "libnativerender.so"</p></li></ol></pre>

  1. 使用XComponent组件加载，本质也是使用了NAPI机制来加载。该加载方式和import加载方式的区别在于，在加载动态库是会将XComponent的NativeXComponent实例暴露到应用的native层中，从而让开发者可以使用XComponent的NDK接口。
* onLoad事件

  * 触发时刻：XComponent准备好surface后触发。
  * 参数context：其上面挂载了暴露在模块上的native方法，使用方法类似于利用 import context2 from "libnativerender.so" 直接加载模块后获得的context2实例。
  * 时序：onLoad事件的触发和Surface相关，其和native侧的OnSurfaceCreated的时序如下图：![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183903.12548533737570165123857886225487:50001231000000:2800:9967BCCC6161C58577EA3A57B2DB0B52ACE7B717E0DA48E43043D2892D5BAD9B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* onDestroy事件触发时刻：XComponent组件被销毁时触发与一般ArkUI的组件销毁时机一致，其和native侧的OnSurfaceDestroyed的时序如下图：

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183903.39425274551570397179915515923335:50001231000000:2800:9CE16121805C1611016FA81DB3537A24C3A4F02F9F0E85B4DB8840D98C3565A7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### 媒体数据写入

XComponent所持有的NativeWindow符合"生产者-消费者"模型

HarmonyOS上Camera、AVPlayer等符合生产者设计的部件都可以将数据写入XComponent持有的NativeWindow并通过XComponent显示。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183903.96230688332081981040429196695933:50001231000000:2800:B497167DC3A8B2AF87BA8FB33D7D2E81B6699F1CA2D5D4FBD7A4A14756414F8B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

开发者可通过绑定XComponentController获得对应XComponent的surfaceId（该id可以唯一确定一个surface），从而传给相应的部件接口。

```
@State surfaceId:string = "";
mXComponentController: XComponentController = new XComponentController();
XComponent({ id: '', type: 'surface', controller: this.mXComponentController })
  .onLoad(() => {
    this.surfaceId = this.mXComponentController.getXComponentSurfaceId()
  })
```

具体部件接口可参考： [VideoPlayer](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-media-0000001427902672-V3#ZH-CN_TOPIC_0000001523488666__avplayer9)、 等。

### component类型

XComponent设置为component类型时通常用于在XComponent内部执行非UI逻辑以实现动态加载显示内容的目的。

说明

type为"component"时，XComponent作为容器，子组件沿垂直方向布局：

* 垂直方向上对齐格式：[FlexAlign](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__flexalign).Start
* 水平方向上对齐格式：[FlexAlign](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__flexalign).Center

不支持所有的事件响应。

布局方式更改和事件响应均可通过挂载子组件来设置。

内部所写的非UI逻辑需要封装在一个或多个函数内。

### 场景示例

```
@Builder
function addText(label: string): void {
  Text(label)
    .fontSize(40)
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello XComponent'
  @State messageCommon: string = 'Hello World'
  build() {
    Row() {
      Column() {
        XComponent({ id: 'xcomponentId-container', type: 'component' }) {
          addText(this.message)
          Divider()
            .margin(4)
            .strokeWidth(2)
            .color('#F1F3F5')
            .width("80%")
          Column() {
            Text(this.messageCommon)
              .fontSize(30)
          }
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183903.46121716272673628919286574423439:50001231000000:2800:15527E238E75DFACE7AF50F0D2BA4F64876C5AFD30690A6C2948620D3E32D4FE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 相关实例

针对XComponent，有以下示例工程可供参考：

* [Native XComponent组件的使用（ArkTS）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/codelabs-0000001443855957-V3?catalogVersion=V3)



# 气泡提示（Popup）

更新时间: 2024-01-15 12:18

Popup属性可绑定在组件上显示气泡弹窗提示，设置弹窗内容、交互逻辑和显示状态。主要用于屏幕录制、信息弹出提醒等显示状态。

气泡分为两种类型，一种是系统提供的气泡[PopupOptions](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-popup-0000001427744792-V3#ZH-CN_TOPIC_0000001574088285__popupoptions%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E)，一种是开发者可以自定义的气泡[CustomPopupOptions](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-popup-0000001427744792-V3#ZH-CN_TOPIC_0000001574088285__custompopupoptions8%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E)。其中PopupOptions为系统提供的气泡，通过配置primaryButton、secondaryButton来设置带按钮的气泡。CustomPopupOptions通过配置[builder](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-builder-0000001524176981-V3)参数来设置自定义的气泡。

## 文本提示气泡

文本提示气泡常用于只展示带有文本的信息提示，不带有任何交互的场景。Popup属性需绑定组件，当bindPopup属性中参数show为true的时候会弹出气泡提示。

在Button组件上绑定Popup属性，每次点击Button按钮，handlePopup会切换布尔值，当其为true时，触发bindPopup弹出气泡。

```
@Entry
@Component
struct PopupExample {
  @State handlePopup: boolean = false
 
  build() {
    Column() {
      Button('PopupOptions')
        .onClick(() => {
          this.handlePopup = !this.handlePopup
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
        })
    }.width('100%').padding({ top: 5 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183904.19517242966863594578564023642145:50001231000000:2800:5B7AA152AD27042261805C501E11F688BE5FF54AD24C1CACE2D2169DDD95BD59.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 带按钮的提示气泡

通过primaryButton、secondaryButton属性为气泡最多设置两个Button按钮，通过此按钮进行简单的交互；开发者可以通过配置action参数来设置想要触发的操作。

```
@Entry
@Component
struct PopupExample22 {
  @State handlePopup: boolean = false
  build() {
    Column() {
      Button('PopupOptions').margin({top:200})
        .onClick(() => {
          this.handlePopup = !this.handlePopup
        })
        .bindPopup(this.handlePopup, {
          message: 'This is a popup with PopupOptions',
          primaryButton:{
            value:'Confirm',
            action: () => {
              this.handlePopup = !this.handlePopup
              console.info('confirm Button click')
            }
          },
          secondaryButton: {
            value: 'Cancel',
            action: () => {
              this.handlePopup = !this.handlePopup
            }
          },
        })
    }.width('100%').padding({ top: 5 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183904.02153846131861124183699977303261:50001231000000:2800:777B723D73F6FD70F63B394B3DB4E43B612EEF73C661ABC22AE94EF8D4656D32.jpeg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 自定义气泡

开发者可以使用构建器CustomPopupOptions创建自定义气泡，@Builder中可以放自定义的内容。除此之外，还可以通过popupColor等参数控制气泡样式。

```
@Entry
@Component
struct Index {
  @State customPopup: boolean = false
  // popup构造器定义弹框内容
  @Builder popupBuilder() {
    Row({ space: 2 }) {
      Image($r("app.media.icon")).width(24).height(24).margin({ left: 5 })
      Text('This is Custom Popup').fontSize(15)
    }.width(200).height(50).padding(5)
  }
  build() {
    Column() {
      Button('CustomPopupOptions')
        .position({x:100,y:200})
        .onClick(() => {
          this.customPopup = !this.customPopup
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder, // 气泡的内容
          placement:Placement.Bottom, // 气泡的弹出位置
          popupColor:Color.Pink // 气泡的背景色
        })
    }
    .height('100%')
  }
}
```

使用者通过配置placement参数将弹出的气泡放到需要提示的位置。弹窗构造器会触发弹出提示信息，来引导使用者完成操作，也让使用者有更好的UI体验。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183904.95488649107231906551153282928459:50001231000000:2800:8751C5DE4B25608D937FD2F92F2EB5300795B8B8421D6685BC5E3DFB88CC84A8.jpeg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
@Entry
@Component
struct Index {
  @State customPopup: boolean = false
  // popup构造器定义弹框内容
  @Builder popupBuilder() {
    Row({ space: 2 }) {
      Image('/images/shengWhite.png').width(30).objectFit(ImageFit.Contain)
      Column(){
        Text('控制人生').fontSize(14).fontWeight(900).fontColor(Color.White).width('100%')
        Text('想要跟唱时，数千万歌曲任你选择，人声随心调整。').fontSize(12).fontColor('#ffeeeeee').width('100%')
      }
    }.width(230).height(80).padding(5)
  }
  build() {
    Row() {
      Text('我要K歌')
      Image('/images/sheng.png').width(35).objectFit(ImageFit.Contain)
        .onClick(() => {
          this.customPopup = !this.customPopup
        })
        .bindPopup(this.customPopup, {
          builder: this.popupBuilder,
        })
    }
    .margin(20)
    .height('100%')
  }
}
```



# 菜单（Menu）

更新时间: 2024-01-15 12:19

Menu是菜单接口，一般用于鼠标右键弹窗、点击弹窗等。具体用法请参考[Menu控制](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-menu-0000001478181385-V3)。

## 创建默认样式的菜单

菜单需要调用bindMenu接口来实现。bindMenu响应绑定组件的点击事件，绑定组件后手势点击对应组件后即可弹出。

```
Button('click for Menu')
  .bindMenu([
  {
    value: 'Menu1',
    action: () => {
      console.info('handle Menu1 select')
    }
  }       
])
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183905.40511566953596291238964381582142:50001231000000:2800:E81EE9DF00C6669728AD4F0B75EF0162B09C7A5E910732CC0B151FE00D056A20.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 创建自定义样式的菜单

当默认样式不满足开发需求时，可使用[@Builder](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-builder-0000001524176981-V3)自定义菜单内容。可通过bindMenu接口进行菜单的自定义。

### @Builder开发菜单内的内容

```
@State select: boolean = true
private iconStr: ResourceStr = $r("app.media.view_list_filled")
private iconStr2: ResourceStr = $r("app.media.view_list_filled")
@Builder
SubMenu() {
  Menu() {
    MenuItem({ content: "复制", labelInfo: "Ctrl+C" })
    MenuItem({ content: "粘贴", labelInfo: "Ctrl+V" })
  }
}

@Builder
MyMenu(){
  Menu() {
    MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" })
    MenuItem({ startIcon: $r("app.media.icon"), content: "菜单选项" }).enabled(false)
    MenuItem({
      startIcon: this.iconStr,
      content: "菜单选项",
      endIcon: $r("app.media.arrow_right_filled"),
      // 当builder参数进行配置时，表示与menuItem项绑定了子菜单。鼠标hover在该菜单项时，会显示子菜单。
      builder: this.SubMenu.bind(this),
    })
    MenuItemGroup({ header: '小标题' }) {
      MenuItem({ content: "菜单选项" })
        .selectIcon(true)
        .selected(this.select)
        .onChange((selected) => {
       console.info("menuItem select" + selected);
       this.iconStr2 = $r("app.media.icon");
        })
      MenuItem({
        startIcon: $r("app.media.view_list_filled"),
        content: "菜单选项",
        endIcon: $r("app.media.arrow_right_filled"),
        builder: this.SubMenu.bind(this)
      })
    }
    MenuItem({
      startIcon: this.iconStr2,
      content: "菜单选项",
      endIcon: $r("app.media.arrow_right_filled")
    })
  }
}
  
```

### bindMenu属性绑定组件

```
Button('click for Menu')
  .bindMenu(this.MyMenu)
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183905.36052184371897385374404162132496:50001231000000:2800:AB20C65B3B30FE1BD3E41AF4FC650E8952E4D36CC44E0B385904A17658053995.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 创建支持右键或长按的菜单

通过bindContextMenu接口进行菜单的自定义及菜单弹出的触发方式：右键或长按。使用bindContextMenu弹出的菜单项是在独立子窗口内的，可显示在应用窗口外部。

* @Builder开发菜单内的内容与上文写法相同。
* 确认菜单的弹出方式，使用bindContextMenu属性绑定组件。示例中为右键弹出菜单。
```
Button('click for Menu')
  .bindContextMenu(this.MyMenu, ResponseType.RightClick)
```



# 页面路由（router）

更新时间: 2024-01-10 11:31

页面路由指在应用程序中实现不同页面之间的跳转和数据传递。HarmonyOS提供了Router模块，通过不同的url地址，可以方便地进行页面路由，轻松地访问不同的页面。本文将从[页面跳转](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#section6414655195312)、[页面返回](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E9%A1%B5%E9%9D%A2%E8%BF%94%E5%9B%9E)和[页面返回前增加一个询问框](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E9%A1%B5%E9%9D%A2%E8%BF%94%E5%9B%9E%E5%89%8D%E5%A2%9E%E5%8A%A0%E4%B8%80%E4%B8%AA%E8%AF%A2%E9%97%AE%E6%A1%86)几个方面介绍Router模块提供的功能。

## 页面跳转

页面跳转是开发过程中的一个重要组成部分。在使用应用程序时，通常需要在不同的页面之间跳转，有时还需要将数据从一个页面传递到另一个页面。

图1 页面跳转
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183905.73177245914949934193787529304382:50001231000000:2800:503A6766708ADAB864585E3F4E77E1421222401D579D3CC78FBFCBE3F7C96221.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

Router模块提供了两种跳转模式，分别是[router.pushUrl()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerpushurl9)和[router.replaceUrl()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerreplaceurl9)。这两种模式决定了目标页是否会替换当前页。

* router.pushUrl()：目标页不会替换当前页，而是压入页面栈。这样可以保留当前页的状态，并且可以通过返回键或者调用[router.back()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerback)方法返回到当前页。
* router.replaceUrl()：目标页会替换当前页，并销毁当前页。这样可以释放当前页的资源，并且无法返回到当前页。

说明

页面栈的最大容量为32个页面。如果超过这个限制，可以调用[router.clear()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerclear)方法清空历史页面栈，释放内存空间。

同时，Router模块提供了两种实例模式，分别是Standard和Single。这两种模式决定了目标url是否会对应多个实例。

* Standard：标准实例模式，也是默认情况下的实例模式。每次调用该方法都会新建一个目标页，并压入栈顶。
* Single：单实例模式。即如果目标页的url在页面栈中已经存在同url页面，则离栈顶最近的同url页面会被移动到栈顶，并重新加载；如果目标页的url在页面栈中不存在同url页面，则按照标准模式跳转。

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

```
import router from '@ohos.router';
```

* 场景一：有一个主页（Home）和一个详情页（Detail），希望从主页点击一个商品，跳转到详情页。同时，需要保留主页在页面栈中，以便返回时恢复状态。这种场景下，可以使用pushUrl()方法，并且使用Standard实例模式（或者省略）。

```
// 在Home页面中
function onJumpClick(): void {
  router.pushUrl({
    url: 'pages/Detail' // 目标url
  }, router.RouterMode.Standard, (err) => {
    if (err) {
      console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke pushUrl succeeded.');
  });
}
```

  说明

  标准实例模式下，router.RouterMode.Standard参数可以省略。
* 场景二：有一个登录页（Login）和一个个人中心页（Profile），希望从登录页成功登录后，跳转到个人中心页。同时，销毁登录页，在返回时直接退出应用。这种场景下，可以使用replaceUrl()方法，并且使用Standard实例模式（或者省略）。

```
// 在Login页面中
function onJumpClick(): void {
  router.replaceUrl({
    url: 'pages/Profile' // 目标url
  }, router.RouterMode.Standard, (err) => {
    if (err) {
      console.error(`Invoke replaceUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke replaceUrl succeeded.');
  })
}
```

  说明

  标准实例模式下，router.RouterMode.Standard参数可以省略。
* 场景三：有一个设置页（Setting）和一个主题切换页（Theme），希望从设置页点击主题选项，跳转到主题切换页。同时，需要保证每次只有一个主题切换页存在于页面栈中，在返回时直接回到设置页。这种场景下，可以使用pushUrl()方法，并且使用Single实例模式。

```
// 在Setting页面中
function onJumpClick(): void {
  router.pushUrl({
    url: 'pages/Theme' // 目标url
  }, router.RouterMode.Single, (err) => {
    if (err) {
      console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke pushUrl succeeded.');
  });
}
```
* 场景四：有一个搜索结果列表页（SearchResult）和一个搜索结果详情页（SearchDetail），希望从搜索结果列表页点击某一项结果，跳转到搜索结果详情页。同时，如果该结果已经被查看过，则不需要再新建一个详情页，而是直接跳转到已经存在的详情页。这种场景下，可以使用replaceUrl()方法，并且使用Single实例模式。

```
// 在SearchResult页面中
function onJumpClick(): void {
  router.replaceUrl({
    url: 'pages/SearchDetail' // 目标url
  }, router.RouterMode.Single, (err) => {
    if (err) {
      console.error(`Invoke replaceUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke replaceUrl succeeded.');})
}
```

以上是不带参数传递的场景。

如果需要在跳转时传递一些数据给目标页，则可以在调用Router模块的方法时，添加一个params属性，并指定一个对象作为参数。例如：

```
class DataModelInfo {
  age: number;
}

class DataModel {
  id: number;
  info: DataModelInfo;
}

function onJumpClick(): void {
  // 在Home页面中
  let paramsInfo: DataModel = {
    id: 123,
    info: {
      age: 20
    }
  };

  router.pushUrl({
    url: 'pages/Detail', // 目标url
    params: paramsInfo // 添加params属性，传递自定义参数
  }, (err) => {
    if (err) {
      console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info('Invoke pushUrl succeeded.');
  })
}
```

在目标页中，可以通过调用Router模块的[getParams()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routergetparams)方法来获取传递过来的参数。例如：

```
const params = router.getParams(); // 获取传递过来的参数对象
const id = params['id']; // 获取id属性的值
const age = params['info'].age; // 获取age属性的值
```

## 页面返回

当用户在一个页面完成操作后，通常需要返回到上一个页面或者指定页面，这就需要用到页面返回功能。在返回的过程中，可能需要将数据传递给目标页，这就需要用到数据传递功能。

图2 页面返回
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183906.98169907922746313941789656678279:50001231000000:2800:750DFB10201E55052720342F37DD77D813F5AFEE19EB5B6EAFC6262F5A8144F4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

<pre class="ts prettyprint linenums hljs typescript"><div class="sun"></div><div class="copybtn"></div><ol class="linenums"><li><p>import router from '@ohos.router';</p></li></ol></pre>

可以使用以下几种方式进行页面返回：

* 方式一：返回到上一个页面。

```
import router from '@ohos.router';
```

  这种方式会返回到上一个页面，即上一个页面在页面栈中的位置。但是，上一个页面必须存在于页面栈中才能够返回，否则该方法将无效。
* 方式二：返回到指定页面。

```
router.back();
```

  这种方式可以返回到指定页面，需要指定目标页的路径。目标页必须存在于页面栈中才能够返回。
* 方式三：返回到指定页面，并传递自定义参数信息。

```
router.back({
  url: 'pages/Home',
  params: {
    info: '来自Home页'
  }
});
```

  这种方式不仅可以返回到指定页面，还可以在返回的同时传递自定义参数信息。这些参数信息可以在目标页中通过调用router.getParams()方法进行获取和解析。

在目标页中，在需要获取参数的位置调用router.getParams()方法即可，例如在[onPageShow()生命周期](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-page-custom-components-lifecycle-0000001524296665-V3)回调中：

```
onPageShow() {
  const params = router.getParams(); // 获取传递过来的参数对象
  const info = params['info']; // 获取info属性的值
}
```

说明

当使用router.back()方法返回到指定页面时，该页面会被重新压入栈顶，而原栈顶页面（包括）到指定页面（不包括）之间的所有页面栈都将被销毁。

另外，如果使用router.back()方法返回到原来的页面，原页面不会被重复创建，因此使用@State声明的变量不会重复声明，也不会触发页面的aboutToAppear()生命周期回调。如果需要在原页面中使用返回页面传递的自定义参数，可以在需要的位置进行参数解析。例如，在onPageShow()生命周期回调中进行参数解析。

## 页面返回前增加一个询问框

在开发应用时，为了避免用户误操作或者丢失数据，有时候需要在用户从一个页面返回到另一个页面之前，弹出一个询问框，让用户确认是否要执行这个操作。

本文将从[系统默认询问框](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E7%B3%BB%E7%BB%9F%E9%BB%98%E8%AE%A4%E8%AF%A2%E9%97%AE%E6%A1%86)和[自定义询问框](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-routing-0000001503325125-V3#ZH-CN_TOPIC_0000001523968678__%E8%87%AA%E5%AE%9A%E4%B9%89%E8%AF%A2%E9%97%AE%E6%A1%86)两个方面来介绍如何实现页面返回前增加一个询问框的功能。

图3 页面返回前增加一个询问框
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183906.55033134735560264295205914009821:50001231000000:2800:53C6371D78ACF3FA5771C3FADB77105A997374E6982A4B6A6641E66A5E21B10A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### 系统默认询问框

为了实现这个功能，可以使用页面路由Router模块提供的两个方法：[router.showAlertBeforeBackPage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routershowalertbeforebackpage9)和[router.back()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerback)来实现这个功能。

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

```
import router from '@ohos.router';
```

如果想要在目标界面开启页面返回询问框，需要在调用[router.back()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routerback)方法之前，通过调用[router.showAlertBeforeBackPage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-router-0000001478061893-V3#ZH-CN_TOPIC_0000001523808578__routershowalertbeforebackpage9)方法设置返回询问框的信息。例如，在支付页面中定义一个返回按钮的点击事件处理函数：

```
// 定义一个返回按钮的点击事件处理函数
function onBackClick(): void {
  // 调用router.showAlertBeforeBackPage()方法，设置返回询问框的信息
  try {
    router.showAlertBeforeBackPage({
      message: '您还没有完成支付，确定要返回吗？' // 设置询问框的内容
    });
  } catch (err) {
    console.error(`Invoke showAlertBeforeBackPage failed, code is ${err.code}, message is ${err.message}`);
  }

  // 调用router.back()方法，返回上一个页面
  router.back();
}
```

其中，router.showAlertBeforeBackPage()方法接收一个对象作为参数，该对象包含以下属性：

* message：string类型，表示询问框的内容。如果调用成功，则会在目标界面开启页面返回询问框；如果调用失败，则会抛出异常，并通过err.code和err.message获取错误码和错误信息。

  当用户点击“返回”按钮时，会弹出确认对话框，询问用户是否确认返回。选择“取消”将停留在当前页目标页；选择“确认”将触发router.back()方法，并根据参数决定如何执行跳转。

### 自定义询问框

自定义询问框的方式，可以使用[弹窗](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-promptaction-0000001478341345-V3)或者[自定义弹窗](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-methods-custom-dialog-box-0000001477981237-V3)实现。这样可以让应用界面与系统默认询问框有所区别，提高应用的用户体验度。本文以弹窗为例，介绍如何实现自定义询问框。

在使用页面路由Router相关功能之前，需要在代码中先导入Router模块。

```
import router from '@ohos.router';
```

在事件回调中，调用弹窗的[promptAction.showDialog()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-promptaction-0000001478341345-V3#ZH-CN_TOPIC_0000001573929081__promptactionshowdialog)方法：

```
function onBackClick() {
  // 弹出自定义的询问框
  promptAction.showDialog({
    message: '您还没有完成支付，确定要返回吗？',
    buttons: [
      {
        text: '取消',
        color: '#FF0000'
      },
      {
        text: '确认',
        color: '#0099FF'
      }
    ]
  }).then((result) => {
    if (result.index === 0) {
      // 用户点击了“取消”按钮
      console.info('User canceled the operation.');
    } else if (result.index === 1) {
      // 用户点击了“确认”按钮
      console.info('User confirmed the operation.');
      // 调用router.back()方法，返回上一个页面
      router.back();
    }
  }).catch((err) => {
    console.error(`Invoke showDialog failed, code is ${err.code}, message is ${err.message}`);
  })
}
```

当用户点击“返回”按钮时，会弹出自定义的询问框，询问用户是否确认返回。选择“取消”将停留在当前页目标页；选择“确认”将触发router.back()方法，并根据参数决定如何执行跳转。



# Navigation

更新时间: 2024-01-15 12:18

[Navigation](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navigation-0000001478341133-V3)组件一般作为页面的根容器，包括单页面、分栏和自适应三种显示模式。同时，Navigation提供了属性来设置页面的标题栏、工具栏、导航栏等。

Navigation组件的页面包含主页和内容页。主页由标题栏、内容区和工具栏组成，可在内容区中使用[NavRouter](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navrouter-0000001478061693-V3)子组件实现导航栏功能。内容页主要显示[NavDestination](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navdestination-0000001477981193-V3)子组件中的内容。

NavRouter是配合Navigation使用的特殊子组件，默认提供点击响应处理，不需要开发者自定义点击事件逻辑。NavRouter有且仅有两个子组件，其中第二个子组件必须是NavDestination。NavDestination是配合NavRouter使用的特殊子组件，用于显示Navigation组件的内容页。当开发者点击NavRouter组件时，会跳转到对应的NavDestination内容区。

## 设置页面显示模式

Navigation组件通过mode属性设置页面的显示模式。

* 自适应模式Navigation组件默认为自适应模式，此时mode属性为NavigationMode.Auto。自适应模式下，当设备宽度大于520vp时，Navigation组件采用分栏模式，反之采用单页面模式。

```
Navigation() {
  ...
}
.mode(NavigationMode.Auto)
```
* 单页面模式
  图1 单页面布局示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.22083766261129926323372459598762:50001231000000:2800:26E46C812A2353787B85A201D811678F4C97E56EF09168F5EF6EE9867708A11F.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  将mode属性设置为NavigationMode.Stack，Navigation组件即可设置为单页面显示模式。

```
Navigation() {
  ...
}
.mode(NavigationMode.Stack)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.15336480528378636863953476133211:50001231000000:2800:66784937ACF83A4401C64FB6B9769AA138CEEAFCDBB00376FE7062E5CDA475CD.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 分栏模式
  图2 分栏布局示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.80686546974892578856180834138451:50001231000000:2800:EA5EAB64D9EED9DA155C74BB5A476561508B26A6C11EBAEC0EF17140778F6471.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  将mode属性设置为NavigationMode.Split，Navigation组件即可设置为分栏显示模式。

```
@Entry
@Component
struct NavigationExample {
  private arr: number[] = [1, 2, 3];

  build() {
    Column() {
      Navigation() {
        TextInput({ placeholder: 'search...' })
          .width("90%")
          .height(40)
          .backgroundColor('#FFFFFF')

        List({ space: 12 }) {
          ForEach(this.arr, (item) => {
            ListItem() {
              NavRouter() {
                Text("NavRouter" + item)
                  .width("100%")
                  .height(72)
                  .backgroundColor('#FFFFFF')
                  .borderRadius(24)
                  .fontSize(16)
                  .fontWeight(500)
                  .textAlign(TextAlign.Center)
                NavDestination() {
                  Text("NavDestinationContent" + item)
                }
                .title("NavDestinationTitle" + item)
              }
            }
          }, item => item)
        }
        .width("90%")
        .margin({ top: 12 })
      }
      .title("主标题")
      .mode(NavigationMode.Split)
      .menus([
        {value: "", icon: "./image/ic_public_search.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=> {}}
      ])
      .toolBar({items: [
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=> {}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=> {}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=> {}}
      ]})
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#F1F3F5')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.38593676869309170092600423878398:50001231000000:2800:F6ECA5CC9F8BBF04FEFBB28E50FA44205ACFAA160717E12A1B164543363E0BDA.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 设置标题栏模式

标题栏在界面顶部，用于呈现界面名称和操作入口，Navigation组件通过titleMode属性设置标题栏模式。

* Mini模式
  普通型标题栏，用于一级页面不需要突出标题的场景。图3 Mini模式标题栏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.59102527920379263325372420276760:50001231000000:2800:D87F6CC17572854649C298FC9781605E2AB18964645C1610815650C0219DD927.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.titleMode(NavigationTitleMode.Mini)
```
* Full模式强调型标题栏，用于一级页面需要突出标题的场景。

  图4 Full模式标题栏
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.73171298361761324502101951665906:50001231000000:2800:250158FAFABBD1E845790620AC33BA4E37436B915661625956474740789197ED.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.titleMode(NavigationTitleMode.Full)
```

## 设置菜单栏

菜单栏位于Navigation组件的右上角，开发者可以通过menus属性进行设置。menus支持Array[[NavigationMenuItem](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navigation-0000001478341133-V3#ZH-CN_TOPIC_0000001523648374__navigationmenuitem%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E)](%5BNavigationMenuItem%5D(https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-navigation-0000001478341133-V3#ZH-CN_TOPIC_0000001523648374__navigationmenuitem%E7%B1%BB%E5%9E%8B%E8%AF%B4%E6%98%8E))和[CustomBuilder](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-builder-0000001524176981-V3)两种参数类型。使用Array`<NavigationMenuItem>`类型时，竖屏最多支持显示3个图标，横屏最多支持显示5个图标，多余的图标会被放入自动生成的更多图标。

图5 设置了3个图标的菜单栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.91167692619942929084265643358720:50001231000000:2800:7FAF3304722308D6ADD3DF6C36B6804FB42BA7975AE97C67A1FD48FC986567BF.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.menus([{value: "", icon: "./image/ic_public_search.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}}])
```

图6 设置了4个图标的菜单栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183907.45474865840653783813126093822041:50001231000000:2800:3F2ED5EA3088DB0CD43B2FDD0D6662C21799699C1F1BCF4ABABD0D6AC187C3D2.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.menus([{value: "", icon: "./image/ic_public_search.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}},
        {value: "", icon: "./image/ic_public_add.svg", action: ()=>{}}])
```

## 设置工具栏

工具栏位于Navigation组件的底部，开发者可以通过toolBar属性进行设置。

图7 工具栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183908.56418621467618143492588730370660:50001231000000:2800:C8AC414315A887F92949045773D4D989191FB5D83255E0B19B1297D6AFCBB39A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

```
Navigation() {
  ...
}
.toolBar({items:[
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=>{}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=>{}},
        {value: "func", icon: "./image/ic_public_highlights.svg", action: ()=>{}}]})
```



# Tabs

更新时间: 2024-01-15 12:19

当页面信息较多时，为了让用户能够聚焦于当前显示的内容，需要对页面内容进行分类，提高页面空间利用率。[Tabs](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-container-tabs-0000001478181433-V3)组件可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。

## 基本布局

Tabs组件的页面组成包含两个部分，分别是TabContent和TabBar。TabContent是内容页，TabBar是导航页签栏，页面结构如下图所示，根据不同的导航类型，布局会有区别，可以分为底部导航、顶部导航、侧边导航，其导航栏分别位于底部、顶部和侧边。图1 Tabs组件布局示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.21345655253077797804764127207022:50001231000000:2800:69E1CBF7FC6896A2A29C90C9748D6407A111048A2BF5628EEB02F4FFBB654190.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

说明

* TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
* TabContent组件不支持设置通用高度属性，其高度由Tabs父组件高度与TabBar组件高度决定。

Tabs使用花括号包裹TabContent，如图2，其中TabContent显示相应的内容页。

图2 Tabs与TabContent使用

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.60157175095985516426849642586217:50001231000000:2800:2B95048EF940211E9ED3C7EEFB881F60D1FA2F67036DDE6B8D4555E6A561F64A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

每一个TabContent对应的内容需要有一个页签，可以通过TabContent的tabBar属性进行配置。在如下TabContent组件上设置属性tabBar，可以设置其对应页签中的内容，tabBar作为内容的页签。

```
 TabContent() {
   Text('首页的内容').fontSize(30)
 }
.tabBar('首页')
```

设置多个内容时，需在Tabs内按照顺序放置。

```
Tabs() {
  TabContent() {
    Text('首页的内容').fontSize(30)
  }
  .tabBar('首页')

  TabContent() {
    Text('推荐的内容').fontSize(30)
  }
  .tabBar('推荐')

  TabContent() {
    Text('发现的内容').fontSize(30)
  }
  .tabBar('发现')
  
  TabContent() {
    Text('我的内容').fontSize(30)
  }
  .tabBar("我的")
}
```

## 底部导航

底部导航是应用中最常见的一种导航方式。底部导航位于应用一级页面的底部，用户打开应用，能够分清整个应用的功能分类，以及页签对应的内容，并且其位于底部更加方便用户单手操作。底部导航一般作为应用的主导航形式存在，其作用是将用户关心的内容按照功能进行分类，迎合用户使用习惯，方便在不同模块间的内容切换。

图3 底部导航栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.82775689739459676219027859800195:50001231000000:2800:DD05A358493A0C5494886F3D370ECEA9F864D4A33282C4AC26EDE747760FF49F.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

导航栏位置使用Tabs的参数barPosition进行设置，默认情况下，导航栏位于顶部，参数默认值为Start。设置为底部导航需要在Tabs传递参数，设置barPosition为End。

```
Tabs({ barPosition: BarPosition.End }) {
  // TabContent的内容：首页、发现、推荐、我的
  ...
}
```

## 顶部导航

当内容分类较多，用户对不同内容的浏览概率相差不大，需要经常快速切换时，一般采用顶部导航模式进行设计，作为对底部导航内容的进一步划分，常见一些资讯类应用对内容的分类为关注、视频、数码，或者手机的主题应用中对主题进行进一步划分为图片、视频、字体等。

图4 顶部导航栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.12556120180176207523409284219607:50001231000000:2800:C284ECE9E62684EDEBA4CDDE8C8762E205BC177C24AC0E25F635727B5471A1B5.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

Tabs组件默认的barPosition参数为Start，即顶部导航模式。

```
Tabs({ barPosition: BarPosition.Start }) {
  // TabContent的内容:关注、视频、游戏、数码、科技、体育、影视
  ...
}
```

## 侧边导航

侧边导航是手机应用较为少见的一种导航模式，更多适用于平板横屏界面，用于对应用进行导航操作，由于用户的视觉习惯是从左到右，侧边导航栏默认为左侧侧边栏。

图5 侧边导航栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.06511767120951281966897698315595:50001231000000:2800:3942B727479C72C437A397D4652C55DECD677C09EE227B44D59BC8B016FF24AC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

实现侧边导航栏需要设置Tabs的属性vertical为true。在底部导航和顶部导航实现中，其默认值为false，表明内容页和导航栏垂直方向排列。

```
Tabs({ barPosition: BarPosition.Start }) {
  // TabContent的内容:首页、发现、推荐、我的
  ...
}
.vertical(true)
.barWidth(100)
.barHeight(200)
```

说明

* vertical为false时，tabbar宽度会默认撑满屏幕的宽度，需要设置barWidth为合适值。
* vertical为true时，tabbar的高度会默认实际内容高度，需要设置barHeight为合适值。

## 限制导航栏的滑动切换

默认情况下，导航栏都支持滑动切换，在一些内容信息量需要进行多级分类的页面，如支持底部导航+顶部导航组合的情况下，底部导航栏的滑动效果与顶部导航出现冲突，此时需要限制底部导航的滑动，避免引起不好的用户体验。图6 限制底部导航栏滑动
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.13175283036663832705667702743867:50001231000000:2800:4F390D747A30DEC7763ED97F9BC8AC1E22ECA06759485921C11BA62F5B2E508D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

控制滑动切换的属性为scrollable，默认值为true，表示可以滑动，若要限制滑动切换页签则需要设置为false。

```
Tabs({ barPosition: BarPosition.End }) {
  TabContent(){
    Column(){
      Tabs(){
        // 顶部导航栏内容
        ...
      }
    }
    .backgroundColor('#ff08a8f1')
    .width('100%')
  }
  .tabBar('首页')

  // 其他TabContent内容：发现、推荐、我的
  ...
}
.scrollable(false)
```

## 固定导航栏

当内容分类较为固定且不具有拓展性时，例如底部导航内容分类一般固定，分类数量一般在3-5个，此时使用固定导航栏。固定导航栏不可滚动，无法被拖拽滚动，内容均分tabBar的宽度。

图7 固定导航栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.03958101396020999970526915740095:50001231000000:2800:B109385A73EC14435240A05FF3DE3D924A5D8FA0B6DB73723EC8E7F87F09A065.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

Tabs的属性barMode是控制导航栏是否可以滚动，默认值为Fixed。

```
Tabs({ barPosition: BarPosition.End }) {
  // TabContent的内容：首页、发现、推荐、我的
  ...
}
.barMode(BarMode.Fixed)
```

## 滚动导航栏

滚动导航栏可以用于顶部导航栏或者侧边导航栏的设置，内容分类较多，屏幕宽度无法容纳所有分类页签的情况下，需要使用可滚动的导航栏，支持用户点击和滑动来加载隐藏的页签内容。

图8 可滚动导航栏
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.37554845990719564401247876847157:50001231000000:2800:8B52BFA57053D9B9791711E31D81B847876DCFA9D13F87B0417AF0DB8D3980CF.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

滚动导航栏需要设置Tabs组件的barMode属性，默认情况下其值为Fixed，表示为固定导航栏，设置为Scrollable即可设置为可滚动导航栏。

```
Tabs({ barPosition: BarPosition.Start }) {
  // TabContent的内容：关注、视频、游戏、数码、科技、体育、影视、人文、艺术、自然、军事
  ...
}
.barMode(BarMode.Scrollable)
```

## 自定义导航栏

对于底部导航栏，一般作为应用主页面功能区分，为了更好的用户体验，会组合文字以及对应语义图标表示页签内容，这种情况下，需要自定义导航页签的样式。

图9 自定义导航栏图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.79380332729199418294824087783888:50001231000000:2800:0C717E6E12EE10F948A89028850990F5A28A7046E067D7EF360B2F1427A741A8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

系统默认情况下采用了下划线标志当前活跃的页签，而自定义导航栏需要自行实现相应的样式，用于区分当前活跃页签和未活跃页签。

设置自定义导航栏需要使用tabBar的参数，以其支持的CustomBuilder的方式传入自定义的函数组件样式。例如这里声明TabBuilder的自定义函数组件，传入参数包括页签文字title，对应位置index，以及选中状态和未选中状态的图片资源。通过当前活跃的currentIndex和页签对应的targetIndex匹配与否，决定UI显示的样式。

```
@Builder TabBuilder(title: string, targetIndex: number, selectedImg: Resource, normalImg: Resource) {
  Column() {
    Image(this.currentIndex === targetIndex ? selectedImg : normalImg)
      .size({ width: 25, height: 25 })
    Text(title)
      .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
  }
  .width('100%')
  .height(50)
  .justifyContent(FlexAlign.Center)
}
```

在TabContent对应tabBar属性中传入自定义函数组件，并传递相应的参数。

```
TabContent() {
  Column(){
    Text('我的内容')  
  }
  .width('100%')
  .height('100%')
  .backgroundColor('#007DFF')
}
.tabBar(this.TabBuilder('我的', 0, $r('app.media.mine_selected'), $r('app.media.mine_normal')))
```

## 切换至指定页签

在不使用自定义导航栏时，系统默认的Tabs会实现切换逻辑。在使用了自定义导航栏后，切换页签的逻辑需要手动实现。即用户点击对应页签时，屏幕需要显示相应的内容页。

图10 使用自定义导航栏实现切换指定页签
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103823.01190442888648648345542803443439:50001231000000:2800:3342BB48655FA61C9B58A7D937FF02CD0F23CC54808668CC04557BDAE1D18976.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

切换指定页签需要使用TabsController，TabsController是Tabs组件的控制器，用于控制Tabs组件进行页签切换。通过TabsController的changeIndex方法来实现跳转至指定索引值对应的TabContent内容。

```
private tabsController : TabsController = new TabsController()
@State currentIndex:number = 0;

@Builder TabBuilder(title: string, targetIndex: number) {
  Column() {
    Text(title)
      .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
  }
  ...
  .onClick(() => {
    this.currentIndex = targetIndex;
    this.tabsController.changeIndex(this.currentIndex);
  })
}
```

使用自定义导航栏时，在tabBar属性中传入对应的@Builder，并传入相应的参数。

```
Tabs({ barPosition: BarPosition.End, controller: this.tabsController }) {
  TabContent(){
    ...
  }.tabBar(this.TabBuilder('首页',0))

  TabContent(){
    ...
  }.tabBar(this.TabBuilder('发现',1))

  TabContent(){
    ...
  }.tabBar(this.TabBuilder('推荐',2))

  TabContent(){
    ...
  }
  .tabBar(this.TabBuilder('我的',3))
}
```

## 滑动切换导航栏

在不使用自定义导航栏的情况下，Tabs默认会实现tabBar与TabContent的切换联动。但在使用了自定义导航栏后，使用TabsController可以实现点击页签与页面内容的联动，但不能实现滑动页面时，页面内容对应页签的联动。即用户在使用滑动屏幕切换页面内容时，页签栏需要同步切换至内容对应的页签。

图11 滑动切换时页签内容不联动
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103824.97637363008863102792742216124246:50001231000000:2800:5793E6FEE471109473B7E32E6D1E53CAC07F521E59C59EF8F332DDA9207D05FE.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

此时需要使用Tabs提供的onChange事件方法，监听索引index的变化，并将其当前活跃的index值传递给currentIndex，实现页签内容的切换。

```
Tabs({ barPosition: BarPosition.End, controller: this.tabsController }) {
  TabContent() {
    ...
  }.tabBar(this.TabBuilder('首页', 0))

  TabContent() {
    ...
  }.tabBar(this.TabBuilder('发现', 1))

  TabContent() {
    ...
  }.tabBar(this.TabBuilder('推荐', 2))

  TabContent() {
    ...
  }
  .tabBar(this.TabBuilder('我的', 3))
}.onChange((index) => {
  this.currentIndex = index
})
```

图12 内容与页签联动
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231204103824.32389872515613396343754191817138:50001231000000:2800:0CCE1E75AE37B22B8FD3E7FC1B25D14CF811FBED236AA2E058FA638A78638E58.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 显示图片（Image）

更新时间: 2024-01-15 12:18

开发者经常需要在应用中显示一些图片，例如：按钮中的icon、网络图片、本地图片等。在应用中显示图片需要使用Image组件实现，Image支持多种图片格式，包括png、jpg、bmp、svg和gif，具体用法请参考[Image](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-basic-components-image-0000001428061728-V3)组件。

Image通过调用接口来创建，接口调用形式如下：

```
Image(src: string | Resource | media.PixelMap)
```

该接口通过图片数据源获取图片，支持本地图片和网络图片的渲染展示。其中，src是图片的数据源，加载方式请参考[加载图片资源](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-graphics-display-0000001451075174-V3#section115090385413)。

## 加载图片资源

Image支持加载存档图、多媒体像素图两种类型。

### 存档图类型数据源

存档图类型的数据源可以分为本地资源、网络资源、Resource资源、媒体库资源和base64。

* 本地资源创建文件夹，将本地图片放入ets文件夹下的任意位置。

  Image组件引入本地图片路径，即可显示图片（根目录为ets文件夹）。

```
Image('images/view.jpg')
.width(200)
```
* 网络资源引入网络图片需申请权限ohos.permission.INTERNET，具体申请方式请参考[权限申请声明](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/accesstoken-guidelines-0000001493744016-V3)。此时，Image组件的src参数为网络图片的链接。

```
Image('https://www.example.com/example.JPG') // 实际使用时请替换为真实地址
```
* Resource资源使用资源格式可以跨包/跨模块引入图片，resources文件夹下的图片都可以通过$r资源接口读取到并转换到Resource格式。

  图1 resources
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.44818105985854355083030956318127:50001231000000:2800:06BA637D1F7806E0F9B3738152D406DEBA3152AEB93E5F863A75C29B411180CD.png?needInitFileName=true?needInitFileName=true)
  调用方式：

```
Image($r('app.media.icon'))
```

  还可以将图片放在rawfile文件夹下。
  图2 rawfile
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.38842991732066072926117600434581:50001231000000:2800:188D77E8894815D6DD62B28666FCD52E23DB15C2AC10402040298F25EB00B6D0.png?needInitFileName=true?needInitFileName=true)
  调用方式：

```
Image($rawfile('snap'))
```
* 媒体库file://data/storage支持file://路径前缀的字符串，用于访问通过媒体库提供的图片路径。

  1. 调用接口获取图库的照片url。
```
import picker from '@ohos.file.picker';

@Entry
@Component
struct Index {
  @State imgDatas: string[] = [];
  // 获取照片url集
  getAllImg() {
    
    let result = new Array<string>();
    try {
      let PhotoSelectOptions = new picker.PhotoSelectOptions();
      PhotoSelectOptions.MIMEType = picker.PhotoViewMIMETypes.IMAGE_TYPE;
      PhotoSelectOptions.maxSelectNumber = 5;
      let photoPicker = new picker.PhotoViewPicker();
      photoPicker.select(PhotoSelectOptions).then((PhotoSelectResult) => {
        this.imgDatas = PhotoSelectResult.photoUris;
        console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
      }).catch((err) => {
        console.error(`PhotoViewPicker.select failed with. Code: ${err.code}, message: ${err.message}`);
      });
    } catch (err) {
      console.error(`PhotoViewPicker failed with. Code: ${err.code}, message: ${err.message}`);    }
  }

  // aboutToAppear中调用上述函数，获取图库的所有图片url，存在imgDatas中
  async aboutToAppear() {
    this.getAllImg();
  }
  // 使用imgDatas的url加载图片。
  build() {
    Column() {
      Grid() {
        ForEach(this.imgDatas, item => {
          GridItem() {
            Image(item)
              .width(200)
          }
        }, item => JSON.stringify(item))
      }
    }.width('100%').height('100%')
  }
}
```
  2. 从媒体库获取的url格式通常如下。
```
Image('file://media/Photos/5')
.width(200)
```
* base64路径格式为data:image/[png|jpeg|bmp|webp];base64,[base64 data]，其中[base64 data]为Base64字符串数据。

  Base64格式字符串可用于存储图片的像素数据，在网页上使用较为广泛。

### 多媒体像素图

PixelMap是图片解码后的像素图，具体用法请参考[图片开发指导](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/image-overview-0000001495825661-V3)。以下示例将加载的网络图片返回的数据解码成PixelMap格式，再显示在Image组件上，

1. 创建PixelMap状态变量。

```
@State image: PixelMap = undefined;
```
2. 引用多媒体。请求网络图片请求，解码编码PixelMap。

   a. 引用网络权限与媒体库权限。
```
import http from '@ohos.net.http';
import ResponseCode from '@ohos.net.http';
import image from '@ohos.multimedia.image';
```
   b. 填写网络图片地址。
```
http.createHttp().request("https://www.example.com/xxx.png",
  (error, data) => {
    if (error){
      console.error(`http reqeust failed with. Code: ${error.code}, message: ${error.message}`);
    } else {
    }
  }
)
```
   c. 将网络地址成功返回的数据，编码转码成pixelMap的图片格式。
```
let code = data.responseCode;
if (ResponseCode.ResponseCode.OK === code) {
  let res: any = data.result  
  let imageSource = image.createImageSource(res);
  let options = {
    alphaType: 0,                     // 透明度
    editable: false,                  // 是否可编辑
    pixelFormat: 3,                   // 像素格式
    scaleMode: 1,                     // 缩略值
    size: { height: 100, width: 100}
   }  // 创建图片大小
    imageSource.createPixelMap(options).then((pixelMap) => {
    this.image = pixelMap
  })
}
```
   d. 显示图片。
```
Button("获取网络图片")
  .onClick(() => {
    this.httpRequest()
  })
Image(this.image).height(100).width(100)
```

## 显示矢量图

Image组件可显示矢量图（svg格式的图片），支持的svg标签为：svg、rect、circle、ellipse、path、line、polyline、polygon和animate。

svg格式的图片可以使用fillColor属性改变图片的绘制颜色。

```
Image($r('app.media.cloud')).width(50)
.fillColor(Color.Blue) 
```

图3 原始图片
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.49132638939465667902670923658814:50001231000000:2800:C139D1CCF371BFD7B1D3668331B25BEE895B1A73FE4F0CF96C89D198F79DAF08.png?needInitFileName=true?needInitFileName=true)

图4 设置绘制颜色后的svg图片
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.44533485388284607816179320753517:50001231000000:2800:6C9A6D9A8DBA27081F9CDB87F766B26556A14015398889E8AA9054B01A15A3E4.png?needInitFileName=true?needInitFileName=true)

## 添加属性

给Image组件设置属性可以使图片显示更灵活，达到一些自定义的效果。以下是几个常用属性的使用示例，完整属性信息详见[Image](https://gitee.com/openharmony/docs/blob/master/zh-cn/application-dev/reference/arkui-ts/ts-basic-components-image.md)。

### 设置图片缩放类型

通过objectFit属性使图片缩放到高度和宽度确定的框内。

```
@Entry
@Component
struct MyComponent {
  scroller: Scroller = new Scroller()

  build() {
    Scroll(this.scroller) {
      Row() {
        Image($r('app.media.img_2')).width(200).height(150)
          .border({ width: 1 })
          .objectFit(ImageFit.Contain).margin(15) // 保持宽高比进行缩小或者放大，使得图片完全显示在显示边界内。
          .overlay('Contain', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.ic_img_2')).width(200).height(150)
          .border({ width: 1 })
          .objectFit(ImageFit.Cover).margin(15)
          // 保持宽高比进行缩小或者放大，使得图片两边都大于或等于显示边界。
          .overlay('Cover', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.img_2')).width(200).height(150)
          .border({ width: 1 })
            // 自适应显示。
          .objectFit(ImageFit.Auto).margin(15)
          .overlay('Auto', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      }
      Row() {
        Image($r('app.media.img_2')).width(200).height(150)
          .border({ width: 1 })
          .objectFit(ImageFit.Fill).margin(15)
          // 不保持宽高比进行放大缩小，使得图片充满显示边界。
          .overlay('Fill', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.img_2')).width(200).height(150)
          .border({ width: 1 })
          // 保持宽高比显示，图片缩小或者保持不变。
          .objectFit(ImageFit.ScaleDown).margin(15)
          .overlay('ScaleDown', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.img_2')).width(200).height(150)
          .border({ width: 1 })
          // 保持原有尺寸显示。
          .objectFit(ImageFit.None).margin(15)
          .overlay('None', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      }
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.70730789301737060152793157499265:50001231000000:2800:307F53FC646F32ECC758E99048AF68BB5F544357A3720F0FFC078343005A20A1.png?needInitFileName=true?needInitFileName=true)

### 图片插值

当原图分辨率较低并且放大显示时，图片会模糊出现锯齿。这时可以使用interpolation属性对图片进行插值，使图片显示得更清晰。

```
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Image($r('app.media.grass'))
          .width('40%')
          .interpolation(ImageInterpolation.None)
          .borderWidth(1)
          .overlay("Interpolation.None", { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)
        Image($r('app.media.grass'))
          .width('40%')
          .interpolation(ImageInterpolation.Low)
          .borderWidth(1)
          .overlay("Interpolation.Low", { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)
      }.width('100%')
      .justifyContent(FlexAlign.Center)

      Row() {
        Image($r('app.media.grass'))
          .width('40%')
          .interpolation(ImageInterpolation.Medium)
          .borderWidth(1)
          .overlay("Interpolation.Medium", { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)
        Image($r('app.media.grass'))
          .width('40%')
          .interpolation(ImageInterpolation.High)
          .borderWidth(1)
          .overlay("Interpolation.High", { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
          .margin(10)
      }.width('100%')
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.44627795441219949916639793978430:50001231000000:2800:2622A02CE12E88F9C3C54E9F7E93E424EC91D445C83294A8B3D16FE24B9CDEB1.png?needInitFileName=true?needInitFileName=true)

### 设置图片重复样式

通过objectRepeat属性设置图片的重复样式方式，重复样式请参考[ImageRepeat](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__imagerepeat)枚举说明。

```
@Entry
@Component
struct MyComponent {
  build() {
    Column({ space: 10 }) {
      Row({ space: 5 }) {
        Image($r('app.media.ic_public_favor_filled_1'))
          .width(110)
          .height(115)
          .border({ width: 1 })
          .objectRepeat(ImageRepeat.XY)
          .objectFit(ImageFit.ScaleDown)
          // 在水平轴和竖直轴上同时重复绘制图片
          .overlay('ImageRepeat.XY', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.ic_public_favor_filled_1'))
          .width(110)
          .height(115)
          .border({ width: 1 })
          .objectRepeat(ImageRepeat.Y)
          .objectFit(ImageFit.ScaleDown)
          // 只在竖直轴上重复绘制图片
          .overlay('ImageRepeat.Y', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.ic_public_favor_filled_1'))
          .width(110)
          .height(115)
          .border({ width: 1 })
          .objectRepeat(ImageRepeat.X)
          .objectFit(ImageFit.ScaleDown)
          // 只在水平轴上重复绘制图片
          .overlay('ImageRepeat.X', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      }
    }.height(150).width('100%').padding(8)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.24860585117936717510875849676556:50001231000000:2800:13E37554C961713DF4E5028ADD2698FCBAD39803C07BA2D35A0CCB103D3283E1.png?needInitFileName=true?needInitFileName=true)

### 设置图片渲染模式

通过renderMode属性设置图片的渲染模式为原色或黑白。

```
@Entry
@Component
struct MyComponent {
  build() {
    Column({ space: 10 }) {
      Row({ space: 50 }) {
        Image($r('app.media.example'))
          // 设置图片的渲染模式为原色 
          .renderMode(ImageRenderMode.Original)
          .width(100)
          .height(100)
          .border({ width: 1 })
            // overlay是通用属性，用于在组件上显示说明文字
          .overlay('Original', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
        Image($r('app.media.example'))
          // 设置图片的渲染模式为黑白
          .renderMode(ImageRenderMode.Template)
          .width(100)
          .height(100)
          .border({ width: 1 })
          .overlay('Template', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      }
    }.height(150).width('100%').padding({ top: 20,right: 10 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.89704977386002803961939303861710:50001231000000:2800:EAF7C1553FF52699B67B519644B8647795CF6D96D58C7EC97A46815BE223584F.png?needInitFileName=true?needInitFileName=true)

### 设置图片解码尺寸

通过sourceSize属性设置图片解码尺寸，降低图片的分辨率。

原图尺寸为1280*960，该示例将图片解码为150*150和400*400。

```
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row({ space: 20 }) {
        Image($r('app.media.example'))
          .sourceSize({
            width: 150,
            height: 150
          })
          .objectFit(ImageFit.ScaleDown)
          .width('25%')
          .aspectRatio(1)
          .border({ width: 1 })
          .overlay('width:150 height:150', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
        Image($r('app.media.example'))
          .sourceSize({
            width: 400,
            height: 400
          })
          .objectFit(ImageFit.ScaleDown)
          .width('25%')
          .aspectRatio(1)
          .border({ width: 1 })
          .overlay('width:400 height:400', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
      }.height(150).width('100%').padding(20)

    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.76189078086015247342829997145896:50001231000000:2800:2C11BBA2ED77DE11718707085A1E135FB666DCB085CEF38C29AEE8841CEC7DB0.png?needInitFileName=true?needInitFileName=true)

### 为图片添加滤镜效果

通过colorFilter修改图片的像素颜色，为图片添加滤镜。

```
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Image($r('app.media.example'))
          .width('40%')
          .margin(10)
        Image($r('app.media.example'))
          .width('40%')
          .colorFilter(
            [1, 1, 0, 0, 0,
             0, 1, 0, 0, 0,
             0, 0, 1, 0, 0,
             0, 0, 0, 1, 0])
          .margin(10)
      }.width('100%')
      .justifyContent(FlexAlign.Center)
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.04575866478054986181381453008820:50001231000000:2800:B2AB2481CF623A6911C2CAF825A996A8D2FB5B845656CF74A0E99C272B43346D.png?needInitFileName=true?needInitFileName=true)

### 同步加载图片

一般情况下，图片加载流程会异步进行，以避免阻塞主线程，影响UI交互。但是特定情况下，图片刷新时会出现闪烁，这时可以使用syncLoad属性，使图片同步加载，从而避免出现闪烁。不建议图片加载较长时间时使用，会导致页面无法响应。

```
Image($r('app.media.icon'))
  .syncLoad(true)
```

## 事件调用

通过在Image组件上绑定onComplete事件，图片加载成功后可以获取图片的必要信息。如果图片加载失败，也可以通过绑定onError回调来获得结果。

```
@Entry
@Component
struct MyComponent {
  @State widthValue: number = 0
  @State heightValue: number = 0
  @State componentWidth: number = 0
  @State componentHeight: number = 0

  build() {
    Column() {
      Row() {
        Image($r('app.media.ic_img_2'))
          .width(200)
          .height(150)
          .margin(15)
          .onComplete(msg => {
            if(msg){
              this.widthValue = msg.width
              this.heightValue = msg.height
              this.componentWidth = msg.componentWidth
              this.componentHeight = msg.componentHeight
            }
          })
            // 图片获取失败，打印结果
          .onError(() => {
            console.info('load image fail')
          })
          .overlay('\nwidth: ' + String(this.widthValue) + ', height: ' + String(this.heightValue) + '\ncomponentWidth: ' + String(this.componentWidth) + '\ncomponentHeight: ' + String(this.componentHeight), {
            align: Alignment.Bottom,
            offset: { x: 0, y: 60 }
          })
      }
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20240110113020.30879826069122299994293553777413:50001231000000:2800:EF30EA87DD6234105C9E870A881A373E00D56A821F61F6E85BE7FFD581D7F28B.png?needInitFileName=true?needInitFileName=true)



# 绘制几何图形（Shape）

更新时间: 2024-01-15 12:18

绘制组件用于在页面绘制图形，Shape组件是绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。具体用法请参考[Shape](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-shape-0000001428061768-V3)。

## 创建绘制组件

绘制组件可以由以下两种形式创建：

* 绘制组件使用Shape作为父组件，实现类似SVG的效果。接口调用为以下形式：

```
Shape(value?: PixelMap)
```

  该接口用于创建带有父组件的绘制组件，其中value用于设置绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则在当前绘制目标中进行绘制。

```
Shape() {
  Rect().width(300).height(50)
}
```
* 绘制组件单独使用，用于在页面上绘制指定的图形。有7种绘制类型，分别为[Circle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-circle-0000001427584896-V3)（圆形）、[Ellipse](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-ellipse-0000001427744848-V3)（椭圆形）、[Line](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-line-0000001478181437-V3)（直线）、[Polyline](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-polyline-0000001478341173-V3)（折线）、[Polygon](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-polygon-0000001478061725-V3)（多边形）、[Path](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-path-0000001477981225-V3)（路径）、[Rect](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-drawing-components-rect-0000001427902488-V3)（矩形）。以Circle的接口调用为例：

```
Circle(options?: {width?: string | number, height?: string | number}
```

  该接口用于在页面绘制圆形，其中width用于设置圆形的宽度，height用于设置圆形的高度，圆形直径由宽高最小值确定。

```
Circle({ width: 150, height: 150 })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.78136929670533928090594734757152:50001231000000:2800:94ECF5E2940B5B640B7D44835822C59BE6A356B0D4953B7A8D13B3694417DB3A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 形状视口viewport

```
viewPort{ x?: number | string, y?: number | string, width?: number | string, height?: number | string }
```

形状视口viewport指定用户空间中的一个矩形，该矩形映射到为关联的 SVG 元素建立的视区边界。viewport属性的值包含x、y、width和height四个可选参数，x 和 y 表示视区的左上角坐标，width和height表示其尺寸。

以下3个示例讲解Viewport具体用法：

* 通过形状视口对图形进行放大与缩小。

```
// 画一个宽高都为150的圆
Text('原始尺寸Circle组件')
Circle({width: 75, height: 75}).fill('#E87361')

Row({space:10}) {
  Column() {
    // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为75的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个直径为75的圆。
    // 绘制结束，viewport会根据组件宽高放大两倍
    Text('shape内放大的Circle组件')
    Shape() {
      Rect().width('100%').height('100%').fill('#0097D4')
      Circle({width: 75, height: 75}).fill('#E87361')
    }
    .viewPort({x: 0, y: 0, width: 75, height: 75})
    .width(150)
    .height(150)
    .backgroundColor('#F5DC62')
  }
  Column() {
    // 创建一个宽高都为150的shape组件，背景色为黄色，一个宽高都为300的viewport。用一个绿色的矩形来填充viewport，在viewport中绘制一个直径为75的圆。
    // 绘制结束，viewport会根据组件宽高缩小两倍。
    Text('Shape内缩小的Circle组件')
    Shape() {
      Rect().width('100%').height('100%').fill('#BDDB69')
      Circle({width: 75, height: 75}).fill('#E87361')
    }
    .viewPort({x: 0, y: 0, width: 300, height: 300})
    .width(150)
    .height(150)
    .backgroundColor('#F5DC62')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.27632915883378190726610759818057:50001231000000:2800:889C15BA0EAEFC56347812B78F207DCEF6C2B25B42466ECFB64001B056BC5A15.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 创建一个宽高都为300的shape组件，背景色为黄色，一个宽高都为300的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个半径为75的圆。

```
Shape() {
  Rect().width("100%").height("100%").fill("#0097D4")
  Circle({ width: 150, height: 150 }).fill("#E87361")
}
  .viewPort({ x: 0, y: 0, width: 300, height: 300 })
  .width(300)
  .height(300)
  .backgroundColor("#F5DC62")
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.64179552777583720438997968478456:50001231000000:2800:13327F3392C2ED70E585BAF3239EA21815224E1D13541955DFB90F18B318D55A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 创建一个宽高都为300的shape组件，背景色为黄色，创建一个宽高都为300的viewport。用一个蓝色的矩形来填充viewport，在viewport中绘制一个半径为75的圆，将viewport向右方和下方各平移150。

```
Shape() {
  Rect().width("100%").height("100%").fill("#0097D4")
  Circle({ width: 150, height: 150 }).fill("#E87361")
}
  .viewPort({ x: -150, y: -150, width: 300, height: 300 })
  .width(300)
  .height(300)
  .backgroundColor("#F5DC62")
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.13793240393822639957610790020266:50001231000000:2800:CCEF2B0E391DCF2E202A5021DC0C15F297D4877E18C6DF00EA674BE40A2DE7FB.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 自定义样式

绘制组件支持通过各种属性对组件样式进行更改。

* 通过fill可以设置组件填充区域颜色。

```
Path()
  .width(100)
  .height(100)
  .commands('M150 0 L300 300 L0 300 Z')
  .fill("#E87361")
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.77262557094866243853163530469643:50001231000000:2800:3DEAEF28F8E57FEE7A0E5ACC89FDB915429A6A57DF2A30AE865208FEDA01AED0.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过stroke可以设置组件边框颜色。

```
Path()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .commands('M150 0 L300 300 L0 300 Z')
  .stroke(Color.Red)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.95553119255264091231684341299450:50001231000000:2800:5B14B787B6EFCE69E2565CD461B7C7F07CFE8A8C0320EB2E263905E98BCF5A59.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过strokeOpacity可以设置边框透明度。

```
Path()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .commands('M150 0 L300 300 L0 300 Z')
  .stroke(Color.Red)
  .strokeWidth(10)
  .strokeOpacity(0.2)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.99186807267582956783438232424736:50001231000000:2800:62C87ACE36CC38659E62C6763F09E32E9825F2058784D32FA407C1A73CB9022A.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过strokeLineJoin可以设置线条拐角绘制样式。拐角绘制样式分为Bevel(使用斜角连接路径段)、Miter(使用尖角连接路径段)、Round(使用圆角连接路径段)。

```
Polyline()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .stroke(Color.Red)
  .strokeWidth(8)
  .points([[20, 0], [0, 100], [100, 90]])
   // 设置折线拐角处为圆弧
  .strokeLineJoin(LineJoinStyle.Round)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.10320095066369038881528492242480:50001231000000:2800:AE0BD18F562101B53F61FE8519DC8D3C0BA2D260DE1C4A0797ADDFB746B76F77.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过strokeMiterLimit设置斜接长度与边框宽度比值的极限值。
  斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。strokeMiterLimit取值需大于等于1，且在strokeLineJoin属性取值LineJoinStyle.Miter时生效。

```
Polyline()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .stroke(Color.Red)
  .strokeWidth(10)
  .points([[20, 0], [20, 100], [100, 100]])
  // 设置折线拐角处为尖角
  .strokeLineJoin(LineJoinStyle.Miter)
  // 设置斜接长度与线宽的比值
  .strokeMiterLimit(1/Math.sin(45))
Polyline()
  .width(100)
  .height(100)
  .fillOpacity(0)
  .stroke(Color.Red)
  .strokeWidth(10)
  .points([[20, 0], [20, 100], [100, 100]])
  .strokeLineJoin(LineJoinStyle.Miter)
  .strokeMiterLimit(1.42)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.03928496003306153883688413289504:50001231000000:2800:B9FB96760F8E92C7370E3F7EC2FC6691D172F0363D05F253DD04D3C335982197.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 通过antiAlias设置是否开启抗锯齿，默认值为true（开启抗锯齿）。

```
//开启抗锯齿
Circle()
  .width(150)
  .height(200)
  .fillOpacity(0)
  .strokeWidth(5)
  .stroke(Color.Black)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.19813619572308854368922564124744:50001231000000:2800:93457386F1F1B2D41E25029AFF96DD38CC5D463DBABAF9C0741E1612D27838D7.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

```
//关闭抗锯齿
Circle()
  .width(150)
  .height(200)
  .fillOpacity(0)
  .strokeWidth(5)
  .stroke(Color.Black)
  .antiAlias(false)
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.71091467993133181863078438767460:50001231000000:2800:512B6DB3D7F97444FBFFD2EE1973AEC245FE0B1E9D6970ED4AC9029374BFD7FD.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 场景示例

* 在Shape的(-80, -5)点绘制一个封闭路径，填充颜色0x317AF7,线条宽度10,边框颜色红色,拐角样式锐角（默认值）。

```
@Entry
@Component
struct ShapeExample {
  build() {
    Column({ space: 10 }) {
      Shape() {
        Path().width(200).height(60).commands('M0 0 L400 0 L400 150 Z')
      }
      .viewPort({ x: -80, y: -5, width: 500, height: 300 })
      .fill(0x317AF7)
      .stroke(Color.Red)
      .strokeWidth(3)
      .strokeLineJoin(LineJoinStyle.Miter)
      .strokeMiterLimit(5)
    }.width('100%').margin({ top: 15 })
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.12221313042066034567406844717340:50001231000000:2800:609D2EC5E6CF482F3D2683E515DFF652DC5ED51131C372ED440C74A16FC8558B.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 绘制一个直径为150的圆，和一个直径为150、线条为红色虚线的圆环（宽高设置不一致时以短边为直径）。

```
@Entry
@Component
struct CircleExample {
  build() {
    Column({ space: 10 }) {
      //绘制一个直径为150的圆
      Circle({ width: 150, height: 150 })
      //绘制一个直径为150、线条为红色虚线的圆环
      Circle()
        .width(150)
        .height(200)
        .fillOpacity(0)
        .strokeWidth(3)
        .stroke(Color.Red)
        .strokeDashArray([1, 2])
    }.width('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183911.57628415286340532337756764752801:50001231000000:2800:5460C6769BC27A268BF4C7EC99E534926F8F85B9E0BD436A8CB46CFBB7D358F3.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 使用画布绘制自定义图形（Canvas）

更新时间: 2024-01-15 12:19

Canvas提供画布组件，用于自定义绘制图形，开发者使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制，绘制对象可以是基础形状、文本、图片等。

## 使用画布组件绘制自定义图形

可以由以下三种形式在画布绘制自定义图形：

* 使用[CanvasRenderingContext2D对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3)在Canvas画布上绘制。

```
@Entry
@Component
struct CanvasExample1 {
  //用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿，true表明开启抗锯齿。
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  //用来创建CanvasRenderingContext2D对象，通过在canvas中调用CanvasRenderingContext2D对象来绘制。
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      //在canvas中调用CanvasRenderingContext2D对象。
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() => {
          //可以在这里绘制内容。
          this.context.strokeRect(50, 50, 200, 150);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.47468295442360551339405751229852:50001231000000:2800:DDD1CA54B71E4C2A2B53568FBA45C0B0827D7F2CABA8CFE6464408034441D2D7.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 离屏绘制是指将需要绘制的内容先绘制在缓存区，再将其转换成图片，一次性绘制到Canvas上，加快了绘制速度。过程为：

  1. 通过transferToImageBitmap方法将离屏画布最近渲染的图像创建为一个ImageBitmap对象。
  2. 通过CanvasRenderingContext2D对象的transferFromImageBitmap方法显示给定的ImageBitmap对象。

  具体使用参考[OffscreenCanvasRenderingContext2D对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-offscreencanvasrenderingcontext2d-0000001427902492-V3)。

```
@Entry
@Component
struct CanvasExample2 {
//用来配置CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。true表明开启抗锯齿
  private settings: RenderingContextSettings = new RenderingContextSettings(true)
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
//用来创建OffscreenCanvasRenderingContext2D对象，width为离屏画布的宽度，height为离屏画布的高度。通过在canvas中调用OffscreenCanvasRenderingContext2D对象来绘制。
  private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)
 
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() =>{
          //可以在这里绘制内容
          this.offContext.strokeRect(50, 50, 200, 150);
          //将离屏绘值渲染的图像在普通画布上显示
          let image = this.offContext.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.42524196131382221037681668799167:50001231000000:2800:71040F4F1F22853BCA439DD50F551AD082BE31F0FC98E5159D2D7C566A513956.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

  说明

  在画布组件中，通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象在Canvas组件上进行绘制时调用的接口相同，另接口参数如无特别说明，单位均为vp。
* 在Canvas上加载Lottie动画时，需要先按照如下方式下载Lottie。

```
import lottie from '@ohos/lottie'
```

  具体接口和示例请参考[Lottie](https://ohpm.openharmony.cn/#/cn/detail/@ohos/lottie)。

## 初始化画布组件

onReady(event: () => void)是Canvas组件初始化完成时的事件回调，调用该事件后，可获取Canvas组件的确定宽高，进一步使用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象调用相关API进行图形绘制。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() => {
    this.context.fillStyle = '#0097D4';
    this.context.fillRect(50, 50, 100, 100);
  })
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.26891313029588282994912948303573:50001231000000:2800:7141A51FA4E195018B4149A6C82457A364D255848CDFE24C642D0E180234807D.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 画布组件绘制方式

在Canvas组件生命周期接口onReady()调用之后，开发者可以直接使用canvas组件进行绘制。或者可以脱离Canvas组件和onready生命周期，单独定义Path2d对象构造理想的路径，并在onready调用之后使用Canvas组件进行绘制。

* 通过CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象直接调用相关API进行绘制。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
    this.context.beginPath();
    this.context.moveTo(50, 50);
    this.context.lineTo(280, 160);
    this.context.stroke();
   })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142813.69468094294715342608204515898987:50001231000000:2800:BE6DC35A3F0B5ED96F9148F183B00578F7F1AE7C653411D9CE90AD850E34BD2F.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 先单独定义path2d对象构造理想的路径，再通过调用CanvasRenderingContext2D对象和OffscreenCanvasRenderingContext2D对象的stroke接口或者fill接口进行绘制，具体使用可以参考[Path2D对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-components-canvas-path2d-0000001428061772-V3)。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     let region = new Path2D();
     region.arc(100, 75, 50, 0, 6.28);
     this.context.stroke(region);
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.11524447272073294339877526018215:50001231000000:2800:C8098EBA37AFFB9DD044D36ACAA4AD15D0A480ACC82A9824BEE6F53EA0E2B8B2.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 画布组件常用方法

OffscreenCanvasRenderingContext2D对象和CanvasRenderingContext2D对象提供了大量的属性和方法，可以用来绘制文本、图形，处理像素等，是Canvas组件的核心。常用接口有[fill](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__fill)(对封闭路径进行填充）、[clip](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__clip)(设置当前路径为剪切路径)、[stroke](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-components-canvas-canvasrenderingcontext2d-0000001428061816-V3#ZH-CN_TOPIC_0000001574128621__stroke)（进行边框绘制操作）等等，同时提供了[fillStyle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__fillstyle)（指定绘制的填充色）、[globalAlpha](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__globalalpha)（设置透明度）与[strokeStyle](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__strokestyle)（设置描边的颜色）等属性修改绘制内容的样式。将通过以下几个方面简单介绍画布组件常见使用方法：

* 基础形状绘制。
  可以通过[arc](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__arc)（绘制弧线路径）、 [ellipse](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__ellipse)（绘制一个椭圆）、[rect](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__rect)（创建矩形路径）等接口绘制基础形状。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     //绘制矩形
     this.context.beginPath();
     this.context.rect(100, 50, 100, 100);
     this.context.stroke();
     //绘制圆形
     this.context.beginPath();
     this.context.arc(150, 250, 50, 0, 6.28);
     this.context.stroke();
     //绘制椭圆
     this.context.beginPath();
     this.context.ellipse(150, 450, 50, 100, Math.PI * 0.25, Math.PI * 0, Math.PI * 2);
     this.context.stroke();
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.76418334241656038967035814198246:50001231000000:2800:4019A204DD491EC9EDFD2B7401BDC62C6201DD1A2378EB603450CC17B6098BCB.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 文本绘制。
  可以通过[fillText](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__filltext)（绘制填充类文本）、[strokeText](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__stroketext)（绘制描边类文本）等接口进行文本绘制。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     //绘制填充类文本
     this.context.font = '50px sans-serif';
     this.context.fillText("Hello World!", 50, 100);
     //绘制描边类文本
     this.context.font = '55px sans-serif';
     this.context.strokeText("Hello World!", 50, 150);
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.49673793291355990078220821223727:50001231000000:2800:BFE812D46B987036EE0436287284379638B2B720F22BE1E4BCB965E6DDD674B5.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 绘制图片和图像像素信息处理。
  可以通过[drawImage](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__drawimage)（图像绘制）、[putImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__putimagedata)（使用[ImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-components-canvas-image-0000001427584952-V3)数据填充新的矩形区域）等接口绘制图片，通过[createImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__createimagedata)（创建新的ImageData 对象）、[getPixelMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__getpixelmap)（以当前canvas指定区域内的像素创建[PixelMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-image-0000001477981401-V3#ZH-CN_TOPIC_0000001523648994__pixelmap7)对象）、[getImageData](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__getimagedata)（以当前canvas指定区域内的像素创建ImageData对象）等接口进行图像像素信息处理。

```
@Entry
@Component
struct GetImageData {
 private settings: RenderingContextSettings = new RenderingContextSettings(true)
 private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
 private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)
 private img:ImageBitmap = new ImageBitmap("/common/images/1234.png")
 
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() =>{
          // 使用drawImage接口将图片画在（0，0）为起点，宽高130的区域
          this.offContext.drawImage(this.img,0,0,130,130);
          // 使用getImageData接口，获得canvas组件区域中，（50，50）为起点，宽高130范围内的绘制内容
          let imagedata = this.offContext.getImageData(50,50,130,130);
          // 使用putImageData接口将得到的ImageData画在起点为（150， 150）的区域中
          this.offContext.putImageData(imagedata,150,150);
          // 将离屏绘制的内容画到canvas组件上
          let image = this.offContext.transferToImageBitmap();
          this.context.transferFromImageBitmap(image);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.20074442686946558048719322116242:50001231000000:2800:2D55310586F6641A9FC2934225D2B8B0475263074577E36FF98A121087DD3451.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
* 其他方法。Canvas中还提供其他类型的方法。渐变（[CanvasGradient对象](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-components-canvas-canvasgradient-0000001478341177-V3)）相关的方法：[createLinearGradient](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__createlineargradient)（创建一个线性渐变色）、[createRadialGradient](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-canvasrenderingcontext2d-0000001478181441-V3#ZH-CN_TOPIC_0000001573928937__createradialgradient)（创建一个径向渐变色）等。

```
Canvas(this.context)
  .width('100%')
  .height('100%')
  .backgroundColor('#F5DC62')
  .onReady(() =>{
     //创建一个径向渐变色的CanvasGradient对象
     let grad = this.context.createRadialGradient(200,200,50, 200,200,200)
     //为CanvasGradient对象设置渐变断点值，包括偏移和颜色
     grad.addColorStop(0.0, '#E87361');
     grad.addColorStop(0.5, '#FFFFF0');
     grad.addColorStop(1.0, '#BDDB69');
     //用CanvasGradient对象填充矩形
     this.context.fillStyle = grad;
     this.context.fillRect(0, 0, 400, 400);
  })
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.48900326339694978662019483576721:50001231000000:2800:A8DB6956E7663CA604E89C8C897A1EFB86EA874A734D82E4C8A59D15E082C226.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 场景示例

* 规则基础形状绘制：

```
@Entry
@Component
struct ClearRect {
 private settings: RenderingContextSettings = new RenderingContextSettings(true);
 private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
 
  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#F5DC62')
        .onReady(() =>{
          // 设定填充样式，填充颜色设为蓝色
          this.context.fillStyle = '#0097D4';
          // 以(50, 50)为左上顶点，画一个宽高200的矩形
          this.context.fillRect(50,50,200,200);
          // 以(70, 70)为左上顶点，清除宽150高100的区域
          this.context.clearRect(70,70,150,100);
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.25174415228801472017747227145886:50001231000000:2800:6A410675FC2C4E388256348F59C201396621E230A44232A513D8B8AFEF8C99E6.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

* 不规则图形绘制。

```
@Entry
@Component
struct Path2d {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Row() {
      Column() {
        Canvas(this.context)
          .width('100%')
          .height('100%')
          .backgroundColor('#F5DC62')
          .onReady(() =>{
            // 使用Path2D的接口构造一个五边形
            let path = new Path2D();
            path.moveTo(150, 50);
            path.lineTo(50, 150);
            path.lineTo(100, 250);
            path.lineTo(200, 250);
            path.lineTo(250, 150);
            path.closePath();
            // 设定填充色为蓝色
            this.context.fillStyle = '#0097D4';
            // 使用填充的方式，将Path2D描述的五边形绘制在canvas组件内部
            this.context.fill(path);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231211142814.44226074908851811461676159441079:50001231000000:2800:7FA74834316AFB5912BAD80390F5563690C01B92FEE492F10C3CA8426C6B5AFF.jpg?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")



# 动画概述

更新时间: 2024-01-15 12:19

动画的原理是在一个时间段内，多次改变UI外观，由于人眼会产生视觉暂留，所以最终看到的就是一个“连续”的动画。UI的一次改变称为一个动画帧，对应一次屏幕刷新，而决定动画流畅度的一个重要指标就是帧率FPS（Frame Per Second），即每秒的动画帧数，帧率越高则动画就会越流畅。

ArkUI中，产生动画的方式是改变属性值且指定动画参数。动画参数包含了如动画时长、变化规律（即曲线）等参数。当属性值发生变化后，按照动画参数，从原来的状态过渡到新的状态，即形成一个动画。

ArkUI提供的动画能力按照页面的分类方式，可分为页面内的动画和页面间的动画。如下图所示，页面内的动画指在一个页面内即可发生的动画，页面间的动画指两个页面跳转时才会发生的动画。

图1 按照页面分类的动画![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183916.61845778518581182389102191722044:50001231000000:2800:44C830DB0CCA7DDEECC53D5292EB65E90B2490A3A6A3B19DBDF55203B564463E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果按照基础能力分，可分为属性动画、显式动画、转场动画三部分。如下图所示。

图2 按照基础能力分类的动画

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183916.55170464610558711114933908596597:50001231000000:2800:E7D6E7F00F00D8946F9821E4F762CE424C334D70D16440A2B3E7F93354742F2E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

本文按照页面的分类方式，从使用场景出发，提供各种动画的使用方法和注意事项，使开发者快速学习动画。



# 布局更新动画

更新时间: 2024-01-15 12:19

[显式动画](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-explicit-animation-0000001478341181-V3)（animateTo）和[属性动画](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-animatorproperty-0000001478181445-V3)（animation）是ArkUI提供的最基础和常用的动画功能。在布局属性（如[尺寸属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-size-0000001428061700-V3)、[位置属性](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-location-0000001427584824-V3)）发生变化时，可以通过属性动画或显式动画，按照动画参数过渡到新的布局参数状态。

| 动画类型 | 特点                                                                                               |
| :------- | :------------------------------------------------------------------------------------------------- |
| 显式动画 | 闭包内的变化均会触发动画，包括由数据变化引起的组件的增删、组件属性的变化等，可以做较为复杂的动画。 |
| 属性动画 | 动画设置简单，属性变化时自动触发动画。                                                             |

## 使用显式动画产生布局更新动画

显式动画的接口为：

```
animateTo(value: AnimateParam, event: () => void): void
```

第一个参数指定动画参数，第二个参数为动画的闭包函数。

以下是使用显式动画产生布局更新动画的示例。示例中，当Column组件的alignItems属性改变后，其子组件的布局位置结果发生变化。只要该属性是在animateTo的闭包函数中修改的，那么由其引起的所有变化都会按照animateTo的动画参数执行动画过渡到终点值。

```
@Entry
@Component
struct LayoutChange {
  // 用于控制Column的alignItems属性
  @State itemAlign: HorizontalAlign = HorizontalAlign.Start;
  allAlign: HorizontalAlign[] = [HorizontalAlign.Start, HorizontalAlign.Center, HorizontalAlign.End];
  alignIndex: number = 0;

  build() {
    Column() {
      Column({ space: 10 }) {
        Button("1").width(100).height(50)
        Button("2").width(100).height(50)
        Button("3").width(100).height(50)
      }
      .margin(20)
      .alignItems(this.itemAlign)
      .borderWidth(2)
      .width("90%")
      .height(200)

      Button("click").onClick(() => {
        // 动画时长为1000ms，曲线为EaseInOut
        animateTo({ duration: 1000, curve: Curve.EaseInOut }, () => {
          this.alignIndex = (this.alignIndex + 1) % this.allAlign.length;
          // 在闭包函数中修改this.itemAlign参数，使Column容器内部孩子的布局方式变化，使用动画过渡到新位置
          this.itemAlign = this.allAlign[this.alignIndex];
        });
      })
    }
    .width("100%")
    .height("100%")
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183916.77423799629747853080363049521371:50001231000000:2800:A156F28767D3F1B7F9162DA006417838BC2E8B6B0ADF045EBC8BF133682E3C24.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

除直接改变布局方式外，也可直接修改组件的宽、高、位置。

```
@Entry
@Component
struct LayoutChange2 {
  @State myWidth: number = 100;
  @State myHeight: number = 50;
  // 标志位，true和false分别对应一组myWidth、myHeight值
  @State flag: boolean = false;

  build() {
    Column({ space: 10 }) {
      Button("text")
        .type(ButtonType.Normal)
        .width(this.myWidth)
        .height(this.myHeight)
        .margin(20)
      Button("area: click me")
        .fontSize(12)
        .margin(20)
        .onClick(() => {
          animateTo({ duration: 1000, curve: Curve.Ease }, () => {
            // 动画闭包中根据标志位改变控制第一个Button宽高的状态变量，使第一个Button做宽高动画
            if (this.flag) {
              this.myWidth = 100;
              this.myHeight = 50;
            } else {
              this.myWidth = 200;
              this.myHeight = 100;
            }
            this.flag = !this.flag;
          });
        })
    }
    .width("100%")
    .height("100%")
  }
}
```

在第二个Button的点击事件中，使用animateTo函数，在闭包中修改this.myWidth和this.myHeight状态变量，而这两个状态变量分别为第一个Button的宽、高属性值，所以第一个Button做了宽高动画。效果如下图。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183916.45286236571555495451236965510599:50001231000000:2800:C3D065F3FCE9EC1FBC4128B6034321DC3152E7E15DFAABFB97C6210F92436CE6.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

与此同时，第二个Button也产生了一个位置动画。这是由于第一个Button的宽高变化后，引起了Column内部其他组件的布局结果也发生了变化，第二个Button的布局发生变化也是由于闭包内改变第一个Button的宽高造成的。

如果不希望第二个Button有动画效果，有两种方式可以实现。一种是给做第一个Button外面再加一个容器，使其动画前后的大小都在容器的范围内，这样第二个Button的位置不会被第一个Button的位置所影响。修改后的核心代码如下。

```
Column({ space: 10 }) {
  Column() {
    // Button放在足够大的容器内，使其不影响更外层的组件位置
    Button("text")
      .type(ButtonType.Normal)
      .width(this.myWidth)
      .height(this.myHeight)
  }
  .margin(20)
  .width(200)
  .height(100)

  Button("area: click me")
    .fontSize(12)
    .onClick(() => {
      animateTo({ duration: 1000, curve: Curve.Ease }, () => {
        // 动画闭包中根据标志位改变控制第一个Button宽高的状态变量，使第一个Button做宽高动画
        if (this.flag) {
          this.myWidth = 100;
          this.myHeight = 50;
        } else {
          this.myWidth = 200;
          this.myHeight = 100;
        }
        this.flag = !this.flag;
      });
    })
}
.width("100%")
.height("100%")
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183916.71982117443709016770745378264267:50001231000000:2800:FD68B9257E3C1D5F7AB7FE8BA218894253971B52DD1663C312AA16934E3943A1.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

另一种方式是给第二个Button添加布局约束，如position的位置约束，使其位置不被第一个Button的宽高影响。核心代码如下：

```
Column({ space: 10 }) {
  Button("text")
    .type(ButtonType.Normal)
    .width(this.myWidth)
    .height(this.myHeight)
    .margin(20)

  Button("area: click me")
    .fontSize(12)
    // 配置position属性固定，使自己的布局位置不被第一个Button的宽高影响
    .position({ x: "30%", y: 200 })
    .onClick(() => {
      animateTo({ duration: 1000, curve: Curve.Ease }, () => {
        // 动画闭包中根据标志位改变控制第一个Button宽高的状态变量，使第一个Button做宽高动画
        if (this.flag) {
          this.myWidth = 100;
          this.myHeight = 50;
        } else {
          this.myWidth = 200;
          this.myHeight = 100;
        }
        this.flag = !this.flag;
      });
    })
}
.width("100%")
.height("100%")
```

## 使用属性动画产生布局更新动画

显式动画把要执行动画的属性的修改放在闭包函数中触发动画，而属性动画则无需使用闭包，把animation属性加在要做属性动画的组件的属性后即可。

属性动画的接口为：

```
animation(value: AnimateParam)
```

其入参为动画参数。想要组件随某个属性值的变化而产生动画，此属性需要加在animation属性之前。有的属性变化不希望通过animation产生属性动画，可以放在animation之后。上面显式动画的示例很容易改为用属性动画实现。例如：

```
@Entry
@Component
struct LayoutChange2 {
  @State myWidth: number = 100;
  @State myHeight: number = 50;
  @State flag: boolean = false;
  @State myColor: Color = Color.Blue;

  build() {
    Column({ space: 10 }) {
      Button("text")
        .type(ButtonType.Normal)
        .width(this.myWidth)
        .height(this.myHeight)
        // animation只对其上面的type、width、height属性生效，时长为1000ms，曲线为Ease
        .animation({ duration: 1000, curve: Curve.Ease })
        // animation对下面的backgroundColor、margin属性不生效
        .backgroundColor(this.myColor)
        .margin(20)
        

      Button("area: click me")
        .fontSize(12)
        .onClick(() => {
          // 改变属性值，配置了属性动画的属性会进行动画过渡
          if (this.flag) {
            this.myWidth = 100;
            this.myHeight = 50;
            this.myColor = Color.Blue;
          } else {
            this.myWidth = 200;
            this.myHeight = 100;
            this.myColor = Color.Pink;
          }
          this.flag = !this.flag;
        })
    }
  }
}
```

上述示例中，第一个button上的animation属性，只对写在animation之前的type、width、height属性生效，而对写在animation之后的backgroundColor、margin属性无效。运行结果是width、height属性会按照animation的动画参数执行动画，而backgroundColor会直接跳变，不会产生动画。效果如下图：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183916.06492086203940663762041982230085:50001231000000:2800:91C5CE56D5EF567C339329FEA802D4C3F91D7C4C0A29EDDFB548ACAADE6CC85D.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

说明

1. 使用属性动画时，会按照指定的属性动画参数执行动画。每个组件可为自己的属性配置不同参数的属性动画。
2. 显式动画会对动画闭包前后造成的所有界面差异执行动画，且使用同一动画参数，适用于统一执行的场景。此外，显式动画也可以用于一些非属性变量造成的动画，如if/else的条件，ForEach使用的数组元素的删减。
3. 如果一个属性配置了属性动画，且在显式动画闭包中改变该属性值，属性动画优先生效，会使用属性动画的动画参数。



# 组件内转场动画

更新时间: 2024-01-15 12:20

组件的插入、删除过程即为组件本身的转场过程，组件的插入、删除动画称为组件内转场动画。通过组件内转场动画，可定义组件出现、消失的效果。

组件内转场动画的接口为：

```
transition(value: TransitionOptions)
```

[transition](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-transition-animation-component-0000001427902496-V3)函数的入参为组件内转场的效果，可以定义平移、透明度、旋转、缩放这几种转场样式的单个或者组合的转场效果，必须和[animateTo](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-layout-update-animation-0000001500356349-V3#section686991962314)一起使用才能产生组件转场效果。

## transition常见用法

type用于指定当前的transition动效生效在组件的变化场景，类型为[TransitionType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__transitiontype)。

* 组件的插入、删除使用同一个动画效果

```
Button()
  .transition({ type: TransitionType.All, scale: { x: 0, y: 0 } })
```

  当type属性为TransitionType.All时，表示指定转场动效生效在组件的所有变化（插入和删除）场景。此时，删除动画和插入动画是相反的过程，删除动画是插入动画的逆播。例如，以上代码定义了一个Button控件。在插入时，组件从scale的x、y均为0的状态，变化到scale的x、y均为1（即完整显示）的默认状态，以逐渐放大的方式出现。在删除时，组件从scale的x、y均为1的默认状态，变化到指定的scale的x、y均为0的状态，逐渐缩小至尺寸为0。
* 组件的插入、删除使用不同的动画效果

```
Button()
  .transition({ type: TransitionType.Insert, translate: { x: 200, y: -200 }, opacity: 0 })
  .transition({ type: TransitionType.Delete, rotate: { x: 0, y: 0, z: 1, angle: 360 } })
```

  当组件的插入和删除需要实现不同的转场动画效果时，可以调用两次transition函数，分别设置type属性为TransitionType.Insert和TransitionType.Delete。例如，以上代码定义了一个Button控件。在插入时，组件从相对于组件正常布局位置x方向平移200vp、y方向平移-200vp的位置、透明度为0的初始状态，变化到x、y方向平移量为0、透明度为1的默认状态，插入动画为平移动画和透明度动画的组合。在删除时，组件从旋转角为0的默认状态，变化到绕z轴旋转360度的终止状态，即绕z轴旋转一周。
* 只定义组件的插入或删除其中一种动画效果。

```
Button()
  .transition({ type: TransitionType.Delete, translate: { x: 200, y: -200 } })
```

  当只需要组件的插入或删除的转场动画效果时，仅需设置type属性为TransitionType.Insert或TransitionType.Delete的transition效果。例如，以上代码定义了一个Button控件。删除时，组件从正常位置、没有平移的默认状态，变化到从相对于正常布局位置x方向平移200vp、y方向平移-200vp的位置的状态。插入该组件并不会产生该组件的转场动画。

## if/else产生组件内转场动画

if/else语句可以控制组件的插入和删除。如下代码即可通过Button的点击事件，控制if的条件是否满足，来控制if下的Image组件是否显示。

```
@Entry
@Component
struct IfElseTransition {
  @State flag: boolean = true;
  @State show: string = 'show';

  build() {
    Column() {
      Button(this.show).width(80).height(30).margin(30)
        .onClick(() => {
          if (this.flag) {
            this.show = 'hide';
          } else {
            this.show = 'show';
          }
          // 点击Button控制Image的显示和消失
          this.flag = !this.flag;
        })
      if (this.flag) {
          Image($r('app.media.mountain')).width(200).height(200)
      }
    }.height('100%').width('100%')
  }
}
```

以上代码没有配置任何动画。接下来，我们将给以上代码加入组件内转场的效果。首先Image组件是由if控制的组件，需要给其加上transition的参数，以指定组件内转场的具体效果。例如，可以如以下代码，给其插入时加上平移效果，删除时加上缩放和透明度效果。

```
if (this.flag) {
  Image($r('app.media.mountain')).width(200).height(200)
    .transition({ type: TransitionType.Insert, translate: { x: 200, y: -200 } })
    .transition({ type: TransitionType.Delete, opacity: 0, scale: { x: 0, y: 0 } })
}
```

以上代码虽然指定了动画的样式，但是未指定动画参数，尚不知道需要用多长时间、怎样的曲线完成该动画。transition必须配合animateTo一起使用，并在animateTo的闭包中，控制组件的插入、删除。对于以上示例代码，即为在animateTo闭包中改变flag的值，该部分代码如下所示。指定动画时长为1000ms，曲线使用animateTo函数默认的曲线，改变flag的值。则由flag变化所引起的一切变化，都会按照该动画参数，产生动画。在这里，flag会影响Image的出现和消失。

```
animateTo({ duration: 1000 }, () => {
  this.flag = !this.flag;
})
```

经过以上过程，当animateTo和transition一起使用时，即产生了组件内转场动画。完整示例代码如下：

```
@Entry
@Component
struct IfElseTransition {
  @State flag: boolean = true;
  @State show: string = 'show';

  build() {
    Column() {
      Button(this.show).width(80).height(30).margin(30)
        .onClick(() => {
          if (this.flag) {
            this.show = 'hide';
          } else {
            this.show = 'show';
          }
          
          animateTo({ duration: 1000 }, () => {
            // 动画闭包内控制Image组件的出现和消失
            this.flag = !this.flag;
          })
        })
      if (this.flag) {
        // Image的出现和消失配置为不同的过渡效果
        Image($r('app.media.mountain')).width(200).height(200)
          .transition({ type: TransitionType.Insert, translate: { x: 200, y: -200 } })
          .transition({ type: TransitionType.Delete, opacity: 0, scale: { x: 0, y: 0 } })
      }
    }.height('100%').width('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183917.74082485703756147376362864655506:50001231000000:2800:41E47EDB7B37BC98F0925B3EC2DB62D106B037F4CD6F9D79AC43A8E98E04485B.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

说明

当配置transition的效果为translate或scale时，本身位置叠加上平移或放大倍数后，动画过程中有可能超过父组件的范围。如果超出父组件的范围时，希望子组件完整的显示，那么可以设置父组件的clip属性为false，使父组件不对子组件产生裁剪。如果超出父组件的范围时，希望超出的子组件部分不显示，那么可以设置父组件的clip属性为true，裁剪掉子组件超出的部分。

## ForEach产生组件内转场动画

和if/else类似，ForEach可以通过控制数组中的元素个数，来控制组件的插入和删除。通过ForEach来产生组件内转场动画，仍然需要两个条件：

* ForEach里的组件配置了transition效果。
* 在animateTo的闭包中控制组件的插入或删除，即控制数组的元素添加和删除。

以下代码是使用ForEach产生组件内转场动画的一个示例。

```
@Entry
@Component
struct ForEachTransition {
  @State numbers: string[] = ["1", "2", "3", "4", "5"]
  startNumber: number = 6;

  build() {
    Column({ space: 10 }) {
      Column() {
        ForEach(this.numbers, (item) => {
          // ForEach下的直接组件需配置transition效果
          Text(item)
            .width(240)
            .height(60)
            .fontSize(18)
            .borderWidth(1)
            .backgroundColor(Color.Orange)
            .textAlign(TextAlign.Center)
            .transition({ type: TransitionType.All, translate: { x: 200 }, scale: { x: 0, y: 0 } })
        }, item => item)
      }
      .margin(10)
      .justifyContent(FlexAlign.Start)
      .alignItems(HorizontalAlign.Center)
      .width("90%")
      .height("70%")

      Button('向头部添加元素')
        .fontSize(16)
        .width(160)
        .onClick(() => {
          animateTo({ duration: 1000 }, () => {
            // 往数组头部插入一个元素，导致ForEach在头部增加对应的组件
            this.numbers.unshift(this.startNumber.toString());
            this.startNumber++;
          })
        })
      Button('向尾部添加元素')
        .width(160)
        .fontSize(16)
        .onClick(() => {
          animateTo({ duration: 1000 }, () => {
            // 往数组尾部插入一个元素，导致ForEach在尾部增加对应的组件
            this.numbers.push(this.startNumber.toString());
            this.startNumber++;
          })
        })
      Button('删除头部元素')
        .width(160)
        .fontSize(16)
        .onClick(() => {
          animateTo({ duration: 1000 }, () => {
            // 删除数组的头部元素，导致ForEach删除头部的组件
            this.numbers.shift();
          })
        })
      Button('删除尾部元素')
        .width(160)
        .fontSize(16)
        .onClick(() => {
          animateTo({ duration: 1000 }, () => {
            // 删除数组的尾部元素，导致ForEach删除尾部的组件
            this.numbers.pop();
          })
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

效果如下图：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183918.93858281535081762776423015131617:50001231000000:2800:27C1A7991FBFCAA4CC9BDDFD3093B25B9F720E5A70E7CEE47267B1DFCD51B51E.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

由于Column布局方式设为了FlexAlign.Start，即竖直方向从头部开始布局。所以往数组末尾添加元素时，并不会对数组中现存元素对应的组件位置造成影响，只会触发新增组件的插入动画。而往数组头部添加元素时，原来数组中的所有元素的下标都增加了，虽然不会触发其添加或者删除，但是会影响到对应组件的位置。所以除新增的组件会做transition动画以外，之前存在于ForEach中组件也会做位置动画。

说明

if/else、ForEach为语法节点，配置组件内转场效果的组件应直接作为语法节点的孩子。由语法节点的增删引起的组件增删，只能触发其直接孩子组件的组件内转场动画，开发者不应期望其对更深层次的组件产生组件转场动画。



# 弹簧曲线动画

更新时间: 2024-01-15 12:21

ArkUI提供了[预置动画曲线](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__curve)，指定了动画属性从起始值到终止值的变化规律，如Linear、Ease、EaseIn等。同时，ArkUI也提供了由弹簧振子物理模型产生的弹簧曲线。通过弹簧曲线，开发者可以设置超过设置的终止值，在终止值附近震荡，直至最终停下来的效果。弹簧曲线的动画效果比其他曲线具有更强的互动性、可玩性。

弹簧曲线的接口包括两类，一类是[springCurve](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-curve-0000001427585072-V3#ZH-CN_TOPIC_0000001523808354__curvesspringcurve9)，另一类是[springMotion](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-curve-0000001427585072-V3#ZH-CN_TOPIC_0000001523808354__curvesspringmotion9)和[responsiveSpringMotion](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-curve-0000001427585072-V3#ZH-CN_TOPIC_0000001523808354__curvesresponsivespringmotion9)，这两种方式都可以产生弹簧曲线。

## 使用springCurve

springCurve的接口为：

```
springCurve(velocity: number, mass: number, stiffness: number, damping: number)
```

构造参数包括初速度，弹簧系统的质量、刚度、阻尼。构建springCurve时，可指定质量为1，根据springCurve中的参数说明，调节刚度、阻尼两个参数，达到想要的震荡效果。

```
import curves from '@ohos.curves';
@Entry
@Component
struct SpringTest {
  @State translateX: number = 0;

  private jumpWithSpeed(speed: number) {
    this.translateX = -1;
    animateTo({ duration: 2000, curve: curves.springCurve(speed, 1, 1, 1.2) }, () => {
      // 以指定初速度进行x方向的平移的弹簧动画
      this.translateX = 0;
    })
  }

  build() {
    Column() {
      Button("button")
        .fontSize(14)
        .width(100)
        .height(50)
        .margin(30)
        .translate({ x: this.translateX })
      Row({space:50}) {
        Button("jump 50").fontSize(14)
          .onClick(() => {
            // 以初速度50的弹簧曲线进行平移
            this.jumpWithSpeed(50);
          })
        Button("jump 200").fontSize(14)
          .onClick(() => {
            // 以初速度200的弹簧曲线进行平移
            this.jumpWithSpeed(200);
          })
      }.margin(30)
    }.height('100%').width('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183918.99764866363706807552419991396607:50001231000000:2800:0B907EF300B71CCE356DDCD0D5227FD89F2FDCA4B916F2EF4EED5311D0251090.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

以上示例中，点击不同的按钮，给定springCurve的不同初速度，button会有“弹性”的到达指定位置，且button的振幅随着速度的增大而变大。另外也可以修改springCurve的质量、刚度、阻尼参数，达到想要的弹性的程度。

说明

速度只是放大了振荡的效果，但系统能否产生振荡的效果，取决于弹簧振子本身的物理参数，即质量、刚度、阻尼三个参数。刚度越小、阻尼越大，springCurve的“弹性”越弱，振荡效果越弱。随着刚度减小或阻尼变大，达到过阻尼状态后，无论速度为多大，都不会有在终点值附近振荡的效果。

## 使用springMotion和responsiveSpringMotion

[springMotion](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-curve-0000001427585072-V3#ZH-CN_TOPIC_0000001523808354__curvesspringmotion9)的接口为：

```
springMotion(response?: number, dampingFraction?: number, overlapDuration?: number)
```

[responsiveSpringMotion](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-curve-0000001427585072-V3#ZH-CN_TOPIC_0000001523808354__curvesresponsivespringmotion9)的接口为：

```
responsiveSpringMotion(response?: number, dampingFraction?: number, overlapDuration?: number)
```

它们的构造参数包括弹簧自然振动周期、阻尼系数、弹性动画衔接时长这三个可选参数，参数的含义请参考其文档。

使用springMotion和responsiveSpringMotion曲线时，duration不生效，适合于跟手动画。

```
import curves from '@ohos.curves';

@Entry
@Component
struct SpringMotionTest {
  @State positionX: number = 100;
  @State positionY: number = 100;
  diameter: number = 50;

  build() {
    Column() {
      Row() {
        Circle({ width: this.diameter, height: this.diameter })
          .fill(Color.Blue)
          .position({ x: this.positionX, y: this.positionY })
          .onTouch((event: TouchEvent) => {
            if (event.type === TouchType.Move) {
              // 跟手过程，使用responsiveSpringMotion曲线
              animateTo({ curve: curves.responsiveSpringMotion() }, () => {
                // 减去半径，以使球的中心运动到手指位置
                this.positionX = event.touches[0].screenX - this.diameter / 2;
                this.positionY = event.touches[0].screenY - this.diameter / 2;
                console.info(`move, animateTo x:${this.positionX}, y:${this.positionY}`);
              })
            } else if (event.type === TouchType.Up) {
              // 离手时，使用springMotion曲线
              animateTo({ curve: curves.springMotion() }, () => {
                this.positionX = 100;
                this.positionY = 100;
                console.info(`touchUp, animateTo x:100, y:100`);
              })
            }
          })
      }
      .width("100%").height("80%")
      .clip(true) // 如果球超出父组件范围，使球不可见
      .backgroundColor(Color.Orange)

      Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Center }) {
        Text("拖动小球").fontSize(16)
      }
      .width("100%")

      Row() {
        Text('点击位置: [x: ' + Math.round(this.positionX) + ', y:' + Math.round(this.positionY) + ']').fontSize(16)
      }
      .padding(10)
      .width("100%")
    }.height('100%').width('100%')
  }
}
```

以上代码是跟手动画的一个示例。通过在onTouch事件中，捕捉触摸的位置，改变组件的translate或者position属性，使其在跟手过程中运动到触摸位置，松手后回到原位置。跟手动画的效果如下：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183918.99013612007164185149404845961462:50001231000000:2800:D3BEB86057369962FD4ECA16E292143141EBF2BD1E972A28A8CF5D919DFBDD83.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

跟手过程推荐使用responsiveSpringMotion曲线，松手过程推荐使用springMotion曲线。跟手过程随着手的位置变化会被多次触发，所以会接连启动多次responsiveSpringMotion动画，松手时启动一次springMotion动画。跟手、松手过程在对同一对象的同一属性上执行动画，且使用了springMotion或responsiveSpringMotion曲线，每次新启动的动画会继承上次动画使用的速度，实现平滑过渡。

说明

1. springCurve可以设置初速度，单一属性存在多个动画时不会互相影响，观察到的是多个动画效果的叠加。
2. springMotion虽然内部有速度机制，但不可由开发者设置。在单一属性存在多个动画时，后一动画会取代前一动画，并继承前一动画的速度。



# 放大缩小视图

更新时间: 2024-01-15 12:20

在不同页面间，有使用相同的元素（例如同一幅图）的场景，可以使用[共享元素转场](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-transition-animation-shared-elements-0000001428061776-V3)动画衔接。为了突出不同页面间相同元素的关联性，可为它们添加共享元素转场动画。如果相同元素在不同页面间的大小有明显差异，即可达到放大缩小视图的效果。

共享元素转场的接口为：

```
sharedTransition(id: string, options?: sharedTransitionOptions)
```

其中根据sharedTransitionOptions中的type参数，共享元素转场分为Exchange类型的共享元素转场和Static类型的共享元素转场。

## Exchange类型的共享元素转场

交换型的共享元素转场，需要两个页面中，存在通过sharedTransition函数配置为相同id的组件，它们称为共享元素。这种类型的共享元素转场适用于两个页面间相同元素的衔接，会从起始页共享元素的位置、大小过渡到目标页的共享元素的位置、大小。如果不指定type，默认为Exchange类型的共享元素转场，这也是最常见的共享元素转场的方式。使用Exchange类型的共享元素转场时，共享元素转场的动画参数由目标页options中的动画参数决定。

## Static类型的共享元素转场

静态型的共享元素转场通常用于页面跳转时，标题逐渐出现或隐藏的场景，只需要在一个页面中有Static的共享元素，不能在两个页面中出现相同id的Static类型的共享元素。在跳转到该页面（即目标页）时，配置Static类型sharedTransition的组件做透明度从0到该组件设定的透明度的动画，位置保持不变。在该页面（即起始页）消失时，做透明度逐渐变为0的动画，位置保持不变。

共享元素转场的动画参数由该组件sharedTransition属性中的动画参数决定。

## 场景示例

下面介绍使用共享元素转场进行放大缩小图片的示例。

```
// src page
import router from '@ohos.router';

@Entry
@Component
struct SharedTransitionSrc {
  build() {
    Column() {
      // 配置Exchange类型的共享元素转场，共享元素id为"sharedImage1"
      Image($r('app.media.mountain')).width(50).height(50)
        .sharedTransition('sharedImage1', { duration: 1000, curve: Curve.Linear })
        .onClick(() => {
          // 点击小图时路由跳转至下一页面
          router.pushUrl({ url: 'pages/myTest/sharedTransitionDst' });
        })
    }
    .padding(10)
    .width("100%")
    .alignItems(HorizontalAlign.Start)
  }
}
```

```
// dest page
import router from '@ohos.router';
@Entry
@Component
struct SharedTransitionDest {
  build() {
    Column() {
      // 配置Static类型的共享元素转场
      Text("SharedTransition dest page")
        .fontSize(16)
        .sharedTransition('text', { duration: 500, curve: Curve.Linear, type: SharedTransitionEffectType.Static })
        .margin({ top: 10 })

      // 配置Exchange类型的共享元素转场，共享元素id为"sharedImage1"
      Image($r('app.media.mountain'))
        .width(150)
        .height(150)
        .sharedTransition('sharedImage1', { duration: 500, curve: Curve.Linear })
        .onClick(() => {
          // 点击图片时路由返回至上一页面
          router.back();
        })
    }
    .width("100%")
    .alignItems(HorizontalAlign.Center)
  }
}
```

上述示例中，第一个页面（src page)和第二个页面（dest page）都配置了id为"sharedImage1"的共享元素转场，使两个页面能匹配到这一组共享元素。从第一个页面跳转到第二个页面时，第一个页面为起始页，第二个页面为目标页。配置id为"sharedImage1"的组件按照目标页中500ms的时长进行共享元素转场，达到放大视图的效果，id为"text"的组件按照配置的Static类型sharedTransition参数中的500ms的时长进行共享元素转场，标题逐渐出现。从第二个页面返回到第一个页面时，第二个页面为起始页，第一个页面为目标页。配置id为"sharedImage1"的组件按照目标页中1000ms的时长进行共享元素转场，缩小为原始视图，id为"text"的组件按照配置的Static类型sharedTransition参数中的500ms的时长进行共享元素转场，标题逐渐隐藏。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183919.92555303250175586956014199772673:50001231000000:2800:65DDDFC2D6F98D690DD1CD78F31673114F46EF734BF1EB1D6D5E53F3327C7507.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")



# 页面转场动画

更新时间: 2024-01-15 12:21

两个页面间发生跳转，一个页面消失，另一个页面出现，这时可以配置各自页面的页面转场参数实现自定义的页面转场效果。[页面转场](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-page-transition-animation-0000001477981233-V3)效果写在pageTransition函数中，通过PageTransitionEnter和PageTransitionExit指定页面进入和退出的动画效果。

PageTransitionEnter的接口为：

```
PageTransitionEnter({type?: RouteType,duration?: number,curve?: Curve | string,delay?: number})
```

PageTransitionExit的接口为：

```
PageTransitionExit({type?: RouteType,duration?: number,curve?: Curve | string,delay?: number})
```

上述接口定义了PageTransitionEnter和PageTransitionExit组件，可通过slide、translate、scale、opacity属性定义不同的页面转场效果。对于PageTransitionEnter而言，这些效果表示入场时起点值，对于PageTransitionExit而言，这些效果表示退场的终点值，这一点与组件转场transition配置方法类似。此外，PageTransitionEnter提供了onEnter接口进行自定义页面入场动画的回调，PageTransitionExit提供了onExit接口进行自定义页面退场动画的回调。

上述接口中的参数type，表示路由生效的类型，这一点开发者容易混淆其含义。页面转场的两个页面，必定有一个页面退出，一个页面进入。如果通过router.pushUrl操作从页面A跳转到页面B，则页面A退出，做页面退场动画，页面B进入，做页面入场动画。如果通过router.back操作从页面B返回到页面A，则页面B退出，做页面退场动画，页面A进入，做页面入场动画。即页面的PageTransitionEnter既可能是由于新增页面(push，入栈)引起的新页面的入场动画，也可能是由于页面返回(back，或pop，出栈)引起的页面栈中老页面的入场动画，为了能区分这两种形式的入场动画，提供了type参数，这样开发者能完全定义所有类型的页面转场效果。

## type配置为RouteType.None

type为RouteType.None表示对页面栈的push、pop操作均生效，type的默认值为RouteType.None。

```
// page A
pageTransition() {
  // 定义页面进入时的效果，从左侧滑入，时长为1200ms，无论页面栈发生push还是pop操作均可生效
  PageTransitionEnter({ type: RouteType.None, duration: 1200 })
    .slide(SlideEffect.Left)
  // 定义页面退出时的效果，向左侧滑出，时长为1000ms，无论页面栈发生push还是pop操作均可生效
  PageTransitionExit({ type: RouteType.None, duration: 1000 })
    .slide(SlideEffect.Left)
}
```

```
// page B
pageTransition() {
  // 定义页面进入时的效果，从右侧滑入，时长为1000ms，无论页面栈发生push还是pop操作均可生效
  PageTransitionEnter({ type: RouteType.None, duration: 1000 })
    .slide(SlideEffect.Right)
  // 定义页面退出时的效果，向右侧滑出，时长为1200ms，无论页面栈发生push还是pop操作均可生效
  PageTransitionExit({ type: RouteType.None, duration: 1200 })
    .slide(SlideEffect.Right)
}
```

假设页面栈为标准实例模式，即页面栈中允许存在重复的页面。可能会有4种场景，对应的页面转场效果如下表。

| 路由操作                                 | 页面A转场效果                                     | 页面B转场效果                                     |
| :--------------------------------------- | :------------------------------------------------ | :------------------------------------------------ |
| router.pushUrl，从页面A跳转到新增的页面B | 页面退出，PageTransitionExit生效，向左侧滑出屏幕  | 页面进入，PageTransitionEnter生效，从右侧滑入屏幕 |
| router.back，从页面B返回到页面A          | 页面进入，PageTransitionEnter生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit生效，向右侧滑出屏幕  |
| router.pushUrl，从页面B跳转到新增的页面A | 页面进入，PageTransitionEnter生效，从左侧滑入屏幕 | 页面退出，PageTransitionExit生效，向右侧滑出屏幕  |
| router.back，从页面A返回到页面B          | 页面退出，PageTransitionExit生效，向左侧滑出屏幕  | 页面进入，PageTransitionEnter生效，从右侧滑入屏幕 |

如果希望pushUrl进入的页面总是从右侧滑入，back时退出的页面总是从右侧滑出，则上表中的第3、4种情况不满足要求，那么需要完整的定义4个页面转场效果。

## type配置为RouteType.Push或RouteType.Pop

type为RouteType.Push表示仅对页面栈的push操作生效，type为RouteType.Pop表示仅对页面栈的pop操作生效。

```
// page A
pageTransition() {
  // 定义页面进入时的效果，从右侧滑入，时长为1200ms，页面栈发生push操作时该效果才生效
  PageTransitionEnter({ type: RouteType.Push, duration: 1200 })
    .slide(SlideEffect.Right)
  // 定义页面进入时的效果，从左侧滑入，时长为1200ms，页面栈发生pop操作时该效果才生效
  PageTransitionEnter({ type: RouteType.Pop, duration: 1200 })
    .slide(SlideEffect.Left)
  // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
  PageTransitionExit({ type: RouteType.Push, duration: 1000 })
    .slide(SlideEffect.Left)
  // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
  PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
    .slide(SlideEffect.Right)
}
```

```
// page B
pageTransition() {
  // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
  PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
    .slide(SlideEffect.Right)
  // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
  PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
    .slide(SlideEffect.Left)
  // 定义页面退出时的效果，向左侧滑出，时长为1200ms，页面栈发生push操作时该效果才生效
  PageTransitionExit({ type: RouteType.Push, duration: 1200 })
    .slide(SlideEffect.Left)
  // 定义页面退出时的效果，向右侧滑出，时长为1200ms，页面栈发生pop操作时该效果才生效
  PageTransitionExit({ type: RouteType.Pop, duration: 1200 })
    .slide(SlideEffect.Right)
}
```

以上代码则完整的定义了所有可能的页面转场样式。假设页面栈为标准实例模式，即页面栈中允许存在重复的页面。可能会有4种场景，对应的页面转场效果如下表。

| 路由操作                                 | 页面A转场效果                                                                     | 页面B转场效果                                                                     |
| :--------------------------------------- | :-------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| router.pushUrl，从页面A跳转到新增的页面B | 页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕  | 页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕 |
| router.back，从页面B返回到页面A          | 页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕  | 页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕   |
| router.pushUrl，从页面B跳转到新增的页面A | 页面进入，PageTransitionEnter且type为RouteType.Push的转场样式生效，从右侧滑入屏幕 | 页面退出，PageTransitionExit且type为RouteType.Push的转场样式生效，向左侧滑出屏幕  |
| router.back，从页面A返回到页面B          | 页面退出，PageTransitionExit且type为RouteType.Pop的转场样式生效，向右侧滑出屏幕   | 页面进入，PageTransitionEnter且type为RouteType.Pop的转场样式生效，从左侧滑入屏幕  |

说明

1. 由于每个页面的页面转场样式都可由开发者独立配置，而页面转场涉及到两个页面，开发者应考虑两个页面的页面转场效果的衔接，如时长尽量保持一致。
2. 如果没有定义匹配的页面转场样式，则该页面使用系统默认的页面转场样式。

## 禁用某页面的页面转场

```
pageTransition() {
  PageTransitionEnter({ type: RouteType.None, duration: 0 })
  PageTransitionExit({ type: RouteType.None, duration: 0 })
}
```

通过设置页面转场的时长为0，可使该页面无页面转场动画。

## 场景示例

下面介绍定义了所有的四种页面转场样式的页面转场动画示例。

```
// PageTransitionSrc1
import router from '@ohos.router';
@Entry
@Component
struct PageTransitionSrc1 {
  build() {
    Column() {
      Image($r('app.media.mountain'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {
            // 路由到下一个页面，push操作
            router.pushUrl({ url: 'pages/myTest/pageTransitionDst1' });
          })
        Button("back")
          .onClick(() => {
            // 返回到上一页面，相当于pop操作
            router.back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%").height("100%")
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {
    // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Right)
    // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Left)
    // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionExit({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Left)
    // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Right)
  }
}
```

```
// PageTransitionDst1
import router from '@ohos.router';
@Entry
@Component
struct PageTransitionDst1 {
  build() {
    Column() {
      Image($r('app.media.forest'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {
            // 路由到下一页面，push操作
            router.pushUrl({ url: 'pages/myTest/pageTransitionSrc1' });
          })
        Button("back")
          .onClick(() => {
            // 返回到上一页面，相当于pop操作
            router.back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%").height("100%")
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {
    // 定义页面进入时的效果，从右侧滑入，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionEnter({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Right)
    // 定义页面进入时的效果，从左侧滑入，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionEnter({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Left)
    // 定义页面退出时的效果，向左侧滑出，时长为1000ms，页面栈发生push操作时该效果才生效
    PageTransitionExit({ type: RouteType.Push, duration: 1000 })
      .slide(SlideEffect.Left)
    // 定义页面退出时的效果，向右侧滑出，时长为1000ms，页面栈发生pop操作时该效果才生效
    PageTransitionExit({ type: RouteType.Pop, duration: 1000 })
      .slide(SlideEffect.Right)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183920.28944752588267170170770714748358:50001231000000:2800:2D0F8A38312DE4868693DE6A61F9C6AE4385A9FE1C4313283107BCD9AC69644A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

下面介绍使用了type为None的页面转场动画示例。

```
// PageTransitionSrc2
import router from '@ohos.router';
@Entry
@Component
struct PageTransitionSrc2 {
  build() {
    Column() {
      Image($r('app.media.mountain'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {
            // 路由到下一页面，push操作
            router.pushUrl({ url: 'pages/myTest/pageTransitionDst2' });
          })
        Button("back")
          .onClick(() => {
            // 返回到上一页面，相当于pop操作
            router.back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%").height("100%")
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {
    // 定义页面进入时的效果，从左侧滑入，时长为1000ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionEnter({ duration: 1000 })
      .slide(SlideEffect.Left)
    // 定义页面退出时的效果，相对于正常页面位置x方向平移100vp，y方向平移100vp，透明度变为0，时长为1200ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionExit({ duration: 1200 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

```
// PageTransitionDst2
import router from '@ohos.router';
@Entry
@Component
struct PageTransitionDst2 {
  build() {
    Column() {
      Image($r('app.media.forest'))
        .width('90%')
        .height('80%')
        .objectFit(ImageFit.Fill)
        .syncLoad(true) // 同步加载图片，使页面出现时图片已经加载完成
        .margin(30)

      Row({ space: 10 }) {
        Button("pushUrl")
          .onClick(() => {
            // 路由到下一页面，push操作
            router.pushUrl({ url: 'pages/myTest/pageTransitionSrc2' });
          })
        Button("back")
          .onClick(() => {
            // 返回到上一页面，相当于pop操作
            router.back();
          })
      }.justifyContent(FlexAlign.Center)
    }
    .width("100%").height("100%")
    .alignItems(HorizontalAlign.Center)
  }

  pageTransition() {
    // 定义页面进入时的效果，从左侧滑入，时长为1200ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionEnter({ duration: 1200 })
      .slide(SlideEffect.Left)
    // 定义页面退出时的效果，相对于正常页面位置x方向平移100vp，y方向平移100vp，透明度变为0，时长为1000ms，无论页面栈发生push还是pop操作均可生效
    PageTransitionExit({ duration: 1000 })
      .translate({ x: 100.0, y: 100.0 })
      .opacity(0)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183920.94226854330135836626570094810133:50001231000000:2800:C54BF37E36CB34BAFCA0EE22AB92CB8C1AF548EE801E8C56E3273A69DE21A53B.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



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



# 触屏事件

更新时间: 2024-01-15 12:20

触屏事件指当手指/手写笔在组件上按下、滑动、抬起时触发的回调事件。包括[点击事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-touch-screen-event-0000001451076450-V3#section348017461591)、[拖拽事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-touch-screen-event-0000001451076450-V3#section523413571914)和[触摸事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-touch-screen-event-0000001451076450-V3#section190612810311)。

图1 触摸事件原理

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.92241939273269651083001202284029:50001231000000:2800:C6E64713CE58EA51AE9D6CA273BD560D49094F7E01431E26EEAEAEDF1FB844D5.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 点击事件

点击事件是指通过手指或手写笔做出一次完整的按下和抬起动作。当发生点击事件时，会触发以下回调函数：

```
onClick(event: (event?: ClickEvent) => void)
```

event参数提供点击事件相对于窗口或组件的坐标位置，以及发生点击的事件源。

例如通过按钮的点击事件控制图片的显示和隐藏。

```
@Entry
@Component
struct IfElseTransition {
  @State flag: boolean = true;
  @State btnMsg: string = 'show';

  build() {
    Column() {
      Button(this.btnMsg).width(80).height(30).margin(30)
        .onClick(() => {
          if (this.flag) {
            this.btnMsg = 'hide';
          } else {
            this.btnMsg = 'show';
          }
          // 点击Button控制Image的显示和消失
          this.flag = !this.flag;
        })
      if (this.flag) {
        Image($r('app.media.icon')).width(200).height(200)
      }
    }.height('100%').width('100%')
  }
}
```

## 拖拽事件

拖拽事件指手指/手写笔长按组件（>=500ms），并拖拽到接收区域释放的事件。拖拽事件触发流程：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.79553760629744196147308102036349:50001231000000:2800:98EB6E6DA9594DCE67DD3B9B64BF0F55EBE28C0227A4CC13B3219B9AF09A03F6.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

拖拽事件的触发通过长按、拖动平移判定，手指平移的距离达到5vp即可触发拖拽事件。ArkUI支持应用内、跨应用的拖拽事件。

拖拽事件提供以下[接口](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-drag-drop-0000001427584820-V3)：

| 接口名称                                                                      | 描述                                                                           |
| :---------------------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| onDragStart(event: (event?: DragEvent, extraParams?: string) => CustomBuilder | DragItemInfo)                                                                  |
| onDragEnter(event: (event?: DragEvent, extraParams?: string) => void)         | 拖拽进入组件接口。DragEvent定义拖拽发生位置，extraParmas表示用户自定义信息     |
| onDragLeave(event: (event?: DragEvent, extraParams?: string) => void)         | 拖拽离开组件接口。DragEvent定义拖拽发生位置，extraParmas表示拖拽事件额外信息。 |
| onDragMove(event: (event?: DragEvent, extraParams?: string) => void)          | 拖拽移动接口。DragEvent定义拖拽发生位置，extraParmas表示拖拽事件额外信息。     |
| onDrop(event: (event?: DragEvent, extraParams?: string) => void)              | 拖拽释放组件接口。DragEvent定义拖拽发生位置，extraParmas表示拖拽事件额外信息。 |

如下是跨窗口拖拽，拖出窗口示例：

```
import image from '@ohos.multimedia.image';

@Entry
@Component
struct Index {
  @State visible: Visibility = Visibility.Visible
  private pixelMapReader = undefined

  aboutToAppear() {
    console.info('begin to create pixmap has info message: ')
    this.createPixelMap()
  }

  createPixelMap() {
    let color = new ArrayBuffer(4 * 96 * 96);
    var buffer = new Uint8Array(color);
    for (var i = 0; i < buffer.length; i++) {
      buffer[i] = (i + 1) % 255;
    }
    let opts = {
      alphaType: 0,
      editable: true,
      pixelFormat: 4,
      scaleMode: 1,
      size: { height: 96, width: 96 }
    }
    const promise = image.createPixelMap(color, opts);
    promise.then((data) => {
      console.info('create pixmap has info message: ' + JSON.stringify(data))
      this.pixelMapReader = data;
    })
  }

  @Builder pixelMapBuilder() {
    Text('drag item')
      .width('100%')
      .height(100)
      .fontSize(16)
      .textAlign(TextAlign.Center)
      .borderRadius(10)
      .backgroundColor(0xFFFFFF)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('App1')
        .width('40%')
        .height(80)
        .fontSize(20)
        .margin(30)
        .textAlign(TextAlign.Center)
        .backgroundColor(Color.Pink)
        .visibility(Visibility.Visible)

      Text('Across Window Drag This')
        .width('80%')
        .height(80)
        .fontSize(16)
        .margin(30)
        .textAlign(TextAlign.Center)
        .backgroundColor(Color.Pink)
        .visibility(this.visible)
        .onDragStart(() => {                    //启动跨窗口拖拽
          console.info('Text onDrag start')
          return { pixelMap: this.pixelMapReader, extraInfo: 'custom extra info.' }
        })
        .onDrop((event: DragEvent, extraParams: string) => {
          console.info('Text onDragDrop,  ')
          this.visible = Visibility.None                    //拖动结束后，使源不可见
        })
    }

    .width('100%')
    .height('100%')
  }
}
```

跨窗口拖拽，拖入示例：

```
@Entry
@Component
struct Index {
  @State number: string[] = ['drag here']
  @State text: string = ''
  @State bool1: boolean = false
  @State bool2: boolean = false
  @State visible: Visibility = Visibility.Visible
  @State visible2: Visibility = Visibility.None
  scroller: Scroller = new Scroller()

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text('App2')
        .width('40%')
        .height(80)
        .fontSize(20)
        .margin(30)
        .textAlign(TextAlign.Center)
        .backgroundColor(Color.Pink)
        .visibility(Visibility.Visible)

      List({ space: 20, initialIndex: 0 }) {
        ForEach(this.number, (item) => {
          ListItem() {
            Text('' + item)
              .width('100%')
              .height(80)
              .fontSize(16)
              .borderRadius(10)
              .textAlign(TextAlign.Center)
              .backgroundColor(0xFFFFFF)
          }
        }, item => item)

        ListItem() {
          Text('Across Window Drag This')
            .width('80%')
            .height(80)
            .fontSize(16)
            .margin(30)
            .textAlign(TextAlign.Center)
            .backgroundColor(Color.Pink)
            .visibility(this.visible2)
        }
      }
      .height('50%')
      .width('90%')
      .border({ width: 1 })
      .divider({ strokeWidth: 2, color: 0xFFFFFF, startMargin: 20, endMargin: 20 })
      .onDragEnter((event: DragEvent, extraParams: string) => {                         //拖拽进去组件
        console.info('List onDragEnter, ' + extraParams)
      })
      .onDragMove((event: DragEvent, extraParams: string) => {                          //拖拽时移动
        console.info('List onDragMove, ' + extraParams)
      })
      .onDragLeave((event: DragEvent, extraParams: string) => {                         //拖拽离开组件
        console.info('List onDragLeave, ' + extraParams)
      })
      .onDrop((event: DragEvent, extraParams: string) => {                              //释放组件
        console.info('List onDragDrop, ' + extraParams)
        this.visible2 = Visibility.Visible                                              //拖拽完成使拖入目标可见
      })
    }
    .width('100%')
    .height('100%')
  }
}
```

## 触摸事件

当手指或手写笔在组件上触碰时，会触发不同动作所对应的事件响应，包括按下（Down）、滑动（Move）、抬起（Up）事件：

```
onTouch(event: (event?: TouchEvent) => void)
```

* event.type为TouchType.Down：表示手指按下。
* event.type为TouchType.Up：表示手指抬起。
* event.type为TouchType.Move：表示手指按住移动。

触摸事件可以同时多指触发，通过event参数可获取触发的手指位置、手指唯一标志、当前发生变化的手指和输入的设备源等信息。

```
// xxx.ets
@Entry
@Component
struct TouchExample {
  @State text: string = '';
  @State eventType: string = '';

  build() {
    Column() {
      Button('Touch').height(40).width(100)
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            this.eventType = 'Down';
          }
          if (event.type === TouchType.Up) {
            this.eventType = 'Up';
          }
          if (event.type === TouchType.Move) {
            this.eventType = 'Move';
          }
          this.text = 'TouchType:' + this.eventType + '\nDistance between touch point and touch element:\nx: '
          + event.touches[0].x + '\n' + 'y: ' + event.touches[0].y + '\nComponent globalPos:('
          + event.target.area.globalPosition.x + ',' + event.target.area.globalPosition.y + ')\nwidth:'
          + event.target.area.width + '\nheight:' + event.target.area.height
        })
      Button('Touch').height(50).width(200).margin(20)
        .onTouch((event: TouchEvent) => {
          if (event.type === TouchType.Down) {
            this.eventType = 'Down';
          }
          if (event.type === TouchType.Up) {
            this.eventType = 'Up';
          }
          if (event.type === TouchType.Move) {
            this.eventType = 'Move';
          }
          this.text = 'TouchType:' + this.eventType + '\nDistance between touch point and touch element:\nx: '
          + event.touches[0].x + '\n' + 'y: ' + event.touches[0].y + '\nComponent globalPos:('
          + event.target.area.globalPosition.x + ',' + event.target.area.globalPosition.y + ')\nwidth:'
          + event.target.area.width + '\nheight:' + event.target.area.height
        })
      Text(this.text)
    }.width('100%').padding(30)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.26639559137043596911390771317569:50001231000000:2800:3388442D26CEB4AA3C8309F31F8A6CE0398DCB298196667E97CAC6502971BBF5.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 键鼠事件

更新时间: 2024-01-15 12:21

键鼠事件指键盘，鼠标外接设备的输入事件。

## 鼠标事件

支持的鼠标事件包含通过外设鼠标、触控板触发的事件。

鼠标事件可触发以下回调：

| 名称                                         | 描述                                                                                                                                                                  |
| :------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| onHover(event: (isHover: boolean) => void)   | 鼠标进入或退出组件时触发该回调。isHover：表示鼠标是否悬浮在组件上，鼠标进入时为true, 退出时为false。                                                                  |
| onMouse(event: (event?: MouseEvent) => void) | 当前组件被鼠标按键点击时或者鼠标在组件上悬浮移动时，触发该回调，event返回值包含触发事件时的时间戳、鼠标按键、动作、鼠标位置在整个屏幕上的坐标和相对于当前组件的坐标。 |

当组件绑定onHover回调时，可以通过[hoverEffect](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-hover-effect-0000001477981177-V3)属性设置该组件的鼠标悬浮态显示效果。

图1 鼠标事件数据流

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.70850655806679963120771428393706:50001231000000:2800:E21F7D619E0EC5BF87750A0ACEC8E802C37E84BDDCAB0FD6872A8613BEC50455.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

鼠标事件传递到ArkUI之后，会先判断鼠标事件是否是左键的按下/抬起/移动，然后做出不同响应：

* 是：鼠标事件先转换成相同位置的触摸事件，执行触摸事件的碰撞测试、手势判断和回调响应。接着去执行鼠标事件的碰撞测试和回调响应。
* 否：事件仅用于执行鼠标事件的碰撞测试和回调响应。

说明

所有单指可响应的触摸事件/手势事件，均可通过鼠标左键来操作和响应。例如当我们需要开发单击Button跳转页面的功能、且需要支持手指点击和鼠标左键点击，那么只绑定一个点击事件（onClick）就可以实现该效果。若需要针对手指和鼠标左键的点击实现不一样的效果，可以在onClick回调中，使用回调参数中的source字段即可判断出当前触发事件的来源是手指还是鼠标。

### onHover

```
onHover(event: (isHover?: boolean) => void)
```

鼠标悬浮事件回调。参数isHover类型为boolean，表示鼠标进入组件或离开组件。该事件不支持自定义冒泡设置，默认父子冒泡。

若组件绑定了该接口，当鼠标指针从组件外部进入到该组件的瞬间会触发事件回调，参数isHover等于true；鼠标指针离开组件的瞬间也会触发该事件回调，参数isHover等于false。

说明

事件冒泡：在一个树形结构中，当子节点处理完一个事件后，再将该事件交给它的父节点处理。

```
// xxx.ets
@Entry
@Component
struct MouseExample {
  @State isHovered: boolean = false;

  build() {
    Column() {
      Button(this.isHovered ? 'Hovered!' : 'Not Hover')
        .width(200).height(100)
        .backgroundColor(this.isHovered ? Color.Green : Color.Gray)
        .onHover((isHover: boolean) => { // 使用onHover接口监听鼠标是否悬浮在Button组件上
          this.isHovered = isHover;
        })
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

该示例创建了一个Button组件，初始背景色为灰色，内容为“Not Hover”。示例中的Button组件绑定了onHover回调，在该回调中将this.isHovered变量置为回调参数：isHover。

当鼠标从Button外移动到Button内的瞬间，回调响应，isHover值等于true，isHovered的值变为true，将组件的背景色改成Color.Green，内容变为“Hovered!”。

当鼠标从Button内移动到Button外的瞬间，回调响应，isHover值等于false，又将组件变成了初始的样式。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.41571006364317589443068562368603:50001231000000:2800:93B1DA82877F98228B05C61CEF05D101ED10D4FA9128BF49F4EE46B57A9DF250.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### onMouse

```
onMouse(event: (event?: MouseEvent) => void)
```

鼠标事件回调。绑定该API的组件每当鼠标指针在该组件内产生行为（MouseAction）时，触发事件回调，参数为[MouseEvent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-mouse-key-0000001478341101-V3#ZH-CN_TOPIC_0000001523648774__mouseevent%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)对象，表示触发此次的鼠标事件。该事件支持自定义冒泡设置，默认父子冒泡。常见用于开发者自定义的鼠标行为逻辑处理。

开发者可以通过回调中的MouseEvent对象获取触发事件的坐标（screenX/screenY/x/y）、按键（[MouseButton](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__mousebutton)）、行为（[MouseAction](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__mouseaction)）、时间戳（timestamp）、交互组件的区域（[EventTarget](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-click-0000001477981153-V3#ZH-CN_TOPIC_0000001523488894__eventtarget8%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)）、事件来源（[SourceType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-gesture-settings-0000001477981181-V3#ZH-CN_TOPIC_0000001523808714__sourcetype%E6%9E%9A%E4%B8%BE%E8%AF%B4%E6%98%8E)）等。MouseEvent的回调函数stopPropagation用于设置当前事件是否阻止冒泡。

说明

按键（MouseButton）的值：Left/Right/Middle/Back/Forward 均对应鼠标上的实体按键，当这些按键被按下或松开时触发这些按键的事件。None表示无按键，会出现在鼠标没有按键按下或松开的状态下，移动鼠标所触发的事件中。

```
// xxx.ets
@Entry
@Component
struct MouseExample {
  @State isHovered: boolean = false;
  @State buttonText: string = '';
  @State columnText: string = '';

  build() {
    Column() {
      Button(this.isHovered ? 'Hovered!' : 'Not Hover')
        .width(200)
        .height(100)
        .backgroundColor(this.isHovered ? Color.Green : Color.Gray)
        .onHover((isHover: boolean) => {
          this.isHovered = isHover
        })
        .onMouse((event: MouseEvent) => {    // 给Button组件设置onMouse回调
          this.buttonText = 'Button onMouse:\n' + '' +
          'button = ' + event.button + '\n' +
          'action = ' + event.action + '\n' +
          'x,y = (' + event.x + ',' + event.y + ')' + '\n' +
          'screenXY=(' + event.screenX + ',' + event.screenY + ')';
        })
      Divider()
      Text(this.buttonText).fontColor(Color.Green)
      Divider()
      Text(this.columnText).fontColor(Color.Red)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .borderWidth(2)
    .borderColor(Color.Red)
    .onMouse((event: MouseEvent) => {    // 给Column组件设置onMouse回调
      this.columnText = 'Column onMouse:\n' + '' +
      'button = ' + event.button + '\n' +
      'action = ' + event.action + '\n' +
      'x,y = (' + event.x + ',' + event.y + ')' + '\n' +
      'screenXY=(' + event.screenX + ',' + event.screenY + ')';
    })
  }
}
```

在onHover示例的基础上，给Button绑定onMouse接口。在回调中，打印出鼠标事件的button/action等回调参数值。同时，在外层的Column容器上，也做相同的设置。整个过程可以分为以下两个动作：

1. 移动鼠标：当鼠标从Button外部移入Button的过程中，仅触发了Column的onMouse回调；当鼠标移入到Button内部后，由于onMouse事件默认是冒泡的，所以此时会同时响应Column的onMouse回调和Button的onMouse回调。此过程中，由于鼠标仅有移动动作没有点击动作，因此打印信息中的button均为0（MouseButton.None的枚举值）、action均为3（MouseAction.Move的枚举值）。
2. 点击鼠标：鼠标进入Button后进行了2次点击，分别是左键点击和右键点击。左键点击时：button = 1（MouseButton.Left的枚举值），按下时 action = 1（MouseAction.Press的枚举值），抬起时 action = 2（MouseAction.Release的枚举值）。

   右键点击时：button = 2（MouseButton.Right的枚举值），按下时 action = 1（MouseAction.Press的枚举值），抬起时 action = 2（MouseAction.Release的枚举值）。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.89991304960755308547060958051626:50001231000000:2800:4E959048BD64E93C258F9A801DBC15F4FA610E402487246C1321C0A9EEADFDDA.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

如果需要阻止鼠标事件冒泡，可以通过调用stopPropagation()方法进行设置。

```
Button(this.isHovered ? 'Hovered!' : 'Not Hover')
  .width(200)
  .height(100)
  .backgroundColor(this.isHovered ? Color.Green : Color.Gray)
  .onHover((isHover: boolean) => {
    this.isHovered = isHover;
  })
  .onMouse((event: MouseEvent) => {
    event.stopPropagation(); // 在Button的onMouse事件中设置阻止冒泡
    this.buttonText = 'Button onMouse:\n' + '' +
    'button = ' + event.button + '\n' +
    'action = ' + event.action + '\n' +
    'x,y = (' + event.x + ',' + event.y + ')' + '\n' +
    'screenXY=(' + event.screenX + ',' + event.screenY + ')';
  })
```

在子组件（Button）的onMouse中，通过回调参数event调用stopPropagation回调方法（如下）即可阻止Button子组件的鼠标事件冒泡到父组件Column上。

```
event.stopPropagation()
```

效果是：当鼠标在Button组件上操作时，仅Button的onMouse回调会响应，Column的onMouse回调不会响应。

### hoverEffect

```
hoverEffect(value: HoverEffect)
```

鼠标悬浮态效果设置的通用属性。参数类型为HoverEffect，HoverEffect提供的Auto、Scale、Highlight效果均为固定效果，开发者无法自定义设置效果参数。

表1 HoverEffect说明| HoverEffect枚举值 | 效果说明 |
| :- | :- |
| ------------------------------- |

| Auto      | 组件默认提供的悬浮态效果，由各组件定义。                                                                                           |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Scale     | 动画播放方式，鼠标悬浮时：组件大小从100%放大至105%，鼠标离开时：组件大小从105%缩小至100%。                                         |
| Highlight | 动画播放方式，鼠标悬浮时：组件背景色叠加一个5%透明度的白色，视觉效果是组件的原有背景色变暗，鼠标离开时：组件背景色恢复至原有样式。 |
| None      | 禁用悬浮态效果                                                                                                                     |

```
// xxx.ets
@Entry
@Component
struct HoverExample {
  build() {
    Column({ space: 10 }) {
      Button('Auto')
        .width(170).height(70)
      Button('Scale')
        .width(170).height(70)
        .hoverEffect(HoverEffect.Scale)
      Button('Highlight')
        .width(170).height(70)
        .hoverEffect(HoverEffect.Highlight)
      Button('None')
        .width(170).height(70)
        .hoverEffect(HoverEffect.None)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.58090470209236308277489980345227:50001231000000:2800:83B261F1A7118CB7CF683E2A4B78E38A0846AFD87976A40E5464B8E4B487FB08.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

Button默认的悬浮态效果就是缩放效果，因此Auto和Scale的效果一样，Highlight会使背板颜色变暗，None会禁用悬浮态效果。

## 按键事件

图2 按键事件数据流

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.25505103564641540285533826287924:50001231000000:2800:6FE6F31DC635BA359B8357056A039EA676D663D97ED8BC9AEFE166206048FECE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

按键事件由外设键盘等设备触发，经驱动和多模处理转换后发送给当前获焦的窗口。窗口获取到事件后，会先给输入法分发（输入法会消费按键用作输入），若输入法未消费该按键事件，才会将事件发给ArkUI框架。因此，当某输入框组件获焦，且打开了输入法，此时大部分按键事件均会被输入法消费，例如字母键会被输入法用来往输入框中输入对应字母字符、方向键会被输入法用来切换选中备选词。

按键事件到ArkUI框架之后，会先找到完整的父子节点获焦链。从叶子节点到根节点，逐一发送按键事件。

### onKeyEvent

```
onKeyEvent(event: (event?: KeyEvent) => void)
```

按键事件回调，当绑定该方法的组件处于[获焦状态](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3)下，外设键盘的按键事件会触发该API的回调响应，回调参数为[KeyEvent](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-events-key-0000001427744780-V3#ZH-CN_TOPIC_0000001523488578__keyevent%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)，可由该参数获得当前按键事件的按键行为（[KeyType](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__keytype)）、键码（[keyCode](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-keycode-0000001544703985-V3#ZH-CN_TOPIC_0000001523488694__keycode)）、按键英文名称（keyText）、事件来源设备类型（[KeySource](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-appendix-enums-0000001478061741-V3#ZH-CN_TOPIC_0000001574248789__keysource)）、事件来源设备id（deviceId）、元键按压状态（metaKey）、时间戳（timestamp）、阻止冒泡设置（stopPropagation）。

```
// xxx.ets
@Entry
@Component
struct KeyEventExample {
  @State buttonText: string = '';
  @State buttonType: string = '';
  @State columnText: string = '';
  @State columnType: string = '';

  build() {
    Column() {
      Button('onKeyEvent')
        .width(140).height(70)
        .onKeyEvent((event: KeyEvent) => { // 给Button设置onKeyEvent事件
          if (event.type === KeyType.Down) {
            this.buttonType = 'Down';
          }
          if (event.type === KeyType.Up) {
            this.buttonType = 'Up';
          }
          this.buttonText = 'Button: \n' +
          'KeyType:' + this.buttonType + '\n' +
          'KeyCode:' + event.keyCode + '\n' +
          'KeyText:' + event.keyText;
        })

      Divider()
      Text(this.buttonText).fontColor(Color.Green)

      Divider()
      Text(this.columnText).fontColor(Color.Red)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    .onKeyEvent((event: KeyEvent) => { // 给父组件Column设置onKeyEvent事件
      if (event.type === KeyType.Down) {
        this.columnType = 'Down';
      }
      if (event.type === KeyType.Up) {
        this.columnType = 'Up';
      }
      this.columnText = 'Column: \n' +
      'KeyType:' + this.buttonType + '\n' +
      'KeyCode:' + event.keyCode + '\n' +
      'KeyText:' + event.keyText;
    })
  }
}
```

上述示例中给组件Button和其父容器Column绑定onKeyEvent。应用打开页面加载后，组件树上第一个可获焦的非容器组件自动获焦，该应用只有一个Button组件，因此该组件会自动获焦，由于Button是Column的子节点，Button获焦也同时意味着Column获焦。获焦机制见[焦点事件](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3)。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183921.74209484332555094655296163918479:50001231000000:2800:6D9527B0C719538826FF13DA4FB631A7D9985D2A903B02C1ABDDDC9AF80509E3.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

打开应用后，依次在键盘上按这些按键：“空格、回车、左Ctrl、左Shift、字母A、字母Z”。

1. 由于onKeyEvent事件默认是冒泡的，所以Button和Column的onKeyEvent都可以响应。
2. 每个按键都有2次回调，分别对应KeyType.Down和KeyType.Up，表示按键被按下、然后抬起。

如果要阻止冒泡，即仅Button响应键盘事件，Column不响应，在Button的onKeyEvent回调中加入event.stopPropagation()方法即可，如下：

```
Button('onKeyEvent')
  .width(140).height(70)
  .onKeyEvent((event: KeyEvent) => {
    // 通过stopPropagation阻止事件冒泡
    event.stopPropagation();
    if (event.type === KeyType.Down) {
      this.buttonType = 'Down';
    }
    if (event.type === KeyType.Up) {
       this.buttonType = 'Up';
    }
     this.buttonText = 'Button: \n' +
     'KeyType:' + this.buttonType + '\n' +
     'KeyCode:' + event.keyCode + '\n' +
     'KeyText:' + event.keyText;
})
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183922.83404024110731712946703172523019:50001231000000:2800:B61DBAE64F20F8B5EDD709772EC5C21C5342E633DBB46A28F03B124D2F709ED5.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)



# 焦点事件

更新时间: 2024-01-15 12:21

## 基本概念

* 焦点指向当前应用界面上唯一的一个可交互元素，当用户使用键盘、电视遥控器、车机摇杆/旋钮等非指向性输入设备与应用程序进行间接交互时，基于焦点的导航和交互是重要的输入手段。

* 默认焦点应用打开或切换页面后，若当前页上存在可获焦的组件，则树形结构的组件树中第一个可获焦的组件默认获得焦点。可以使用[自定义默认焦点](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section171125411552)进行自定义指定。
* 获焦指组件获得了焦点，同一时刻，应用中最多只有1个末端组件是获焦的，且此时它的所有祖宗组件（整个组件链）均是获焦的。当期望某个组件获焦，须确保该组件及其所有的祖宗节点均是可获焦的（[focusable](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section39379335537)属性为true）。
* 失焦指组件从获焦状态变成了非获焦状态，失去了焦点。组件失焦时，它的所有祖宗组件（失焦组件链）与新的获焦组件链不相同的节点都会失焦。
* 走焦表示焦点在当前应用中转移的过程，走焦会带来原焦点组件的失焦和新焦点组件的获焦。应用中焦点发生变化的方式按行为可分为两类：

  * 主动走焦：指开发者/用户主观的行为导致焦点移动，包含：外接键盘上按下TAB/方向键、使用[requestFocus](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section575715264209)主动给指定组件申请焦点、组件[focusOnTouch](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section18413926142017)属性为true后点击组件。
  * 被动走焦：指组件焦点因其他操作被动的转移焦点，此特性为焦点系统默认行为，无法由开发者自由设定，例如当使用if-else语句将处于获焦的组件删除/将处于获焦的组件（或其父组件）置成不可获焦时、当页面切换时。
* 焦点态获焦组件的样式，不同组件的焦点态样式大同小异，默认情况下焦点态不显示，仅使用外接键盘按下TAB键/方向键时才会触发焦点态样式出现。首次触发焦点态显示的TAB键/方向键不会触发走焦。当应用接收到点击事件时（包括手指触屏的按下事件和鼠标左键的按下事件），自动隐藏焦点态样式。焦点态样式由后端组件定义，开发者无法修改。

## 走焦规则

走焦规则是指用户使用“TAB键/SHIFT+TAB键/方向键”主动进行走焦，或焦点系统在执行被动走焦时的顺序规则。组件的走焦规则默认由走焦系统定义，由焦点所在的容器决定。

* 线性走焦：常见的容器有Flex、Row、Column、List，这些都是典型的单方向容器，组件在这些容器内的排列都是线性的，那么走焦规则也是线性的。走焦的方向和方向键的方向一致。
  图1 线性走焦示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.25702503225803755273941022132954:50001231000000:2800:4F939934A2B4B8C06BE2673E02884184413CFF17A45638157C85178981BA73BE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
  例如Row容器，使用方向键左右（←/→）即可将焦点在相邻的2个可获焦组件之间来回切换。
* 十字走焦：使用方向键上(↑)下(↓)左(←)右(→)可以使焦点在相邻的组件上切换。典型的是Grid容器，如下图：
  图2 Grid组件十字走焦示意图
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.27694438892253040633871447766659:50001231000000:2800:7A3154C69658CE4C24B60E5D76FA419B6D37529DC7256777438E7F40A6D1017E.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

  说明

  * TAB/SHIFT+TAB键在以上两种走焦规则上的功能和方向键一致。TAB键等同于“先执行方向键右，若无法走焦，再执行方向键下”，SHIFT+TAB键等同于“先执行方向键左，若无法走焦，再执行方向键上”。
  * 触发走焦的按键是按下的事件（DOWN事件）。
  * 删除组件、设置组件无法获焦后，会使用线性走焦规则，自动先往被删除/Unfocusable组件的前置兄弟组件上走焦，无法走焦的话，再往后置兄弟组件上走焦。
* tabIndex走焦：给组件设置[tabIndex](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-focus-0000001478061677-V3)通用属性，自定义组件的TAB键/SHIFT+TAB键的走焦顺序。
* 区域走焦：给容器组件设置tabIndex通用属性，再结合[groupDefaultFocus](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section10159926142016)通用属性，自定义容器区域的TAB键/SHIFT+TAB键的走焦顺序和默认获焦组件。
* 走焦至容器组件规则：当焦点走焦到容器（该容器没有配置groupDefaultFocus）上时，若该容器组件为首次获焦，则会先计算目标容器组件的子组件的区域位置，得到距离目标容器中心点最近的子组件，焦点会走到目标容器上的该子组件上。若该容器非首次获焦，焦点会自动走焦到上一次目标容器中获焦的子组件。
* 焦点交互：当某组件获焦时，该组件的固有点击任务或开发者绑定的onClick回调任务，会自动挂载到空格/回车按键上，当按下按键时，任务就和手指/鼠标点击一样被执行。

说明

本文涉及到的焦点均为组件焦点，另外一个焦点的概念是：窗口焦点，指向当前获焦的窗口。当窗口失焦时，该窗口应用中的所有获焦组件全部失焦。

## 监听组件的焦点变化

```
onFocus(event: () => void)
```

获焦事件回调，绑定该API的组件获焦时，回调响应。

```
onBlur(event:() => void)
```

失焦事件回调，绑定该API的组件失焦时，回调响应。

onFocus和onBlur两个接口通常成对使用，来监听组件的焦点变化。

以下示例代码展示获焦/失焦回调的使用方法：

```
// xxx.ets
@Entry
@Component
struct FocusEventExample {
  @State oneButtonColor: Color = Color.Gray;
  @State twoButtonColor: Color = Color.Gray;
  @State threeButtonColor: Color = Color.Gray;

  build() {
    Column({ space: 20 }) {
      // 通过外接键盘的上下键可以让焦点在三个按钮间移动，按钮获焦时颜色变化，失焦时变回原背景色
      Button('First Button')
        .width(260)
        .height(70)
        .backgroundColor(this.oneButtonColor)
        .fontColor(Color.Black)
          // 监听第一个组件的获焦事件，获焦后改变颜色
        .onFocus(() => {
          this.oneButtonColor = Color.Green;
        })
          // 监听第一个组件的失焦事件，失焦后改变颜色
        .onBlur(() => {
          this.oneButtonColor = Color.Gray;
        })

      Button('Second Button')
        .width(260)
        .height(70)
        .backgroundColor(this.twoButtonColor)
        .fontColor(Color.Black)
          // 监听第二个组件的获焦事件，获焦后改变颜色
        .onFocus(() => {
          this.twoButtonColor = Color.Green;
        })
          // 监听第二个组件的失焦事件，失焦后改变颜色
        .onBlur(() => {
          this.twoButtonColor = Color.Grey;
        })

      Button('Third Button')
        .width(260)
        .height(70)
        .backgroundColor(this.threeButtonColor)
        .fontColor(Color.Black)
          // 监听第三个组件的获焦事件，获焦后改变颜色
        .onFocus(() => {
          this.threeButtonColor = Color.Green;
        })
          // 监听第三个组件的失焦事件，失焦后改变颜色
        .onBlur(() => {
          this.threeButtonColor = Color.Gray ;
        })
    }.width('100%').margin({ top: 20 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.39065820623301072413498377733999:50001231000000:2800:64D616DF4A1476BBB7478AA25EDDEF1F31F973EED3F4A160A0812AD67F9E67FD.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

上述示例包含以下4步：

1. 应用打开时，“First Button”默认获取焦点，onFocus回调响应，背景色变成绿色。
2. 按下TAB键（或方向键下↓），“First Button”显示焦点态样式：组件外围有一个蓝色的闭合框。不触发走焦，焦点仍然在“First Button”上。
3. 按下TAB键（或方向键下↓），触发走焦，“Second Button”获焦，onFocus回调响应，背景色变成绿色；“First Button”失焦、onBlur回调响应，背景色变回灰色。
4. 按下TAB键（或方向键下↓），触发走焦，“Third Button”获焦，onFocus回调响应，背景色变成绿色；“Second Button”失焦、onBlur回调响应，背景色变回灰色。

## 设置组件是否获焦

通过focusable接口设置组件是否可获焦：

```
focusable(value: boolean)
```

按照组件的获焦能力可大致分为三类：

* 默认可获焦的组件，通常是有交互行为的组件，例如Button、Checkbox，TextInput组件，此类组件无需设置任何属性，默认即可获焦。
* 有获焦能力，但默认不可获焦的组件，典型的是Text、Image组件，此类组件缺省情况下无法获焦，若需要使其获焦，可使用通用属性focusable(true)使能。
* 无获焦能力的组件，通常是无任何交互行为的展示类组件，例如Blank、Circle组件，此类组件即使使用focusable属性也无法使其可获焦。

说明

* focusable为false表示组件不可获焦，同样可以使组件变成不可获焦的还有通用属性[enabled](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-universal-attributes-enable-0000001427584828-V3)。
* 当某组件处于获焦状态时，将其的focusable属性或enabled属性设置为false，会自动使该组件失焦，然后焦点按照[走焦规则](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section772713441042)将焦点转移给其他组件。

表1 基础组件获焦能力| 基础组件 | 是否有获焦能力 | focusable默认值 | 走焦规则 |
| :- | :- | :- | :- |
| ------------------------------------------------------- |

| AlphabetIndexer | 是 | true  | 线性走焦      |
| --------------- | -- | ----- | ------------- |
| Blank           | 否 | false | /             |
| Button          | 是 | true  | /             |
| Checkbox        | 是 | true  | /             |
| CheckboxGroup   | 是 | true  | /             |
| DataPanel       | 否 | false | /             |
| DatePicker      | 是 | true  | 线性走焦      |
| Divider         | 否 | false | /             |
| Gauge           | 否 | false | /             |
| Image           | 是 | false | /             |
| ImageAnimator   | 是 | false | /             |
| LoadingProgress | 否 | false | /             |
| Marquee         | 否 | false | /             |
| Menu            | 是 | true  | 线性走焦      |
| MenuItem        | 是 | true  | /             |
| MenuItemGroup   | 是 | true  | 线性走焦      |
| Navigation      | 否 | false | 组件自定义    |
| NavRouter       | 否 | false | 跟随子容器    |
| NavDestination  | 否 | false | 线性走焦      |
| PatternLock     | 否 | false | /             |
| Progress        | 否 | false | /             |
| QRCode          | 否 | false | /             |
| Radio           | 是 | true  | /             |
| Rating          | 是 | true  | /             |
| RichText        | 否 | false | /             |
| ScrollBar       | 否 | false | /             |
| Search          | 是 | true  | /             |
| Select          | 是 | true  | 线性走焦      |
| Slider          | 是 | true  | /             |
| Span            | 否 | false | /             |
| Stepper         | 是 | true  | /             |
| StepperItem     | 是 | true  | /             |
| Text            | 是 | false | /             |
| TextArea        | 是 | true  | /             |
| TextClock       | 否 | false | /             |
| TextInput       | 是 | true  | /             |
| TextPicker      | 是 | true  | 线性走焦      |
| TextTimer       | 否 | false | /             |
| TimePicker      | 是 | true  | 线性走焦      |
| Toggle          | 是 | true  | /             |
| Web             | 是 | true  | Web组件自定义 |
| XComponent      | 否 | false | /             |

表2 容器组件获焦能力| 容器组件 | 是否可获焦 | focusable默认值 | 走焦规则 |
| :- | :- | :- | :- |
| --------------------------------------------------- |

| Badge             | 否 | false | /              |
| ----------------- | -- | ----- | -------------- |
| Column            | 是 | true  | 线性走焦       |
| ColumnSplit       | 是 | true  | /              |
| Counter           | 是 | true  | 线性走焦       |
| Flex              | 是 | true  | 线性走焦       |
| GridCol           | 是 | true  | 容器组件自定义 |
| GridRow           | 是 | true  | 容器组件自定义 |
| Grid              | 是 | true  | 容器组件自定义 |
| GridItem          | 是 | true  | 跟随子组件     |
| List              | 是 | true  | 线性走焦       |
| ListItem          | 是 | true  | 跟随子组件     |
| ListItemGroup     | 是 | true  | 跟随List组件   |
| Navigator         | 否 | true  | 容器组件自定义 |
| Panel             | 否 | true  | 跟随子组件     |
| Refresh           | 否 | false | /              |
| RelativeContainer | 否 | true  | 容器组件自定义 |
| Row               | 是 | true  | 线性走焦       |
| RowSplit          | 是 | true  | /              |
| Scroll            | 是 | true  | 线性走焦       |
| SideBarContainer  | 是 | true  | 线性走焦       |
| Stack             | 是 | true  | 线性走焦       |
| Swiper            | 是 | true  | 容器组件自定义 |
| Tabs              | 是 | true  | 容器组件自定义 |
| TabContent        | 是 | true  | 跟随子组件     |

表3 媒体组件获焦能力| 媒体组件 | 是否可获焦 | focusable默认值 | 走焦规则 |
| :- | :- | :- | :- |
| --------------------------------------------------- |

| Video | 是 | true | / |
| ----- | -- | ---- | - |

表4 画布组件获焦能力| 画布组件 | 是否可获焦 | focusable默认值 | 走焦规则 |
| :- | :- | :- | :- |
| --------------------------------------------------- |

| Canvas | 否 | false | / |
| ------ | -- | ----- | - |

以下示例为大家展示focusable接口的使用方法：

```
// xxx.ets
@Entry
@Component
struct FocusableExample {
  @State textFocusable: boolean = true;
  @State color1: Color = Color.Yellow;
  @State color2: Color = Color.Yellow;

  build() {
    Column({ space: 5 }) {
      Text('Default Text')    // 第一个Text组件未设置focusable属性，默认不可获焦
        .borderColor(this.color1)
        .borderWidth(2)
        .width(300)
        .height(70)
        .onFocus(() => {
          this.color1 = Color.Blue;
        })
        .onBlur(() => {
          this.color1 = Color.Yellow;
        })
      Divider()

      Text('focusable: ' + this.textFocusable)    // 第二个Text设置了focusable属性，初始值为true
        .borderColor(this.color2)
        .borderWidth(2)
        .width(300)
        .height(70)
        .focusable(this.textFocusable)
        .onFocus(() => {
          this.color2 = Color.Blue;
        })
        .onBlur(() => {
          this.color2 = Color.Yellow;
        })

      Divider()

      Row() {
        Button('Button1')
          .width(140).height(70)
        Button('Button2')
          .width(160).height(70)
      }

      Divider()
      Button('Button3')
        .width(300).height(70)

      Divider()
    }.width('100%').justifyContent(FlexAlign.Center)
    .onKeyEvent((e) => {    // 绑定onKeyEvent，在该Column组件获焦时，按下'F'键，可将第二个Text的focusable置反
      if (e.keyCode === 2022 && e.type === KeyType.Down) {
        this.textFocusable = !this.textFocusable;
      }
    })
  }
}
```

运行效果：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.07623555428879286720246543581811:50001231000000:2800:C54E1BF2705FA595C727CB12C9EAFF719A59BC038FEB90EE4EA4619DDC57DED3.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

上述示例包含默认获焦和主动走焦两部分：

默认获焦：

* 根据[默认焦点](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#ZH-CN_TOPIC_0000001573929209__li103868415218)的说明，该应用打开后，默认第一个可获焦元素获焦：
* 第一个Text组件没有设置focusable(true)属性，该Text组件无法获焦。
* 第二个Text组件的focusable属性显式设置为true，说明该组件可获焦，那么默认焦点将置到它身上。

主动走焦：

按键盘F键，触发onKeyEvent，focusable置为false，Text组件变成不可获焦，焦点自动转移，按照[被动走焦](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#ZH-CN_TOPIC_0000001573929209__li1307183710313)中的说明项，焦点会自动从Text组件先向上寻找下一个可获焦组件，由于上一个组件是一个不可获焦的Text，所以向下寻找下一个可获焦的组件，找到并使焦点转移到Row容器上，根据[走焦至容器规则](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section772713441042)，计算Button1和Button2的位置，Button2比Button1更大，因此焦点会自动转移到Button2上。

## 自定义默认焦点

```
defaultFocus(value: boolean)
```

焦点系统在页面初次构建完成时，会搜索当前页下的所有组件，找到第一个绑定了defaultFocus(true)的组件，然后将该组件置为默认焦点，若无任何组件绑定defaultFocus(true)，则将第一个找到的可获焦的组件置为默认焦点。

以如下应用为例，应用布局如下：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.98533855599908613540300548305321:50001231000000:2800:720C7FDFCBB2D449BA5C6AB152A0824820A5B2E0D1044FD000A8CDB061EEFEDE.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

以下是实现该应用的示例代码，且示例代码中没有设置defaultFocus：

```
// xxx.ets
import promptAction from '@ohos.promptAction';

class MyDataSource implements IDataSource {
  private list: number[] = [];
  private listener: DataChangeListener;

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): any {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this.listener = listener;
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController()
  private data: MyDataSource = new MyDataSource([])

  aboutToAppear(): void {
    let list = []
    for (let i = 1; i <= 4; i++) {
      list.push(i.toString());
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Row({ space: 20 }) {
            Column() {
              Button('1').width(200).height(200)
                .fontSize(40)
                .backgroundColor('#dadbd9')
            }

            Column({ space: 20 }) {
              Row({ space: 20 }) {
                Button('2')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
                Button('3')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
              }

              Row({ space: 20 }) {
                Button('4')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
                Button('5')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
              }

              Row({ space: 20 }) {
                Button('6')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
                Button('7')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
              }
            }
          }
          .width(480)
          .height(380)
          .justifyContent(FlexAlign.Center)
          .borderWidth(2)
          .borderColor(Color.Gray)
          .backgroundColor(Color.White)
        }, item => item)
      }
      .cachedCount(2)
      .index(0)
      .interval(4000)
      .indicator(true)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .curve(Curve.Linear)
      .onChange((index: number) => {
        console.info(index.toString());
      })
      .margin({ left: 20, top: 20, right: 20 })

      Row({ space: 40 }) {
        Button('←')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .fontColor(Color.Black)
          .backgroundColor(Color.Transparent)
          .onClick(() => {
            this.swiperController.showPrevious();
          })
        Button('→')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .fontColor(Color.Black)
          .backgroundColor(Color.Transparent)
          .onClick(() => {
            this.swiperController.showNext();
          })
      }
      .width(480)
      .height(50)
      .justifyContent(FlexAlign.Center)
      .borderWidth(2)
      .borderColor(Color.Gray)
      .backgroundColor('#f7f6dc')

      Row({ space: 40 }) {
        Button('Cancel')
          .fontSize(30)
          .fontColor('#787878')
          .type(ButtonType.Normal)
          .width(140)
          .height(50)
          .backgroundColor('#dadbd9')
        
        Button('OK')
          .fontSize(30)
          .fontColor('#787878')
          .type(ButtonType.Normal)
          .width(140)
          .height(50)
          .backgroundColor('#dadbd9')
          .onClick(() => {
            promptAction.showToast({ message: 'Button OK on clicked' });
          })
      }
      .width(480)
      .height(80)
      .justifyContent(FlexAlign.Center)
      .borderWidth(2)
      .borderColor(Color.Gray)
      .backgroundColor('#dff2e4')
      .margin({ left: 20, bottom: 20, right: 20 })
    }.backgroundColor('#f2f2f2')
    .margin({ left: 50, top: 50, right: 20 })
  }
}
```

当前应用上无任何defaultFocus设置，所以第一个可获焦的组件默认获取焦点，按下TAB键/方向键让获焦的组件显示焦点态样式：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.92124079650710211806698429555178:50001231000000:2800:5418DC105DCFC7ECBEEBDEF58519544C3B9C837EC062BF66CDB2033D10717D9E.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

假设开发者想让应用打开的时候，无需执行多余的切换焦点操作，直接点击按键的空格/回车键，就可以执行Button-OK的onClick回调操作，那么就可以给这个Button绑定defaultFocus(true)，让它成为该页面上的默认焦点：

```
Button('OK')
  .defaultFocus(true)    // 设置Button-OK为defaultFocus
  .fontSize(30)
  .fontColor('#787878')
  .type(ButtonType.Normal)
  .width(140).height(50).backgroundColor('#dadbd9')
  .onClick(() => {
    promptAction.showToast({ message: 'Button OK on clicked' });
  })
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.35865723821945437080706644386536:50001231000000:2800:A46C76A0C4CC07EDC6E5BB202AB7CCFDEDA0EF4D31692A6A4B7DEFA0B422B234.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

打开应用后按TAB键，Button-OK显示了焦点态，说明默认焦点变更到了Button-OK上。然后按下空格，响应了Button-OK的onClick事件。

## 自定义TAB键走焦顺序

```
tabIndex(index: number)
```

tabIndex用于设置自定义TAB键走焦顺序，默认值为0。使用“TAB/Shift+TAB键”走焦时（方向键不影响），系统会自动获取到所有配置了tabIndex大于0的组件，然后按照递增/递减排序进行走焦。

以[defaultFocus](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section171125411552)提供的示例为例，默认情况下的走焦顺序如下：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.17253452402691149882277685067936:50001231000000:2800:CB5AF59B7D3514F73D774F5E0F52C037EF1633167444D3C69990CFF4735EF9E4.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

默认的走焦顺序从第一个获焦组件一路走到最后一个获焦组件，会经历Button1->Button4->Button5->Button7->左箭头->右箭头->ButtonOK。这种走焦队列比较完整，遍历了大部分的组件。但缺点是从第一个走到最后一个所经历的路径较长。

如果想实现快速的从第一个走到最后一个，又不想牺牲太多的遍历完整性，就可以使用tabIndex通用属性。

比如：开发者把白色的区域当为一个整体，黄色的区域当为一个整体，绿色的区域当为一个整体，实现Button1->左箭头->ButtonOK这种队列的走焦顺序，只需要在Button1、左箭头、ButtonOK这三个组件上依次增加tabIndex(1)、tabIndex(2)、tabIndex(3)。tabIndex的参数表示TAB走焦的顺序（从大于0的数字开始，从小到大排列）。

```
  Button('1').width(200).height(200)
    .fontSize(40)
    .backgroundColor('#dadbd9')
    .tabIndex(1)    // Button-1设置为第一个tabIndex节点
```

```
  Button('←')
    .fontSize(40)
    .fontWeight(FontWeight.Bold)
    .fontColor(Color.Black)
    .backgroundColor(Color.Transparent)
    .onClick(() => {
      this.swiperController.showPrevious();
    })
    .tabIndex(2)    // Button-左箭头设置为第二个tabIndex节点
```

```
Button('OK')
  .fontSize(30)
  .fontColor('#787878')
  .type(ButtonType.Normal)
  .width(140).height(50).backgroundColor('#dadbd9')
  .onClick(() => {
    promptAction.showToast({ message: 'Button OK on clicked' });
  })
  .tabIndex(3)    // Button-OK设置为第三个tabIndex节点
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.80999271011369766011953570766277:50001231000000:2800:511F85857AE5560DD26183515961C580647A8040B789C7631C75235DE68830DF.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

说明

* 当焦点处于tabIndex(大于0)节点上时，TAB/ShiftTAB会优先在tabIndex(大于0)的队列中寻找后置/前置的节点，存在则走焦至相应的tabIndex节点。若不存在，则使用默认的走焦逻辑继续往后/往前走焦。
* 当焦点处于tabIndex(等于0)节点上时，TAB/ShiftTAB使用默认的走焦逻辑走焦，走焦的过程中会跳过tabIndex(大于0)和tabIndex(小于0）的节点。
* 当焦点处于tabIndex(小于0)节点上时，TAB/ShiftTAB无法走焦。

### groupDefaultFocus

```
groupDefaultFocus(value: boolean)
```

[自定义TAB键走焦顺序](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#section1537973935515)中所展示的使用tabIndex完成快速走焦的能力有如下问题：

每个区域（白色/黄色/绿色三个区域）都设置了某个组件为tabIndex节点（白色-Button1、黄色-左箭头、绿色-ButtonOK），但这样设置之后，只能在这3个组件上按TAB/ShiftTab键走焦时会有快速走焦的效果。

解决方案是给每个区域的容器设置tabIndex，但是这样设置的问题是：第一次走焦到容器上时，获焦的子组件是默认的第一个可获焦组件，并不是自己想要的组件（Button1、左箭头、ButtonOK）。

这样便引入了groupDefaultFocus通用属性，参数：boolean，默认值：false。

用法需和tabIndex组合使用，使用tabIndex给区域（容器）绑定走焦顺序，然后给Button1、左箭头、ButtonOK绑定groupDefaultFocus(true)，这样在首次走焦到目标区域（容器）上时，它的绑定了groupDefaultFocus(true)的子组件同时获得焦点。

```
// xxx.ets
import promptAction from '@ohos.promptAction';

class MyDataSource implements IDataSource {
  private list: number[] = [];
  private listener: DataChangeListener;

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): any {
    return this.list[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this.listener = listener;
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct SwiperExample {
  private swiperController: SwiperController = new SwiperController()
  private data: MyDataSource = new MyDataSource([])

  aboutToAppear(): void {
    let list = []
    for (let i = 1; i <= 4; i++) {
      list.push(i.toString());
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (item: string) => {
          Row({ space: 20 }) {    // 设置该Row组件为tabIndex的第一个节点
            Column() {
              Button('1').width(200).height(200)
                .fontSize(40)
                .backgroundColor('#dadbd9')
                .groupDefaultFocus(true)    // 设置Button-1为第一个tabIndex的默认焦点
            }

            Column({ space: 20 }) {
              Row({ space: 20 }) {
                Button('2')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
                Button('3')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
              }

              Row({ space: 20 }) {
                Button('4')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
                Button('5')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
              }

              Row({ space: 20 }) {
                Button('6')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
                Button('7')
                  .width(100)
                  .height(100)
                  .fontSize(40)
                  .type(ButtonType.Normal)
                  .borderRadius(20)
                  .backgroundColor('#dadbd9')
              }
            }
          }
          .width(480)
          .height(380)
          .justifyContent(FlexAlign.Center)
          .borderWidth(2)
          .borderColor(Color.Gray)
          .backgroundColor(Color.White)
          .tabIndex(1)
        }, item => item)
      }
      .cachedCount(2)
      .index(0)
      .interval(4000)
      .indicator(true)
      .loop(true)
      .duration(1000)
      .itemSpace(0)
      .curve(Curve.Linear)
      .onChange((index: number) => {
        console.info(index.toString());
      })
      .margin({ left: 20, top: 20, right: 20 })

      Row({ space: 40 }) {    // 设置该Row组件为第二个tabIndex节点
        Button('←')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .fontColor(Color.Black)
          .backgroundColor(Color.Transparent)
          .onClick(() => {
            this.swiperController.showPrevious();
          })
          .groupDefaultFocus(true)    // 设置Button-左箭头为第二个tabIndex节点的默认焦点
        Button('→')
          .fontSize(40)
          .fontWeight(FontWeight.Bold)
          .fontColor(Color.Black)
          .backgroundColor(Color.Transparent)
          .onClick(() => {
            this.swiperController.showNext();
          })
      }
      .width(480)
      .height(50)
      .justifyContent(FlexAlign.Center)
      .borderWidth(2)
      .borderColor(Color.Gray)
      .backgroundColor('#f7f6dc')
      .tabIndex(2)

      Row({ space: 40 }) {    // 设置该Row组件为第三个tabIndex节点
        Button('Cancel')
          .fontSize(30)
          .fontColor('#787878')
          .type(ButtonType.Normal)
          .width(140)
          .height(50)
          .backgroundColor('#dadbd9')

        Button('OK')
          .fontSize(30)
          .fontColor('#787878')
          .type(ButtonType.Normal)
          .width(140)
          .height(50)
          .backgroundColor('#dadbd9')
          .defaultFocus(true)
          .onClick(() => {
            promptAction.showToast({ message: 'Button OK on clicked' });
          })
          .groupDefaultFocus(true)    // 设置Button-OK为第三个tabIndex节点的默认焦点
      }
      .width(480)
      .height(80)
      .justifyContent(FlexAlign.Center)
      .borderWidth(2)
      .borderColor(Color.Gray)
      .backgroundColor('#dff2e4')
      .margin({ left: 20, bottom: 20, right: 20 })
      .tabIndex(3)
    }.backgroundColor('#f2f2f2')
    .margin({ left: 50, top: 50, right: 20 })
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.74684783576230022775426929536217:50001231000000:2800:07EC32CE109DE5E1098BCF2A5D93EBF18BB8ABED920DB47059774CC9D6F5899A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

### focusOnTouch

```
focusOnTouch(value: boolean)
```

点击获焦能力，参数：boolean，默认值：false（输入类组件：TextInput、TextArea、Search、Web默认值是true）。

点击是指使用触屏或鼠标左键进行单击，默认为false的组件，例如Button，不绑定该API时，点击Button不会使其获焦，当给Button绑定focusOnTouch(true)时，点击Button会使Button立即获得焦点。

给容器绑定focusOnTouch(true)时，点击容器区域，会立即使容器的第一个可获焦组件获得焦点。

示例代码：

```
// requestFocus.ets
import promptAction from '@ohos.promptAction';

@Entry
@Component
struct RequestFocusExample {
  @State idList: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'N']

  build() {
    Column({ space:20 }){
      Button("id: " + this.idList[0] + " focusOnTouch(true) + focusable(false)")
        .width(400).height(70).fontColor(Color.White).focusOnTouch(true)
        .focusable(false)
      Button("id: " + this.idList[1] + " default")
        .width(400).height(70).fontColor(Color.White)
      Button("id: " + this.idList[2] + " focusOnTouch(false)")
        .width(400).height(70).fontColor(Color.White).focusOnTouch(false)
      Button("id: " + this.idList[3] + " focusOnTouch(true)")
        .width(400).height(70).fontColor(Color.White).focusOnTouch(true)
    }.width('100%').margin({ top:20 })
  }
}
```

效果：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.30364911169868361697909207453175:50001231000000:2800:B4F81F0DF117E1CCBC6298EE8E276D2CB00994FD1B8119B502904442545B99AA.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

解读：

Button-A虽然设置了focusOnTouch(true)，但是同时也设置了focusable(false)，该组件无法获焦，因此点击后也无法获焦；

Button-B不设置相关属性，点击后不会获焦；

Button-C设置了focusOnTouch(false)，同Button-B，点击后也不会获焦；

Button-D设置了focusOnTouch(true)，点击即可使其获焦；

说明

由于[焦点态](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-common-events-focus-event-0000001455502044-V3#ZH-CN_TOPIC_0000001573929209__li1676511513418)的阐述的特性，焦点态在屏幕接收点击事件后会立即清除。因此该示例代码在每次点击后，需要再次按下TAB键使焦点态再次显示，才可知道当前焦点所在的组件。

### focusControl.requestFocus

```
focusControl.requestFocus(id: string)
```

主动申请焦点能力的全局方法，参数：string，参数表示被申请组件的id（通用属性id设置的字符串）。

使用方法为：在任意执行语句中调用该API，指定目标组件的id为方法参数，当程序执行到该语句时，会立即给指定的目标组件申请焦点。

代码示例：

```
// requestFocus.ets
import promptAction from '@ohos.promptAction';

@Entry
@Component
struct RequestFocusExample {
  @State idList: string[] = ['A', 'B', 'C', 'D', 'E', 'F', 'N']
  @State requestId: number = 0

  build() {
    Column({ space:20 }){
      Row({space: 5}) {
        Button("id: " + this.idList[0] + " focusable(false)")
          .width(200).height(70).fontColor(Color.White)
          .id(this.idList[0])
          .focusable(false)
        Button("id: " + this.idList[1])
          .width(200).height(70).fontColor(Color.White)
          .id(this.idList[1])
      }
      Row({space: 5}) {
        Button("id: " + this.idList[2])
          .width(200).height(70).fontColor(Color.White)
          .id(this.idList[2])
        Button("id: " + this.idList[3])
          .width(200).height(70).fontColor(Color.White)
          .id(this.idList[3])
      }
      Row({space: 5}) {
        Button("id: " + this.idList[4])
          .width(200).height(70).fontColor(Color.White)
          .id(this.idList[4])
        Button("id: " + this.idList[5])
          .width(200).height(70).fontColor(Color.White)
          .id(this.idList[5])
      }
    }.width('100%').margin({ top:20 })
    .onKeyEvent((e) => {
      if (e.keyCode >= 2017 && e.keyCode <= 2022) {
        this.requestId = e.keyCode - 2017;
      } else if (e.keyCode === 2030) {
        this.requestId = 6;
      } else {
        return;
      }
      if (e.type !== KeyType.Down) {
        return;
      }
      let res = focusControl.requestFocus(this.idList[this.requestId]);
      if (res) {
        promptAction.showToast({message: 'Request success'});
      } else {
        promptAction.showToast({message: 'Request failed'});
      }
    })
  }
}
```

效果：

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183924.78611452337760762090433074882708:50001231000000:2800:C03A7687BB489A5AFE9A788017FE566D068A525E10E99ED6B6AFC87D19AACC40.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

解读：页面中共6个Button组件，其中Button-A组件设置了focusable(false)，表示其不可获焦，在外部容器的onKeyEvent中，监听按键事件，当按下A ~ F按键时，分别去申请Button A ~ F 的焦点，另外按下N键，是给当前页面上不存在的id的组件去申请焦点。

1. 按下TAB键，由于第一个组件Button-A设置了无法获焦，那么默认第二个组件Button-B获焦，Button-B展示焦点态样式；
2. 键盘上按下A键，申请Button-A的焦点，气泡显示Request failed，表示无法获取到焦点，焦点位置未改变；
3. 键盘上按下B键，申请Button-B的焦点，气泡显示Request success，表示获焦到了焦点，焦点位置原本就在Button-B，位置未改变；
4. 键盘上按下C键，申请Button-C的焦点，气泡显示Request success，表示获焦到了焦点，焦点位置从Button-B变更为Button-C；
5. 键盘上按下D键，申请Button-D的焦点，气泡显示Request success，表示获焦到了焦点，焦点位置从Button-C变更为Button-D；
6. 键盘上按下E键，申请Button-E的焦点，气泡显示Request success，表示获焦到了焦点，焦点位置从Button-D变更为Button-E；
7. 键盘上按下F键，申请Button-F的焦点，气泡显示Request success，表示获焦到了焦点，焦点位置从Button-E变更为Button-F；
8. 键盘上按下N键，申请未知组件的焦点，气泡显示Request failed，表示无法获取到焦点，焦点位置不变；



# 绑定手势方法

更新时间: 2024-01-15 12:21

通过给各个组件绑定不同的手势事件，并设计事件的响应方式，当手势识别成功时，ArkUI框架将通过事件回调通知组件手势识别的结果。

## gesture（常规手势绑定方法）

```
.gesture(gesture: GestureType, mask?: GestureMask)
```

gesture为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。

例如，可以将点击手势TapGesture通过gesture手势绑定方法绑定到Text组件上。

```
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        // 采用gesture手势绑定方法绑定TapGesture
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
  }
}
```

## priorityGesture（带优先级的手势绑定方法）

```
.priorityGesture(gesture: GestureType, mask?: GestureMask)。
```

priorityGesture是带优先级的手势绑定方法，可以在组件上绑定优先识别的手势。

在默认情况下，当父组件和子组件使用gesture绑定同类型的手势时，子组件优先识别通过gesture绑定的手势。当父组件使用priorityGesture绑定与子组件同类型的手势时，父组件优先识别通过priorityGesture绑定的手势。

例如，当父组件Column和子组件Text同时绑定TapGesture手势时，父组件以带优先级手势priorityGesture的形式进行绑定时，优先响应父组件绑定的TapGesture。

```
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('Text TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
    // 设置为priorityGesture时，点击文本区域会忽略Text组件的TapGesture手势事件，优先响应父组件Column的TapGesture手势事件
    .priorityGesture(
      TapGesture()
        .onAction(() => {
          console.info('Column TapGesture is onAction');
        }), GestureMask.IgnoreInternal)
  }
}
```

## parallelGesture（并行手势绑定方法）

```
.parallelGesture(gesture: GestureType, mask?: GestureMask)
```

parallelGesture是并行的手势绑定方法，可以在父子组件上绑定可以同时响应的相同手势。

在默认情况下，手势事件为非冒泡事件，当父子组件绑定相同的手势时，父子组件绑定的手势事件会发生竞争，最多只有一个组件的手势事件能够获得响应。而当父组件绑定了并行手势parallelGesture时，父子组件相同的手势事件都可以触发，实现类似冒泡效果。

```
// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text('Gesture').fontSize(28)
        .gesture(
          TapGesture()
            .onAction(() => {
              console.info('Text TapGesture is onAction');
            }))
    }
    .height(200)
    .width(250)
    // 设置为parallelGesture时，点击文本区域会同时响应父组件Column和子组件Text的TapGesture手势事件
    .parallelGesture(
      TapGesture()
        .onAction(() => {
          console.info('Column TapGesture is onAction');
        }), GestureMask.IgnoreInternal)
  }
}
```

说明

当父组件和子组件同时绑定单击手势事件和双击手势事件时，父组件和子组件均只响应单击手势事件。



# 单一手势

更新时间: 2024-01-10 11:35

## 点击手势（TapGesture）

```
TapGesture(value?:{count?:number; fingers?:number})
```

点击手势支持单次点击和多次点击，拥有两个可选参数：

* count：非必填参数，声明该点击手势识别的连续点击次数。默认值为1，若设置小于1的非法值会被转化为默认值。如果配置多次点击，上一次抬起和下一次按下的超时时间为300毫秒。
* fingers：非必填参数，用于声明触发点击的手指数量，最小值为1，最大值为10，默认值为1。当配置多指时，若第一根手指按下300毫秒内未有足够的手指数按下则手势识别失败。当实际点击手指数超过配置值时，手势识别失败。
  以在Text组件上绑定双击手势（count值为2的点击手势）为例：

```
// xxx.ets
@Entry
@Component
struct Index {
  @State value: string = "";
  
  build() {
    Column() {
      Text('Click twice').fontSize(28)
        .gesture(
          // 绑定count为2的TapGesture
          TapGesture({ count: 2 })
            .onAction((event: GestureEvent) => {
              this.value = JSON.stringify(event.fingerList[0]);
            }))
      Text(this.value)
    }
    .height(200)
    .width(250)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183925.19538553553489306293062854408456:50001231000000:2800:B8C76B6242CAABA3189756A612B5F09AC1B12C49345737B7C01DC550768206C1.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 长按手势（LongPressGesture）

```
LongPressGesture(value?:{fingers?:number; repeat?:boolean; duration?:number})
```

长按手势用于触发长按手势事件，触发长按手势的最少手指数量为1，最短长按事件为500毫秒，拥有三个可选参数：

* fingers：非必选参数，用于声明触发长按手势所需要的最少手指数量，最小值为1，最大值为10，默认值为1。
* repeat：非必选参数，用于声明是否连续触发事件回调，默认值为false。
* duration：非必选参数，用于声明触发长按所需的最短时间，单位为毫秒，默认值为500。

以在Text组件上绑定可以重复触发的长按手势为例：

```
// xxx.ets
@Entry
@Component
struct Index {
  @State count: number = 0;

  build() {
    Column() {
      Text('LongPress OnAction:' + this.count).fontSize(28)
        .gesture(
          // 绑定可以重复触发的LongPressGesture
          LongPressGesture({ repeat: true })
            .onAction((event: GestureEvent) => {
              if (event.repeat) {
                this.count++;
              }
            })
            .onActionEnd(() => {
              this.count = 0;
            })
        )
    }
    .height(200)
    .width(250)
    .padding(20)
    .border({ width: 3 })
    .margin(30)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183925.31983175690407854646442553524840:50001231000000:2800:FAC0AE586D267A66206D6F2B46EE1783AC6C7C4247D2A9499272F20735FBC4D9.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 拖动手势（PanGesture）

```
PanGestureOptions(value?:{ fingers?:number; direction?:PanDirection; distance?:number})
```

拖动手势用于触发拖动手势事件，滑动达到最小滑动距离（默认值为5vp）时拖动手势识别成功，拥有三个可选参数：

* fingers：非必选参数，用于声明触发拖动手势所需要的最少手指数量，最小值为1，最大值为10，默认值为1。
* direction：非必选参数，用于声明触发拖动的手势方向，此枚举值支持逻辑与（&）和逻辑或（|）运算。默认值为Pandirection.All。
* distance：非必选参数，用于声明触发拖动的最小拖动识别距离，单位为vp，默认值为5。

以在Text组件上绑定拖动手势为例，可以通过在拖动手势的回调函数中修改组件的布局位置信息来实现组件的拖动：

```
// xxx.ets
@Entry
@Component
struct Index {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;

  build() {
    Column() {
      Text('PanGesture Offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
        .fontSize(28)
        .height(200)
        .width(300)
        .padding(20)
        .border({ width: 3 })
          // 在组件上绑定布局位置信息
        .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
        .gesture(
          // 绑定拖动手势
          PanGesture()
            .onActionStart((event: GestureEvent) => {
              console.info('Pan start');
            })
              // 当触发拖动手势时，根据回调函数修改组件的布局位置信息
            .onActionUpdate((event: GestureEvent) => {
              this.offsetX = this.positionX + event.offsetX;
              this.offsetY = this.positionY + event.offsetY;
            })
            .onActionEnd(() => {
              this.positionX = this.offsetX;
              this.positionY = this.offsetY;
            })
        )
    }
    .height(200)
    .width(250)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183925.83643943528183002913420961584727:50001231000000:2800:EA810BDA13EED5529144E927ACB6986BCD920E26564C52FF4048529C32D50CFD.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

说明

大部分可滑动组件，如List、Grid、Scroll、Tab等组件是通过PanGesture实现滑动，在组件内部的子组件绑定[拖动手势（PanGesture）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-single-gesture-0000001450596854-V3#section128381857165115)或者[滑动手势（SwipeGesture）](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-single-gesture-0000001450596854-V3#section8341417185216)会导致手势竞争。

当在子组件绑定PanGesture时，在子组件区域进行滑动仅触发子组件的PanGesture。如果需要父组件响应，需要通过修改手势绑定方法或者子组件向父组件传递消息进行实现，或者通过修改父子组件的PanGesture参数distance使得拖动更灵敏。当子组件绑定SwipeGesture时，由于PanGesture和SwipeGesture触发条件不同，需要修改PanGesture和SwipeGesture的参数以达到所需效果。

## 捏合手势（PinchGesture）

```
PinchGesture(value?:{fingers?:number; distance?:number})
```

捏合手势用于触发捏合手势事件，触发捏合手势的最少手指数量为2指，最大为5指，最小识别距离为5vp，拥有两个可选参数：

* fingers：非必选参数，用于声明触发捏合手势所需要的最少手指数量，最小值为2，最大值为5，默认值为2。
* distance：非必选参数，用于声明触发捏合手势的最小距离，单位为vp，默认值为5。

以在Column组件上绑定三指捏合手势为例，可以通过在捏合手势的函数回调中获取缩放比例，实现对组件的缩小或放大：

```
// xxx.ets
@Entry
@Component
struct Index {
  @State scaleValue: number = 1;
  @State pinchValue: number = 1;
  @State pinchX: number = 0;
  @State pinchY: number = 0;

  build() {
    Column() {
      Column() {
        Text('PinchGesture scale:\n' + this.scaleValue)
        Text('PinchGesture center:\n(' + this.pinchX + ',' + this.pinchY + ')')
      }
      .height(200)
      .width(300)
      .border({ width: 3 })
      .margin({ top: 100 })
      // 在组件上绑定缩放比例，可以通过修改缩放比例来实现组件的缩小或者放大
      .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
      .gesture(
        // 在组件上绑定三指触发的捏合手势
        PinchGesture({ fingers: 3 })
          .onActionStart((event: GestureEvent) => {
            console.info('Pinch start');
          })
            // 当捏合手势触发时，可以通过回调函数获取缩放比例，从而修改组件的缩放比例
          .onActionUpdate((event: GestureEvent) => {
            this.scaleValue = this.pinchValue * event.scale;
            this.pinchX = event.pinchCenterX;
            this.pinchY = event.pinchCenterY;
          })
          .onActionEnd(() => {
            this.pinchValue = this.scaleValue;
            console.info('Pinch end');
          })
      )
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183925.60642990883974858107532960084472:50001231000000:2800:3FEFC4BFDE95305EC428FDA384A48E56D78C45F864CE84C26F159297701195E3.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 旋转手势（RotationGesture）

```
RotationGesture(value?:{fingers?:number; angle?:number})
```

旋转手势用于触发旋转手势事件，触发旋转手势的最少手指数量为2指，最大为5指，最小改变度数为1度，拥有两个可选参数：

* fingers：非必选参数，用于声明触发旋转手势所需要的最少手指数量，最小值为2，最大值为5，默认值为2。
* angle：非必选参数，用于声明触发旋转手势的最小改变度数，单位为deg，默认值为1。

以在Text组件上绑定旋转手势实现组件的旋转为例，可以通过在旋转手势的回调函数中获取旋转角度，从而实现组件的旋转：

```
// xxx.ets
@Entry
@Component
struct Index {
  @State angle: number = 0;
  @State rotateValue: number = 0;

  build() {
    Column() {
      Text('RotationGesture angle:' + this.angle).fontSize(28)
        // 在组件上绑定旋转布局，可以通过修改旋转角度来实现组件的旋转
        .rotate({ angle: this.angle })
        .gesture(
          RotationGesture()
            .onActionStart((event: GestureEvent) => {
              console.info('RotationGesture is onActionStart');
            })
              // 当旋转手势生效时，通过旋转手势的回调函数获取旋转角度，从而修改组件的旋转角度
            .onActionUpdate((event: GestureEvent) => {
              this.angle = this.rotateValue + event.angle;
              console.info('RotationGesture is onActionEnd');
            })
              // 当旋转结束抬手时，固定组件在旋转结束时的角度
            .onActionEnd(() => {
              this.rotateValue = this.angle;
              console.info('RotationGesture is onActionEnd');
            })
            .onActionCancel(() => {
              console.info('RotationGesture is onActionCancel');
            })
        )
    }
    .height(200)
    .width(250)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.71072180665641019796906117314219:50001231000000:2800:6A338B595F8F58273EB55D77D43CABD38AC9594D6ADA2FBFE67C5520D890801A.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

## 滑动手势（SwipeGesture）

```
SwipeGesture(value?:{fingers?:number; direction?:SwipeDirection; speed?:number})
```

滑动手势用于触发滑动事件，当滑动速度大于100vp/s时可以识别成功，拥有三个可选参数：

* fingers：非必选参数，用于声明触发滑动手势所需要的最少手指数量，最小值为1，最大值为10，默认值为1。
* direction：非必选参数，用于声明触发滑动手势的方向，此枚举值支持逻辑与（&）和逻辑或（|）运算。默认值为SwipeDirection.All。
* speed：非必选参数，用于声明触发滑动的最小滑动识别速度，单位为vp/s，默认值为100。

以在Column组件上绑定滑动手势实现组件的旋转为例：

```
// xxx.ets
@Entry
@Component
struct Index {
  @State rotateAngle: number = 0;
  @State speed: number = 1;

  build() {
    Column() {
      Column() {
        Text("SwipeGesture speed\n" + this.speed)
        Text("SwipeGesture angle\n" + this.rotateAngle)
      }
      .border({ width: 3 })
      .width(300)
      .height(200)
      .margin(100)
      // 在Column组件上绑定旋转，通过滑动手势的滑动速度和角度修改旋转的角度
      .rotate({ angle: this.rotateAngle })
      .gesture(
        // 绑定滑动手势且限制仅在竖直方向滑动时触发
        SwipeGesture({ direction: SwipeDirection.Vertical })
          // 当滑动手势触发时，获取滑动的速度和角度，实现对组件的布局参数的修改
          .onAction((event: GestureEvent) => {
            this.speed = event.speed;
            this.rotateAngle = event.angle;
          })
      )
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.59546356236475757562047858687728:50001231000000:2800:DECF01901141C34A7E14012FF051C365157B76D25670F6656FE76934AE60A638.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

说明

当SwipeGesture和PanGesture同时绑定时，若二者是以默认方式或者互斥方式进行绑定时，会发生竞争。SwipeGesture的触发条件为滑动速度达到100vp/s，PanGesture的触发条件为滑动距离达到5vp，先达到触发条件的手势触发。可以通过修改SwipeGesture和PanGesture的参数以达到不同的效果。



# 组合手势

更新时间: 2024-01-15 12:22

组合手势由多种单一手势组合而成，通过在GestureGroup中使用不同的GestureMode来声明该组合手势的类型，支持[顺序识别](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-combined-gestures-0000001500756325-V3#section156281401547)、[并行识别](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-combined-gestures-0000001500756325-V3#section1823210218551)和[互斥识别](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-gesture-events-combined-gestures-0000001500756325-V3#section9464141510553)三种类型。

```
GestureGroup(mode:GestureMode, ...gesture:GestureType[])
```

* mode：必选参数，为GestureMode枚举类。用于声明该组合手势的类型。
* gesture：必选参数，为由多个手势组合而成的数组。用于声明组合成该组合手势的各个手势。

## 顺序识别

顺序识别组合手势对应的GestureMode为Sequence。顺序识别组合手势将按照手势的注册顺序识别手势，直到所有的手势识别成功。当顺序识别组合手势中有一个手势识别失败时，所有的手势识别失败。

以一个由长按手势和拖动手势组合而成的顺序手势为例：

在一个Column组件上绑定了translate属性，通过修改该属性可以设置组件的位置移动。然后在该组件上绑定LongPressGesture和PanGesture组合而成的Sequence组合手势。当触发LongPressGesture时，更新显示的数字。当长按后进行拖动时，根据拖动手势的回调函数，实现组件的拖动。

```
// xxx.ets
@Entry
@Component
struct Index {
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State count: number = 0;
  @State positionX: number = 0;
  @State positionY: number = 0;
  @State borderStyles: BorderStyle = BorderStyle.Solid

  build() {
    Column() {
      Text('sequence gesture\n' + 'LongPress onAction:' + this.count + '\nPanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
        .fontSize(28)
    }
    // 绑定translate属性可以实现组件的位置移动
    .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
    .height(250)
    .width(300)
    //以下组合手势为顺序识别，当长按手势事件未正常触发时不会触发拖动手势事件
    .gesture(
      // 声明该组合手势的类型为Sequence类型
      GestureGroup(GestureMode.Sequence,
        // 该组合手势第一个触发的手势为长按手势，且长按手势可多次响应
        LongPressGesture({ repeat: true })
          // 当长按手势识别成功，增加Text组件上显示的count次数
          .onAction((event: GestureEvent) => {
            if (event.repeat) {
              this.count++;
            }
            console.info('LongPress onAction');
          })
          .onActionEnd(() => {
            console.info('LongPress end');
          }),
        // 当长按之后进行拖动，PanGesture手势被触发
        PanGesture()
          .onActionStart(() => {
            this.borderStyles = BorderStyle.Dashed;
            console.info('pan start');
          })
            // 当该手势被触发时，根据回调获得拖动的距离，修改该组件的位移距离从而实现组件的移动
          .onActionUpdate((event: GestureEvent) => {
            this.offsetX = this.positionX + event.offsetX;
            this.offsetY = this.positionY + event.offsetY;
            console.info('pan update');
          })
          .onActionEnd(() => {
            this.positionX = this.offsetX;
            this.positionY = this.offsetY;
            this.borderStyles = BorderStyle.Solid;
          })
      )
    )
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.85052660339284035269589071194336:50001231000000:2800:8D2AB684A12DCE469D08D79FE190C171F7C50AD0BA7F29FCA0DD1488CA5F2904.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

说明

拖拽事件是一种典型的顺序识别组合手势事件，由长按手势事件和滑动手势事件组合而成。只有先长按达到长按手势事件预设置的时间后进行滑动才会触发拖拽事件。如果长按事件未达到或者长按后未进行滑动，拖拽事件均识别失败。

## 并行识别

并行识别组合手势对应的GestureMode为Parallel。并行识别组合手势中注册的手势将同时进行识别，直到所有手势识别结束。并行识别手势组合中的手势进行识别时互不影响。

以在一个Column组件上绑定点击手势和双击手势组成的并行识别手势为例，由于单击手势和双击手势是并行识别，因此两个手势可以同时进行识别，二者互不干涉。

```
// xxx.ets
@Entry
@Component
struct Index {
  @State count1: number = 0;
  @State count2: number = 0;

  build() {
    Column() {
      Text('parallel gesture\n' + 'tapGesture count is 1:' + this.count1 + '\ntapGesture count is 2:' + this.count2 + '\n')
        .fontSize(28)
    }
    .height(200)
    .width(250)
    // 以下组合手势为并行并别，单击手势识别成功后，若在规定时间内再次点击，双击手势也会识别成功
    .gesture(
      GestureGroup(GestureMode.Parallel,
        TapGesture({ count: 1 })
          .onAction(() => {
            this.count1++;
          }),
        TapGesture({ count: 2 })
          .onAction(() => {
            this.count2++;
          })
      )
    )
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.82519055666191538534855600477746:50001231000000:2800:95F05B667D8FED1C2CDAA735929307D60941C498CBA818B78EA05A6C9EE6D81A.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

说明

当由单击手势和双击手势组成一个并行识别组合手势后，在区域内进行点击时，单击手势和双击手势将同时进行识别。

当只有单次点击时，单击手势识别成功，双击手势识别失败。

当有两次点击时，若两次点击相距时间在规定时间内（默认规定时间为300毫秒），触发两次单击事件和一次双击事件。

当有两次点击时，若两次点击相距时间超出规定时间，触发两次单击事件不触发双击事件。

## 互斥识别

互斥识别组合手势对应的GestureMode为Exclusive。互斥识别组合手势中注册的手势将同时进行识别，若有一个手势识别成功，则结束手势识别，其他所有手势识别失败。

以在一个Column组件上绑定单击手势和双击手势组合而成的互斥识别组合手势为例，由于单击手势只需要一次点击即可触发而双击手势需要两次，每次的点击事件均被单击手势消费而不能积累成双击手势，所以双击手势无法触发。

```
// xxx.ets
@Entry
@Component
struct Index {
  @State count1: number = 0;
  @State count2: number = 0;

  build() {
    Column() {
      Text('parallel gesture\n' + 'tapGesture count is 1:' + this.count1 + '\ntapGesture count is 2:' + this.count2 + '\n')
        .fontSize(28)
    }
    .height(200)
    .width(250)
    //以下组合手势为互斥并别，单击手势识别成功后，双击手势会识别失败
    .gesture(
      GestureGroup(GestureMode.Exclusive,
        TapGesture({ count: 1 })
          .onAction(() => {
            this.count1++;
          }),
        TapGesture({ count: 2 })
          .onAction(() => {
            this.count2++;
          })
      )
    )
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.92093350098805804920082722106002:50001231000000:2800:E8C16647F904FD8537B632B550D19B09095D283B43C881F0A9907B198065E094.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

说明

当由单击手势和双击手势组成一个互斥识别组合手势后，在区域内进行点击时，单击手势和双击手势将同时进行识别。

当只有单次点击时，单击手势识别成功，双击手势识别失败。

当有两次点击时，单击手势在第一次点击时即宣告识别成功，此时双击手势已经失败。即使在规定时间内进行了第二次点击，双击手势事件也不会进行响应，此时会触发单击手势事件的第二次识别成功。



# 性能提升的推荐方法

更新时间: 2024-01-15 12:19

开发者若使用低性能的代码实现功能场景可能不会影响应用的正常运行，但却会对应用的性能造成负面影响。本章节列举出了一些可提升性能的场景供开发者参考，以避免应用实现上带来的性能劣化。

## 使用数据懒加载

开发者在使用长列表时，如果直接采用循环渲染方式，如下所示，会一次性加载所有的列表元素，一方面会导致页面启动时间过长，影响用户体验，另一方面也会增加服务器的压力和流量，加重系统负担。

```
@Entry
@Component
struct MyComponent {
  @State arr: number[] = Array.from(Array(100), (v,k) =>k);  //构造0-99的数组
  build() {
    List() {
      ForEach(this.arr, (item: number) => {
        ListItem() {
          Text(`item value: ${item}`)
        }
      }, (item: number) => item.toString())
    }
  }
}
```

上述代码会在页面加载时将100个列表元素全部加载，这并非我们需要的，我们希望从数据源中按需迭代加载数据并创建相应组件，因此需要使用数据懒加载，如下所示：

```
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = []

  public totalCount(): number {
    return 0
  }

  public getData(index: number): any {
    return undefined
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener')
      this.listeners.push(listener)
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener')
      this.listeners.splice(pos, 1)
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded()
    })
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index)
    })
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index)
    })
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index)
    })
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to)
    })
  }
}

class MyDataSource extends BasicDataSource {
  private dataArray: string[] = ['item value: 0', 'item value: 1', 'item value: 2']

  public totalCount(): number {
    return this.dataArray.length
  }

  public getData(index: number): any {
    return this.dataArray[index]
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data)
    this.notifyDataAdd(index)
  }

  public pushData(data: string): void {
    this.dataArray.push(data)
    this.notifyDataAdd(this.dataArray.length - 1)
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource()

  build() {
    List() {
      LazyForEach(this.data, (item: string) => {
        ListItem() {
          Row() {
            Text(item).fontSize(20).margin({ left: 10 })
          }
        }
        .onClick(() => {
          this.data.pushData('item value: ' + this.data.totalCount())
        })
      }, item => item)
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.02045249509486897221240782505629:50001231000000:2800:7B89BEAD34CB1459B2A9DE35E64BBC9B1E8B1E7A99F06C8B725BE7226DA865B1.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

上述代码在页面加载时仅初始化加载三个列表元素，之后每点击一次列表元素，将增加一个列表元素。

## 设置List组件的宽高

在使用Scroll容器组件嵌套List组件加载长列表时，若不指定List的宽高尺寸，则默认全部加载。

说明

Scroll嵌套List时：

* List没有设置宽高，会布局List的所有子组件。
* List设置宽高，会布局List显示区域内的子组件。
* List使用[ForEach](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-foreach-0000001524537153-V3)加载子组件时，无论是否设置List的宽高，都会加载所有子组件。
* List使用[LazyForEach](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-rendering-control-lazyforeach-0000001524417213-V3)加载子组件时，没有设置List的宽高，会加载所有子组件，设置了List的宽高，会加载List显示区域内的子组件。

```
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = []

  public totalCount(): number {
    return 0
  }

  public getData(index: number): any {
    return undefined
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener')
      this.listeners.push(listener)
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener')
      this.listeners.splice(pos, 1)
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded()
    })
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index)
    })
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index)
    })
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index)
    })
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to)
    })
  }
}

class MyDataSource extends BasicDataSource {
  private dataArray: Array<string> = new Array(100).fill('test')

  public totalCount(): number {
    return this.dataArray.length
  }

  public getData(index: number): any {
    return this.dataArray[index]
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data)
    this.notifyDataAdd(index)
  }

  public pushData(data: string): void {
    this.dataArray.push(data)
    this.notifyDataAdd(this.dataArray.length - 1)
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource()

  build() {
    Scroll() {
      List() {
        LazyForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Row() {
              Text('item value: ' + item + (index + 1)).fontSize(20).margin(10)
            }
          }
        })
      }
    }
  }
}
```

因此，此场景下建议设置List子组件的宽高。

```
class BasicDataSource implements IDataSource {
  private listeners: DataChangeListener[] = []

  public totalCount(): number {
    return 0
  }

  public getData(index: number): any {
    return undefined
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    if (this.listeners.indexOf(listener) < 0) {
      console.info('add listener')
      this.listeners.push(listener)
    }
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const pos = this.listeners.indexOf(listener);
    if (pos >= 0) {
      console.info('remove listener')
      this.listeners.splice(pos, 1)
    }
  }

  notifyDataReload(): void {
    this.listeners.forEach(listener => {
      listener.onDataReloaded()
    })
  }

  notifyDataAdd(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataAdd(index)
    })
  }

  notifyDataChange(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataChange(index)
    })
  }

  notifyDataDelete(index: number): void {
    this.listeners.forEach(listener => {
      listener.onDataDelete(index)
    })
  }

  notifyDataMove(from: number, to: number): void {
    this.listeners.forEach(listener => {
      listener.onDataMove(from, to)
    })
  }
}

class MyDataSource extends BasicDataSource {
  private dataArray: Array<string> = new Array(100).fill('test')

  public totalCount(): number {
    return this.dataArray.length
  }

  public getData(index: number): any {
    return this.dataArray[index]
  }

  public addData(index: number, data: string): void {
    this.dataArray.splice(index, 0, data)
    this.notifyDataAdd(index)
  }

  public pushData(data: string): void {
    this.dataArray.push(data)
    this.notifyDataAdd(this.dataArray.length - 1)
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource()

  build() {
    Scroll() {
      List() {
        LazyForEach(this.data, (item: string, index: number) => {
          ListItem() {
            Text('item value: ' + item + (index + 1)).fontSize(20).margin(10)
          }.width('100%')
        })
      }.width('100%').height(500)
    }.backgroundColor(Color.Pink)
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.80427703540662378877116923999067:50001231000000:2800:CE786441D503FD27799061A35CF17DADB3278B864F438931A368EECC173294A8.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 使用条件渲染替代显隐控制

如下所示，开发者在使用visibility通用属性控制组件的显隐状态时，仍存在组件的重新创建过程，造成性能上的损耗。

```
@Entry
@Component
struct MyComponent {
  @State isVisible: Visibility = Visibility.Visible;

  build() {
    Column() {
      Button("显隐切换")
        .onClick(() => {
          if (this.isVisible == Visibility.Visible) {
            this.isVisible = Visibility.None
          } else {
            this.isVisible = Visibility.Visible
          }
        })
      Row().visibility(this.isVisible)
        .width(300).height(300).backgroundColor(Color.Pink)
    }.width('100%')
  }
}
```

要避免这一问题，可使用if条件渲染代替visibility属性变换，如下所示：

```
@Entry
@Component
struct MyComponent {
  @State isVisible: boolean = true;

  build() {
    Column() {
      Button("显隐切换")
        .onClick(() => {
          this.isVisible = !this.isVisible
        })
      if (this.isVisible) {
        Row()
          .width(300).height(300).backgroundColor(Color.Pink)
      }
    }.width('100%')
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.42354039746716189182317565279081:50001231000000:2800:1E131393982AB0F1B701C540EA007D0D6E5635C3ECDB2B6AEC8FD1177C6B65AE.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 使用Column/Row替代Flex

由于Flex容器组件默认情况下存在shrink导致二次布局，这会在一定程度上造成页面渲染上的性能劣化。

```
@Entry
@Component
struct MyComponent {
  build() {
    Flex({ direction: FlexDirection.Column }) {
      Flex().width(300).height(200).backgroundColor(Color.Pink)
      Flex().width(300).height(200).backgroundColor(Color.Yellow)
      Flex().width(300).height(200).backgroundColor(Color.Grey)
    }
  }
}
```

上述代码可将Flex替换为Column、Row，在保证实现的页面布局效果相同的前提下避免Flex二次布局带来的负面影响。

```
@Entry
@Component
struct MyComponent {
  build() {
    Column() {
      Row().width(300).height(200).backgroundColor(Color.Pink)
      Row().width(300).height(200).backgroundColor(Color.Yellow)
      Row().width(300).height(200).backgroundColor(Color.Grey)
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.95424880545142727796297534483601:50001231000000:2800:E8ED683870D685CFAD25510994146039A8D5EA6A6F45EEA3EE9B2130ECDA27A3.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 减少应用滑动白块

应用通过增大List/Grid控件的cachedCount参数，调整UI的加载范围。cachedCount表示屏幕外List/Grid预加载item的个数。

如果需要请求网络图片，可以在item滑动到屏幕显示之前，提前下载好内容，从而减少滑动白块。

如下是使用cachedCount参数的例子：

```
@Entry
@Component
struct MyComponent {
  private source: MyDataSource = new MyDataSource();

  build() {
    List() {
      LazyForEach(this.source, item => {
        ListItem() {
          Text("Hello" + item)
            .fontSize(50)
            .onAppear(() => {
              console.log("appear:" + item)
            })
        }
      })
    }.cachedCount(3) // 扩大数值appear日志范围会变大
  }
}

class MyDataSource implements IDataSource {
  data: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];

  public totalCount(): number {
    return this.data.length
  }

  public getData(index: number): any {
    return this.data[index]
  }

  registerDataChangeListener(listener: DataChangeListener): void {
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183926.74485876354332835439838904290533:50001231000000:2800:B996C845EFD58A97C5CF4C36624521C01AEF77B988566E6DC40BCD6FBF89BBD0.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

使用说明：

cachedCount的增加会增大UI的cpu、内存开销。使用时需要根据实际情况，综合性能和用户体验进行调整。



