import sys
import pygame
def check_event():
    #키보드와 마우스 이벤트에 응답합니다.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()