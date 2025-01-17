# CriCraque
import sys
import pygame
from pygame.examples.aliens import SCORE
from pygame.key import key_code

pygame.init()

SCREENWIDTH = 844
SCREENHEIGHT = 597

window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Cricraque")

Arriere = pygame.image.load("images\Arriere_plan.png")
Balle_a = pygame.image.load("images\Balle_a.png")
Balle_b = pygame.image.load("images\Balle_b.png")
Balle_c = pygame.image.load("images\Balle_c.png")
Balle_d = pygame.image.load("images\Balle_d.png")
Ball_f = pygame.image.load("images\Ball_f.png")
Balle_e = pygame.image.load("images\Balle_e.png")

effet_but_marque = pygame.mixer.Sound("sounds/goal.mp3")


rect_Arriere = Arriere.get_rect(center=(SCREENWIDTH/2, SCREENHEIGHT/2))
rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 +370, SCREENHEIGHT/2 - 60))
rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))

Postion = [(90,125),(400,125), (695,125),
           (90,305), (400,305),(695,305,),
           (90,480) ,(400,480), (695,480)]



# chargement de polices et textes
font = pygame.font.Font(None, 100)
fontGameOver = pygame.font.Font(None, 300)
text_game_over = font.render("GAME OVER!", True, (255, 255, 255))
rect_game_over = text_game_over.get_rect(center=(SCREENWIDTH/2, SCREENHEIGHT/2))
image_score_player_1 = font.render("0", True, (0,0,0))
image_score_player_2 = font.render("0", True, (0,0,0))
rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH/2 - 100, 100))
rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH/2 + 100, 100))       


score_player_1 = 0
score_player_2 = 0

clock = pygame.time.Clock()

game_rennung = True
time_passed = 0

TIMEUP = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEUP, 2000, 1)

pygame.mixer.music.set_volume(0.2)

while game_rennung:
    
    # Delta time
    dt = clock.tick(60) / 1000.0
    time_passed += dt
      
    #INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            game_rennung = False
            

        if event.type == pygame .JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")

        if event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")

        if event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} moved to {event.value}")
            

        # Récupérer les touches
        keys = pygame.key.get_pressed()

        # Filtrer les touches a, b, c, d, e et f du clavier
        # filtrer le touche a
        if keys[pygame.K_1] and keys[pygame.K_a]:
            rect_Balle_a = Postion[0]
        elif keys[pygame.K_2] and keys[pygame.K_a]:
            rect_Balle_a = Postion[1]
        elif keys[pygame.K_3] and keys[pygame.K_a]:
            rect_Balle_a = Postion[2]
        elif keys[pygame.K_4] and keys[pygame.K_a]:
            rect_Balle_a = Postion[3]
        elif keys[pygame.K_5] and keys[pygame.K_a]:
            rect_Balle_a = Postion[4]
        elif keys[pygame.K_6] and keys[pygame.K_a]:
            rect_Balle_a = Postion[5]
        elif keys[pygame.K_7] and keys[pygame.K_a]:
            rect_Balle_a = Postion[6]
        elif keys[pygame.K_8] and keys[pygame.K_a]:
            rect_Balle_a = Postion[7]
        elif keys[pygame.K_9] and keys[pygame.K_a]:
            rect_Balle_a = Postion[8]
        
        # filtrer le touche b
        if keys[pygame.K_1] and keys[pygame.K_b]:
            rect_Balle_b = Postion[0]
        elif keys[pygame.K_2] and keys[pygame.K_b]:
            rect_Balle_b = Postion[1]
        elif keys[pygame.K_3] and keys[pygame.K_b]:
            rect_Balle_b = Postion[2]
        elif keys[pygame.K_4] and keys[pygame.K_b]:
            rect_Balle_b = Postion[3]
        elif keys[pygame.K_5] and keys[pygame.K_b]:
            rect_Balle_b = Postion[4]
        elif keys[pygame.K_6] and keys[pygame.K_b]:
            rect_Balle_b = Postion[5]
        elif keys[pygame.K_7] and keys[pygame.K_b]:
            rect_Balle_b = Postion[6]
        elif keys[pygame.K_8] and keys[pygame.K_b]:
            rect_Balle_b = Postion[7]
        elif keys[pygame.K_9] and keys[pygame.K_b]:
            rect_Balle_b = Postion[8]
         #filtrer le touche c   
        if keys[pygame.K_1] and keys[pygame.K_c]:
            rect_Balle_c = Postion[0]
        elif keys[pygame.K_2] and keys[pygame.K_c]:
            rect_Balle_c = Postion[1]
        elif keys[pygame.K_3] and keys[pygame.K_c]:
            rect_Balle_c = Postion[2]
        elif keys[pygame.K_4] and keys[pygame.K_c]:
            rect_Balle_c = Postion[3]
        elif keys[pygame.K_5] and keys[pygame.K_c]:
            rect_Balle_c = Postion[4]
        elif keys[pygame.K_6] and keys[pygame.K_c]:
            rect_Balle_c = Postion[5]
        elif keys[pygame.K_7] and keys[pygame.K_c]:
            rect_Balle_c = Postion[6]
        elif keys[pygame.K_8] and keys[pygame.K_c]:
            rect_Balle_c = Postion[7]
        elif keys[pygame.K_9] and keys[pygame.K_c]:
            rect_Balle_c = Postion[8]
        #filtrer le touche d
        if keys[pygame.K_1] and keys[pygame.K_d]:
            rect_Balle_d = Postion[0]
        elif keys[pygame.K_2] and keys[pygame.K_d]:
            rect_Balle_d = Postion[1]
        elif keys[pygame.K_3] and keys[pygame.K_d]:
            rect_Balle_d = Postion[2]
        elif keys[pygame.K_4] and keys[pygame.K_d]:
            rect_Balle_d = Postion[3]
        elif keys[pygame.K_5] and keys[pygame.K_d]:
            rect_Balle_d = Postion[4]
        elif keys[pygame.K_6] and keys[pygame.K_d]:
            rect_Balle_d = Postion[5]
        elif keys[pygame.K_7] and keys[pygame.K_d]:
            rect_Balle_d = Postion[6]
        elif keys[pygame.K_8] and keys[pygame.K_d]:
            rect_Balle_d = Postion[7]
        elif keys[pygame.K_9] and keys[pygame.K_d]:
            rect_Balle_d = Postion[8]
            #filtrer le touche e
        if keys[pygame.K_1] and keys[pygame.K_e]:
            rect_Balle_e = Postion[0]
        elif keys[pygame.K_2] and keys[pygame.K_e]:
            rect_Balle_e = Postion[1]
        elif keys[pygame.K_3] and keys[pygame.K_e]:
            rect_Balle_e = Postion[2]
        elif keys[pygame.K_4] and keys[pygame.K_e]:
            rect_Balle_e = Postion[3]
        elif keys[pygame.K_5] and keys[pygame.K_e]:
            rect_Balle_e = Postion[4]
        elif keys[pygame.K_6] and keys[pygame.K_e]:
            rect_Balle_e = Postion[5]
        elif keys[pygame.K_7] and keys[pygame.K_e]:
            rect_Balle_e = Postion[6]
        elif keys[pygame.K_8] and keys[pygame.K_e]:
            rect_Balle_e = Postion[7]
        elif keys[pygame.K_9] and keys[pygame.K_e]:
            rect_Balle_e = Postion[8]
            #filtrer le touche f
        if keys[pygame.K_1] and keys[pygame.K_f]:
            rect_Ball_f = Postion[0]
        elif keys[pygame.K_2] and keys[pygame.K_f]:
            rect_Ball_f = Postion[1]
        elif keys[pygame.K_3] and keys[pygame.K_f]:
            rect_Ball_f = Postion[2]
        elif keys[pygame.K_4] and keys[pygame.K_f]:
            rect_Ball_f = Postion[3]
        elif keys[pygame.K_5] and keys[pygame.K_f]:
            rect_Ball_f = Postion[4]
        elif keys[pygame.K_6] and keys[pygame.K_f]:
            rect_Ball_f = Postion[5]
        elif keys[pygame.K_7] and keys[pygame.K_f]:
            rect_Ball_f = Postion[6]
        elif keys[pygame.K_8] and keys[pygame.K_f]:
            rect_Ball_f = Postion[7]
        elif keys[pygame.K_9] and keys[pygame.K_f]:
            rect_Ball_f = Postion[8]
            
            
    #UPDATE
    #position unique de la balle a
    if rect_Balle_a == rect_Balle_b:
         rect_Balle_b = (SCREENWIDTH/2 - 399, SCREENHEIGHT/2 + 5)
    elif rect_Balle_a == rect_Balle_c:
        rect_Balle_c = (SCREENWIDTH/2 - 399, SCREENHEIGHT/2 + 99)
    elif rect_Balle_a == rect_Balle_d:
         rect_Balle_d = (SCREENWIDTH/2 +340, SCREENHEIGHT/2 - 80)
    elif rect_Balle_a == rect_Balle_e:
        rect_Balle_e = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 10)
    elif rect_Balle_a == rect_Ball_f:
         rect_Ball_f = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 100)
    #position unique de la balle b
    if rect_Balle_b == rect_Balle_c:
        rect_Balle_c = (SCREENWIDTH/2 - 399, SCREENHEIGHT/2 + 99)
    elif rect_Balle_b == rect_Balle_d:
         rect_Balle_d = (SCREENWIDTH/2 +340, SCREENHEIGHT/2 - 80)
    elif rect_Balle_b == rect_Balle_e:
        rect_Balle_e = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 10)
    elif rect_Balle_b == rect_Ball_f:
         rect_Ball_f = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 100)
    #position unique de la balle c
    elif rect_Balle_c == rect_Balle_d:
         rect_Balle_d = (SCREENWIDTH/2 +340, SCREENHEIGHT/2 - 80)
    elif rect_Balle_c == rect_Balle_e:
        rect_Balle_e = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 10)
    elif rect_Balle_c == rect_Ball_f:
         rect_Ball_f = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 100)
    #position unique de la balle d     
    if rect_Balle_d == rect_Balle_e:
        rect_Balle_e = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 10)
    elif rect_Balle_d == rect_Ball_f:
         rect_Ball_f = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 100)
    #position unique de la balle d     
    if rect_Balle_e == rect_Ball_f:
        rect_Ball_f = (SCREENWIDTH/2 + 340, SCREENHEIGHT/2 + 100)
         
    #logiques des points
    if rect_Balle_a == Postion[0]:
         if rect_Balle_b == Postion[1]:
            if rect_Balle_c == Postion[2]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 +370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))
    elif rect_Balle_d == Postion[0]: 
        if rect_Balle_e == Postion[1]:
            if rect_Ball_f == Postion[2]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 +370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))
    if rect_Balle_a == Postion[0]: 
        if rect_Balle_b == Postion[3]:
            if rect_Balle_c == Postion[6]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30)) 
    elif rect_Balle_d == Postion[0]: 
        if rect_Balle_e == Postion[3]:
            if rect_Ball_f == Postion[6]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))  
    if rect_Balle_a == Postion[0]: 
        if rect_Balle_b == Postion[4]:
            if rect_Balle_c == Postion[8]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))   
    elif rect_Balle_d == Postion[0]: 
        if rect_Balle_e == Postion[4]:
            if rect_Ball_f == Postion[8]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))
    if rect_Balle_a == Postion[1]: 
        if rect_Balle_b == Postion[4]:
            if rect_Balle_c == Postion[7]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30)) 
    elif rect_Balle_d == Postion[1]: 
        if rect_Balle_e == Postion[4]:
            if rect_Ball_f == Postion[7]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))  
    if rect_Balle_a == Postion[2]: 
        if rect_Balle_b == Postion[5]:
            if rect_Balle_c == Postion[8]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))   
    elif rect_Balle_d == Postion[2]: 
        if rect_Balle_e == Postion[5]:
            if rect_Ball_f == Postion[8]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))  
    if rect_Balle_a == Postion[3]: 
        if rect_Balle_b == Postion[4]:
            if rect_Balle_c == Postion[5]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))
    elif rect_Balle_d == Postion[3]: 
        if rect_Balle_e == Postion[4]:
            if rect_Ball_f == Postion[5]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))   
    if rect_Balle_a == Postion[6]: 
        if rect_Balle_b == Postion[7]:
            if rect_Balle_c == Postion[8]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))  
    elif rect_Balle_d == Postion[6]: 
        if rect_Balle_e == Postion[7]:
            if rect_Ball_f == Postion[8]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30)) 
    if rect_Balle_a == Postion[2]: 
        if rect_Balle_b == Postion[4]:
            if rect_Balle_c == Postion[6]:
                score_player_1 = score_player_1 + 1
                image_score_player_1 = font.render(str(score_player_1), True, (0, 0, 0))
                rect_score_player_1 = image_score_player_1.get_rect(center=(SCREENWIDTH / 2 - 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))  
    elif rect_Balle_d == Postion[2]: 
        if rect_Balle_e == Postion[4]:
            if rect_Ball_f == Postion[6]:
                score_player_2 = score_player_2 + 1
                image_score_player_2 = font.render(str(score_player_2), True, (0, 0, 0))
                rect_score_player_2 = image_score_player_2.get_rect(center=(SCREENWIDTH / 2 + 100, 100))
                pygame.time.set_timer(TIMEUP, 2000, 1)
                effet_but_marque.play()
                rect_Balle_a = Balle_a.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 - 60))
                rect_Balle_b = Balle_b.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 30))
                rect_Balle_c = Balle_c.get_rect(center=(SCREENWIDTH/2 - 370, SCREENHEIGHT/2 + 120))
                rect_Balle_d= Balle_d.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 - 60))
                rect_Ball_f = Ball_f.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 120))
                rect_Balle_e = Balle_e.get_rect(center=(SCREENWIDTH/2 + 370, SCREENHEIGHT/2 + 30))                                                                                                                                                               
            
    #RENDER
    window.fill((19, 24, 75))
    window.blit(Arriere,rect_Arriere)
    window.blit(Balle_a, rect_Balle_a)
    window.blit(Balle_b, rect_Balle_b)
    window.blit(Balle_c, rect_Balle_c)
    window.blit(Balle_d, rect_Balle_d)
    window.blit(Ball_f, rect_Ball_f)
    window.blit(Balle_e, rect_Balle_e)
    window.blit(image_score_player_1, rect_score_player_1)
    window.blit(image_score_player_2, rect_score_player_2)


    pygame.display.flip()

pygame.quit()
sys.exit(0)
