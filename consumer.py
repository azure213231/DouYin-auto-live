import pyautogui
import pygetwindow
import redis
import time
import pygetwindow as gw
import re
import win32gui
import win32con
from pywinauto import Application, findwindows

loop_sec = 0.1
press_sec = 0.5
list_name = 'douyin'
# key_list = ('w', 's', 'a', 'd', 'j', 'k', 'u', 'i', 'z', 'x', 'f', 'enter', 'shift', 'backspace')
key_list = ('000','666', '888','999')  #接收的指令白名单
gift_key_list = ('小心心','玫瑰','抖音','人气票')  #接收的礼物指令白名单
like_key_list = ('点赞数100流星雨','点赞数300小日子')  #点赞指令白名单

def init_redis():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    return r

def list_all_windows():
    windows = findwindows.find_elements()
    for window in windows:
        # 使用 .name 获取窗口标题
        print(window.name)

def init_pywinauto():
    # 使用正则表达式来匹配包含 "OBS" 的窗口标题
    # list_all_windows()
    app = Application(backend="win32").connect(title_re=".*OBS.*")
    window = app.window(title_re=".*OBS.*")  # 匹配任何包含 OBS 字样的窗口
    print("Window found:", window)
    return app

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

def control(pywinauto,key_name):
    global last_like_count  # 声明使用全局变量
    # print("key_name =", key_name)
    if key_name == None:
        # print("本次无指令发出")
        return
    key_name = key_name.lower()

    # 方式1
    # focus_window('OBS')

    #方式2
    # # 找到OBS窗口
    # windows = pywinauto.windows(title_re="OBS")
    # # 遍历所有找到的窗口
    # for win in windows:
    #     print(win.window_text())
    #     win.set_focus()  # 将窗口设置为活跃窗口

    #方式3
    # 找到OBS窗口
    obs_window = pywinauto.window(title_re="OBS")
    obs_window.set_focus()

    # 弹幕
    if key_name in key_list:

        if key_name == '000' or key_name == '000':
            pyautogui.hotkey('ctrl', '1')
            time.sleep(press_sec)

        if key_name == '666' or key_name == '666':
            pyautogui.hotkey('ctrl', '2')
            time.sleep(press_sec)

        if key_name == '888' or key_name == '888':
            pyautogui.hotkey('ctrl', '3')
            time.sleep(press_sec)

        if key_name == '999' or key_name == '999':
            pyautogui.hotkey('ctrl', '4')
            time.sleep(press_sec)

        # if key_name == '333' or key_name == '333':
        #     pyautogui.hotkey('ctrl', '9')
        #     time.sleep(press_sec)
        #
        # if key_name == '灯' or key_name == '灯':
        #     pyautogui.hotkey('ctrl', '6')
        #     time.sleep(press_sec)
        #
        # if key_name == '秋' or key_name == '秋':
        #     pyautogui.hotkey('ctrl', '7')
        #     time.sleep(press_sec)
        #
        # if key_name == '雪' or key_name == '雪':
        #     pyautogui.hotkey('ctrl', '8')
        #     time.sleep(press_sec)
        #
        # if key_name == '季' or key_name == '季':
        #     pyautogui.hotkey('ctrl', '9')
        #     time.sleep(press_sec)

    # 点赞
    if key_name in like_key_list:
        if key_name == '点赞数100流星雨':
            # 点赞触发快捷键
            print('触发点赞事件：点赞数100流星雨')
            pyautogui.hotkey('ctrl', '9')
            time.sleep(press_sec)

        if key_name == '点赞数300小日子':
            # 点赞触发快捷键
            print('触发点赞事件：点赞数300小日子')
            pyautogui.hotkey('alt', '1')
            time.sleep(press_sec)

    # 礼物
    if key_name in gift_key_list:

        if key_name == '小心心' or key_name == '小心心':
            pyautogui.hotkey('ctrl', '5')
            time.sleep(press_sec)

        # if key_name == '人气票' or key_name == '人气票':
        #     pyautogui.hotkey('ctrl', '8')
        #     time.sleep(press_sec)

        if key_name == '玫瑰' or key_name == '玫瑰':
            pyautogui.hotkey('ctrl', '7')
            time.sleep(press_sec)

        if key_name == '人气票' or key_name == '人气票':
            pyautogui.hotkey('ctrl', '6')
            time.sleep(press_sec)

        if key_name == '抖音' or key_name == '抖音':
            pyautogui.hotkey('ctrl', '8')
            time.sleep(press_sec)




if __name__ == '__main__':
    r = init_redis()
    pywinauto = init_pywinauto()
    print("开始监听弹幕消息, loop_sec =", loop_sec)
    # print_window_titles()
    while True:
        key_name = r.lpop(list_name)
        r.delete(list_name)
        control(pywinauto,key_name)
        time.sleep(loop_sec)
