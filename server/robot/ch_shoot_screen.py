
import pyautogui


def screenshot(name, region=None):
    pyautogui.screenshot(name, region=(region[0] * 2, region[1] * 2, region[2] * 2, region[3] * 2))
