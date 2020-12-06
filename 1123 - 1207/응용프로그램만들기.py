import os
import pygame
import random
from time import sleep

WHITE = (255,255,255)
RED = (255,0,0)
pad_width = 1024
pad_height = 1024
background_height = -1024
meteor_width = 75
aircraft_width = 180
aircraft_height = 180

fireball1_width = 56
fireball1_height = 136
fireball2_width = 59
fireball2_height = 85

def drawScore(count, hit):
    global gamepad
    
    font = pygame.font.SysFont(None, 25)
    text = font.render('Meteor Passed: ' + str(count), True, WHITE)
    hit_text = font.render('Meteor hit: ' + str(hit), True, WHITE)
    gamepad.blit(text, (0,0))
    gamepad.blit(hit_text, (0,15))
    

def gameOver():
    global gamepad
    dispMessage('Game Over')

def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamepad
    
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((pad_width/2),(pad_height/2))
    gamepad.blit(TextSurf, TextRect)
    pygame.display.update()
    sleep(2)
    runGame()
    
def crash():
    global gamepad
    dispMessage("Crashed!")

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x,y))

def runGame():
    global gamepad,aircraft, clock, background1, background2
    global meteor, fires, bullet, boom
    
    isShotMeteor = False
    boom_count = 0
    
    meteor_passed = 0
    meteor_hit = 0
    
    bullet_xy = []
    
    x = pad_width * 0.80 #819.2
    y = pad_height * 0.80 #819.2
    x_change = 0
    
    background1_y = 0
    background2_y = background_height
    
    meteor_x = random.randrange(aircraft_width/2, pad_width - aircraft_width/2)
    meteor_y = 0
    
    fire_x = random.randrange(0, pad_width)
    fire_y = 0
    random.shuffle(fires)
    fire = fires[0]
    
    crashed = False #6. 종료를 위한 플래그
    while not crashed:
        print(meteor_x)
        for event in pygame.event.get(): #7. 다양한 이벤트를 반복해서 리턴해준다
            if event.type == pygame.QUIT:#이벤트 1. 창을 닫으면 종료
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #왼쪽 이동
                    x_change = -10
                elif event.key == pygame.K_RIGHT: #오른쪽 이동
                    x_change = 10
                elif event.key == pygame.K_LCTRL: #공격
                    bullet_x = x + aircraft_width/2 - 3 #819.2 + 180/2
                    bullet_y = y# + aircraft_height #819.2# + 180
                    bullet_xy.append([bullet_x, bullet_y]) #리스트에 추가
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0
        
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
        
        drawScore(meteor_passed, meteor_hit)
        
        if meteor_passed >= 3:
            gameOver()
        
        #비행선 위치
        x += x_change #x = 819.2
        if x<0: 
            x = 0
        elif x > pad_width - aircraft_width:
            x = pad_width - aircraft_width
        
        #유성 위치
        meteor_y += 5
        if meteor_y >= pad_height:
            meteor_passed += 1
            meteor_x = random.randrange(aircraft_width/2, pad_width - aircraft_width/2)
            meteor_y = 0
        
        
        #불덩이 위치    
        if fire[1] == None:
            fire_y += 15
        else:
            fire_y += 10
        
        if fire_y >= pad_height:
            fire_x = random.randrange(0, pad_width)
            fire_y = 0
            random.shuffle(fires)
            fire = fires[0]
        if fire[1] != None:
            drawObject(fire[1], fire_x, fire_y)
        
        #유성과 충돌
        if y < meteor_y: #비행선이 유성을 지나칠 때
            #비행선 왼쪽 좌표 유성 좌표 안 일때
            #비행선 오른쪽 좌표 유성 좌표 안 일때
            if(x > meteor_x and x<meteor_x + meteor_width) or \
                (x+aircraft_width > meteor_x and x+aircraft_width < meteor_x+meteor_width):
                crash()
            #유성이 비행선 width 안일 때  
            if x<meteor_x and x+aircraft_width > meteor_x+meteor_width:
                crash()
        #불덩이와 충돌
        if fire[1] != None:
            if fire[0] == 0:
                fireball_width = fireball1_width
                fireball_height = fireball1_height
            elif fire[0] == 1:
                fireball_width = fireball2_width
                fireball_height = fireball2_height
            
            if y < fire_y:
                if(x > fire_x and x<fire_x + fireball_width) or \
                    (x+fireball_width > fire_x and x+fireball_width < fire_x+fireball_width):
                    crash()
                #유성이 비행선 width 안일 때  
                if x<fire_x and x+aircraft_width > fire_x+fireball_width:
                    crash()
                    
        drawObject(aircraft, x, y)

        #총알 위치
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 15 #y좌표
                bullet_xy[i][1] = bxy[1]
                
                #boom check
                if bxy[1] < meteor_y: #총알 y위치 < 유성 y위치 (만나거나 둘이 지나쳤다면)
                    if bxy[0] > meteor_x and bxy[0] < meteor_x + meteor_width: #유성 width 안이라면
                        bullet_xy.remove(bxy)
                        isShotMeteor = True
                        
                if bxy[1] < 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)
                              
        if not isShotMeteor: #총알이 유성에 맞지 않았다면 실행
            drawObject(meteor, meteor_x, meteor_y)
        else: #총알이 유성에 맞으면 실행
            drawObject(boom, meteor_x, meteor_y)
            boom_count += 1
            if boom_count > 5: #위치 다시 랜덤
                boom_count = 0
                meteor_passed -= 1
                meteor_hit += 1
                meteor_x = random.randrange(0, pad_width - meteor_width)
                meteor_y = pad_height
                isShotMeteor = False
                
        pygame.display.update()
        clock.tick(120)
    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2
    global meteor, fires, bullet, boom
    
    fires = []# 파이어, None을 담을 리스트
    
    pygame.init()#1.라이브러리 호출
    gamepad = pygame.display.set_mode((pad_width, pad_height))#2.게임판 크기 설정
    pygame.display.set_caption('pyGalaga')#3.타이틀설정
    aircraft = pygame.image.load('galaga.png') #4.비행선 로드
    background1 = pygame.image.load('배경.png') #5. 배경로드
    background2 = background1.copy() #5-1 움직일 배경 복사
    meteor = pygame.image.load('메테오.png') #6-1. 장애물 로드
    #이미지 크기가 다르므로 식별자가 필요
    fires.append((0,pygame.image.load('fireball.png')))#6-2 장애물 로드
    fires.append((1,pygame.image.load('fireball2.png')))#6-3 장애물 로드
    
    for i in range(3):  #불덩이 시간차
        fires.append((i+2,None))
        
    bullet = pygame.image.load('bullet.png') #7 총알 로드
    boom = pygame.image.load('boom.png')#8 피격 이펙트 로드
    
    clock = pygame.time.Clock()#4.fps 설정
    runGame()#5. 초기화 마무리 후 호출
    
initGame()