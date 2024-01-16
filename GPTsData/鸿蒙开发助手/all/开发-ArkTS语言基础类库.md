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



# 并发概述

更新时间: 2024-01-15 11:54

并发是指在同一时间段内，能够处理多个任务的能力。为了提升应用的响应速度与帧率，以及防止耗时任务对主线程的干扰，HarmonyOS系统提供了异步并发和多线程并发两种处理策略。

* 异步并发是指异步代码在执行到一定程度后会被暂停，以便在未来某个时间点继续执行，这种情况下，同一时间只有一段代码在执行。
* 多线程并发允许在同一时间段内同时执行多段代码。在主线程继续响应用户操作和更新UI的同时，后台也能执行耗时操作，从而避免应用出现卡顿。

并发能力在多种场景中都有应用，其中包括[单次I/O任务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/single-io-development-0000001681129701-V3)、[CPU密集型任务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/cpu-intensive-task-development-0000001681369757-V3)、[I/O密集型任务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/io-intensive-task-development-0000001681489597-V3)和[同步任务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/sync-task-development-0000001632370254-V3)等。开发者可以根据不同的场景，选择相应的并发策略进行优化和开发。

ArkTS支持异步并发和多线程并发。

* Promise和async/await提供异步并发能力，适用于单次I/O任务的开发场景。详细请参见[异步并发概述](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/async-concurrency-overview-0000001632690002-V3)。
* TaskPool和Worker提供多线程并发能力，适用于CPU密集型任务、I/O密集型任务和同步任务等并发场景。详细请参见[多线程并发概述](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/multi-thread-concurrency-overview-0000001632530090-V3)。



# 异步并发概述

更新时间: 2024-01-15 11:54

Promise和async/await提供异步并发能力，是标准的JS异步语法。异步代码会被挂起并在之后继续执行，同一时间只有一段代码执行，适用于[单次I/O任务](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/single-io-development-0000001681129701-V3)的场景开发，例如一次网络请求、一次文件读写等操作。

异步语法是一种编程语言的特性，允许程序在执行某些操作时不必等待其完成，而是可以继续执行其他操作。

## Promise

Promise是一种用于处理异步操作的对象，可以将异步操作转换为类似于同步操作的风格，以方便代码编写和维护。Promise提供了一个状态机制来管理异步操作的不同阶段，并提供了一些方法来注册回调函数以处理异步操作的成功或失败的结果。

Promise有三种状态：pending（进行中）、fulfilled（已完成）和rejected（已拒绝）。Promise对象创建后处于pending状态，并在异步操作完成后转换为fulfilled或rejected状态。

最基本的用法是通过构造函数实例化一个Promise对象，同时传入一个带有两个参数的函数，通常称为executor函数。executor函数接收两个参数：resolve和reject，分别表示异步操作成功和失败时的回调函数。例如，以下代码创建了一个Promise对象并模拟了一个异步操作：

```
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    const randomNumber = Math.random();
    if (randomNumber > 0.5) {
      resolve(randomNumber);
    } else {
      reject(new Error('Random number is too small'));
    }
  }, 1000);
});
```

上述代码中，setTimeout函数模拟了一个异步操作，并在1秒钟后随机生成一个数字。如果随机数大于0.5，则执行resolve回调函数并将随机数作为参数传递；否则执行reject回调函数并传递一个错误对象作为参数。

Promise对象创建后，可以使用then方法和catch方法指定fulfilled状态和rejected状态的回调函数。then方法可接受两个参数，一个处理fulfilled状态的函数，另一个处理rejected状态的函数。只传一个参数则表示状态改变就执行，不区分状态结果。使用catch方法注册一个回调函数，用于处理“失败”的结果，即捕获Promise的状态改变为rejected状态或操作失败抛出的异常。例如：

```
promise.then(result => {
  console.info(`Random number is ${result}`);
}).catch(error => {
  console.error(error.message);
});
```

上述代码中，then方法的回调函数接收Promise对象的成功结果作为参数，并将其输出到控制台上。如果Promise对象进入rejected状态，则catch方法的回调函数接收错误对象作为参数，并将其输出到控制台上。

## async/await

async/await是一种用于处理异步操作的Promise语法糖，使得编写异步代码变得更加简单和易读。通过使用async关键字声明一个函数为异步函数，并使用await关键字等待Promise的解析（完成或拒绝），以同步的方式编写异步操作的代码。

async函数是一个返回Promise对象的函数，用于表示一个异步操作。在async函数内部，可以使用await关键字等待一个Promise对象的解析，并返回其解析值。如果一个async函数抛出异常，那么该函数返回的Promise对象将被拒绝，并且异常信息会被传递给Promise对象的onRejected()方法。

下面是一个使用async/await的例子，其中模拟了一个异步操作，该操作会在3秒钟后返回一个字符串。

```
async function myAsyncFunction() {
  const result = await new Promise((resolve) => {
    setTimeout(() => {
      resolve('Hello, world!');
    }, 3000);
  });
  console.info(String(result)); // 输出： Hello, world!
}

myAsyncFunction();
```

在上述示例代码中，使用了await关键字来等待Promise对象的解析，并将其解析值存储在result变量中。

需要注意的是，由于要等待异步操作完成，因此需要将整个操作包在async函数中。除了在async函数中使用await外，还可以使用try/catch块来捕获异步操作中的异常。

```
async function myAsyncFunction() {
  try {
    const result = await new Promise((resolve) => {
      resolve('Hello, world!');
    });
  } catch (e) {
    console.error(`Get exception: ${e}`);
  }
}

myAsyncFunction();
```



# 单次I/O任务开发指导

更新时间: 2024-01-15 11:54

Promise和async/await提供异步并发能力，适用于单次I/O任务的场景开发，本文以使用异步进行单次文件写入为例来提供指导。

1. 实现单次I/O任务逻辑。
```
import fs from '@ohos.file.fs';
import common from '@ohos.app.ability.common';

async function write(data: string, file: fs.File): Promise<void> {
  fs.write(file.fd, data).then((writeLen: number) => {
    console.info('write data length is: ' + writeLen)
  }).catch((err) => {
    console.error(`Failed to write data. Code is ${err.code}, message is ${err.message}`);
  })
}
```
2. 采用异步能力调用单次I/O任务。示例中的filePath的获取方式请参见[获取应用文件路径](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%B7%AF%E5%BE%84)。
```
async function testFunc(): Promise<void> {
  let context = getContext() as common.UIAbilityContext;
  let filePath: string = context.filesDir + "/test.txt"; // 应用文件路径
  let file: fs.File = await fs.open(filePath, fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
  write('Hello World!', file).then(() => {
    console.info('Succeeded in writing data.');
  }).catch((err) => {
    console.error(`Failed to write data. Code is ${err.code}, message is ${err.message}`);
  })
  fs.close(file);
}
testFunc();
```



# 多线程并发概述

更新时间: 2024-01-15 11:54

## 简介

并发模型是用来实现不同应用场景中并发任务的编程模型，常见的并发模型分为基于内存共享的并发模型和基于消息通信的并发模型。

Actor并发模型作为基于消息通信并发模型的典型代表，不需要开发者去面对锁带来的一系列复杂偶发的问题，同时并发度也相对较高，因此得到了广泛的支持和使用，也是当前ArkTS语言选择的并发模型。

由于Actor模型的内存隔离特性，所以需要进行跨线程的数据序列化传输。

## 数据传输对象

目前支持传输的数据对象可以分为[普通对象](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/multi-thread-concurrency-overview-0000001632530090-V3#ZH-CN_TOPIC_0000001632530090__%E6%99%AE%E9%80%9A%E5%AF%B9%E8%B1%A1)、[可转移对象](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/multi-thread-concurrency-overview-0000001632530090-V3#ZH-CN_TOPIC_0000001632530090__%E5%8F%AF%E8%BD%AC%E7%A7%BB%E5%AF%B9%E8%B1%A1)、[可共享对象](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/multi-thread-concurrency-overview-0000001632530090-V3#ZH-CN_TOPIC_0000001632530090__%E5%8F%AF%E5%85%B1%E4%BA%AB%E5%AF%B9%E8%B1%A1)、[Native绑定对象](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/multi-thread-concurrency-overview-0000001632530090-V3#section13599616134818)四种。

### 普通对象

普通对象传输采用标准的结构化克隆算法（Structured Clone）进行序列化，此算法可以通过递归的方式拷贝传输对象，相较于其他序列化的算法，支持的对象类型更加丰富。

序列化支持的类型包括：除Symbol之外的基础类型、Date、String、RegExp、Array、Map、Set、Object（仅限简单对象，比如通过“{}”或者“new Object”创建，普通对象仅支持传递属性，不支持传递其原型及方法）、ArrayBuffer、TypedArray。

### 可转移对象

可转移对象（Transferable object）传输采用地址转移进行序列化，不需要内容拷贝，会将ArrayBuffer的所有权转移给接收该ArrayBuffer的线程，转移后该ArrayBuffer在发送它的线程中变为不可用，不允许再访问。

```
// 定义可转移对象
let buffer = new ArrayBuffer(100);
```

### 可共享对象

共享对象SharedArrayBuffer，拥有固定长度，可以存储任何类型的数据，包括数字、字符串等。

共享对象传输指SharedArrayBuffer支持在多线程之间传递，传递之后的SharedArrayBuffer对象和原始的SharedArrayBuffer对象可以指向同一块内存，进而达到内存共享的目的。

SharedArrayBuffer对象存储的数据在同时被修改时，需要通过原子操作保证其同步性，即下个操作开始之前务必需要等到上个操作已经结束。

```
// 定义可共享对象，可以使用Atomics进行操作
let sharedBuffer = new SharedArrayBuffer(1024);
```

### Native绑定对象

Native绑定对象（Native Binding Object）是系统所提供的对象，该对象与底层系统功能进行绑定，提供直接访问底层系统功能的能力。

当前支持序列化传输的Native绑定对象主要包含：[Context](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3)和[RemoteObject](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-rpc-0000001427902704-V3#ZH-CN_TOPIC_0000001523488478__remoteobject)。

Context对象包含应用程序组件的上下文信息，它提供了一种访问系统服务和资源的方式，使得应用程序组件可以与系统进行交互。获取Context信息的方法可以参考[获取上下文信息](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3)。

RemoteObject对象的主要作用是实现远程通信的功能，它允许在不同的进程间传递对象的引用，使得不同进程之间可以共享对象的状态和方法，服务提供者必须继承此类，RemoteObject对象的创建可以参考[RemoteObject的实现](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-rpc-0000001427902704-V3#ZH-CN_TOPIC_0000001523488478__remoteobject)。

## TaskPool和Worker

ArkTS提供了TaskPool和Worker两种并发能力供开发者选择，其具体的实现特点和各自的适用场景存在差异，详细请参见[TaskPool和Worker的对比](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/taskpool-vs-worker-0000001632849934-V3)。



# TaskPool和Worker的对比

更新时间: 2024-01-15 12:18

TaskPool（任务池）和Worker的作用是为应用程序提供一个多线程的运行环境，用于处理耗时的计算任务或其他密集型任务。可以有效地避免这些任务阻塞主线程，从而最大化系统的利用率，降低整体资源消耗，并提高系统的整体性能。

本文将从[实现特点](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/taskpool-vs-worker-0000001632849934-V3#ZH-CN_TOPIC_0000001632849934__%E5%AE%9E%E7%8E%B0%E7%89%B9%E7%82%B9%E5%AF%B9%E6%AF%94)和[适用场景](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/taskpool-vs-worker-0000001632849934-V3#ZH-CN_TOPIC_0000001632849934__%E9%80%82%E7%94%A8%E5%9C%BA%E6%99%AF%E5%AF%B9%E6%AF%94)两个方面来进行TaskPool与Worker的比较，同时提供了各自运作机制和注意事项的相关说明。

## 实现特点对比

表1 TaskPool和Worker的实现特点对比

| 实现             | TaskPool                                                                                                                     | Worker                                                                                                                       |
| :--------------- | :--------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| 内存模型         | 线程间隔离，内存不共享。                                                                                                     | 线程间隔离，内存不共享。                                                                                                     |
| 参数传递机制     | 采用标准的结构化克隆算法（Structured Clone）进行序列化、反序列化，完成参数传递。支持ArrayBuffer转移和SharedArrayBuffer共享。 | 采用标准的结构化克隆算法（Structured Clone）进行序列化、反序列化，完成参数传递。支持ArrayBuffer转移和SharedArrayBuffer共享。 |
| 参数传递         | 直接传递，无需封装，默认进行transfer。                                                                                       | 消息对象唯一参数，需要自己封装。                                                                                             |
| 方法调用         | 直接将方法传入调用。                                                                                                         | 在Worker线程中进行消息解析并调用对应方法。                                                                                   |
| 返回值           | 异步调用后默认返回。                                                                                                         | 主动发送消息，需在onmessage解析赋值。                                                                                        |
| 生命周期         | TaskPool自行管理生命周期，无需关心任务负载高低。                                                                             | 开发者自行管理Worker的数量及生命周期。                                                                                       |
| 任务池个数上限   | 自动管理，无需配置。                                                                                                         | 同个进程下，最多支持同时开启8个Worker线程。                                                                                  |
| 任务执行时长上限 | 无限制。                                                                                                                     | 无限制。                                                                                                                     |
| 设置任务的优先级 | 不支持。                                                                                                                     | 不支持。                                                                                                                     |
| 执行任务的取消   | 支持取消任务队列中等待的任务。                                                                                               | 不支持。                                                                                                                     |

## 适用场景对比

TaskPool偏向独立任务维度，该任务在线程中执行，无需关注线程的生命周期，超长任务（大于3分钟）会被系统自动回收；而Worker偏向线程的维度，支持长时间占据线程执行，需要主动管理线程生命周期。

常见的一些开发场景及适用具体说明如下：

* 有关联的一系列同步任务。例如在一些需要创建、使用句柄的场景中，句柄创建每次都是不同的，该句柄需永久保存，保证使用该句柄进行操作，需要使用Worker。
* 需要频繁取消的任务。例如图库大图浏览场景，为提升体验，会同时缓存当前图片左右侧各2张图片，往一侧滑动跳到下一张图片时，要取消另一侧的一个缓存任务，需要使用TaskPool。
* 大量或者调度点较分散的任务。例如大型应用的多个模块包含多个耗时任务，不方便使用8个Worker去做负载管理，推荐采用TaskPool。

## TaskPool运作机制

图1 TaskPool运作机制示意图
![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231218140407.72303471733304822498895920144597:50001231000000:2800:9A860A4FCCC3489885487880A15C59278303784CCD5BF08B1CAC971E4500C61B.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

TaskPool支持开发者在主线程封装任务抛给任务队列，系统选择合适的工作线程，进行任务的分发及执行，再将结果返回给主线程。接口直观易用，支持任务的执行、取消。工作线程数量上限为4。

## Worker运作机制

图2 Worker运作机制示意图

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231218140407.10000975603531062670663869108718:50001231000000:2800:F764A32A736E101B2C0F4AFF3BF4E7270A7BEB3CFD00A02E2226BE34094C5D22.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

创建Worker的线程称为宿主线程（不一定是主线程，工作线程也支持创建Worker子线程），Worker自身的线程称为Worker子线程（或Actor线程、工作线程）。每个Worker子线程与宿主线程拥有独立的实例，包含基础设施、对象、代码段等。Worker子线程和宿主线程之间的通信是基于消息传递的，Worker通过序列化机制与宿主线程之间相互通信，完成命令及数据交互。

## TaskPool注意事项

* 实现任务的函数需要使用装饰器[@Concurrent](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-concurrent-0000001700975510-V3)标注，且仅支持在.ets文件中使用。

* 实现任务的函数入参需满足序列化支持的类型，详情请参见[数据传输对象](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/multi-thread-concurrency-overview-0000001632530090-V3#ZH-CN_TOPIC_0000001632530090__%E6%95%B0%E6%8D%AE%E4%BC%A0%E8%BE%93%E5%AF%B9%E8%B1%A1)。
* 由于不同线程中上下文对象是不同的，因此TaskPool工作线程只能使用线程安全的库，例如UI相关的非线程安全库不能使用。
* 序列化传输的数据量大小限制为16MB。

## Worker注意事项

* 创建Worker时，传入的Worker.ts路径在不同版本有不同的规则，详情请参见[文件路径注意事项](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/taskpool-vs-worker-0000001632849934-V3#ZH-CN_TOPIC_0000001632849934__%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)。

* Worker创建后需要手动管理生命周期，且最多同时运行的Worker子线程数量为8个，详情请参见[生命周期注意事项](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/taskpool-vs-worker-0000001632849934-V3#ZH-CN_TOPIC_0000001632849934__%E7%94%9F%E5%91%BD%E5%91%A8%E6%9C%9F%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)。
* [Ability类型](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-package-structure-stage-0000001478061425-V3)的Module支持使用Worker，[Library类型](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-package-structure-stage-0000001478061425-V3)的Module不支持使用Worker。
* 创建Worker不支持使用其他Module的Worker.ts文件，即不支持跨模块调用Worker。
* 由于不同线程中上下文对象是不同的，因此Worker线程只能使用线程安全的库，例如UI相关的非线程安全库不能使用。
* 序列化传输的数据量大小限制为16MB。

### 文件路径注意事项

当使用Worker模块具体功能时，均需先构造Worker实例对象，其构造函数与API版本相关。

```
// 导入模块
import worker from '@ohos.worker';

// API 9及之后版本使用：
const worker1 = new worker.ThreadWorker(scriptURL);
// API 8及之前版本使用：
const worker1 = new worker.Worker(scriptURL);
```

构造函数需要传入Worker的路径（scriptURL），Worker文件存放位置默认路径为Worker文件所在目录与pages目录属于同级。

Stage模型

构造函数中的scriptURL示例如下：

```
// 导入模块
import worker from '@ohos.worker';

// 写法一
// Stage模型-目录同级（entry模块下，workers目录与pages目录同级）
const worker1 = new worker.ThreadWorker('entry/ets/workers/MyWorker.ts', {name:"first worker in Stage model"});
// Stage模型-目录不同级（entry模块下，workers目录是pages目录的子目录）
const worker2 = new worker.ThreadWorker('entry/ets/pages/workers/MyWorker.ts');

// 写法二
// Stage模型-目录同级（entry模块下，workers目录与pages目录同级），假设bundlename是com.example.workerdemo
const worker3 = new worker.ThreadWorker('@bundle:com.example.workerdemo/entry/ets/workers/worker');
// Stage模型-目录不同级（entry模块下，workers目录是pages目录的子目录），假设bundlename是com.example.workerdemo
const worker4 = new worker.ThreadWorker('@bundle:com.example.workerdemo/entry/ets/pages/workers/worker');
```

* 基于Stage模型工程目录结构，写法一的路径含义：
  * entry：module.json5文件中module的name属性对应值。
  * ets：用于存放ets源码，固定目录。
  * workers/MyWorker.ts：worker源文件在ets目录下的路径。
* 基于Stage模型工程目录结构，写法二的路径含义：
  * @bundle：固定标签。
  * bundlename：当前应用包名。
  * entryname：module.json5文件中module的name属性对应值。
  * ets：用于存放ets源码，固定目录。
  * workerdir/workerfile：worker源文件在ets目录下的路径，可不带文件后缀名。

FA模型

构造函数中的scriptURL示例如下：

```
// 导入模块
import worker from '@ohos.worker';

// FA模型-目录同级（entry模块下，workers目录与pages目录同级）
const worker1 = new worker.ThreadWorker('workers/worker.js', {name:'first worker in FA model'});
// FA模型-目录不同级（entry模块下，workers目录与pages目录的父目录同级）
const worker2 = new worker.ThreadWorker('../workers/worker.js');
```

### 生命周期注意事项

* Worker的创建和销毁耗费性能，建议开发者合理管理已创建的Worker并重复使用。Worker空闲时也会一直运行，因此当不需要Worker时，可以调用[terminate()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__terminate9)接口或[parentPort.close()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__close9)方法主动销毁Worker。若Worker处于已销毁或正在销毁等非运行状态时，调用其功能接口，会抛出相应的错误。

* Worker存在数量限制，支持最多同时存在8个Worker。
  * 在API version 8及之前的版本，当Worker数量超出限制时，会抛出“Too many workers, the number of workers exceeds the maximum.”错误。
  * 从API version 9开始，当Worker数量超出限制时，会抛出“Worker initialization failure, the number of workers exceeds the maximum.”错误。



# @Concurrent装饰器：校验并发函数

更新时间: 2024-01-15 12:19

在使用[TaskPoo](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-taskpool-0000001544703993-V3)l时，执行的并发函数需要使用该装饰器修饰，否则无法通过相关校验。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

## 装饰器说明

| @Concurrent并发装饰器  | 说明                                                                                             |
| :----------------------- | :------------------------------------------------------------------------------------------------- |
| 装饰器参数             | 无。                                                                                             |
| 使用场景               | 仅支持在Stage模型的工程中使用。                                                                  |
| 装饰的函数类型         | 允许标注async函数或普通函数。禁止标注generator、箭头函数、method。不支持类成员函数或者匿名函数。 |
| 装饰的函数内的变量类型 | 允许使用local变量、入参和通过import引入的变量。禁止使用闭包变量。                                |

## 装饰器使用示例



```
import taskpool from '@ohos.taskpool';

@Concurrent
function add(num1: number, num2: number): number {
  return num1 + num2;
}

async function ConcurrentFunc(): Promise<void> {
  try {
    let task: taskpool.Task = new taskpool.Task(add, 1, 2);
    console.info("taskpool res is: " + await taskpool.execute(task));
  } catch (e) {
    console.error("taskpool execute error is: " + e);
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            ConcurrentFunc();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```



# CPU密集型任务开发指导

更新时间: 2024-01-15 12:19

CPU密集型任务是指需要占用系统资源处理大量计算能力的任务，需要长时间运行，这段时间会阻塞线程其它事件的处理，不适宜放在主线程进行。例如图像处理、视频编码、数据分析等。

基于多线程并发机制处理CPU密集型任务可以提高CPU利用率，提升应用程序响应速度。

当进行一系列同步任务时，推荐使用Worker；而进行大量或调度点较为分散的独立任务时，不方便使用8个Worker去做负载管理，推荐采用TaskPool。接下来将以图像直方图处理以及后台长时间的模型预测任务分别进行举例。

## 使用TaskPool进行图像直方图处理

1. 实现图像处理的业务逻辑。
2. 数据分段，将各段数据通过不同任务的执行完成图像处理。
  创建[Task](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-taskpool-0000001544703993-V3#ZH-CN_TOPIC_0000001574248457__task)，通过[execute()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-taskpool-0000001544703993-V3#ZH-CN_TOPIC_0000001574248457__taskpoolexecute-1)执行任务，在当前任务结束后，会将直方图处理结果同时返回。
3. 结果数组汇总处理。

```
import taskpool from '@ohos.taskpool';

@Concurrent
function imageProcessing(dataSlice: ArrayBuffer) {
  // 步骤1: 具体的图像处理操作及其他耗时操作
  return dataSlice;
}

function histogramStatistic(pixelBuffer: ArrayBuffer) {
  // 步骤2: 分成三段并发调度
  let number = pixelBuffer.byteLength / 3;
  let buffer1 = pixelBuffer.slice(0, number);
  let buffer2 = pixelBuffer.slice(number, number * 2);
  let buffer3 = pixelBuffer.slice(number * 2);

  let task1 = new taskpool.Task(imageProcessing, buffer1);
  let task2 = new taskpool.Task(imageProcessing, buffer2);
  let task3 = new taskpool.Task(imageProcessing, buffer3);

  taskpool.execute(task1).then((ret: ArrayBuffer[]) => {
    // 步骤3: 结果处理
  });
  taskpool.execute(task2).then((ret: ArrayBuffer[]) => {
    // 步骤3: 结果处理
  });
  taskpool.execute(task3).then((ret: ArrayBuffer[]) => {
    // 步骤3: 结果处理
  });
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let data: ArrayBuffer;
            histogramStatistic(data);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

## 使用Worker进行长时间数据分析

本文通过某地区提供的房价数据训练一个简易的房价预测模型，该模型支持通过输入房屋面积和房间数量去预测该区域的房价，模型需要长时间运行，房价预测需要使用前面的模型运行结果，因此需要使用Worker。

1. DevEco Studio提供了Worker创建的模板，新建一个Worker线程，例如命名为“MyWorker”。
  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231218140408.87340488082680049893045001954655:50001231000000:2800:37F81EA60854CE8DDEDA5269AF76D5486FCAAD748F82435792A46BFA3F814743.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)
2. 在主线程中通过调用ThreadWorker的[constructor()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__constructor9)方法创建Worker对象，当前线程为宿主线程。

```
import worker from '@ohos.worker';

const workerInstance = new worker.ThreadWorker('entry/ets/workers/MyWorker.ts');
```
3. 在宿主线程中通过调用[onmessage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__onmessage9)方法接收Worker线程发送过来的消息，并通过调用[postMessage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__postmessage9)方法向Worker线程发送消息。
  例如向Worker线程发送训练和预测的消息，同时接收Worker线程发送回来的消息。

```
// 接收Worker子线程的结果
workerInstance.onmessage = function(e) {
  // data：Worker线程发送的信息
  let data = e.data;
  console.info('MyWorker.ts onmessage');
}

workerInstance.onerror = function (d) {
  // 接收Worker子线程的错误信息
}

// 向Worker子线程发送训练消息
workerInstance.postMessage({ 'type': 0 });
// 向Worker子线程发送预测消息
workerInstance.postMessage({ 'type': 1, 'value': [90, 5] });
```
4. 在MyWorker.ts文件中绑定Worker对象，当前线程为Worker线程。

```
import worker, { ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@ohos.worker';

let workerPort: ThreadWorkerGlobalScope = worker.workerPort;
```
5. 在Worker线程中通过调用[onmessage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__onmessage9-1)方法接收宿主线程发送的消息内容，并通过调用[postMessage()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__postmessage9-2)方法向宿主线程发送消息。
  例如在Worker线程中定义预测模型及其训练过程，同时与主线程进行信息交互。

```
import worker, { ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@ohos.worker';

let workerPort: ThreadWorkerGlobalScope = worker.workerPort;

// 定义训练模型及结果 
let result;

// 定义预测函数
function predict(x) {
  return result[x];
}

// 定义优化器训练过程
function optimize() {
  result = {};
}

// Worker线程的onmessage逻辑
workerPort.onmessage = function (e: MessageEvents) {
  let data = e.data
  // 根据传输的数据的type选择进行操作
  switch (data.type) {
    case 0:
    // 进行训练
      optimize();
    // 训练之后发送主线程训练成功的消息
      workerPort.postMessage({ type: 'message', value: 'train success.' });
      break;
    case 1:
    // 执行预测
      const output = predict(data.value);
    // 发送主线程预测的结果
      workerPort.postMessage({ type: 'predict', value: output });
      break;
    default:
      workerPort.postMessage({ type: 'message', value: 'send message is invalid' });
      break;
  }
}
```
6. 在Worker线程中完成任务之后，执行Worker线程销毁操作。销毁线程的方式主要有两种：根据需要可以在宿主线程中对Worker线程进行销毁；也可以在Worker线程中主动销毁Worker线程。
  在宿主线程中通过调用[onexit()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__onexit9)方法定义Worker线程销毁后的处理逻辑。

```
// Worker线程销毁后，执行onexit回调方法
workerInstance.onexit = function() {
  console.info("main thread terminate");
}
```

  方式一：在宿主线程中通过调用[terminate()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__terminate9)方法销毁Worker线程，并终止Worker接收消息。

```
// 销毁Worker线程
workerInstance.terminate();
```

  方式二：在Worker线程中通过调用[close()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-worker-0000001427902752-V3#ZH-CN_TOPIC_0000001574088505__close9)方法主动销毁Worker线程，并终止Worker接收消息。

```
// 销毁线程
workerPort.close();
```



# I/O密集型任务开发指导

更新时间: 2024-01-15 11:54

使用异步并发可以解决单次I/O任务阻塞的问题，但是如果遇到I/O密集型任务，同样会阻塞线程中其它任务的执行，这时需要使用多线程并发能力来进行解决。

I/O密集型任务的性能重点通常不在于CPU的处理能力，而在于I/O操作的速度和效率。这种任务通常需要频繁地进行磁盘读写、网络通信等操作。此处以频繁读写系统文件来模拟I/O密集型并发任务的处理。

1. 定义并发函数，内部密集调用I/O能力。
```
import fs from '@ohos.file.fs';

// 定义并发函数，内部密集调用I/O能力
@Concurrent
async function concurrentTest(fileList: string[]) {
  // 写入文件的实现
  async function write(data, filePath) {
    let file = await fs.open(filePath, fs.OpenMode.READ_WRITE);
    await fs.write(file.fd, data);
    fs.close(file);
  }
  // 循环写文件操作
  for (let i = 0; i < fileList.length; i++) {
    write('Hello World!', fileList[i]).then(() => {
      console.info(`Succeeded in writing the file. FileList: ${fileList[i]}`);
    }).catch((err) => {
      console.error(`Failed to write the file. Code is ${err.code}, message is ${err.message}`)
      return false;
    })
  }
  return true;
}
```
2. 使用TaskPool执行包含密集I/O的并发函数：通过调用[execute()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-taskpool-0000001544703993-V3#ZH-CN_TOPIC_0000001574248457__taskpoolexecute)方法执行任务，并在回调中进行调度结果处理。示例中的filePath1和filePath2的获取方式请参见[获取应用文件路径](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/application-context-stage-0000001427744560-V3#ZH-CN_TOPIC_0000001574128741__%E8%8E%B7%E5%8F%96%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E8%B7%AF%E5%BE%84)。
```
import taskpool from '@ohos.taskpool';

let filePath1 = ...; // 应用文件路径
let filePath2 = ...;

// 使用TaskPool执行包含密集I/O的并发函数
// 数组较大时，I/O密集型任务任务分发也会抢占主线程，需要使用多线程能力
taskpool.execute(concurrentTest, [filePath1, filePath2]).then((ret) => {
  // 调度结果处理
  console.info(`The result: ${ret}`);
})
```



# 同步任务开发指导

更新时间: 2024-01-15 11:54

同步任务是指在多个线程之间协调执行的任务，其目的是确保多个任务按照一定的顺序和规则执行，例如使用锁来防止数据竞争。

同步任务的实现需要考虑多个线程之间的协作和同步，以确保数据的正确性和程序的正确执行。

由于TaskPool偏向于单个独立的任务，因此当各个同步任务之间相对独立时推荐使用TaskPool，例如一系列导入的静态方法，或者单例实现的方法。如果同步任务之间有关联性，则需要使用Worker，例如无法单例创建的类对象实现的方法。

## 使用TaskPool处理同步任务

当调度独立的同步任务，或者一系列同步任务为静态方法实现，或者可以通过单例构造唯一的句柄或类对象，可在不同任务池之间使用时，推荐使用TaskPool。

1. 定义并发函数，内部调用同步方法。
2. 创建任务，并通过TaskPool执行，再对异步结果进行操作。创建[Task](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-taskpool-0000001544703993-V3#ZH-CN_TOPIC_0000001574248457__task)，通过[execute()](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-taskpool-0000001544703993-V3#ZH-CN_TOPIC_0000001574248457__taskpoolexecute-1)执行同步任务。

模拟一个包含同步调用的单实例类。

```
// Handle.ts 代码
export default class Handle {
  static getInstance() {
    // 返回单例对象
  }

  static syncGet() {
    // 同步Get方法
    return;
  }

  static syncSet(num: number) {
    // 同步Set方法
    return;
  }
}
```

业务使用TaskPool调用相关同步方法的代码。

```
// Index.ets代码
import taskpool from '@ohos.taskpool';
import Handle from './Handle'; // 返回静态句柄

// 步骤1: 定义并发函数，内部调用同步方法
@Concurrent
function func(num: number) {
  // 调用静态类对象中实现的同步等待调用
  Handle.syncSet(num);
  // 或者调用单例对象中实现的同步等待调用
  Handle.getInstance().syncGet();
  return true;
}

// 步骤2: 创建任务并执行
async function asyncGet() {
  // 创建task并传入函数func
  let task = new taskpool.Task(func, 1);
  // 执行task任务，获取结果res
  let res = await taskpool.execute(task);
  // 对同步逻辑后的结果进行操作
  console.info(String(res));
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // 步骤3: 执行并发操作
            asyncGet();
          })
      }
      .width('100%')
      .height('100%')
    }
  }
}
```

## 使用Worker处理关联的同步任务

当一系列同步任务需要使用同一个句柄调度，或者需要依赖某个类对象调度，无法在不同任务池之间共享时，需要使用Worker。

1. 在主线程中创建Worker对象，同时接收Worker线程发送回来的消息。
```
import worker from '@ohos.worker';

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            let w = new worker.ThreadWorker('entry/ets/workers/MyWorker.ts');
            w.onmessage = function (d) {
              // 接收Worker子线程的结果
            }
            w.onerror = function (d) {
              // 接收Worker子线程的错误信息
            }
            // 向Worker子线程发送Set消息
            w.postMessage({'type': 0, 'data': 'data'})
            // 向Worker子线程发送Get消息
            w.postMessage({'type': 1})
            // ...
            // 根据实际业务，选择时机以销毁线程
            w.terminate()
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
2. 在Worker线程中绑定Worker对象，同时处理同步任务逻辑。
```
// handle.ts代码
export default class Handle {
  syncGet() {
    return;
  }

  syncSet(num: number) {
    return;
  }
}

// Worker.ts代码
import worker, { ThreadWorkerGlobalScope, MessageEvents } from '@ohos.worker';
import Handle from './handle.ts'  // 返回句柄

var workerPort : ThreadWorkerGlobalScope = worker.workerPort;

// 无法传输的句柄，所有操作依赖此句柄
var handler = new Handle()

// Worker线程的onmessage逻辑
workerPort.onmessage = function(e : MessageEvents) {
  switch (e.data.type) {
    case 0:
      handler.syncSet(e.data.data);
      workerPort.postMessage('success set');
    case 1:
      handler.syncGet();
      workerPort.postMessage('success get');
  }
}
```



# 容器类库概述

更新时间: 2024-01-15 11:54

容器类库，用于存储各种数据类型的元素，并具备一系列处理数据元素的方法，作为纯数据结构容器来使用具有一定的优势。

容器类采用了类似静态语言的方式来实现，并通过对存储位置以及属性的限制，让每种类型的数据都能在完成自身功能的基础上去除冗余逻辑，保证了数据的高效访问，提升了应用的性能。

当前提供了线性和非线性两类容器，共14种。每种容器都有自身的特性及使用场景，详情请参见[线性容器](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/linear-container-0000001681209893-V3)和[非线性容器](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/nonlinear-container-0000001632530094-V3)。



# 线性容器

更新时间: 2024-01-15 12:18

线性容器实现能按顺序访问的数据结构，其底层主要通过数组实现，包括ArrayList、Vector、List、LinkedList、Deque、Queue、Stack七种。

线性容器，充分考虑了数据访问的速度，运行时（Runtime）通过一条字节码指令就可以完成增、删、改、查等操作。

## ArrayList

[ArrayList](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-arraylist-0000001427585156-V3)即动态数组，可用来构造全局的数组对象。 当需要频繁读取集合中的元素时，推荐使用ArrayList。

ArrayList依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为10，并支持动态扩容，每次扩容大小为原始容量的1.5倍。

ArrayList进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                                         | 描述                                                                 |
| :------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| 增加元素                                                                                                                                     | 通过add(element: T)函数每次在数组尾部增加一个元素。                  |
| 通过insert(element: T, index: number)在指定位置插入一个元素。                                                                                |                                                                      |
| 访问元素                                                                                                                                     | 通过arr[index]获取指定index对应的value值，通过指令获取保证访问速度。 |
| 通过forEach(callbackFn: (value: T, index?: number, arrlist?: ArrayList`<T>`) => void, thisArg?: Object): void访问整个ArrayList容器的元素。 |                                                                      |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                                             |                                                                      |
| 修改元素                                                                                                                                     | 通过arr[index] = xxx修改指定index位置对应的value值。                 |
| 删除元素                                                                                                                                     | 通过remove(element: T)删除第一个匹配到的元素。                       |
| 通过removeByRange(fromIndex: number, toIndex:number)删除指定范围内的元素。                                                                   |                                                                      |

## Vector



说明

API version 9开始，该接口不再维护，推荐使用[ArrayList](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-arraylist-0000001427585156-V3)。

[Vector](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-vector-0000001477981485-V3)是指连续存储结构，可用来构造全局的数组对象。Vector依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为10，并支持动态扩容，每次扩容大小为原始容量的2倍。

Vector和[ArrayList](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-arraylist-0000001427585156-V3)相似，都是基于数组实现，但Vector提供了更多操作数组的接口。Vector在支持操作符访问的基础上，还增加了get/set接口，提供更为完善的校验及容错机制，满足用户不同场景下的需求。

Vector进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                        | 描述                                                                 |
| :-------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| 增加元素                                                                                                                    | 通过add(element: T)函数每次在数组尾部增加一个元素。                  |
| 通过insert(element: T, index: number)在指定位置插入一个元素。                                                               |                                                                      |
| 访问元素                                                                                                                    | 通过vec[index]获取指定index对应的value值，通过指令获取保证访问速度。 |
| 通过get(index: number)获取指定index位置对应的元素。                                                                         |                                                                      |
| 通过getLastElement()获取最后一个元素。                                                                                      |                                                                      |
| 通过getIndexOf(element:T)获取第一个匹配到元素的位置。                                                                       |                                                                      |
| 通过getLastIndexOf(element:T)获取最后一个匹配到元素的位置。                                                                 |                                                                      |
| 通过forEach(callbackFn: (value: T, index?: number, Vector?: Vector`<T>`) => void, thisArg?: Object)访问整个Vector的元素。 |                                                                      |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                            |                                                                      |
| 修改元素                                                                                                                    | 通过vec[index]=xxx修改指定index位置对应的value值。                   |
| 通过set(index:number,element:T)修改指定index位置的元素值为element。                                                         |                                                                      |
| 通过setLength(newSize:number)设置Vector的长度大小。                                                                         |                                                                      |
| 删除元素                                                                                                                    | 通过removeByIndex(index:number)删除index位置对应的value值。          |
| 通过remove(element:T)删除第一个匹配到的元素。                                                                               |                                                                      |
| 通过removeByRange(fromIndex:number,toIndex:number)删除指定范围内的元素。                                                    |                                                                      |

## List

[List](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-list-0000001428062020-V3)可用来构造一个单向链表对象，即只能通过头结点开始访问到尾节点。List依据泛型定义，在内存中的存储位置可以是不连续的。

List和[LinkedList](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-linkedlist-0000001427902748-V3)相比，LinkedList是双向链表，可以快速地在头尾进行增删，而List是单向链表，无法双向操作。

当需要频繁的插入删除时，推荐使用List高效操作。

可以通过get/set等接口对存储的元素进行修改，List进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                          | 描述                                                                  |
| :---------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| 增加元素                                                                                                                      | 通过add(element: T)函数每次在数组尾部增加一个元素。                   |
| 通过insert(element: T, index: number)在指定位置插入一个元素。                                                                 |                                                                       |
| 访问元素                                                                                                                      | 通过list[index]获取指定index对应的value值，通过指令获取保证访问速度。 |
| 通过get(index: number)获取指定index位置对应的元素。                                                                           |                                                                       |
| 通过getFirst()获取第一个元素。                                                                                                |                                                                       |
| 通过getLast()获取最后一个元素。                                                                                               |                                                                       |
| 通过getIndexOf(element: T)获取第一个匹配到元素的位置。                                                                        |                                                                       |
| 通过getLastIndexOf(element: T)获取最后一个匹配到元素的位置。                                                                  |                                                                       |
| 通过forEach(callbackfn: (value:T, index?: number, list?: List`<T>`)=> void,thisArg?: Object)访问整个List的元素。            |                                                                       |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                              |                                                                       |
| 修改元素                                                                                                                      | 通过list[index] = xxx修改指定index位置对应的value值。                 |
| 通过set(index:number, element: T)修改指定index位置的元素值为element。                                                         |                                                                       |
| 通过replaceAllElements(callbackFn:(value: T,index?: number,list?: List`<T>`)=>T,thisArg?: Object)对List内元素进行替换操作。 |                                                                       |
| 删除元素                                                                                                                      | 通过removeByIndex(index:number)删除index位置对应的value值。           |
| 通过remove(element:T)删除第一个匹配到的元素。                                                                                 |                                                                       |

## LinkedList

[LinkedList](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-linkedlist-0000001427902748-V3)可用来构造一个双向链表对象，可以在某一节点向前或者向后遍历List。LinkedList依据泛型定义，在内存中的存储位置可以是不连续的。

LinkedList和[List](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-list-0000001428062020-V3)相比，LinkedList是双向链表，可以快速地在头尾进行增删，而List是单向链表，无法双向操作。

LinkedList和[ArrayList](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-arraylist-0000001427585156-V3)相比，插入数据效率LinkedList优于ArrayList，而查询效率ArrayList优于LinkedList。

当需要频繁的插入删除时，推荐使用LinkedList高效操作。

可以通过get/set等接口对存储的元素进行修改，LinkedList进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                              | 描述                                                                  |
| :-------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------- |
| 增加元素                                                                                                                          | 通过add(element: T)函数每次在数组尾部增加一个元素。                   |
| 通过insert(index: number, element: T)在指定位置插入一个元素。                                                                     |                                                                       |
| 访问元素                                                                                                                          | 通过list[index]获取指定index对应的value值，通过指令获取保证访问速度。 |
| 通过get(index: number)获取指定index位置对应的元素。                                                                               |                                                                       |
| 通过getFirst()获取第一个元素。                                                                                                    |                                                                       |
| 通过getLast()获取最后一个元素。                                                                                                   |                                                                       |
| 通过getIndexOf(element: T)获取第一个匹配到元素的位置。                                                                            |                                                                       |
| 通过getLastIndexOf(element: T)获取最后一个匹配到元素的位置。                                                                      |                                                                       |
| 通过forEach(callbackFn: (value: T, index?: number, list?: LinkedList`<T>`) => void, thisArg?: Object)访问整个LinkedList的元素。 |                                                                       |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                                  |                                                                       |
| 修改元素                                                                                                                          | 通过list[index]=xxx修改指定index位置对应的value值。                   |
| 通过set(index: number,element: T)修改指定index位置的元素值为element。                                                             |                                                                       |
| 删除元素                                                                                                                          | 通过removeByIndex(index: number)删除index位置对应的value值。          |
| 通过remove(element: T)删除第一个匹配到的元素。                                                                                    |                                                                       |

## Deque

[Deque](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-deque-0000001427745116-V3)可用来构造双端队列对象，存储元素遵循先进先出以及先进后出的规则，双端队列可以分别从队头或者队尾进行访问。

Deque依据泛型定义，要求存储位置是一片连续的内存空间，其初始容量大小为8，并支持动态扩容，每次扩容大小为原始容量的2倍。Deque底层采用循环队列实现，入队及出队操作效率都比较高。

Deque和[Queue](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-queue-0000001427745120-V3)相比，Queue的特点是先进先出，只能在头部删除元素，尾部增加元素。

Deque和[Vector](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-vector-0000001477981485-V3)相比，它们都支持在两端增删元素，但Deque不能进行中间插入的操作。对头部元素的插入删除效率高于Vector，而Vector访问元素的效率高于Deque。

需要频繁在集合两端进行增删元素的操作时，推荐使用Deque。

Deque进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                    | 描述                                                                                                                  |
| :---------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| 增加元素                                                                                                                | 通过insertFront(element: T)函数每次在队头增加一个元素。                                                               |
| 增加元素                                                                                                                | 通过insertEnd(element: T)函数每次在队尾增加一个元素。                                                                 |
| 访问元素                                                                                                                | 通过getFirst()获取队首元素的value值，但是不进行出队操作。                                                             |
| 通过getLast()获取队尾元素的value值，但是不进行出队操作。                                                                |                                                                                                                       |
| 通过popFirst()获取队首元素的value值，并进行出队操作。                                                                   |                                                                                                                       |
| 通过popLast()获取队尾元素的value值，并进行出队操作。                                                                    |                                                                                                                       |
| 通过forEach(callbackFn:(value: T, index?: number, deque?: Deque`<T>`) => void, thisArg?: Object)访问整个Deque的元素。 |                                                                                                                       |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                        |                                                                                                                       |
| 修改元素                                                                                                                | 通过forEach(callbackFn:(value: T, index?: number, deque?: Deque`<T>`)=> void, thisArg?: Object)对队列进行修改操作。 |
| 删除元素                                                                                                                | 通过popFirst()对队首元素进行出队操作并删除。                                                                          |
| 通过popLast()对队尾元素进行出队操作并删除。                                                                             |                                                                                                                       |

## Queue

[Queue](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-queue-0000001427745120-V3)可用来构造队列对象，存储元素遵循先进先出的规则。

Queue依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为8，并支持动态扩容，每次扩容大小为原始容量的2倍。

Queue底层采用循环队列实现，入队及出队操作效率都比较高。

Queue和[Deque](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-deque-0000001427745116-V3)相比，Queue只能在一端删除一端增加，Deque可以两端增删。

一般符合先进先出的场景可以使用Queue。

Queue进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                    | 描述                                                                                                                  |
| :---------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| 增加元素                                                                                                                | 通过add(element: T)函数每次在队尾增加一个元素。                                                                       |
| 访问元素                                                                                                                | 通过getFirst()获取队首元素的value值，但是不进行出队操作。                                                             |
| 通过pop()获取队首元素的value值，并进行出队操作。                                                                        |                                                                                                                       |
| 通过forEach(callbackFn: (value: T, index?: number, queue?: Queue`<T>`) => void,thisArg?: Object)访问整个Queue的元素。 |                                                                                                                       |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                        |                                                                                                                       |
| 修改元素                                                                                                                | 通过forEach(callbackFn:(value: T, index?: number, queue?: Queue`<T>`) => void,thisArg?: Object)对队列进行修改操作。 |
| 删除元素                                                                                                                | 通过pop()对队首进行出队操作并删除。                                                                                   |

## Stack

[Stack](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-stack-0000001478181701-V3)可用来构造栈对象，存储元素遵循先进后出的规则。

Stack依据泛型定义，要求存储位置是一片连续的内存空间，初始容量大小为8，并支持动态扩容，每次扩容大小为原始容量的1.5倍。Stack底层基于数组实现，入栈出栈均从数组的一端操作。

Stack和[Queue](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-queue-0000001427745120-V3)相比，Queue基于循环队列实现，只能在一端删除，另一端插入，而Stack都在一端操作。

一般符合先进后出的场景可以使用Stack。

Stack进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                     | 描述                                                                                                                       |
| :----------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| 增加元素                                                                                                                 | 通过push(item: T)函数每次在栈顶增加一个元素。                                                                              |
| 访问元素                                                                                                                 | 通过peek()获取栈顶元素的value值，但是不进行出栈操作。                                                                      |
| 通过pop()获取栈顶的value值，并进行出栈操作。                                                                             |                                                                                                                            |
| 通过forEach(callbackFn: (value: T, index?: number, stack?: Stack`<T>`) => void, thisArg?: Object)访问整个Stack的元素。 |                                                                                                                            |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                         |                                                                                                                            |
| 通过locate(element: T)获取元素对应的位置。                                                                               |                                                                                                                            |
| 修改元素                                                                                                                 | 通过forEach(callbackFn:(value: T, index?: number, stack?: Stack`<T>`) => void, thisArg?: Object)对栈内元素进行修改操作。 |
| 删除元素                                                                                                                 | 通过pop()对栈顶进行出栈操作并删除。                                                                                        |

## 线性容器的使用

此处列举常用的线性容器ArrayList、Vector、Deque、Stack、List的使用示例，包括导入模块、增加元素、访问元素及修改等操作。示例代码如下所示：

```
// ArrayList
import ArrayList from '@ohos.util.ArrayList'; // 导入ArrayList模块

let arrayList = new ArrayList();
arrayList.add('a');
arrayList.add(1); // 增加元素
console.info(`result: ${arrayList[0]}`); // 访问元素
arrayList[0] = 'one'; // 修改元素
console.info(`result: ${arrayList[0]}`);

// Vector
import Vector from '@ohos.util.Vector'; // 导入Vector模块

let vector = new Vector();
vector.add('a');
let b1 = [1, 2, 3];
vector.add(b1);
vector.add(false); // 增加元素
console.info(`result: ${vector[0]}`); // 访问元素
console.info(`result: ${vector.getFirstElement()}`); // 访问元素

// Deque
import Deque from '@ohos.util.Deque'; // 导入Deque模块

let deque = new Deque;
deque.insertFront('a');
deque.insertFront(1); // 增加元素
console.info(`result: ${deque[0]}`); // 访问元素
deque[0] = 'one'; // 修改元素
console.info(`result: ${deque[0]}`);

// Stack
import Stack from '@ohos.util.Stack'; // 导入Stack模块 

let stack = new Stack();
stack.push('a');
stack.push(1); // 增加元素
console.info(`result: ${stack[0]}`); // 访问元素
stack.pop(); // 删除栈顶元素并返回该删除元素
console.info(`result: ${stack.length}`);

// List
import List from '@ohos.util.List'; // 导入List模块

let list = new List;
list.add('a');
list.add(1);
let b2 = [1, 2, 3];
list.add(b2); // 增加元素
console.info(`result: ${list[0]}`); // 访问元素
console.info(`result: ${list.get(0)}`); // 访问元素
```



# 非线性容器

更新时间: 2024-01-15 11:54

非线性容器实现能快速查找的数据结构，其底层通过hash或者红黑树实现，包括HashMap、HashSet、TreeMap、TreeSet、LightWeightMap、LightWeightSet、PlainArray七种。非线性容器中的key及value的类型均满足ECMA标准。

## HashMap

[HashMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashmap-0000001478181697-V3)可用来存储具有关联关系的key-value键值对集合，存储元素中key是唯一的，每个key会对应一个value值。

HashMap依据泛型定义，集合中通过key的hash值确定其存储位置，从而快速找到键值对。HashMap的初始容量大小为16，并支持动态扩容，每次扩容大小为原始容量的2倍。HashMap底层基于HashTable实现，冲突策略采用链地址法。

HashMap和[TreeMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-treemap-0000001478341441-V3)相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存取，效率较低。

[HashSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashset-0000001478341437-V3)基于HashMap实现。HashMap的输入参数由key、value两个值组成。在HashSet中，只对value对象进行处理。

需要快速存取、删除以及插入键值对数据时，推荐使用HashMap。

HashMap进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                  | 描述                                                                 |
| :-------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| 增加元素                                                                                                              | 通过set(key: K, value: V)函数每次在HashMap增加一个键值对。           |
| 访问元素                                                                                                              | 通过get(key: K)获取key对应的value值。                                |
| 通过keys()返回一个迭代器对象，包含map中的所有key值。                                                                  |                                                                      |
| 通过values()返回一个迭代器对象，包含map中的所有value值。                                                              |                                                                      |
| 通过entries()返回一个迭代器对象，包含map中的所有键值对。                                                              |                                                                      |
| forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object)访问整个map的元素。           |                                                                      |
| 通过[Symbol.iterator]():IterableIterator<[K,V]>迭代器进行数据访问。                                                      |                                                                      |
| 修改元素                                                                                                              | 通过replace(key: K, newValue: V)对指定key对应的value值进行修改操作。 |
| 通过forEach(callbackFn: (value?: V, key?: K, map?: HashMap<K, V>) => void, thisArg?: Object)对map中元素进行修改操作。 |                                                                      |
| 删除元素                                                                                                              | 通过remove(key: K)对map中匹配到的键值对进行删除操作。                |
| 通过clear()清空整个map集合。                                                                                          |                                                                      |

## HashSet

[HashSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashset-0000001478341437-V3)可用来存储一系列值的集合，存储元素中value是唯一的。

HashSet依据泛型定义，集合中通过value的hash值确定其存储位置，从而快速找到该值。HashSet初始容量大小为16，支持动态扩容，每次扩容大小为原始容量的2倍。value的类型满足ECMA标准中要求的类型。HashSet底层数据结构基于HashTable实现，冲突策略采用链地址法。

HashSet基于[HashMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashmap-0000001478181697-V3)实现。在HashSet中，只对value对象进行处理。

HashSet和[TreeSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-treeset-0000001478061981-V3)相比，HashSet中的数据无序存放，即存放元素的顺序和取出的顺序不一致，而TreeSet是有序存放。它们集合中的元素都不允许重复，但HashSet允许放入null值，TreeSet不建议插入空值，可能会影响排序结果。

可以利用HashSet不重复的特性，当需要不重复的集合或需要去重某个集合的时候使用。

HashSet进行增、删、改、查操作的常用API如下：

| 操作                                                                                                             | 描述                                                                                                                    |
| :--------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| 增加元素                                                                                                         | 通过add(value: T)函数每次在HashSet增加一个值。                                                                          |
| 访问元素                                                                                                         | 通过values()返回一个迭代器对象，包含set中的所有value值。                                                                |
| 通过entries()返回一个迭代器对象，包含类似键值对的数组，键值都是value。                                           |                                                                                                                         |
| 通过forEach(callbackFn: (value?: T, key?: T, set?: HashSet`<T>`) => void, thisArg?: Object)访问整个set的元素。 |                                                                                                                         |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                 |                                                                                                                         |
| 修改元素                                                                                                         | 通过forEach(callbackFn: (value?: T, key?: T, set?: HashSet`<T>`) => void, thisArg?: Object)对set中value进行修改操作。 |
| 删除元素                                                                                                         | 通过remove(value: T)对set中匹配到的值进行删除操作。                                                                     |
| 通过clear()清空整个set集合。                                                                                     |                                                                                                                         |

## TreeMap

[TreeMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-treemap-0000001478341441-V3)可用来存储具有关联关系的key-value键值对集合，存储元素中key是唯一的，每个key会对应一个value值。

TreeMap依据泛型定义，集合中的key值是有序的，TreeMap的底层是一棵二叉树，可以通过树的二叉查找快速的找到键值对。key的类型满足ECMA标准中要求的类型。TreeMap中的键值是有序存储的。TreeMap底层基于红黑树实现，可以进行快速的插入和删除。

TreeMap和[HashMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashmap-0000001478181697-V3)相比，HashMap依据键的hashCode存取数据，访问速度较快。而TreeMap是有序存取，效率较低。

一般需要存储有序键值对的场景，可以使用TreeMap。

TreeMap进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                  | 描述                                                                |
| :-------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------ |
| 增加元素                                                                                                              | 通过set(key: K,value: V)函数每次在TreeMap增加一个键值对。           |
| 访问元素                                                                                                              | 通过get(key: K)获取key对应的value值。                               |
| 通过getFirstKey()获取map中排在首位的key值。                                                                           |                                                                     |
| 通过getLastKey()获取map中排在未位的key值。                                                                            |                                                                     |
| 通过keys()返回一个迭代器对象，包含map中的所有key值。                                                                  |                                                                     |
| 通过values()返回一个迭代器对象，包含map中的所有value值。                                                              |                                                                     |
| 通过entries()返回一个迭代器对象，包含map中的所有键值对。                                                              |                                                                     |
| 通过forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object)访问整个map的元素。       |                                                                     |
| 通过[Symbol.iterator]():IterableIterator<[K,V]>迭代器进行数据访问。                                                      |                                                                     |
| 修改元素                                                                                                              | 通过replace(key: K,newValue: V)对指定key对应的value值进行修改操作。 |
| 通过forEach(callbackFn: (value?: V, key?: K, map?: TreeMap<K, V>) => void, thisArg?: Object)对map中元素进行修改操作。 |                                                                     |
| 删除元素                                                                                                              | 通过remove(key: K)对map中匹配到的键值对进行删除操作。               |
| 通过clear()清空整个map集合。                                                                                          |                                                                     |

## TreeSet

[TreeSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-treeset-0000001478061981-V3)可用来存储一系列值的集合，存储元素中value是唯一的。

TreeSet依据泛型定义，集合中的value值是有序的，TreeSet的底层是一棵二叉树，可以通过树的二叉查找快速的找到该value值，value的类型满足ECMA标准中要求的类型。TreeSet中的值是有序存储的。TreeSet底层基于红黑树实现，可以进行快速的插入和删除。

TreeSet基于[TreeMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-treemap-0000001478341441-V3)实现，在TreeSet中，只对value对象进行处理。TreeSet可用于存储一系列值的集合，元素中value唯一且有序。

TreeSet和[HashSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashset-0000001478341437-V3)相比，HashSet中的数据无序存放，而TreeSet是有序存放。它们集合中的元素都不允许重复，但HashSet允许放入null值，TreeSet不建议插入空值，可能会影响排序结果。

一般需要存储有序集合的场景，可以使用TreeSet。

TreeSet进行增、删、改、查操作的常用API如下：

| 操作                                                                                                             | 描述                                                                                                                    |
| :--------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------- |
| 增加元素                                                                                                         | 通过add(value: T)函数每次在TreeSet增加一个值。                                                                          |
| 访问元素                                                                                                         | 通过values()返回一个迭代器对象，包含set中的所有value值。                                                                |
| 通过entries()返回一个迭代器对象，包含类似键值对的数组，键值都是value。                                           |                                                                                                                         |
| 通过getFirstValue()获取set中排在首位的value值。                                                                  |                                                                                                                         |
| 通过getLastValue()获取set中排在未位的value值。                                                                   |                                                                                                                         |
| 通过forEach(callbackFn: (value?: T, key?: T, set?: TreeSet`<T>`) => void, thisArg?: Object)访问整个set的元素。 |                                                                                                                         |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                 |                                                                                                                         |
| 修改元素                                                                                                         | 通过forEach(callbackFn: (value?: T, key?: T, set?: TreeSet`<T>`) => void, thisArg?: Object)对set中value进行修改操作。 |
| 删除元素                                                                                                         | 通过remove(value: T)对set中匹配到的值进行删除操作。                                                                     |
| 通过clear()清空整个set集合。                                                                                     |                                                                                                                         |

## LightWeightMap

[LightWeightMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-lightweightmap-0000001478061977-V3)可用来存储具有关联关系的key-value键值对集合，存储元素中key是唯一的，每个key会对应一个value值。LightWeightMap依据泛型定义，采用更加轻量级的结构，底层标识唯一key通过hash实现，其冲突策略为线性探测法。集合中的key值的查找依赖于hash值以及二分查找算法，通过一个数组存储hash值，然后映射到其他数组中的key值以及value值，key的类型满足ECMA标准中要求的类型。

初始默认容量大小为8，每次扩容大小为原始容量的2倍。

LightWeightMap和[HashMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashmap-0000001478181697-V3)都是用来存储键值对的集合，LightWeightMap占用内存更小。

当需要存取key-value键值对时，推荐使用占用内存更小的LightWeightMap。

LightWeightMap进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                         | 描述                                                                             |
| :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| 增加元素                                                                                                                     | 通过set(key: K,value: V)函数每次在LightWeightMap增加一个键值对。                 |
| 访问元素                                                                                                                     | 通过get(key: K)获取key对应的value值。                                            |
| 通过getIndexOfKey(key: K)获取map中指定key的index。                                                                           |                                                                                  |
| 通过getIndexOfValue(value: V)获取map中指定value出现的第一个的index。                                                         |                                                                                  |
| 通过keys()返回一个迭代器对象，包含map中的所有key值。                                                                         |                                                                                  |
| 通过values()返回一个迭代器对象，包含map中的所有value值。                                                                     |                                                                                  |
| 通过entries()返回一个迭代器对象，包含map中的所有键值对。                                                                     |                                                                                  |
| 通过getKeyAt(index: number)获取指定index对应的key值。                                                                        |                                                                                  |
| 通过getValueAt(index: number)获取指定index对应的value值。                                                                    |                                                                                  |
| 通过forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object)访问整个map的元素。       |                                                                                  |
| 通过[Symbol.iterator]():IterableIterator<[K,V]>迭代器进行数据访问。                                                             |                                                                                  |
| 修改元素                                                                                                                     | 通过setValueAt(index: number, newValue: V)对指定index对应的value值进行修改操作。 |
| 通过forEach(callbackFn: (value?: V, key?: K, map?: LightWeightMap<K, V>) => void, thisArg?: Object)对map中元素进行修改操作。 |                                                                                  |
| 删除元素                                                                                                                     | 通过remove(key: K)对map中匹配到的键值对进行删除操作。                            |
| 通过removeAt(index: number)对map中指定index的位置进行删除操作。                                                              |                                                                                  |
| 通过clear()清空整个map集合。                                                                                                 |                                                                                  |

## LightWeightSet

[LightWeightSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-lightweightset-0000001477981481-V3)可用来存储一系列值的集合，存储元素中value是唯一的。

LightWeightSet依据泛型定义，采用更加轻量级的结构，初始默认容量大小为8，每次扩容大小为原始容量的2倍。集合中的value值的查找依赖于hash以及二分查找算法，通过一个数组存储hash值，然后映射到其他数组中的value值，value的类型满足ECMA标准中要求的类型。

LightWeightSet底层标识唯一value基于hash实现，其冲突策略为线性探测法，查找策略基于二分查找法。

LightWeightSet和[HashSet](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-hashset-0000001478341437-V3)都是用来存储键值的集合，LightWeightSet的占用内存更小。

当需要存取某个集合或是对某个集合去重时，推荐使用占用内存更小的LightWeightSet。

LightWeightSet进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                    | 描述                                                                                                                          |
| :---------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------- |
| 增加元素                                                                                                                | 通过add(obj: T)函数每次在LightWeightSet增加一个值。                                                                           |
| 访问元素                                                                                                                | 通过getIndexOf(key: T)获取对应的index值。                                                                                     |
| 通过values()返回一个迭代器对象，包含map中的所有value值。                                                                |                                                                                                                               |
| 通过entries()返回一个迭代器对象，包含map中的所有键值对。                                                                |                                                                                                                               |
| 通过getValueAt(index: number)获取指定index对应的value值。                                                               |                                                                                                                               |
| 通过forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet`<T>`) => void, thisArg?: Object)访问整个set的元素。 |                                                                                                                               |
| 通过[Symbol.iterator]():IterableIterator`<T>`迭代器进行数据访问。                                                        |                                                                                                                               |
| 修改元素                                                                                                                | 通过forEach(callbackFn: (value?: T, key?: T, set?: LightWeightSet`<T>`) => void, thisArg?: Object)对set中元素进行修改操作。 |
| 删除元素                                                                                                                | 通过remove(key: K)对set中匹配到的键值对进行删除操作。                                                                         |
| 通过removeAt(index: number)对set中指定index的位置进行删除操作。                                                         |                                                                                                                               |
| 通过clear()清空整个set集合。                                                                                            |                                                                                                                               |

## PlainArray

[PlainArray](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-plainarray-0000001427585160-V3)可用来存储具有关联关系的键值对集合，存储元素中key是唯一的，并且对于PlainArray来说，其key的类型为number类型。每个key会对应一个value值，类型依据泛型的定义，PlainArray采用更加轻量级的结构，集合中的key值的查找依赖于二分查找算法，然后映射到其他数组中的value值。

初始默认容量大小为16，每次扩容大小为原始容量的2倍。

PlainArray和[LightWeightMap](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-lightweightmap-0000001478061977-V3)都是用来存储键值对，且均采用轻量级结构，但PlainArray的key值类型只能为number类型。

当需要存储key值为number类型的键值对时，可以使用PlainArray。

PlainArray进行增、删、改、查操作的常用API如下：

| 操作                                                                                                                                          | 描述                                                                         |
| :-------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 增加元素                                                                                                                                      | 通过add(key: number,value: T)函数每次在PlainArray增加一个键值对。            |
| 访问元素                                                                                                                                      | 通过get(key: number)获取key对应的value值。                                   |
| 通过getIndexOfKey(key: number)获取PlainArray中指定key的index。                                                                                |                                                                              |
| 通过getIndexOfValue(value: T)获取PlainArray中指定value的index。                                                                               |                                                                              |
| 通过getKeyAt(index: number)获取指定index对应的key值。                                                                                         |                                                                              |
| 通过getValueAt(index: number)获取指定index对应的value值。                                                                                     |                                                                              |
| 通过forEach(callbackFn: (value: T, index?: number, PlainArray?: PlainArray`<T>`) => void, thisArg?: Object)访问整个plainarray的元素。       |                                                                              |
| 通过[Symbol.iterator]():IterableIterator<[number, T]>迭代器进行数据访问。                                                                        |                                                                              |
| 修改元素                                                                                                                                      | 通过setValueAt(index:number, value: T)对指定index对应的value值进行修改操作。 |
| 通过forEach(callbackFn: (value: T, index?: number, PlainArray?: PlainArray`<T>`) => void, thisArg?: Object)对plainarray中元素进行修改操作。 |                                                                              |
| 删除元素                                                                                                                                      | 通过remove(key: number)对plainarray中匹配到的键值对进行删除操作。            |
| 通过removeAt(index: number)对plainarray中指定index的位置进行删除操作。                                                                        |                                                                              |
| 通过removeRangeFrom(index: number, size: number)对plainarray中指定范围内的元素进行删除操作。                                                  |                                                                              |
| 通过clear()清空整个PlainArray集合。                                                                                                           |                                                                              |

## 非线性容器的使用

此处列举常用的非线性容器HashMap、TreeMap、LightWeightMap、PlainArray的使用示例，包括导入模块、增加元素、访问元素及修改等操作，示例代码如下所示：

```
// HashMap
import HashMap from '@ohos.util.HashMap'; // 导入HashMap模块

let hashMap = new HashMap();
hashMap.set('a', 123);
hashMap.set(4, 123); // 增加元素
console.info(`result: ${hashMap.hasKey(4)}`); // 判断是否含有某元素
console.info(`result: ${hashMap.get('a')}`); // 访问元素

// TreeMap
import TreeMap from '@ohos.util.TreeMap'; // 导入TreeMap模块

let treeMap = new TreeMap();
treeMap.set('a', 123);
treeMap.set('6', 356); // 增加元素
console.info(`result: ${treeMap.get('a')}`); // 访问元素
console.info(`result: ${treeMap.getFirstKey()}`); // 访问首元素
console.info(`result: ${treeMap.getLastKey()}`); // 访问尾元素

// LightWeightMap
import LightWeightMap from '@ohos.util.LightWeightMap'; // 导入LightWeightMap模块

let lightWeightMap = new LightWeightMap();
lightWeightMap.set('x', 123);
lightWeightMap.set('8', 356); // 增加元素
console.info(`result: ${lightWeightMap.get('a')}`); // 访问元素
console.info(`result: ${lightWeightMap.get('x')}`); // 访问元素
console.info(`result: ${lightWeightMap.getIndexOfKey('8')}`); // 访问元素

// PlainArray
import PlainArray from '@ohos.util.PlainArray' // 导入PlainArray模块

let plainArray = new PlainArray();
plainArray.add(1, 'sdd');
plainArray.add(2, 'sff'); // 增加元素
console.info(`result: ${plainArray.get(1)}`); // 访问元素
console.info(`result: ${plainArray.getKeyAt(1)}`); // 访问元素
```



# XML概述

更新时间: 2024-01-15 11:54

XML（可扩展标记语言）是一种用于描述数据的标记语言，旨在提供一种通用的方式来传输和存储数据，特别是Web应用程序中经常使用的数据。XML并不预定义标记。因此，XML更加灵活，并且可以适用于广泛的应用领域。

XML文档由元素（element）、属性（attribute）和内容（content）组成。

* 元素指的是标记对，包含文本、属性或其他元素。
* 属性提供了有关元素的其他信息。
* 内容则是元素包含的数据或子元素。

XML还可以通过使用XML Schema或DTD（文档类型定义）来定义文档结构。这些机制允许开发人员创建自定义规则以验证XML文档是否符合其预期的格式。

XML还支持命名空间、实体引用、注释、处理指令等特性，使其能够灵活地适应各种数据需求。

语言基础类库提供了XML相关的基础能力，包括：[XML的生成](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-generation-0000001681489601-V3)、[XML的解析](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-parsing-0000001632370258-V3)和[XML的转换](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-conversion-0000001632690010-V3)。



# XML生成

更新时间: 2024-01-15 11:54

XML可以作为数据交换格式，被各种系统和应用程序所支持。例如Web服务，可以将结构化数据以XML格式进行传递。

XML还可以作为消息传递格式，在分布式系统中用于不同节点之间的通信与交互。

## 注意事项

* XML标签必须成对出现，生成开始标签就要生成结束标签。

* XML标签对大小写敏感，开始标签与结束标签大小写要一致。

## 开发步骤

XML模块提供XmlSerializer类来生成XML文件，输入为固定长度的Arraybuffer或DataView对象，该对象用于存放输出的XML数据。

通过调用不同的方法来写入不同的内容，如startElement(name: string)写入元素开始标记，setText(text: string)写入标签值。

XML模块的API接口可以参考[@ohos.xml](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-xml-0000001428062024-V3)的详细描述，按需求调用对应函数可以生成一份完整的XML文件。

1. 引入模块。

```
import xml from '@ohos.xml'; 
import util from '@ohos.util';
```
2. 创建缓冲区，构造XmlSerializer对象（可以基于Arraybuffer构造XmlSerializer对象， 也可以基于DataView构造XmlSerializer对象）。

```
// 1.基于Arraybuffer构造XmlSerializer对象
let arrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
let thatSer = new xml.XmlSerializer(arrayBuffer); // 基于Arraybuffer构造XmlSerializer对象

// 2.基于DataView构造XmlSerializer对象
let arrayBuffer = new ArrayBuffer(2048); // 创建一个2048字节的缓冲区
let dataView = new DataView(arrayBuffer); // 使用DataView对象操作ArrayBuffer对象
let thatSer = new xml.XmlSerializer(dataView); // 基于DataView构造XmlSerializer对象
```
3. 调用XML元素生成函数。

```
thatSer.setDeclaration(); // 写入xml的声明
thatSer.startElement('bookstore'); // 写入元素开始标记
thatSer.startElement('book'); // 嵌套元素开始标记
thatSer.setAttributes('category', 'COOKING'); // 写入属性及属性值
thatSer.startElement('title');
thatSer.setAttributes('lang', 'en');
thatSer.setText('Everyday'); // 写入标签值
thatSer.endElement(); // 写入结束标记
thatSer.startElement('author');
thatSer.setText('Giada');
thatSer.endElement();
thatSer.startElement('year');
thatSer.setText('2005');
thatSer.endElement();
thatSer.endElement();
thatSer.endElement();
```
4. 使用Uint8Array操作Arraybuffer，调用TextDecoder对Uint8Array解码后输出。

```
let view = new Uint8Array(arrayBuffer); // 使用Uint8Array读取arrayBuffer的数据
let textDecoder = util.TextDecoder.create(); // 调用util模块的TextDecoder类
let res = textDecoder.decodeWithStream(view); // 对view解码
console.info(res);
```

  输出结果如下：

```
<?xml version=\"1.0\" encoding=\"utf-8\"?><bookstore>\r\n  <book category=\"COOKING\">\r\n    <title lang=\"en\">Everyday</title>\r\n    <author>Giada</author>\r\n    <year>2005</year>\r\n  </book>\r\n</bookstore>
```



# XML解析

更新时间: 2024-01-15 11:54

对于以XML作为载体传递的数据，实际使用中需要对相关的节点进行解析，一般包括[解析XML标签和标签值](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-parsing-0000001632370258-V3#ZH-CN_TOPIC_0000001632370258__%E8%A7%A3%E6%9E%90xml%E6%A0%87%E7%AD%BE%E5%92%8C%E6%A0%87%E7%AD%BE%E5%80%BC)、[解析XML属性和属性值](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-parsing-0000001632370258-V3#ZH-CN_TOPIC_0000001632370258__%E8%A7%A3%E6%9E%90xml%E5%B1%9E%E6%80%A7%E5%92%8C%E5%B1%9E%E6%80%A7%E5%80%BC)、[解析XML事件类型和元素深度](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/xml-parsing-0000001632370258-V3#ZH-CN_TOPIC_0000001632370258__%E8%A7%A3%E6%9E%90xml%E4%BA%8B%E4%BB%B6%E7%B1%BB%E5%9E%8B%E5%92%8C%E5%85%83%E7%B4%A0%E6%B7%B1%E5%BA%A6)三类场景。

XML模块提供XmlPullParser类对XML文件解析，输入为含有XML文本的ArrayBuffer或DataView，输出为解析得到的信息。

表1 XML解析选项

| 名称                           | 类型                                                | 必填 | 说明                                                                                                 |
| :----------------------------- | :-------------------------------------------------- | :--- | :--------------------------------------------------------------------------------------------------- |
| supportDoctype                 | boolean                                             | 否   | 是否忽略文档类型。默认为false，表示对文档类型进行解析。                                              |
| ignoreNameSpace                | boolean                                             | 否   | 是否忽略命名空间。默认为false，表示对命名空间进行解析。                                              |
| tagValueCallbackFunction       | (name: string, value: string) => boolean            | 否   | 获取tagValue回调函数，打印标签及标签值。默认为null，表示不进行XML标签和标签值的解析。                |
| attributeValueCallbackFunction | (name: string, value: string) => boolean            | 否   | 获取attributeValue回调函数， 打印属性及属性值。默认为null，表示不进行XML属性和属性值的解析。         |
| tokenValueCallbackFunction     | (eventType: EventType, value: ParseInfo) => boolean | 否   | 获取tokenValue回调函数，打印标签事件类型及parseInfo对应属性。默认为null，表示不进行XML事件类型解析。 |

## 注意事项

* XML解析及转换需要确保传入的XML数据符合标准格式。

* XML解析目前不支持按指定节点解析对应的节点值。

## 解析XML标签和标签值

1. 引入模块。

```
import xml from '@ohos.xml';
import util from '@ohos.util'; // 需要使用util模块函数对文件编码
```
2. 对XML文件编码后调用XmlPullParser。
  可以基于ArrayBuffer构造XmlPullParser对象， 也可以基于DataView构造XmlPullParser对象。

```
let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '<title>Play</title>' +
    '<lens>Work</lens>' +
    '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml); // 对数据编码，防止包含中文字符乱码
// 1.基于ArrayBuffer构造XmlPullParser对象
let that = new xml.XmlPullParser(arrBuffer.buffer, 'UTF-8');

// 2.基于DataView构造XmlPullParser对象
let dataView = new DataView(arrBuffer.buffer);
let that = new xml.XmlPullParser(dataView, 'UTF-8');
```
3. 自定义回调函数，本例直接打印出标签及标签值。

```
let str = '';
function func(name, value){
  str = name + value;
  console.info(str);
  return true; //true:继续解析 false:停止解析
}
```
4. 设置解析选项，调用parse函数。

```
let options = {supportDoctype:true, ignoreNameSpace:true, tagValueCallbackFunction:func};
that.parse(options);
```

  输出结果如下所示：

```
note
title
Play
title
lens
Work
lens
note
```

## 解析XML属性和属性值

1. 引入模块。

```
import xml from '@ohos.xml';
import util from '@ohos.util'; // 需要使用util模块函数对文件编码
```
2. 对XML文件编码后调用XmlPullParser。

```
let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title>Play</title>' +
    '    <title>Happy</title>' +
    '    <lens>Work</lens>' +
    '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml); // 对数据编码，防止包含中文字符乱码
let that = new xml.XmlPullParser(arrBuffer.buffer, 'UTF-8');
```
3. 自定义回调函数，本例直接打印出属性及属性值。

```
let str = '';
function func(name, value){
  str += name + ' ' + value + ' ';
  return true; // true:继续解析 false:停止解析
}
```
4. 设置解析选项，调用parse函数。

```
let options = {supportDoctype:true, ignoreNameSpace:true, attributeValueCallbackFunction:func};
that.parse(options);
console.info(str); // 一次打印出所有的属性及其值
```

  输出结果如下所示：

```
importance high logged true // note节点的属性及属性值
```

## 解析XML事件类型和元素深度

1. 引入模块。

```
import xml from '@ohos.xml';
import util from '@ohos.util'; // 需要使用util模块函数对文件编码
```
2. 对XML文件编码后调用XmlPullParser。

```
let strXml =
  '<?xml version="1.0" encoding="utf-8"?>' +
  '<note importance="high" logged="true">' +
  '<title>Play</title>' +
  '</note>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml); // 对数据编码，防止包含中文字符乱码
let that = new xml.XmlPullParser(arrBuffer.buffer, 'UTF-8');
```
3. 自定义回调函数，本例直接打印元素事件类型及元素深度。

```
let str = '';
function func(name, value){
  str = name + ' ' + value.getDepth(); // getDepth 获取元素的当前深度
  console.info(str)
  return true; //true:继续解析 false:停止解析
}
```
4. 设置解析选项，调用parse函数。

```
let options = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func};
that.parse(options);
```

  输出结果如下所示：

```
0 0 // 0：<?xml version="1.0" encoding="utf-8"?> 对应事件类型START_DOCUMENT值为0  0：起始深度为0
2 1 // 2：<note importance="high" logged="true"> 对应事件类型START_TAG值为2       1：深度为1
2 2 // 2：<title>对应事件类型START_TAG值为2                                       2：深度为2
4 2 // 4：Play对应事件类型TEXT值为4                                               2：深度为2
3 2 // 3：</title>对应事件类型END_TAG值为3                                        2：深度为2
3 1 // 3：</note>对应事件类型END_TAG值为3                                         1：深度为1（与<note对应>）
1 0 // 1：对应事件类型END_DOCUMENT值为1                                           0：深度为0
```

## 场景示例

此处以调用所有解析选项为例，提供解析XML标签、属性和事件类型的开发示例。

```
import xml from '@ohos.xml';
import util from '@ohos.util';

let strXml =
  '<?xml version="1.0" encoding="UTF-8"?>' +
    '<book category="COOKING">' +
    '<title lang="en">Everyday</title>' +
    '<author>Giada</author>' +
    '</book>';
let textEncoder = new util.TextEncoder();
let arrBuffer = textEncoder.encodeInto(strXml);
let that = new xml.XmlPullParser(arrBuffer.buffer, 'UTF-8');
let str = '';

function tagFunc(name, value) {
  str = name + value;
  console.info('tag-' + str);
  return true;
}

function attFunc(name, value) {
  str = name + ' ' + value;
  console.info('attri-' + str);
  return true;
}

function tokenFunc(name, value) {
  str = name + ' ' + value.getDepth();
  console.info('token-' + str);
  return true;
}

let options = {
  supportDocType: true,
  ignoreNameSpace: true,
  tagValueCallbackFunction: tagFunc,
  attributeValueCallbackFunction: attFunc,
  tokenValueCallbackFunction: tokenFunc
};
that.parse(options);
```

输出结果如下所示：

```
tag-
token-0 0
tag-book
attri-category COOKING
token-2 1
tag-title
attri-lang en
token-2 2
tag-Everyday
token-4 2
tag-title
token-3 2
tag-author
token-2 2
tag-Giada
token-4 2
tag-author
token-3 2
tag-book
token-3 1
tag-
token-1 0
```



# XML转换

更新时间: 2024-01-15 11:54

将XML文本转换为JavaScript对象可以更轻松地处理和操作数据，并且更适合在JavaScript应用程序中使用。

语言基础类库提供ConvertXML类将XML文本转换为JavaScript对象，输入为待转换的XML字符串及转换选项，输出为转换后的JavaScript对象。具体转换选项可见[@ohos.convertxml](https://developer.harmonyos.com/cn/docs/documentation/doc-references-V3/js-apis-convertxml-0000001478341433-V3)。

## 注意事项

XML解析及转换需要确保传入的XML数据符合标准格式。

## 开发步骤

此处以XML转为JavaScript对象后获取其标签值为例，说明转换效果。

1. 引入模块。

```
import convertxml from '@ohos.convertxml';
```
2. 输入待转换的XML，设置转换选项。

```
let xml =
  '<?xml version="1.0" encoding="utf-8"?>' +
    '<note importance="high" logged="true">' +
    '    <title>Happy</title>' +
    '    <todo>Work</todo>' +
    '    <todo>Play</todo>' +
    '</note>';
let options = {
  // trim: false 转换后是否删除文本前后的空格，否
  // declarationKey: "_declaration" 转换后文件声明使用_declaration来标识
  // instructionKey: "_instruction" 转换后指令使用_instruction标识
  // attributesKey: "_attributes" 转换后属性使用_attributes标识
  // textKey: "_text" 转换后标签值使用_text标识
  // cdataKey: "_cdata" 转换后未解析数据使用_cdata标识
  // docTypeKey: "_doctype" 转换后文档类型使用_doctype标识
  // commentKey: "_comment" 转换后注释使用_comment标识
  // parentKey: "_parent" 转换后父类使用_parent标识
  // typeKey: "_type" 转换后元素类型使用_type标识
  // nameKey: "_name" 转换后标签名称使用_name标识
  // elementsKey: "_elements" 转换后元素使用_elements标识
  trim: false,
  declarationKey: "_declaration",
  instructionKey: "_instruction",
  attributesKey: "_attributes",
  textKey: "_text",
  cdataKey: "_cdata",
  docTypeKey: "_doctype",
  commentKey: "_comment",
  parentKey: "_parent",
  typeKey: "_type",
  nameKey: "_name",
  elementsKey: "_elements"
}
```
3. 调用转换函数，打印结果。

```
let conv = new convertxml.ConvertXML();
let result = conv.convertToJSObject(xml, options);
let strRes = JSON.stringify(result); // 将js对象转换为json字符串，用于显式输出
console.info(strRes);
// 也可以直接处理转换后的JS对象，获取标签值
let title = result['_elements'][0]['_elements'][0]['_elements'][0]['_text']; // 解析<title>标签对应的值
let todo = result['_elements'][0]['_elements'][1]['_elements'][0]['_text']; // 解析<todo>标签对应的值
let todo2 = result['_elements'][0]['_elements'][2]['_elements'][0]['_text']; // 解析<todo>标签对应的值
console.info(title); // Happy
console.info(todo); // Work
console.info(todo2); // Play
```

  输出结果如下所示：

```
strRes:
{"_declaration":{"_attributes":{"version":"1.0","encoding":"utf-8"}},"_elements":[{"_type":"element","_name":"note",
 "_attributes":{"importance":"high","logged":"true"},"_elements":[{"_type":"element","_name":"title",
 "_elements":[{"_type":"text","_text":"Happy"}]},{"_type":"element","_name":"todo",
 "_elements":[{"_type":"text","_text":"Work"}]},{"_type":"element","_name":"todo",
 "_elements":[{"_type":"text","_text":"Play"}]}]}]}
title:Happy
todo:Work
todo2:Play
```



