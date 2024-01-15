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

