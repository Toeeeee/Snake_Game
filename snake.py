import pygame
import time
import random
 
pygame.init()

w = 600
h = 600 

# Khởi tạo màn hình 
screen = pygame.display.set_mode((w,h)) 
pygame.display.set_caption("Snake of Toeee") 
clock = pygame.time.Clock()

snake_block = 10 
snake_speed = 15 

font_style = pygame.font.SysFont("ubuntu", 25)
score_font = pygame.font.SysFont("ubuntu", 35)

def flowers() : 
    flower = pygame.image.load('image/flower.png') 
    screen.blit(flower,(440,100)) 
    screen.blit(flower,(90,340)) 
    screen.blit(flower,(350,489)) 

def grasses () :
    grass = pygame.image.load('image/grass.png') 
    screen.blit(grass,(100,70)) 
    screen.blit(grass,(150,510)) 
    screen.blit(grass,(400,189)) 
    screen.blit(grass,(500,432)) 
    screen.blit(grass,(200,300)) 

def draw_HCN () :
    pygame.draw.rect(screen, 'brown', [40,40,510,10])
    pygame.draw.rect(screen, 'brown', [40,40,10,510])
    pygame.draw.rect(screen, 'brown', [550,40,10,510])
    pygame.draw.rect(screen, 'brown', [40,550,520,10])

    
def Your_score (score) : 
    value = score_font.render("Your Score: " + str(score), True, 'tomato' ) 
    screen.blit(value, [0,0] ) 

def Snake(snake_block, snake_list ): 
    for i in snake_list : 
        pygame.draw.rect(screen, 'yellow', [i[0], i[1], snake_block , snake_block]) 

def message(msg, color) : 
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [w / 6, h / 3])

def Screen(): 
    openning = pygame.image.load('image/openning.png') 
    running = True 
    while running : 
        screen.fill('blue') 
        screen.blit(openning,(0,0)) 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : 
                running = False
        pygame.display.update()
        time.sleep(1) 
        break 
    if running == False :     
        pygame.quit()
        quit()

def GameLoop():

    running = True
    game_close = False

    x1 = w / 2
    y1 = h / 2
    
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(70, w - snake_block - 70 ) / 10.0) * 10.0
    foody = round(random.randrange(70, h - snake_block - 70 ) / 10.0) * 10.0
 
    while running == True :
        while game_close == True:
            screen.fill('darkgreen')
            message("You Lost! Press UP-Play Again or DOWN-Quit", 'red')
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get() : 
                if event.type == pygame.KEYDOWN : 
                    if event.key == pygame.K_DOWN : 
                        running = False 
                        game_close = False 
                    if event.key == pygame.K_UP: 
                        gameLoop() 
                if event.type == pygame.QUIT : 
                    running = False 
                    game_close = False 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= w - 61  or x1 < 61 or y1 >= h - 61 or y1 < 61:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill('darkgreen')
        draw_HCN() 
        grasses()
        flowers()
        pygame.draw.rect(screen, 'orangered', [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        Snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(70, w - snake_block - 70 ) / 10.0) * 10.0
            foody = round(random.randrange(70, h - snake_block - 70 ) / 10.0) * 10.0
            Length_of_snake += 1

        pygame.display.update()
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

Screen()
GameLoop()