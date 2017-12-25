import sys

import pygame

from settings import Settings

from ship import Ship

def  run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hegiht))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship =Ship(screen)

    #设置背景颜色
    bg_color = (ai_settings.bg_color)
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
        #每次循环都冲毁屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #绘制让最近的屏幕可见
        pygame.display.flip()
run_game()