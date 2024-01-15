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

