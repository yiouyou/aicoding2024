# 卡片数据交互说明

更新时间: 2024-01-15 12:24

ArkTS卡片框架提供了updateForm()接口和requestForm()接口主动触发卡片的页面刷新。

![](https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyPub/011/111/111/0000000000011111111.20231121183819.01402491542662555973018250125079:50001231000000:2800:FF1AC116533BDD04701231F7E91BF4C77DF992B1F3BC7662C0DD0AF302C68690.png?needInitFileName=true?needInitFileName=true?needInitFileName=true?needInitFileName=true "点击放大")

| 接口        | 是否系统能力 | 约束                                                                                 |
| :---------- | :----------- | :----------------------------------------------------------------------------------- |
| updateForm  | 否           | 1. 提供方调用。2. 提供方仅允许刷新自己的卡片，其他提供方的卡片无法刷新。             |
| requestForm | 是           | 1. 使用方调用。2. 仅允许刷新添加到当前使用方的卡片，添加到其他使用方的卡片无法刷新。 |

下面介绍卡片页面刷新的典型场景。

