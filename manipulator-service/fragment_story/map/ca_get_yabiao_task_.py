import infrastructure
import time
import time
import pyautogui
from logger import logger

# 红色导标旗镖局520 151
def ca_520_151():
    infrastructure.Keyboard.hot_key('alt', 'e')
    time.sleep(1)
    infrastructure.screen.move_find_image('../../images/7/ca.png')
    infrastructure.Mouse.right_click(num=2)
    time.sleep(1)
    infrastructure.screen.move_find_image('../../images/7/ca_520_151.png')
    infrastructure.Mouse.left_click()
    time.sleep(1)
    infrastructure.Keyboard.hot_key('alt', 'e')
    infrastructure.Keyboard.press('f9')
    infrastructure.screen.move_find_image('../../images/ca/ca_520_159.png')
    infrastructure.Mouse.left_click()
    time.sleep(2)
    infrastructure.Keyboard.press('f9')
    infrastructure.screen.move_find_image('../../images/ca/ca_biao_33_20.png')
    infrastructure.Mouse.left_click()
    time.sleep(5)
    infrastructure.Mouse.right_click(num=3)
    infrastructure.Keyboard.press('f9')
    infrastructure.screen.move_find_image('../../images/ca/ca_biao_npc1.png', confidence=0.7)
    infrastructure.Mouse.left_click(num=1)
    time.sleep(1)
    infrastructure.screen.move_find_image('../../images/ca/ca_biao_tree.png', confidence=0.7)
    infrastructure.Mouse.left_click(num=1)
    time.sleep(2)
    infrastructure.Keyboard.press('f9')
    infrastructure.screen.move_find_image('../../images/ca/ca_biao_npc1.png', confidence=0.7)
    infrastructure.Mouse.left_click(num=1)
    time.sleep(1)
    box = infrastructure.screen.find_image('../../images/ca/ca_biao_message1.png')
    if box is None:
        logger.launch_logger('镖局启动人工验证')
        pyautogui.alert(text='人工验证完成', title='进入人工验证', button='OK')
        infrastructure.screen.move_find_image('../../images/ca/ca_biao_message2.png')
        infrastructure.Mouse.left_click(num=1)
    else:
        infrastructure.screen.move(box.left, box.top)
        infrastructure.Mouse.left_click(num=1)
        time.sleep(1)
        infrastructure.screen.move_find_image('../../images/ca/ca_biao_message2.png')
        infrastructure.Mouse.left_click(num=1)


# ca_520_151()