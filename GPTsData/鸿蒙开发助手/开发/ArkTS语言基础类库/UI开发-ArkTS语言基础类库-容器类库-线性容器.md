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

