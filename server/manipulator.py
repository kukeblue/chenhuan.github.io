
# import robot.ch_shoot_screen as ch_shoot_screen
# from pyautogui import screenshot
# import _thread
# import ocr.index as ocr
# from log import logger
import win32gui
import win32api
import win32con
import time


class Manipulator:
    mouse_position = [0, 0]
    position = [240, 225]
    size = [800, 600]
    region = (240, 225, 0, 0);
    area = (0, 0, 0, 0);
    hwnd = None
    # self.position[0], self.position[1], self.size[0] + self.position[0], self.size[1] + self.position[1])

    def __init__(self):
        hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
        self.hwnd = hwnd
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        left = left / 2
        top = top / 2
        right = right / 2
        bottom = bottom / 2
        print(left, top, right, bottom)
        self.position = [left, top]
        self.size = [right - left, bottom - top]
        self.region = (left, top, self.size[0], self.size[1]);
        # _thread.start_new_thread(self.loop_update_state, ())

    @staticmethod
    def shoot_game_window(path, region):
        print('todo')
        # return ch_shoot_screen.screenshot(path, region=region)

    def mouse_left_click(self, x, y):
        hwnd = self.hwnd
        print(hwnd)
        y += 36
        time.sleep(0.05)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(0.05)
        win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
        time.sleep(0.05)

    def loop_update_state(self):
        print('todo')
        # while True:
        #     time.sleep(1)
            # self.mouse_position = [pyautogui.position().x, pyautogui.position().y];

    def find_text(self):
        # logger.launch_logger(msg='开始区域找字' + str(self.region) )
        image = self.shoot_game_window('text.png', self.region);
        # res = ocr.get_text_from_image('text.png')
        # logger.launch_logger(msg='查找成功: 文字条数-' + str(res['words_result_num']) + ' 内容-' +str(res['words_result']))







