# @Link装饰器：父子双向同步

更新时间: 2024-01-10 11:59

子组件中被@Link装饰的变量与其父组件中对应的数据源建立双向数据绑定。

说明

从API version 9开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Link装饰的变量与其父组件中的数据源共享相同的值。

## 限制条件

@Link装饰器不能在@Entry装饰的自定义组件中使用。

## 装饰器使用规则说明

| @Link变量装饰器    | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 装饰器参数         | 无                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 同步类型           | 双向同步。父组件中@State, @StorageLink和@Link 和子组件@Link可以建立双向数据同步，反之亦然。                                                                                                                                                                                                                                                                                                                                                                                |
| 允许装饰的变量类型 | Object、class、string、number、boolean、enum类型，以及这些类型的数组。嵌套类型的场景请参考[观察变化](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-link-0000001524297305-V3#section7141136115513)。类型必须被指定，且和双向绑定状态变量的类型相同。不支持any，不支持简单类型和复杂类型的联合类型，不允许使用undefined和null。说明不支持Length、ResourceStr、ResourceColor类型，Length、ResourceStr、ResourceColor为简单类型和复杂类型的联合类型。 |
| 被装饰变量的初始值 | 无，禁止本地初始化。                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## 变量的传递/访问规则说明

| 传递/访问            | 说明                                                                                                                                                                                                                                                                                                                                               |
| :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 从父组件初始化和更新 | 必选。与父组件@State, @StorageLink和@Link 建立双向绑定。允许父组件中@State、@Link、@Prop、@Provide、@Consume、@ObjectLink、@StorageLink、@StorageProp、@LocalStorageLink和@LocalStorageProp装饰变量初始化子组件@Link。从API version 9开始，@Link子组件从父组件初始化@State的语法为Comp({ aLink: this.aState })。同样Comp({aLink: $aState})也支持。 |
| 用于初始化子组件     | 允许，可用于初始化常规变量、@State、@Link、@Prop、@Provide。                                                                                                                                                                                                                                                                                       |
| 是否支持组件外访问   | 私有，只能在所属组件内访问。                                                                                                                                                                                                                                                                                                                       |

**图1 **初始化规则图示

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214112403.62635290675035694891354294387167:50001231000000:2800:43017267DF8F6832D0F5E48B477973C14CDDBD66988BA6389B7043BE214B3C6D.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

## 观察变化和行为表现

### 观察变化

* 当装饰的数据类型为boolean、string、number类型时，可以同步观察到数值的变化，示例请参考[简单类型和类对象类型的@Link](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-link-0000001524297305-V3#section614118685518)。

* 当装饰的数据类型为class或者Object时，可以观察到赋值和属性赋值的变化，即Object.keys(observedObject)返回的所有属性，示例请参考[简单类型和类对象类型的@Link](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-link-0000001524297305-V3#section614118685518)。
* 当装饰的对象是array时，可以观察到数组添加、删除、更新数组单元的变化，示例请参考[数组类型的@Link](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-link-0000001524297305-V3#section99561777591)。

### 框架行为

@Link装饰的变量和其所属的自定义组件共享生命周期。

为了了解@Link变量初始化和更新机制，有必要先了解父组件和拥有@Link变量的子组件的关系，初始渲染和双向更新的流程（以父组件为@State为例）。

1. 初始渲染：执行父组件的build()函数后将创建子组件的新实例。初始化过程如下：
  1. 必须指定父组件中的@State变量，用于初始化子组件的@Link变量。子组件的@Link变量值与其父组件的数据源变量保持同步（双向数据同步）。
  2. 父组件的@State状态变量包装类通过构造函数传给子组件，子组件的@Link包装类拿到父组件的@State的状态变量后，将当前@Link包装类this指针注册给父组件的@State变量。
2. @Link的数据源的更新：即父组件中状态变量更新，引起相关子组件的@Link的更新。处理步骤：
  1. 通过初始渲染的步骤可知，子组件@Link包装类把当前this指针注册给父组件。父组件@State变量变更后，会遍历更新所有依赖它的系统组件（elementid）和状态变量（比如@Link包装类）。
  2. 通知@Link包装类更新后，子组件中所有依赖@Link状态变量的系统组件（elementId）都会被通知更新。以此实现父组件对子组件的状态数据同步。
3. @Link的更新：当子组件中@Link更新后，处理步骤如下（以父组件为@State为例）：
  1. @Link更新后，调用父组件的@State包装类的set方法，将更新后的数值同步回父组件。
  2. 子组件@Link和父组件@State分别遍历依赖的系统组件，进行对应的UI的更新。以此实现子组件@Link同步回父组件@State。

## 使用场景

### 简单类型和类对象类型的@Link

以下示例中，点击父组件ShufflingContainer中的“Parent View: Set yellowButton”和“Parent View: Set GreenButton”，可以从父组件将变化同步给子组件。

1.点击子组件GreenButton和YellowButton中的Button，子组件会发生相应变化，将变化同步给父组件。因为@Link是双向同步，会将变化同步给@State。

2.当点击父组件ShufflingContainer中的Button时，@State变化，也会同步给@Link，子组件也会发生对应的刷新。

```
class GreenButtonState {
  width: number = 0;

  constructor(width: number) {
    this.width = width;
  }
}

@Component
struct GreenButton {
  @Link greenButtonState: GreenButtonState;

  build() {
    Button('Green Button')
      .width(this.greenButtonState.width)
      .height(40)
      .backgroundColor('#64bb5c')
      .fontColor('#FFFFFF，90%')
      .onClick(() => {
        if (this.greenButtonState.width < 700) {
          // 更新class的属性，变化可以被观察到同步回父组件
          this.greenButtonState.width += 60;
        } else {
          // 更新class，变化可以被观察到同步回父组件
          this.greenButtonState = new GreenButtonState(180);
        }
      })
  }
}

@Component
struct YellowButton {
  @Link yellowButtonState: number;

  build() {
    Button('Yellow Button')
      .width(this.yellowButtonState)
      .height(40)
      .backgroundColor('#f7ce00')
      .fontColor('#FFFFFF，90%')
      .onClick(() => {
        // 子组件的简单类型可以同步回父组件
        this.yellowButtonState += 40.0;
      })
  }
}

@Entry
@Component
struct ShufflingContainer {
  @State greenButtonState: GreenButtonState = new GreenButtonState(180);
  @State yellowButtonProp: number = 180;

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
        // 简单类型从父组件@State向子组件@Link数据同步
        Button('Parent View: Set yellowButton')
          .width(312)
          .height(40)
          .margin(12)
          .fontColor('#FFFFFF，90%')
          .onClick(() => {
            this.yellowButtonProp = (this.yellowButtonProp < 700) ? this.yellowButtonProp + 40 : 100;
          })
        // class类型从父组件@State向子组件@Link数据同步
        Button('Parent View: Set GreenButton')
          .width(312)
          .height(40)
          .margin(12)
          .fontColor('#FFFFFF，90%')
          .onClick(() => {
            this.greenButtonState.width = (this.greenButtonState.width < 700) ? this.greenButtonState.width + 100 : 100;
          })
        // class类型初始化@Link
        GreenButton({ greenButtonState: $greenButtonState }).margin(12)
        // 简单类型初始化@Link
        YellowButton({ yellowButtonState: $yellowButtonProp }).margin(12)
      }
    }
  }
}
```

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214112403.88521765484814948298731311760065:50001231000000:2800:00F16043A0F85A1508EA1F6E39F21BEEC9DD3C99A45F2D00B8CADF2F8BF91D79.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

### 数组类型的@Link

```
@Component
struct Child {
  @Link items: number[];

  build() {
    Column() {
      Button(`Button1: push`)
        .margin(12)
        .width(312)
        .height(40)
        .fontColor('#FFFFFF，90%')
        .onClick(() => {
          this.items.push(this.items.length + 1);
        })
      Button(`Button2: replace whole item`)
        .margin(12)
        .width(312)
        .height(40)
        .fontColor('#FFFFFF，90%')
        .onClick(() => {
          this.items = [100, 200, 300];
        })
    }
  }
}

@Entry
@Component
struct Parent {
  @State arr: number[] = [1, 2, 3];

  build() {
    Column() {
      Child({ items: $arr })
        .margin(12)
      ForEach(this.arr,
        (item: void) => {
          Button(`${item}`)
            .margin(12)
            .width(312)
            .height(40)
            .backgroundColor('#11a2a2a2')
            .fontColor('#e6000000')
        },
        (item: ForEachInterface) => item.toString()
      )
    }
  }
}
```

上文所述，ArkUI框架可以观察到数组元素的添加，删除和替换。在该示例中@State和@Link的类型是相同的number[]，不允许将@Link定义成number类型（@Link item : number），并在父组件中用@State数组中每个数据项创建子组件。如果要使用这个场景，可以参考[@Prop](https://developer.harmonyos.com/cn/docs/documentation/doc-guides-V3/arkts-prop-0000001473537702-V3#ZH-CN_TOPIC_0000001574128565__section0418145414102)和@Observed。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231214112403.50863358864155139636669372757023:50001231000000:2800:6960FDC7D879311FF8CF5B8D5280824089D13EC2BCDA218DABD4332344288653.gif?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true)

