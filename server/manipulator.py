
import robot.ch_shoot_screen as ch_shoot_screen


class Manipulator:
    position = [0, 0]
    size = [800, 600]
    region = (0, 0, 0, 0);
    # self.position[0], self.position[1], self.size[0] + self.position[0], self.size[1] + self.position[1])

    def shoot_game_window(self):
        print('全屏幕截图')
        ch_shoot_screen.screenshot('window.png', region=(self.region))
        print('截图成功')



