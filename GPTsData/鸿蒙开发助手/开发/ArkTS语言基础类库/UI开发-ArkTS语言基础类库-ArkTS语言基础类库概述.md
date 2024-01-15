# ArkTS语言基础类库概述

更新时间: 2024-01-15 12:17

ArkTS语言基础类库是HarmonyOS系统上为应用开发者提供的常用基础能力，主要包含能力如下图所示。

图1 ArkTS语言基础类库能力示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121184001.31042134052528435813962585267082:50001231000000:2800:D3932B543B13F2266F337FFE84FD1C3580CE973D38863F857329A75CA64D0BBC.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

* 提供[异步并发和多线程并发](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/concurrency-overview-0000001681489593-V3)的能力。
  * 支持Promise和async/await等标准的JS异步并发能力。
  * TaskPool为应用程序提供一个多线程的运行环境，降低整体资源的消耗、提高系统的整体性能，开发者无需关心线程实例的生命周期。
  * Worker支持多线程并发，支持Worker线程和宿主线程之间进行通信，开发者需要主动创建和关闭Worker线程。
* 提供常见的[容器类库增、删、改、查](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/container-overview-0000001681129705-V3)的能力。
* 提供XML、URL、URI构造和解析的能力。
  * XML被设计用来传输和存储数据，是一种可扩展标记语言。语言基础类库提供了[XML生成、解析与转换](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-overview-0000001681369765-V3)的能力。
  * URL、URI构造和解析能力：其中[URI](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-uri-0000001477981477-V3)是统一资源标识符，可以唯一标识一个资源。[URL](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-url-0000001427902744-V3)为统一资源定位符，可以提供找到该资源的路径。
* 提供常见的[字符串和二进制数据处理](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-util-0000001428062016-V3)的能力，以及[控制台打印](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-logs-0000001428061992-V3)的相关能力。
  * 字符串编解码功能。
  * 基于Base64的字节编码和解码功能。
  * 提供常见的有理数操作支持，包括有理数的比较、获取分子分母等功能。
  * 提供Scope接口用于描述一个字段的有效范围。
  * 提供二进制数据处理的能力，常见于TCP流或文件系统操作等场景中用于处理二进制数据流。
  * Console提供控制台打印的能力。
* 提供[获取进程信息和操作进程](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-process-0000001478061973-V3)的能力。

