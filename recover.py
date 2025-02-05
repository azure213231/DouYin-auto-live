import random
import time

import pygetwindow as gw
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import win32gui
import win32con

# 定义消息数组
output_texts = [
    '每日固定开播时间，持续优化内容，喜欢白噪音、冥想、助眠音乐的朋友可以点点关注，祝你好梦[玫瑰]',
    '欢迎大家来到睡眠小乖，每日用雨声陪伴你入睡，喜欢的家人们记得点点关注'
]
#output_texts = []
# 发送间隔时间（秒）
sleep_time = 5

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


class ChromeAutomation:
    def __init__(self):
        self.driver = None

    def init_chrome(self):
        # ChromeDriver 路径
        chrome_driver_path = 'E:\\DevTool\\chromedriver-win64\\chromedriver.exe'

        # 配置 Chrome 选项
        chrome_options = Options()
        chrome_options.debugger_address = '127.0.0.1:9222'  # 指定调试地址
        # chrome_options.add_argument('--remote-debugging-port=9222')  # 设置调试端口号

        # 初始化 Service 对象
        service = Service(executable_path=chrome_driver_path)

        # 初始化 WebDriver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def recover(self):
        try:
            # 打开网页
            # self.driver.get('https://live.douyin.com/153620661859')

            # 等待直到元素可见
            # 创建 WebDriverWait 对象时，传入一个有效的超时值，例如 10 秒
            chat_textarea = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'chat-textarea'))
            )
            # print("输入框已找到")

            # 从数组中随机选择输出文本
            output_text = random.choice(output_texts)

            # 清空现有内容并输入新的内容
            chat_textarea.clear()
            chat_textarea.send_keys(output_text)
            # print("填写: " + self.output_text)

            # 等待直到 SVG 元素可见
            svg_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'svg.webcast-chatroom___send-btn.btn-icon'))
            )

            # focus_window('Chrome')
            # 使用 ActionChains 模拟点击
            actions = ActionChains(self.driver)
            actions.move_to_element(svg_element).click().perform()
            print("已发送: " + output_text)

        except Exception as e:
            print(f"发生错误: {e}")


if __name__ == '__main__':
    automation = ChromeAutomation()
    automation.init_chrome()
    # 定时调用 recover 方法
    while True:
        automation.recover()
        print("等待" + str(sleep_time) + "秒...")
        time.sleep(sleep_time)  # 5 分钟（300 秒）
