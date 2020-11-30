import pygame
import random

WHITE = (255,255,255)
pad_width = 1024
pad_height = 1024
background_height = -1024

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

'''
drawObject로 통합
def back(background, x,y):
    global gamepad
    gamepad.blit(background, (x,y))

def airplane(x,y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x,y))
'''
def runGame():
    global gamepad,aircraft, clock, background1, background2
    
    x = pad_width * 0.875
    y = pad_height * 0.875
    x_change = 0
    
    background1_y = 0
    background2_y = background_height
    
    crashed = False #6. 종료를 위한 플래그
    while not crashed:
        for event in pygame.event.get(): #7. 다양한 이벤트를 반복해서 리턴해준다
            if event.type == pygame.QUIT:#이벤트 1. 창을 닫으면 종료
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0
        x += x_change
                
        #게임판을 다시 그림
        gamepad.fill(WHITE)
        
        background1_y += 4 #0 <- -512 <- -1024 <- 1024 <- 512 <- 0 <- -512
        background2_y += 4 #-512 <- -1024 <- 1024 <- 512 <- 0
        
        if background1_y == -background_height:
            background1_y = background_height #-1024
            
        if background2_y == -background_height:
            background2_y = background_height #-1024
            
        drawObject(background1,0, background1_y)
        drawObject(background2,0, background2_y)
        
        drawObject(aircraft, x, y)
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2
    
    
    pygame.init()#1.라이브러리 호출
    gamepad = pygame.display.set_mode((pad_width, pad_height))#2.게임판 크기 설정
    pygame.display.set_caption('pyGalaga')#3.타이틀설정
    aircraft = pygame.image.load('galaga.png')
    background1 = pygame.image.load('배경.png')
    background2 = background1.copy()
    
    clock = pygame.time.Clock()#4.fps 설정
    runGame()#5. 초기화 마무리 후 호출
    
initGame()