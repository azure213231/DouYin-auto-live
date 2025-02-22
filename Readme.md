#### 注意事项

1. 使用chrome浏览器
2. 保持pycharm为窗口模式，否则容易导致代码失效。（无法获取到chrome中的按钮元素）
3. 网页中打开的抖音需要登录，否则定时弹幕脚本无法发送
4. 使用谷歌浏览器打开直播间，浏览器只能有这一个窗口
5. 确认ws_release获取弹幕成功后，开启脚本
6. 保持pycharm为窗口模式



#### 如何使用

1. 运行ws_release捕获抖音弹幕

2. 运行redis用于数据分发

3. 使用pycharm打开项目DouYin-auto-live

4. 运行get_message获取弹幕

5. 运行consumer针对弹幕处理

6. 运行recover自动发送弹幕，需要Chrome登录账号

7. 使用chorm打开对应直播间即可监测

   <img src="\img\image.png" style="zoom:50%;" />





#### 自定义代码修改

1、弹幕触发关键词以及对应按键逻辑
增加需要触发的礼物或者弹幕
修改对应快捷键

<img src="\img\image2.png" style="zoom:50%;" />

<img src="\img\image3.png" style="zoom:50%;" />





2、定时随机弹幕
recover中进行修改
添加新的弹幕按照格式进行添加
自定义发送时间直接修改并重新运行即可

<img src="\img\image8.png" style="zoom:50%;" />



3、抖音弹幕交互信息分析（想要新增礼物等）
在get_message中将红框中#去除，重新运行
等待接收直播间的对应礼物
停止get_message脚本
在douyinMessage中查看对应的操作type类型，如送礼是type5
在控制台中查询type为5的数据，即可找到最近送出的礼物名称

<img src="\img\1721195042719.png" style="zoom:50%;" />





4、点赞一定数量触发特效代码
运行message、consumer即可生效，开启成功后在message中会正常输出
message中，顶部可以修改点赞最小次数触发，默认100触发一次

<img src="\img\image5.png" style="zoom:50%;" />



5、抖音弹幕记录
运行message即可保存弹幕
保存弹幕路径为message下，自动按照日期划分文件，新的弹幕会进行续写
保存信息为  时间-昵称-内容

<img src="\img\image6.png" style="zoom:50%;" />

<img src="\img\image7.png" style="zoom:50%;" />

