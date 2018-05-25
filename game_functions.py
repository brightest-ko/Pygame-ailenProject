import sys
import pygame
def check_event():
    #키보드와 마우스 이벤트에 응답합니다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update_screen( ai_settings , screen , ship ):
    #화면에 있는 이미지를 업데이트하고 새 화면에 그립니다.
    #루프를 실행할 때마다 화면을 다시 그립니다.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
   
    #가장 최근에 그린 화면을 표시합니다.
    pygame.display.flip()