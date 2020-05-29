import pyautogui
from logger import logger


class Mouse:
    @staticmethod
    def left_click(num=1):
        logger.launch_logger('左击鼠标' + str(num) + '次')
        pyautogui.click(clicks=num)

    @staticmethod
    def right_click(num=1):
        logger.launch_logger('右击鼠标' + str(num) + '次')
        pyautogui.click(num=1, button='right')

    @staticmethod
    def move_to(x, y):
        logger.launch_logger('鼠标移动到' + str(x) + ',' + str(y))
        pyautogui.moveTo(x, y)


