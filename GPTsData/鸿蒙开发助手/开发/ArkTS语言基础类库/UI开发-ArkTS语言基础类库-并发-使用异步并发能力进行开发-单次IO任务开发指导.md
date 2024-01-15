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

