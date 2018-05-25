import sys
import pygame

def check_event(ship):
    #키보드와 마우스 이벤트에 응답합니다.
    for event in pygame.event.get():
        print(event)
        
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #우주선을 오른쪽으로 움직입니다.
                #ship.rect.centerx += 1
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #우주선을 오른쪽으로 움직입니다.
                #ship.rect.centerx += 1
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
                
def update_screen( ai_settings , screen , ship ):
    #화면에 있는 이미지를 업데이트하고 새 화면에 그립니다.
    #루프를 실행할 때마다 화면을 다시 그립니다.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
   
    #가장 최근에 그린 화면을 표시합니다.
    pygame.display.flip()
    