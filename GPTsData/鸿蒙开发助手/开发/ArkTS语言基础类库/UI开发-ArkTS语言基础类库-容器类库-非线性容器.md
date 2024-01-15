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

