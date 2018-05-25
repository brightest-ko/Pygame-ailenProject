import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    # Start the main loop for the game
    while True:
        gf.check_event()
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        '''
        #루프를 실행할 때마다 화면을 다시 그립니다.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()
        
run_game()