import asyncio,json
import websockets
import asyncio
import redis
import datetime
import os

list_name = 'douyin'
# key_list = ('w', 's', 'a', 'd', 'j', 'k', 'u', 'i', 'z', 'x', 'f', 'enter', 'shift', 'backspace')
key_list = ('000','666', '888','999')  #接收的指令白名单
gift_key_list = ('小心心','玫瑰','抖音','人气票')  #接收的礼物指令白名单

def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r


async def process():

    async with websockets.connect("ws://127.0.0.1:8888/",ping_interval=None) as ws:  #ping_interval=None 是为了防止sockets断开
        while True:
            try:
                message = await asyncio.wait_for(ws.recv(), timeout=30)
                # print('Received: ' + message)
                # 打印所有信息
                # print(message)
                message = json.loads(message)
                # print(  message )

                # 弹幕
                if message.get("Type") == 1:
                    Data = json.loads(message.get("Data"))
                    speak_message = Data.get("Content")

                    # 保存弹幕
                    User = Data.get("User")
                    nick_name = User.get("Nickname")
                    save_pop_up_message(nick_name,speak_message)

                    r = init_redis()
                    found_key = None

                    for key in key_list:
                        if key.lower() in speak_message.lower():
                            found_key = key
                            break

                    if found_key:
                        print('弹幕推送队列：', found_key)
                        r.rpush(list_name, found_key)

                # 点赞
                if message.get("Type") == 2:
                    Data = json.loads(message.get("Data"))
                    speak_message = Data.get("Total")

                    r = init_redis()
                    found_key = 'like:' + str(speak_message)
                    #
                    # for key in key_list:
                    #     if key.lower() in speak_message.lower():
                    #         found_key = key
                    #         break

                    if found_key:
                        print('点赞推送队列：', found_key)
                        r.rpush(list_name, found_key)

                # 礼物
                if message.get("Type") == 5:
                    Data = json.loads(message.get("Data"))
                    gift_name = Data.get("GiftName")

                    r = init_redis()
                    found_key = None

                    for key in gift_key_list:
                        if key.lower() in gift_name.lower():
                            found_key = key
                            break

                    if found_key:
                        print('礼物推送队列：', found_key)
                        r.rpush(list_name, found_key)



                    # list_str = list(speak_message)
                    # print("弹幕拆分:", list_str)
                    # for char in list_str:
                    #     if char.lower() in key_list:
                    #         print('推送队列：', char.lower())
                    #         r = init_redis()
                    #
                    #         char_l = char.lower()
                    #
                    #         r.rpush(list_name,char_l)

                # if message.get("Type") == 5:
                #     Data = json.loads(message.get("Data"))
                #     git_name = Data.get("GiftName")
                #     print('推送队列：', git_name.lower())
                #     r = init_redis()
                #     char_l = git_name.lower()
                #     r.rpush(list_name, char_l)

            except asyncio.TimeoutError as e:
                continue
            except websockets.exceptions.ConnectionClosed as e:
                print('连接已经关闭')
                print(e)
                continue

# 保存弹幕信息
def save_pop_up_message(nickname, content):
    # 获取当前时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # 定义文件名
    filename = "message/" + filename_date + "TiktokPopUpRecord.txt"

    # 检查文件是否存在，如果不存在则创建
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("时间 - 用户昵称: 消息内容\n")  # 写入表头

    # 以追加模式打开文件并写入内容
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{current_time} - {nickname}: {content}\n")
        print('弹幕已记录')

asyncio.run(process())


