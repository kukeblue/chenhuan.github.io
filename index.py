
import win32gui
import win32api
import win32con
import time
# import pyautogui


# def mouse_click(x, y):
#     win32api.SetCursorPos([x, y])
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# long_position = win32api.MAKELONG(1296, 37)
# hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
# print(hwnd)
# hwnd = '000305BA'
# win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, 0)

def mouse_left_click(x, y):
    hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
    print(hwnd)
    y += 36
    time.sleep(0.05)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
    time.sleep(0.05)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, win32api.MAKELONG(x, y))
    time.sleep(0.05)
    raise Exception('line xxx')


mouse_left_click(100, 100)
print('执行完毕')
# mouse_click(100, 100)
