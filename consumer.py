import pyautogui
import pygetwindow
import redis
import time
import pygetwindow as gw
import re
import win32gui
import win32con

loop_sec = 0.1
press_sec = 0.5
list_name = 'douyin'
# key_list = ('w', 's', 'a', 'd', 'j', 'k', 'u', 'i', 'z', 'x', 'f', 'enter', 'shift', 'backspace')
key_list = ('000','666', '888','999','333')  #接收的指令白名单
gift_key_list = ('小心心','玫瑰','抖音','人气票')  #接收的礼物指令白名单

def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r

def find_window_with_partial_title(partial_title):
    matching_windows = []

    def enum_windows_callback(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if partial_title in title:
                matching_windows.append(hwnd)

    win32gui.EnumWindows(enum_windows_callback, None)
    return matching_windows


def focus_window(partial_title):
    try:
        windows = find_window_with_partial_title(partial_title)
        if not windows:
            print(f"未找到包含 '{partial_title}' 的窗口")
            return

        hwnd = windows[0]

        # 尝试恢复窗口（如果最小化）
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        time.sleep(1)  # 等待窗口恢复

        # 尝试将窗口置于前台
        win32gui.SetForegroundWindow(hwnd)
        print(f"已激活窗口: {win32gui.GetWindowText(hwnd)}")

    except Exception as e:
        print(f"发生了其他错误: {e}")


def print_window_titles():
    # 获取所有窗口的列表
    all_windows = gw.getAllWindows()
    for window in all_windows:
        # 打印窗口的标题
        print(window.title)

def control(key_name):
    # print("key_name =", key_name)
    if key_name == None:
        # print("本次无指令发出")
        return
    key_name = key_name.lower()

    focus_window('OBS')

    # print("\033[发出指令:{}\033[0m".format(key_name))

    # 弹幕
    if key_name in key_list:
        # press_key = '';

        if key_name == '000' or key_name == '000':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '1')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        if key_name == '666' or key_name == '666':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '2')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        if key_name == '888' or key_name == '888':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '3')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        if key_name == '999' or key_name == '999':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '4')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        if key_name == '333' or key_name == '333':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '9')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)
        #
        # if key_name == '灯' or key_name == '灯':
        #     press_key = 'R'
        #     # pyautogui.keyDown(press_key)
        #     pyautogui.hotkey('ctrl', '6')
        #     time.sleep(press_sec)
        #     # pyautogui.keyUp(key_name)
        #     # time.sleep(press_sec)
        #
        # if key_name == '秋' or key_name == '秋':
        #     press_key = 'R'
        #     # pyautogui.keyDown(press_key)
        #     pyautogui.hotkey('ctrl', '7')
        #     time.sleep(press_sec)
        #     # pyautogui.keyUp(key_name)
        #     # time.sleep(press_sec)
        #
        # if key_name == '雪' or key_name == '雪':
        #     press_key = 'R'
        #     # pyautogui.keyDown(press_key)
        #     pyautogui.hotkey('ctrl', '8')
        #     time.sleep(press_sec)
        #     # pyautogui.keyUp(key_name)
        #     # time.sleep(press_sec)
        #
        # if key_name == '季' or key_name == '季':
        #     press_key = 'R'
        #     # pyautogui.keyDown(press_key)
        #     pyautogui.hotkey('ctrl', '9')
        #     time.sleep(press_sec)
        #     # pyautogui.keyUp(key_name)
        #     # time.sleep(press_sec)

        if press_key != '':
            print("发出指令: " + key_name + "，执行按键: " + press_key)
            # time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            print("结束指令", key_name)

    # 礼物
    if key_name in gift_key_list:
        press_key = '';

        if key_name == '小心心' or key_name == '小心心':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '5')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        # if key_name == '人气票' or key_name == '人气票':
        #     press_key = 'R'
        #     # pyautogui.keyDown(press_key)
        #     pyautogui.hotkey('ctrl', '8')
        #     time.sleep(press_sec)
        #     # pyautogui.keyUp(key_name)
        #     # time.sleep(press_sec)

        if key_name == '玫瑰' or key_name == '玫瑰':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '7')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        if key_name == '人气票' or key_name == '人气票':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '6')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)

        if key_name == '抖音' or key_name == '抖音':
            press_key = 'R'
            # pyautogui.keyDown(press_key)
            pyautogui.hotkey('ctrl', '8')
            time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            # time.sleep(press_sec)


        if press_key != '':
            print("发出指令: " + key_name + "，执行按键: " + press_key)
            # time.sleep(press_sec)
            # pyautogui.keyUp(key_name)
            print("结束指令", key_name)

        # print("\033[发出指令:{}\033[0m".format(key_name))
        # pyautogui.keyDown(key_name)

        # if key_name == 'a' or key_name == 'd':a
            # print("发出指令w")
        #     pyautogui.keyDown('w')

        # time.sleep(press_sec)
        # pyautogui.keyUp(key_name)

        # if key_name == 'a' or key_name == 'd':
        #     print("发出指令w")
        #     pyautogui.keyUp('w')

        # print("结束指令", key_name)

if __name__ == '__main__':
    r = init_redis()
    print("开始监听弹幕消息, loop_sec =", loop_sec)
    # print_window_titles()
    while True:
        key_name = r.lpop(list_name)
        r.delete(list_name)
        control(key_name)
        time.sleep(loop_sec)
