import win32gui
import pyautogui
from baidu_api import BApi
from logger import logger


class Screen:
    screen_rect = [0, 0, 0, 0];
    region = (0, 0, 0, 0)

    def __init__(self, window_class, window_title):
        # hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
        hwnd = win32gui.FindWindow(window_class, window_title)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        self.hwnd = hwnd
        self.screen_rect = [left, top, right, bottom]
        self.region = (left, top, right - left, bottom - top)
        logger.launch_logger('绑定窗口成功' + str(self.screen_rect))

    def relative_move_to(self, x, y):
        logger.launch_logger('移动到窗口内:' + str(x) + ',' + str(y))
        pyautogui.moveTo(self.screen_rect[0] + x, self.screen_rect[1] + y)

    def find_image(self, image_path, confidence=0.9):
        logger.launch_logger('查找图片:' + image_path)
        image_location = pyautogui.locateOnScreen(image_path, confidence=confidence, region=self.region)

        if image_location is not None:
            logger.launch_logger('图片' + image_path + '查找成功')
            return image_location
        else:
            raise Exception('图片' + image_path + '查找失败')

    def find_area_text(self, region):
        if region is None:
            region = self.region
        else:
            region[0] = region[0] + self.screen_rect[0]
            region[1] = region[1] + self.screen_rect[1]
        logger.launch_logger('开始区域找子:' + str(region))
        im = pyautogui.screenshot('find_area_text.png', region=tuple(region))
        logger.launch_logger('find_area_text.png 保存成功')
        BApi.find_text('find_area_text.png')
