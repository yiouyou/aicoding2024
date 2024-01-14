# Environment：设备环境查询

更新时间: 2024-01-10 11:59

开发者如果需要应用程序运行的设备的环境参数，以此来作出不同的场景判断，比如多语言，暗黑模式等，需要用到Environment设备环境查询。

Environment是ArkUI框架在应用程序启动时创建的单例对象。它为AppStorage提供了一系列描述应用程序运行状态的属性。Environment的所有属性都是不可变的（即应用不可写入），所有的属性都是简单类型。

## Environment内置参数

| 键                   | 数据类型        | 描述                                                                             |
| :------------------- | :-------------- | :------------------------------------------------------------------------------- |
| accessibilityEnabled | boolean         | 获取无障碍屏幕读取是否启用。                                                     |
| colorMode            | ColorMode enum  | 色彩模型类型：选项为ColorMode.light: 浅色，ColorMode.Dark: 深色。                |
| fontScale            | number          | 字体大小比例，范围: [0.85, 1.45]。                                               |
| layoutDirection      | LayoutDirection | 字体粗细程度，范围: [0.6, 1.6]。                                                 |
| accessibilityEnabled | boolean         | 布局方向类型：包括LayoutDirection.LTR: 从左到右，LayoutDirection.RTL: 从右到左。 |
| languageCode         | string          | 当前系统语言值，取值必须为小写字母, 例如zh。                                     |

## 使用场景



### 从UI中访问Environment参数

* 使用Environment.EnvProp将设备运行的环境变量存入AppStorage中：

```
// 将设备的语言code存入AppStorage，默认值为en
Environment.EnvProp('languageCode', 'en');
```

* 可以使用@StorageProp链接到Component中。
```
@StorageProp('languageCode') lang : string = 'en';
```

设备环境到Component的更新链：Environment --> AppStorage -->Component。

说明

@StorageProp关联的环境参数可以在本地更改，但不能同步回AppStorage中，因为应用对环境变量参数是不可写的，只能在Environment中查询。

```
// 将设备languageCode存入AppStorage中
Environment.EnvProp('languageCode', 'en');

@Entry
@Component
struct Index {
  @StorageProp('languageCode') languageCode: string = 'en';

  build() {
    Row() {
      Column() {
        // 输出当前设备的languageCode
        Text(this.languageCode)
      }
    }
  }
}
```

### 应用逻辑使用Environment

```
// 使用Environment.EnvProp将设备运行languageCode存入AppStorage中；
Environment.EnvProp('languageCode', 'en');
// 从AppStorage获取单向绑定的languageCode的变量
const lang: SubscribedAbstractProperty<string> = AppStorage.Prop('languageCode');

if (lang.get() === 'zh') {
  console.info('你好');
} else {
  console.info('Hello!');
}
```

