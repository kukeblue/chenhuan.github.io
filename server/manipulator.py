
import robot.ch_shoot_screen as ch_shoot_screen
import pyautogui
import time
import _thread
import ocr.index as ocr
from log import logger
import win32gui


class Manipulator:
    mouse_position = [0, 0]
    position = [240, 225]
    size = [800, 600]
    region = (240, 225, 0, 0);
    area = (0, 0, 0, 0);
    # self.position[0], self.position[1], self.size[0] + self.position[0], self.size[1] + self.position[1])

    def __init__(self):
        hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        left = left / 2
        top = top / 2
        right = right / 2
        bottom = bottom / 2
        print(left, top, right, bottom)
        self.position = [left, top]
        self.size = [right - left, bottom - top]
        self.region = (left, top, self.size[0], self.size[1]);
        _thread.start_new_thread(self.loop_update_state, ())

    @staticmethod
    def shoot_game_window(path, region):
        return ch_shoot_screen.screenshot(path, region=region)

    @staticmethod
    def do_click(num=1):
        pyautogui.click(clicks=num)

    @staticmethod
    def do_move_to(x, y):
        pyautogui.moveTo(x, y, pyautogui.easeOutQuad)

    @staticmethod
    def do_move(x, y):
        pyautogui.move(x, y)

    def loop_update_state(self):
        while True:
            time.sleep(1)
            self.mouse_position = [pyautogui.position().x, pyautogui.position().y];

    def find_text(self):
        logger.launch_logger(msg='开始区域找字' + str(self.region) )
        image = self.shoot_game_window('text.png', self.region);
        res = ocr.get_text_from_image('text.png')
        logger.launch_logger(msg='查找成功: 文字条数-' + str(res['words_result_num']) + ' 内容-' +str(res['words_result']))










