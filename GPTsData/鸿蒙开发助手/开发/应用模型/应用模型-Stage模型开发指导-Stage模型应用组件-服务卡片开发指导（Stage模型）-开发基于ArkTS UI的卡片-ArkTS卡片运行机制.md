# ArkTS卡片运行机制

更新时间: 2024-01-15 12:19

## 实现原理

图1 ArkTS卡片实现原理
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183815.84950479601709236953856307066692:50001231000000:2800:24CE798F44299BD4053A0967CBAD12932312EA9CA22571F526C914EC9FDDAFE9.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* 卡片使用方：显示卡片内容的宿主应用，控制卡片在宿主中展示的位置，当前仅系统应用可以作为卡片使用方。
* 卡片提供方：提供卡片显示内容的应用，控制卡片的显示内容、控件布局以及控件点击事件。
* 卡片管理服务：用于管理系统中所添加卡片的常驻代理服务，提供[formProvider](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-app-form-formprovider-0000001544464081-V3)接口能力，同时提供卡片对象的管理与使用以及卡片周期性刷新等能力。
* 卡片渲染服务：用于管理卡片渲染实例，渲染实例与卡片使用方上的卡片组件一一绑定。卡片渲染服务运行卡片页面代码widgets.abc进行渲染，并将渲染后的数据发送至卡片使用方对应的卡片组件。

图2 ArkTS卡片渲染服务运行原理
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183815.70324623892566542504943558891522:50001231000000:2800:D0976010FBE176746DD88FF624885BD25BAAF25B71B956FF9BCB81F13528EBFA.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

与JS卡片相比，ArkTS卡片支持在卡片中运行逻辑代码，为确保ArkTS卡片发生问题后不影响卡片使用方应用的使用，ArkTS卡片新增了卡片渲染服务用于运行卡片页面代码widgets.abc，卡片渲染服务由卡片管理服务管理。卡片使用方的每个卡片组件都对应了卡片渲染服务里的一个渲染实例，同一应用提供方的渲染实例运行在同一个虚拟机运行环境中，不同应用提供方的渲染实例运行在不同的虚拟机运行环境中，通过虚拟机运行环境隔离不同应用提供方卡片之间的资源与状态。开发过程中需要注意的是globalThis对象的使用，相同应用提供方的卡片globalThis对象是同一个，不同应用提供方的卡片globalThis对象是不同的。

## ArkTS卡片的优势

卡片作为应用的一个快捷入口，ArkTS卡片相较于JS卡片具备如下几点优势：

* 统一开发范式，提升开发体验和开发效率。OpenHarmony在2022年发布了声明式范式的UI开发框架，而卡片还延续了css/hml/json三段式类Web范式的开发方式，提高了开发者的学习成本，提供ArkTS卡片能力后，统一了卡片和页面的开发范式，页面的布局可以直接复用到卡片布局中，提升开发体验和开发效率。

  图3 卡片工程结构对比
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183815.31341413307437818634965999621111:50001231000000:2800:A0700F36404CC8476BFB529FC8474D1AE441340772C11E186493AF60E4199792.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")
* 增强了卡片的能力，使卡片更加万能。

  * 新增了动效的能力：ArkTS卡片开放了[属性动画](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-animatorproperty-0000001478181445-V3)和[显式动画](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/ts-explicit-animation-0000001478341181-V3)的能力，使卡片的交互更加友好。
  * 新增了自定义绘制的能力：ArkTS卡片开放了Canvas画布组件，卡片可以使用自定义绘制的能力构建更多样的显示和交互效果。
  * 允许卡片中运行逻辑代码：开放逻辑代码运行后很多业务逻辑可以在卡片内部自闭环，拓宽了卡片的业务适用场景。

## ArkTS卡片的约束

ArkTS卡片相较于JS卡片具备了更加丰富的能力，但也增加了使用卡片进行恶意行为的风险。由于ArkTS卡片显示在使用方应用中，使用方应用一般为桌面应用，为确保桌面的使用体验以及功耗相关考虑，对ArkTS卡片的能力做了以下约束：

* 不支持加载so。
* 不支持使用native语言开发。
* 仅支持声明式范式的[部分](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-ui-widget-page-overview-0000001553173049-V3)组件、事件、动效、数据管理、状态管理和API能力。
* 卡片的事件处理和使用方的事件处理是独立的，建议在使用方支持左右滑动的场景下卡片内容不要使用左右滑动功能的组件，以防手势冲突影响交互体验。

除此之外，当前ArkTS卡片还存在如下约束：

* 暂不支持导入模块。
* 暂不支持极速预览。
* 暂不支持断点调试能力。
* 暂不支持Hot Reload热重载。

