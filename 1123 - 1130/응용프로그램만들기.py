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
    global meteor, fires
    
    x = pad_width * 0.80
    y = pad_height * 0.80
    x_change = 0
    
    background1_y = 0
    background2_y = background_height
    
    meteor_x = random.randrange(0, pad_width)
    meteor_y = 0
    
    fire_x = random.randrange(0, pad_width)
    fire_y = 0
    random.shuffle(fires)
    fire = fires[0]
    
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
        
        #배경 draw
        background1_y += 2 # 0 => 1024 => -1024 => 0
        background2_y += 2 # -1024 => 0 => 1024 => -1024
        if background1_y == -background_height: #1024
            background1_y = background_height #-1024       
        if background2_y == -background_height: #1024
            background2_y = background_height #-1024      
        drawObject(background1,0, background1_y)
        drawObject(background2,0, background2_y)
        
        #유성 위치
        meteor_y += 7
        if meteor_y >= pad_height:
            meteor_x = random.randrange(0, pad_width)
            meteor_y = 0
        drawObject(meteor, meteor_x, meteor_y)
         
        #불덩이 위치    
        if fire == None:
            fire_y += 20
        else:
            fire_y += 10
        
        if fire_y >= pad_height:
            fire_x = random.randrange(0, pad_width)
            fire_y = 0
            random.shuffle(fires)
            fire = fires[0]
        if fire != None:
            drawObject(fire, fire_x, fire_y)
        
        #비행선 위치
        drawObject(aircraft, x, y)
       
        pygame.display.update()
        clock.tick(120)
    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2
    global meteor, fires
    
    fires = []# 파이어, None을 담을 리스트
    
    pygame.init()#1.라이브러리 호출
    gamepad = pygame.display.set_mode((pad_width, pad_height))#2.게임판 크기 설정
    pygame.display.set_caption('pyGalaga')#3.타이틀설정
    aircraft = pygame.image.load('galaga.png') #4.비행선 로드
    background1 = pygame.image.load('배경.png') #5. 배경로드
    background2 = background1.copy() #5-1 움직일 배경 복사
    meteor = pygame.image.load('메테오.png') #6-1. 장애물 로드
    fires.append(pygame.image.load('fireball.png'))#6-2 장애물 로드
    fires.append(pygame.image.load('fireball2.png'))#6-3 장애물 로
    
    for i in range(5):  #불덩이 시간차
        fires.append(None)
    
    clock = pygame.time.Clock()#4.fps 설정
    runGame()#5. 초기화 마무리 후 호출
    
initGame()