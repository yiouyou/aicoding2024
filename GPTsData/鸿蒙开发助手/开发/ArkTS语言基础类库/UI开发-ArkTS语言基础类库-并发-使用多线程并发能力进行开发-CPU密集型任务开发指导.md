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

