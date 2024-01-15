# 通过message事件刷新卡片内容

更新时间: 2024-01-15 12:25

在卡片页面中可以通过postCardAction接口触发message事件拉起FormExtensionAbility，然后由FormExtensionAbility刷新卡片内容，下面是这种刷新方式的简单示例。

* 在卡片页面通过注册Button的onClick点击事件回调，并在回调中调用postCardAction接口触发message事件拉起FormExtensionAbility。

```
let storage = new LocalStorage();

@Entry(storage)
@Component
struct WidgetCard {
  @LocalStorageProp('title') title: string = 'init';
  @LocalStorageProp('detail') detail: string = 'init';

  build() {
    Column() {
      Button('刷新')
        .onClick(() => {
          postCardAction(this, {
            'action': 'message',
            'params': {
              'msgTest': 'messageEvent'
            }
          });
        })
      Text(`${this.title}`)
      Text(`${this.detail}`)
    }
    .width('100%')
    .height('100%')
  }
}
```
* 在FormExtensionAbility的onFormEvent生命周期中调用updateForm接口刷新卡片。

```
import formBindingData from '@ohos.app.form.formBindingData';
import FormExtensionAbility from '@ohos.app.form.FormExtensionAbility';
import formProvider from '@ohos.app.form.formProvider';

export default class EntryFormAbility extends FormExtensionAbility {
  onFormEvent(formId, message) {
    // Called when a specified message event defined by the form provider is triggered.
    console.info(`FormAbility onEvent, formId = ${formId}, message: ${JSON.stringify(message)}`);
    let formData = {
      'title': 'Title Update Success.', // 和卡片布局中对应
      'detail': 'Detail Update Success.', // 和卡片布局中对应
    };
    let formInfo = formBindingData.createFormBindingData(formData)
    formProvider.updateForm(formId, formInfo).then((data) => {
      console.info('FormAbility updateForm success.' + JSON.stringify(data));
    }).catch((error) => {
      console.error('FormAbility updateForm failed: ' + JSON.stringify(error));
    })
  }

  ...
}
```

  运行效果如下图所示。

  ![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183819.67493386673415860980849818971052:50001231000000:2800:5596EADBA3EEA07F179E38C4B057DE0D76C4BAF6ACD367AAED2DBF6FE5EC21D8.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

