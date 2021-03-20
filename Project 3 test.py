import pygame
import time
import random
 
pygame.init()
 
display_width = 800#x cord
display_height = 600#y cord
 
BLACK = (0,0,0)#colors
WHITE = (255,255,255)
RED = (225,0,0)
GREEN = (0,225,0)
BLUE = (0,0,225)
LIGHTGREEN = (0,255,0)
LIGHTRED = (255,0,0)
LIGHTBLUE = (0,0,255)
SWBLUE = (102, 178, 255)
LIGHTPINK = (255,0,255)
PINK = (255,102,255)
LIGHTORANGE = (255,128,0)
ORANGE = (255,153,51)
LIGHTYELLOW = (255,255,0)
YELLOW = (255,255,51)
LIGHTPURPLE = (127,0,255)
PURPLE = (153,51,255)



HLS = pygame.image.load("hlsprite.jpg")#images/pictures/sprites
LBS = pygame.image.load("lbsprite.jpg")
TJS = pygame.image.load("tjsprite.jpg")
HLSC = pygame.image.load("hlsprite_char.jpg")
LBSC = pygame.image.load("lbsprite_char.jpg")
TJSC = pygame.image.load("tjsprite_char.jpg")
CITY1 = pygame.image.load("city1.jpg") 
CITY2 = pygame.image.load("city2.jpg")
CITY3 = pygame.image.load("city3.jpg")
SHOP1 = pygame.image.load("shop1.jpg")
OFFICE1 = pygame.image.load("office1.jpg")
ICON = pygame.image.load("Pogchamp.jpg")
BACK1 = pygame.image.load("intro_back.jpg")
BACK2 = pygame.image.load("back2.jpg")
HUD = pygame.image.load("hud.jpg")
SCROLL = pygame.image.load("scroll.png")
HELMET = pygame.image.load("helmet.png")
SWORD = pygame.image.load("sword.png")
POTION = pygame.image.load("potion.png")
VOODOO = pygame.image.load("voodoo.png")
CAVE = pygame.image.load("cave.jpg")
MALL = pygame.image.load("mall.jpg")
STEVEN = pygame.image.load("steven.png")


SELECTSOUND = pygame.mixer.Sound("select_sound.wav")

stats = [['Strength', 1], ['Defense', 1]]
loot = [['Hp:', 100], ['Coin', 0]]
##char = None
##char_selection_number = 1

pygame.display.set_icon(ICON)#game image
block_color = (53,115,255)

pause = False


gameDisplay = pygame.display.set_mode((display_width,display_height))#sets displays to dw and dh(x,y cords)
pygame.display.set_caption('POGGERS THE GAME')#game title
clock = pygame.time.Clock()

 


def text_objects(text, font):#TEXT controls with white
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):#TEXT controls with swblue
    textSurface = font.render(text, True, SWBLUE)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
##    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)    
 

def results():
    results1 = True

    while results1:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                      
        gameDisplay.blit(BACK1, (0,0))
        largeText = pygame.font.SysFont("comicsansms",64)
        if loot[0][1] >= 51:
            TextSurf4, TextRect4 = text_objects("YOU WON", largeText)
            TextRect4.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf4, TextRect4)
        if loot[0][1] <= 50:
            TextSurf4, TextRect4 = text_objects("YOU LOST", largeText)
            TextRect4.center = ((display_width/2),(display_height/2))
            gameDisplay.blit(TextSurf4, TextRect4)
        
        button("PLAY AGAIN",300,350,150,50,BLUE,LIGHTBLUE,game_intro2)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_intro(welcome, game):

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
               
        gameDisplay.blit(BACK1, (0,0))
        largeText = pygame.font.SysFont("comicsansms",64)
        TextSurf, TextRect = text_objects(str(game), largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf2, TextRect2 = text_objects(str(welcome), largeText)
        TextRect2.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf2, TextRect2)
        SELECTSOUND.play()
        
        

        button("START",150,450,100,50,GREEN,LIGHTGREEN,char_select)
        button("QUIT",550,450,100,50,RED,LIGHTRED,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro2():

    intro2 = True

    while intro2:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        loot[0][1] = 100
        loot[1][1] = 0
        stats[0][1] = 1
        stats[1][1] = 1
        gameDisplay.blit(BACK1, (0,0))
        largeText = pygame.font.SysFont("comicsansms",64)
        TextSurf, TextRect = text_objects("POGGERS THE GAME", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        TextSurf2, TextRect2 = text_objects("WELCOME TO", largeText)
        TextRect2.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf2, TextRect2)
        SELECTSOUND.play()
        
        

        button("START",150,450,100,50,GREEN,LIGHTGREEN,char_select)
        button("QUIT",550,450,100,50,RED,LIGHTRED,quitgame)

        pygame.display.update()
        clock.tick(15)
        
        
    
    

    
def char_select():
    global pause
 
    charselection = False
 
    while not charselection:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        gameDisplay.blit(BACK1, (0,0))
        largeText = pygame.font.SysFont("comicsansms",25)
        TextSurf, TextRect = text_objects("CHOOSE A CHARACTER", largeText)
        TextRect.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf, TextRect)

        gameDisplay.blit(HLSC, (25,300))
        gameDisplay.blit(LBSC, (325,300))
        gameDisplay.blit(TJSC, (625,300))
        
        button("Huey Lewis",25,450,150,50,GREEN,LIGHTGREEN,char1)
        button("Limp Bizkit",325,450,150,50,RED,LIGHTRED,char2)
        button("Tony Jr.",625,450,150,50,BLUE,LIGHTBLUE,char3)
        

        pygame.display.update()
        clock.tick(15)

def char1():
    hlcs = True

    while hlcs:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        char_selection_number = 1
        loot[1][1] = 500
        
        gameDisplay.blit(BACK1, (0,0))
        gameDisplay.blit(HLS, (275,300))
        largeText = pygame.font.SysFont("comicsansms",64)
        TextSurf4, TextRect4 = text_objects("You selected Huey Lewis", largeText)
        TextRect4.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf4, TextRect4)
        TextSurf4, TextRect4 = text_objects("You start with 500 coins", largeText)
        TextRect4.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf4, TextRect4)

        
        button("CONTINUE TO STORY",550,550,250,50,BLUE,LIGHTBLUE,story)

        pygame.display.update()
        clock.tick(15)

def char2():
    lbcs = True

    while lbcs:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        char_selection_number = 2
        stats[1][1] = 2
        
        gameDisplay.blit(BACK1, (0,0))
        gameDisplay.blit(LBS, (275,300))
        largeText = pygame.font.SysFont("comicsansms",64)
        TextSurf4, TextRect4 = text_objects("You selected Limp Bizkit", largeText)
        TextRect4.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf4, TextRect4)
        TextSurf4, TextRect4 = text_objects("You start with 2 Defense", largeText)
        TextRect4.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf4, TextRect4)

        
        button("CONTINUE TO STORY",550,550,250,50,BLUE,LIGHTBLUE,story)

        pygame.display.update()
        clock.tick(15)

def char3():
    tjcs = True

    while tjcs:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        char_selection_number = 3
        stats[0][1] = 2
        
        gameDisplay.blit(BACK1, (0,0))
        gameDisplay.blit(TJS, (275,300))
        largeText = pygame.font.SysFont("comicsansms",64)
        TextSurf4, TextRect4 = text_objects("You selected Tony Jr.", largeText)
        TextRect4.center = ((display_width/2),(100))
        gameDisplay.blit(TextSurf4, TextRect4)
        TextSurf4, TextRect4 = text_objects("You start with 2 Strength", largeText)
        TextRect4.center = ((display_width/2),(200))
        gameDisplay.blit(TextSurf4, TextRect4)

        
        button("CONTINUE TO STORY",550,550,250,50,BLUE,LIGHTBLUE,story)

        pygame.display.update()
        clock.tick(15)
def story():
    storytell = False
 
    while not storytell:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(BACK2, (0,0))
        largeText = pygame.font.SysFont("comicsansms",24)
        TextSurf, TextRect = text_objects2("The city of Poggers is a wonderful city with many nice people", largeText)
        TextSurf2, TextRect2 = text_objects2("and places to go to. There are many citizens that enjoy Poggers.", largeText)
        TextSurf3, TextRect3 = text_objects2("Poggers is a very big city with many tall and short buildings.", largeText)
        TextSurf4, TextRect4 = text_objects2("In the tallest building is a man named Steven Armstrong.", largeText)
        TextSurf5, TextRect5 = text_objects2("Steven, worked his whole life, getting to where he is today.", largeText)
        TextSurf6, TextRect6 = text_objects2("Steven is one of the wealthiest people in the city, so wealthy", largeText)
        TextSurf7, TextRect7 = text_objects2("he has been in magazines and newspapers. Unfortunately, Steven", largeText)
        TextSurf8, TextRect8 = text_objects2("cheated his way to the top, using blood and dark magic.", largeText)
        TextSurf9, TextRect9 = text_objects2("When Steven was young his parents were murdered making", largeText)
        TextSurf10, TextRect10 = text_objects2("him an orphan. Steven was sent to an adoption center.", largeText)##
        TextSurf11, TextRect11 = text_objects2("Steven hated it there and wanted to find a family.", largeText)
        TextSurf12, TextRect12 = text_objects2("One night Steven ran away from the", largeText)
        TextSurf13, TextRect13 = text_objects2("adoption center and ran away.", largeText)
        TextSurf14, TextRect14 = text_objects2("", largeText)
        TextSurf15, TextRect15 = text_objects2("", largeText)
        TextSurf16, TextRect16 = text_objects2("", largeText)
        TextSurf17, TextRect17 = text_objects2("", largeText)
        TextSurf18, TextRect18 = text_objects2("", largeText)
        TextSurf19, TextRect19 = text_objects2("", largeText)
##      TextSurf11, TextRect11 = text_objects2("", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(60))
        TextRect3.center = ((display_width/2),(90))
        TextRect4.center = ((display_width/2),(120))
        TextRect5.center = ((display_width/2),(150))
        TextRect6.center = ((display_width/2),(180))
        TextRect7.center = ((display_width/2),(210))
        TextRect8.center = ((display_width/2),(240))
        TextRect9.center = ((display_width/2),(270))
        TextRect10.center = ((display_width/2),(300))
        TextRect11.center = ((display_width/2),(330))
        TextRect12.center = ((display_width/2),(360))
        TextRect13.center = ((display_width/2),(390))
        TextRect14.center = ((display_width/2),(420))
        TextRect15.center = ((display_width/2),(450))
        TextRect16.center = ((display_width/2),(480))
        TextRect17.center = ((display_width/2),(510))
        TextRect18.center = ((display_width/2),(540))
        TextRect19.center = ((display_width/2),(570))
##        TextRect12.center = ((display_width/2),(300))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)
        gameDisplay.blit(TextSurf7, TextRect7)
        gameDisplay.blit(TextSurf8, TextRect8)
        gameDisplay.blit(TextSurf9, TextRect9)
        gameDisplay.blit(TextSurf10, TextRect10)
        gameDisplay.blit(TextSurf11, TextRect11)
        gameDisplay.blit(TextSurf12, TextRect12)
        gameDisplay.blit(TextSurf13, TextRect13)
        gameDisplay.blit(TextSurf14, TextRect14)
        gameDisplay.blit(TextSurf15, TextRect15)
        gameDisplay.blit(TextSurf16, TextRect16)
        gameDisplay.blit(TextSurf17, TextRect17)
        gameDisplay.blit(TextSurf18, TextRect18)
        gameDisplay.blit(TextSurf19, TextRect19)
        button("->",700,500,100,50,BLUE,LIGHTBLUE,story2)


        pygame.display.update()
        clock.tick(15)

def story2():
    storytell2 = False
 
    while not storytell2:
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(BACK2, (0,0))
        largeText = pygame.font.SysFont("comicsansms",24)
        TextSurf, TextRect = text_objects2("Steven didn't have any survival skills so", largeText)
        TextSurf2, TextRect2 = text_objects2("he starved to death. Fortunately for Steven,", largeText)
        TextSurf3, TextRect3 = text_objects2("he was saved by a mysterious person.", largeText)
        TextSurf4, TextRect4 = text_objects2("This mysterious person took Steven", largeText)
        TextSurf5, TextRect5 = text_objects2("as their own and raised him. Steven was ", largeText)
        TextSurf6, TextRect6 = text_objects2("taught all sorts of magic making him into a weapon.", largeText)
        TextSurf7, TextRect7 = text_objects2("One day Steven had enough with Poggers", largeText)
        TextSurf8, TextRect8 = text_objects2("and wanted to make his own city to rule.", largeText)
        TextSurf9, TextRect9 = text_objects2("Steven started to turn people against", largeText)
        TextSurf10, TextRect10 = text_objects2("each other. Steven controlled the minds", largeText)
        TextSurf11, TextRect11 = text_objects2("of people and used them to do his dirty work.", largeText)
        TextSurf12, TextRect12 = text_objects2("Others saw that Steven was doing this and", largeText)
        TextSurf13, TextRect13 = text_objects2("started a force against Steven. This team", largeText)
        TextSurf14, TextRect14 = text_objects2("was called the Kappers.", largeText)
        TextSurf15, TextRect15 = text_objects2("They let anyone join and", largeText)
        TextSurf16, TextRect16 = text_objects2("now are trying to take down Steven.", largeText)
        TextSurf17, TextRect17 = text_objects2("You are a member and", largeText)
        TextSurf18, TextRect18 = text_objects2("will try to defeat him", largeText)
        TextSurf19, TextRect19 = text_objects2("Can you do it?", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(60))
        TextRect3.center = ((display_width/2),(90))
        TextRect4.center = ((display_width/2),(120))
        TextRect5.center = ((display_width/2),(150))
        TextRect6.center = ((display_width/2),(180))
        TextRect7.center = ((display_width/2),(210))
        TextRect8.center = ((display_width/2),(240))
        TextRect9.center = ((display_width/2),(270))
        TextRect10.center = ((display_width/2),(300))
        TextRect11.center = ((display_width/2),(330))
        TextRect12.center = ((display_width/2),(360))
        TextRect13.center = ((display_width/2),(390))
        TextRect14.center = ((display_width/2),(420))
        TextRect15.center = ((display_width/2),(450))
        TextRect16.center = ((display_width/2),(480))
        TextRect17.center = ((display_width/2),(510))
        TextRect18.center = ((display_width/2),(540))
        TextRect19.center = ((display_width/2),(570))
##        TextRect12.center = ((display_width/2),(300))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        gameDisplay.blit(TextSurf4, TextRect4)
        gameDisplay.blit(TextSurf5, TextRect5)
        gameDisplay.blit(TextSurf6, TextRect6)
        gameDisplay.blit(TextSurf7, TextRect7)
        gameDisplay.blit(TextSurf8, TextRect8)
        gameDisplay.blit(TextSurf9, TextRect9)
        gameDisplay.blit(TextSurf10, TextRect10)
        gameDisplay.blit(TextSurf11, TextRect11)
        gameDisplay.blit(TextSurf12, TextRect12)
        gameDisplay.blit(TextSurf13, TextRect13)
        gameDisplay.blit(TextSurf14, TextRect14)
        gameDisplay.blit(TextSurf15, TextRect15)
        gameDisplay.blit(TextSurf16, TextRect16)
        gameDisplay.blit(TextSurf17, TextRect17)
        gameDisplay.blit(TextSurf18, TextRect18)
        gameDisplay.blit(TextSurf19, TextRect19)
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path1start)


        pygame.display.update()
        clock.tick(15)


def path1start():#PATH 1
    road1start = True
 
    while road1start:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY1, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("There are six streets you can go down.", largeText)
        TextSurf2, TextRect2 = text_objects("Choose one to progress:", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        button("STREET 1",150,400,100,50,RED,LIGHTRED,p1b1)
        button("STREET2",300,400,100,50,GREEN,LIGHTGREEN,p1b2)
        button("STREET 3",450,400,100,50,BLUE,LIGHTBLUE,p1b3)
        button("STREET 4",150,500,100,50,ORANGE,LIGHTORANGE,p1b4)
        button("STREET 5",300,500,100,50,PINK,LIGHTPINK,p1b5)
        button("STREET 6",450,500,100,50,PURPLE,LIGHTPURPLE,p1b6)

        pygame.display.update()
        clock.tick(15)

def p1b1():
    path1button1 = True
 
    while path1button1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
               
        gameDisplay.blit(CITY1, (0,0))
        gameDisplay.blit(HUD, (0,0))

        
        
        if loot[1][1] == 0:
          loot[1][1] = 500
        if loot[1][1] == 500:
          loot[1][1] = 1000
        
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You walk down the street and find a wallet.", largeText)
        TextSurf2, TextRect2 = text_objects("You gain some coins", largeText)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path2start)

        pygame.display.update()
        clock.tick(15)

def p1b2():
    path1button2 = True
 
    while path1button2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()

             
        gameDisplay.blit(CITY1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You walk down the street and find a bus and take it.", largeText)
        TextSurf2, TextRect2 = text_objects("You skip the next street..", largeText)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path3start)

        pygame.display.update()
        clock.tick(15)

def p1b3():
    path1button3 = True
 
    while path1button3:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        if loot[0][1] == 100:
            loot[0][1] = 75
            
        gameDisplay.blit(CITY1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You run into some rabid dogs and they attack you.", largeText)
        TextSurf2, TextRect2 = text_objects("You take 25 hp health and run away.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path2start)

        pygame.display.update()
        clock.tick(15)

def p1b4():
    path1button4 = True
 
    while path1button4:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        
        if loot[0][1] == 100:
            loot[0][1] = 15
            
        gameDisplay.blit(CITY1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a lit campfire and sit by it for a while.", largeText)
        TextSurf2, TextRect2 = text_objects("You gain 5 hp.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path2start)

        pygame.display.update()
        clock.tick(15)

def p1b5():
    path1button5 = True
 
    while path1button5:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        if stats[1][1] == 1:
          stats[1][1] = 2
        if stats[1][1] == 2:
          stats[1][1] = 3
          
##        print(stats)     
        gameDisplay.blit(CITY1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a stand of hats and pickup a baseball cap.", largeText)
        TextSurf2, TextRect2 = text_objects("Your defense increased", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path2start)

        pygame.display.update()
        clock.tick(15)

def p1b6():
    path1button6 = True
 
    while path1button6:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        if stats[0][1] == 1:
          stats[0][1] = 2
        if stats[0][1] == 2:
          stats[0][1] = 3
                    
        gameDisplay.blit(CITY1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You walk down the street and find a golf club on the ground.", largeText)
        TextSurf2, TextRect2 = text_objects("Your strength increased.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path2start)

        pygame.display.update()
        clock.tick(15)

def path2start():#PATH 2
    road2start = True
 
    while road2start:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY2, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("There are six streets you can go down.", largeText)
        TextSurf2, TextRect2 = text_objects("Choose one to progress:", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        button("STREET 1",150,400,100,50,RED,LIGHTRED,p2b1)
        button("STREET2",300,400,100,50,GREEN,LIGHTGREEN,p2b2)
        button("STREET 3",450,400,100,50,BLUE,LIGHTBLUE,p2b3)
        button("STREET 4",150,500,100,50,ORANGE,LIGHTORANGE,p2b4)
        button("STREET 5",300,500,100,50,PINK,LIGHTPINK,p2b5)

        pygame.display.update()
        clock.tick(15)

def p2b1():
    path2button1 = True
 
    while path2button1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()

        if loot[0][1] == 100:
          loot[0][1] = 75
        if loot[0][1] == 105:
          loot[0][1] = 80
        if loot[0][1] == 75:
          loot[0][1] = 50
          
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You run into a gang with weapons. ", largeText)
        TextSurf3, TextRect3 = text_objects("they attack you.", largeText)
        TextSurf2, TextRect2 = text_objects("You lose 25 hp.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(550))
        TextRect3.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path3start)

        pygame.display.update()
        clock.tick(15)

def p2b2():
    path2button2 = True
 
    while path2button2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You run into a big rock in the middle of the street.", largeText)
        TextSurf2, TextRect2 = text_objects("You stare and nothing happens.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path3start)

        pygame.display.update()
        clock.tick(15)

def p2b3():
    path2button3 = True
 
    while path2button3:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()

        if loot[1][1] == 0:
          loot[1][1] = 200
        if loot[1][1] == 500:
          loot[1][1] = 700
        if loot[1][1] == 1000:
          loot[1][1] = 1200
            
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a big dumpster and search it.", largeText)
        TextSurf2, TextRect2 = text_objects("You find some coin.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path3start)

        pygame.display.update()
        clock.tick(15)

def p2b4():
    path2button4 = True
 
    while path2button4:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        if stats[0][1] == 1:
          stats[0][1] = 2
        if stats[0][1] == 2:
          stats[0][1] = 3
        if stats[0][1] == 3:
          stats[0][1] = 4

               
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",28)
        TextSurf, TextRect = text_objects("You run into the karate kid and he teaches you how to fight.", largeText)
        TextSurf2, TextRect2 = text_objects("teaches you how to fight. You gained some strength.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path3start)

        pygame.display.update()
        clock.tick(15)

def p2b5():
    path2button5 = True
 
    while path2button5:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        if stats[1][1] == 1:
          stats[1][1] = 2
        if stats[1][1] == 2:
          stats[1][1] = 3
        if stats[1][1] == 3:
          stats[1][1] = 4
                     
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a shield on the ground.", largeText)
        TextSurf2, TextRect2 = text_objects("You gained some defense.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path3start)

        pygame.display.update()
        clock.tick(15)


def path3start():#PATH 3
    road3start = True
 
    while road3start:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY3, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("There are six streets you can go down.", largeText)
        TextSurf2, TextRect2 = text_objects("Choose one to progress:", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        button("STREET 1",150,400,100,50,RED,LIGHTRED,p3b1)
        button("STREET2",300,400,100,50,GREEN,LIGHTGREEN,p3b2)
        button("STREET 3",450,400,100,50,BLUE,LIGHTBLUE,p3b3)
        button("STREET 4",150,500,100,50,ORANGE,LIGHTORANGE,p3b4)


        pygame.display.update()
        clock.tick(15)

def p3b1():
    path3button1 = True
 
    while path3button1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        if stats[1][1] == 1:
          stats[1][1] = 2
        if stats[1][1] == 2:
          stats[1][1] = 3
        if stats[1][1] == 3:
          stats[1][1] = 4
        if stats[1][1] == 4:
          stats[1][1] = 5
          
        gameDisplay.blit(CITY3, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find some goggles on the ground.", largeText)
        TextSurf2, TextRect2 = text_objects("You some defense.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path4start)

        pygame.display.update()
        clock.tick(15)

def p3b2():
    path3button2 = True
 
    while path3button2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        if stats[0][1] == 1:
          stats[0][1] = 2
        if stats[0][1] == 2:
          stats[0][1] = 3
        if stats[0][1] == 3:
          stats[0][1] = 4
        if stats[0][1] == 4:
          stats[0][1] = 5
          
                
        gameDisplay.blit(CITY3, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a vending machine and get a soda.", largeText)
        TextSurf2, TextRect2 = text_objects("You gained some defesne", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path4start)

        pygame.display.update()
        clock.tick(15)

def p3b3():
    path3button3 = True
 
    while path3button3:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        

        if loot[0][1] == 50:
            loot[0][1] = 40
        if loot[0][1] == 75:
            loot[0][1] = 65
        if loot[0][1] == 100:
            loot[0][1] = 90
        if loot[0][1] == 105:
            loot[0][1] = 95
        
        gameDisplay.blit(CITY3, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a giant spider and it bites you.", largeText)
        TextSurf2, TextRect2 = text_objects("You lose 10 hp", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path4start)

        pygame.display.update()
        clock.tick(15)

def p3b4():
    path3button4 = True
 
    while path3button4:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        if loot[0][1] == 50:
            loot[0][1] = 35
        if loot[0][1] == 75:
            loot[0][1] = 60
        if loot[0][1] == 100:
            loot[0][1] = 85
        if loot[0][1] == 105:
            loot[0][1] = 90
            
        gameDisplay.blit(CITY3, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",28)
        TextSurf, TextRect = text_objects("You find a robot with a flamethrower.", largeText)
        TextSurf2, TextRect2 = text_objects("You disable the robot but get burned for 15 hp.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path4start)

        pygame.display.update()
        clock.tick(15)


def path4start():#STORE OR PATH
    road4start = True
 
    while road4start:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a broken down cabin with a light on.", largeText)
        TextSurf2, TextRect2 = text_objects("Do you go inside ", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        
        button("Yes",150,400,100,50,RED,LIGHTRED,p4b1)
        button("No",300,400,100,50,GREEN,LIGHTGREEN,p4b2)


        pygame.display.update()
        clock.tick(15)

def p4b1():
    path4button1 = True
 
    while path4button1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",28)
        TextSurf, TextRect = text_objects("You enter the cabin and its actually a shop.", largeText)
        TextSurf2, TextRect2 = text_objects("An old man greets you and asks you to buy some stuff.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,insideshop)

        pygame.display.update()
        clock.tick(15)

def insideshop():
    shopinside = True

    while shopinside:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("What would you like to buy", largeText)
        TextSurf2, TextRect2 = text_objects(str(loot[1][1]), largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(SCROLL, (380,303))
        gameDisplay.blit(HELMET, (140,303))
        gameDisplay.blit(VOODOO, (260,303))
        gameDisplay.blit(SWORD, (20,303))
        gameDisplay.blit(POTION, (500,303))
        
        
        button("$200",20,400,100,50,RED,LIGHTRED,insideshop2)
        button("$500",140,400,100,50,ORANGE,LIGHTORANGE,insideshop3)
        button("$700",260,400,100,50,PINK,LIGHTPINK,insideshop4)
        button("$1000",380,400,100,50,PURPLE,LIGHTPURPLE,insideshop5)
        button("$1200",500,400,100,50,GREEN,LIGHTGREEN,insideshop6)


        pygame.display.update()
        clock.tick(15)

def insideshop2():
    shopinside2 = True
 
    while shopinside2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        if loot[1][1] == 0:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)   
        if loot[1][1] == 200:
            TextSurf, TextRect = text_objects("You pay the old man $200 for the sword", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)     
        if loot[1][1] == 500:
            TextSurf, TextRect = text_objects("You pay the old man $200 for the sword", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 700:
            TextSurf, TextRect = text_objects("You pay the old man $200 for the sword", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1000:
            TextSurf, TextRect = text_objects("You pay the old man $200 for the sword", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1200:
            TextSurf, TextRect = text_objects("You pay the old man $200 for the sword", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
            
        button("->",700,550,100,50,BLUE,LIGHTBLUE,insideshop2p)

        pygame.display.update()
        clock.tick(15)
        
def insideshop2p():
    shopinside2p = True
 
    while shopinside2p:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        
        if loot[1][1] == 200 and stats[0][1] == 1:
           loot[1][1] = 0
           stats[0][1] = 2
        if loot[1][1] == 500 and stats[0][1] == 1:
           loot[1][1] = 300
           stats[0][1] = 2
        if loot[1][1] == 700 and stats[0][1] == 1:
           loot[1][1] = 500
           stats[0][1] = 2
        if loot[1][1] == 1000 and stats[0][1] == 1:
           loot[1][1] = 800
           stats[0][1] = 2
        if loot[1][1] == 1200 and stats[0][1] == 1:
           loot[1][1] = 1000
           stats[0][1] = 2
        if loot[1][1] == 200 and stats[0][1] == 2:
           loot[1][1] = 0
           stats[0][1] = 3
        if loot[1][1] == 500 and stats[0][1] == 2:
           loot[1][1] = 300
           stats[0][1] = 3
        if loot[1][1] == 700 and stats[0][1] == 2:
           loot[1][1] = 500
           stats[0][1] = 3
        if loot[1][1] == 1000 and stats[0][1] == 2:
           loot[1][1] = 800
           stats[0][1] = 3
        if loot[1][1] == 1200 and stats[0][1] == 2:
           loot[1][1] = 1000
           stats[0][1] = 3
        if loot[1][1] == 200 and stats[0][1] == 3:
           loot[1][1] = 0
           stats[0][1] = 4
        if loot[1][1] == 500 and stats[0][1] == 3:
           loot[1][1] = 300
           stats[0][1] = 4
        if loot[1][1] == 700 and stats[0][1] == 3:
           loot[1][1] = 500
           stats[0][1] = 4
        if loot[1][1] == 1000 and stats[0][1] == 3:
           loot[1][1] = 800
           stats[0][1] = 4
        if loot[1][1] == 1200 and stats[0][1] == 3:
           loot[1][1] = 1000
           stats[0][1] = 4
        if loot[1][1] == 200 and stats[0][1] == 4:
           loot[1][1] = 0
           stats[0][1] = 5
        if loot[1][1] == 500 and stats[0][1] == 4:
           loot[1][1] = 300
           stats[0][1] = 5
        if loot[1][1] == 700 and stats[0][1] == 4:
           loot[1][1] = 500
           stats[0][1] = 5
        if loot[1][1] == 1000 and stats[0][1] == 4:
           loot[1][1] = 800
           stats[0][1] = 5
        if loot[1][1] == 1200 and stats[0][1] == 4:
           loot[1][1] = 1000
           stats[0][1] = 5
        if loot[1][1] == 200 and stats[0][1] == 5:
           loot[1][1] = 0
           stats[0][1] = 6
        if loot[1][1] == 500 and stats[0][1] == 5:
           loot[1][1] = 300
           stats[0][1] = 6
        if loot[1][1] == 700 and stats[0][1] == 5:
           loot[1][1] = 500
           stats[0][1] = 6
        if loot[1][1] == 1000 and stats[0][1] == 5:
           loot[1][1] = 800
           stats[0][1] = 6
        if loot[1][1] == 1200 and stats[0][1] == 5:
           loot[1][1] = 1000
           stats[0][1] = 6
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You leave the shop", largeText)
        TextSurf2, TextRect2 = text_objects("thanking the old man", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("->",350,500,100,50,BLUE,LIGHTBLUE,path5start)

        pygame.display.update()
        clock.tick(15)

def insideshop3():
    shopinside3 = True
 
    while shopinside3:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        if loot[1][1] == 0:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave. ", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)   
        if loot[1][1] == 200:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)     
        if loot[1][1] == 500:
            TextSurf, TextRect = text_objects("You pay the old man $500 for the helmet", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Defense", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 700:
            TextSurf, TextRect = text_objects("You pay the old man $500 for the helmet", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Defense", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1000:
            TextSurf, TextRect = text_objects("You pay the old man $500 for the helmet", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Defense", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1200:
            TextSurf, TextRect = text_objects("You pay the old man $500 for the helmet", largeText)
            TextSurf2, TextRect2 = text_objects("You gain +1 Defense", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
            
        button("->",700,550,100,50,BLUE,LIGHTBLUE,insideshop3p)

        pygame.display.update()
        clock.tick(15)
        
def insideshop3p():
    shopinside3p = True
 
    while shopinside3p:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        

        if loot[1][1] == 500 and stats[1][1] == 1:
           loot[1][1] = 0
           stats[1][1] = 2
        if loot[1][1] == 700 and stats[1][1] == 1:
           loot[1][1] = 200
           stats[1][1] == 2
        if loot[1][1] == 1000 and stats[1][1] == 1:
           loot[1][1] = 500
           stats[1][1] == 2
        if loot[1][1] == 1200 and stats[1][1] == 1:
           loot[1][1] = 700
           stats[1][1] == 2
        if loot[1][1] == 500 and stats[1][1] == 2:
           loot[1][1] = 0
           stats[1][1] = 3
        if loot[1][1] == 700 and stats[1][1] == 2:
           loot[1][1] = 200
           stats[1][1] == 3
        if loot[1][1] == 1000 and stats[1][1] == 2:
           loot[1][1] = 500
           stats[1][1] == 3
        if loot[1][1] == 1200 and stats[1][1] == 2:
           loot[1][1] = 700
           stats[1][1] == 3
        if loot[1][1] == 500 and stats[1][1] == 3:
           loot[1][1] = 0
           stats[1][1] = 4
        if loot[1][1] == 700 and stats[1][1] == 3:
           loot[1][1] = 200
           stats[1][1] == 4
        if loot[1][1] == 1000 and stats[1][1] == 3:
           loot[1][1] = 500
           stats[1][1] == 4
        if loot[1][1] == 1200 and stats[1][1] == 3:
           loot[1][1] = 700
           stats[1][1] == 4
        if loot[1][1] == 500 and stats[1][1] == 4:
           loot[1][1] = 0
           stats[1][1] = 5
        if loot[1][1] == 700 and stats[1][1] == 4:
           loot[1][1] = 200
           stats[1][1] == 5
        if loot[1][1] == 1000 and stats[1][1] == 4:
           loot[1][1] = 500
           stats[1][1] == 5
        if loot[1][1] == 1200 and stats[1][1] == 4:
           loot[1][1] = 700
           stats[1][1] == 5
        if loot[1][1] == 500 and stats[1][1] == 5:
           loot[1][1] = 0
           stats[1][1] = 6
        if loot[1][1] == 700 and stats[1][1] == 5:
           loot[1][1] = 200
           stats[1][1] == 6
        if loot[1][1] == 1000 and stats[1][1] == 5:
           loot[1][1] = 500
           stats[1][1] == 6
        if loot[1][1] == 1200 and stats[1][1] == 5:
           loot[1][1] = 700
           stats[1][1] == 6
           
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You leave the shop", largeText)
        TextSurf2, TextRect2 = text_objects("thanking the old man", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("->",350,500,100,50,BLUE,LIGHTBLUE,path5start)

        pygame.display.update()
        clock.tick(15)

def insideshop4():
    shopinside4 = True
 
    while shopinside4:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",30)
        if loot[1][1] == 0:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)   
        if loot[1][1] == 200:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)     
        if loot[1][1] == 500:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 700:
            TextSurf, TextRect = text_objects("You pay the old man $700 for the voodoo doll", largeText)
            TextSurf2, TextRect2 = text_objects("You get +2 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1000:
            TextSurf, TextRect = text_objects("You pay the old man $700 for the voodoo doll", largeText)
            TextSurf2, TextRect2 = text_objects("You get +2 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1200:
            TextSurf, TextRect = text_objects("You pay the old man $700 for the voodoo doll", largeText)
            TextSurf2, TextRect2 = text_objects("You get +2 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
            
        button("->",700,550,100,50,BLUE,LIGHTBLUE,insideshop4p)

        pygame.display.update()
        clock.tick(15)
        
def insideshop4p():
    shopinside4p = True
 
    while shopinside4p:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()

   
        if loot[1][1] == 700 and stats[0][1] == 1:
           loot[1][1] = 0
           stats[0][1] == 3
        if loot[1][1] == 1000 and stats[0][1] == 1:
           loot[1][1] = 300
           stats[0][1] == 3
        if loot[1][1] == 1200 and stats[0][1] == 1:
           loot[1][1] = 500
           stats[0][1] == 3
        if loot[1][1] == 700 and stats[0][1] == 2:
           loot[1][1] = 0
           stats[0][1] == 4
        if loot[1][1] == 1000 and stats[0][1] == 2:
           loot[1][1] = 300
           stats[0][1] == 4
        if loot[1][1] == 1200 and stats[0][1] == 2:
           loot[1][1] = 500
           stats[0][1] == 4
        if loot[1][1] == 700 and stats[0][1] == 3:
           loot[1][1] = 0
           stats[0][1] == 5
        if loot[1][1] == 1000 and stats[0][1] == 3:
           loot[1][1] = 300
           stats[0][1] == 5
        if loot[1][1] == 1200 and stats[0][1] == 3:
           loot[1][1] = 500
           stats[0][1] == 5
        if loot[1][1] == 700 and stats[0][1] == 4:
           loot[1][1] = 0
           stats[0][1] == 6
        if loot[1][1] == 1000 and stats[0][1] == 4:
           loot[1][1] = 300
           stats[0][1] == 6
        if loot[1][1] == 1200 and stats[0][1] == 4:
           loot[1][1] = 500
           stats[0][1] == 6
        if loot[1][1] == 700 and stats[0][1] == 5:
           loot[1][1] = 0
           stats[0][1] == 7
        if loot[1][1] == 1000 and stats[0][1] == 5:
           loot[1][1] = 300
           stats[0][1] == 7
        if loot[1][1] == 1200 and stats[0][1] == 5:
           loot[1][1] = 500
           stats[0][1] == 7

           
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You leave the shop", largeText)
        TextSurf2, TextRect2 = text_objects("thanking the old man", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("->",350,500,100,50,BLUE,LIGHTBLUE,path5start)

        pygame.display.update()
        clock.tick(15)

def insideshop5():
    shopinside5 = True
 
    while shopinside5:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        if loot[1][1] == 0:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave. ", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)   
        if loot[1][1] == 200:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)     
        if loot[1][1] == 500:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 700:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1000:
            TextSurf, TextRect = text_objects("You pay the old man $1000 for the scroll", largeText)
            TextSurf2, TextRect2 = text_objects("You get +3 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1200:
            TextSurf, TextRect = text_objects("You pay the old man $1000 for the scroll", largeText)
            TextSurf2, TextRect2 = text_objects("You get +3 Strength", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
            
        button("->",700,550,100,50,BLUE,LIGHTBLUE,insideshop5p)

        pygame.display.update()
        clock.tick(15)
        
def insideshop5p():
    shopinside5p = True
 
    while shopinside5p:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        
 
    

        if loot[1][1] == 1000 and stats[0][1] == 1:
           loot[1][1] = 0
           stats[0][1] = 4
        if loot[1][1] == 1200 and stats[0][1] == 1:
           loot[1][1] = 200
           stats[0][1] = 4
        if loot[1][1] == 1000 and stats[0][1] == 2:
           loot[1][1] = 0
           stats[0][1] = 5
        if loot[1][1] == 1200 and stats[0][1] == 2:
           loot[1][1] = 200
           stats[0][1] = 5
        if loot[1][1] == 1000 and stats[0][1] == 3:
           loot[1][1] = 0
           stats[0][1] = 6
        if loot[1][1] == 1200 and stats[0][1] == 3:
           loot[1][1] = 200
           stats[0][1] = 6
        if loot[1][1] == 1000 and stats[0][1] == 4:
           loot[1][1] = 0
           stats[0][1] = 7
        if loot[1][1] == 1200 and stats[0][1] == 4:
           loot[1][1] = 200
           stats[0][1] = 7
        if loot[1][1] == 1000 and stats[0][1] == 5:
           loot[1][1] = 0
           stats[0][1] = 8
        if loot[1][1] == 1200 and stats[0][1] == 5:
           loot[1][1] = 200
           stats[0][1] = 8
           
           
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You leave the shop", largeText)
        TextSurf2, TextRect2 = text_objects("thanking the old man", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("->",350,500,100,50,BLUE,LIGHTBLUE,path5start)

        pygame.display.update()
        clock.tick(15)

def insideshop6():
    shopinside6 = True
 
    while shopinside6:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        if loot[1][1] == 0:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave. ", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)   
        if loot[1][1] == 200:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2)     
        if loot[1][1] == 500:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 700:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1000:
            TextSurf, TextRect = text_objects("You realize you have no money", largeText)
            TextSurf2, TextRect2 = text_objects("And feel the urge to leave.", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
        if loot[1][1] == 1200:
            TextSurf, TextRect = text_objects("You pay the old man $1200 for the potion", largeText)
            TextSurf2, TextRect2 = text_objects("You get +3 Defense", largeText)
            TextRect.center = ((display_width/2),(30))
            TextRect2.center = ((display_width/2),(70))
            gameDisplay.blit(TextSurf, TextRect)
            gameDisplay.blit(TextSurf2, TextRect2) 
            
        button("->",700,550,100,50,BLUE,LIGHTBLUE,insideshop6p)

        pygame.display.update()
        clock.tick(15)
        
def insideshop6p():
    shopinside6p = True
 
    while shopinside6p:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
        

        if loot[1][1] == 1200 and stats[1][1] == 1:
           loot[1][1] = 0
           stats[1][1] = 4
        if loot[1][1] == 1200 and stats[1][1] == 2:
           loot[1][1] = 0
           stats[1][1] = 5
        if loot[1][1] == 1200 and stats[1][1] == 3:
           loot[1][1] = 0
           stats[1][1] = 6
        if loot[1][1] == 1200 and stats[1][1] == 4:
           loot[1][1] = 0
           stats[1][1] = 7
        if loot[1][1] == 1200 and stats[1][1] == 5:
           loot[1][1] = 0
           stats[1][1] = 8
           
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You leave the shop", largeText)
        TextSurf2, TextRect2 = text_objects("thanking the old man", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        button("->",350,500,100,50,BLUE,LIGHTBLUE,path5start)

        pygame.display.update()
        clock.tick(15)
        
def p4b2():
    path4button2 = True
 
    while path4button2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(SHOP1, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You continue your journey.", largeText)
        TextSurf2, TextRect2 = text_objects("You walk to the next street.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path5start)

        pygame.display.update()
        clock.tick(15)

def path5start():#PATH 5
    road5start = True
 
    while road5start:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY2, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("There are four streets you can go down.", largeText)
        TextSurf2, TextRect2 = text_objects("Choose one to progress:", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        button("STREET 1",150,400,100,50,RED,LIGHTRED,p5b1)
        button("STREET2",300,400,100,50,GREEN,LIGHTGREEN,p5b2)
        button("STREET 3",450,400,100,50,BLUE,LIGHTBLUE,p5b3)
        button("STREET 4",150,500,100,50,ORANGE,LIGHTORANGE,p5b4)


        pygame.display.update()
        clock.tick(15)

def p5b1():
    path5button1 = True
 
    while path5button1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
              
        loot[0][1] = 0      
        gameDisplay.blit(CAVE, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You run into the mafia.", largeText)
        TextSurf2, TextRect2 = text_objects("They kidnap you and never escape.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,results)

        pygame.display.update()
        clock.tick(15)

def p5b2():
    path5button2 = True
 
    while path5button2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()

        if loot[0][1] == 50:
            loot[0][1] = 40
        if loot[0][1] == 75:
            loot[0][1] = 65
        if loot[0][1] == 100:
            loot[0][1] = 90
        if loot[0][1] == 105:
            loot[0][1] = 95
        if loot[0][1] == 35:
            loot[0][1] = 10
        if loot[0][1] == 75:
            loot[0][1] = 50
        if loot[0][1] == 100:
            loot[0][1] = 75
        if loot[0][1] == 105:
            loot[0][1] = 80
            
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",28)
        TextSurf, TextRect = text_objects("A zombie comes out of the ground.", largeText)
        TextSurf2, TextRect2 = text_objects("It bites you and you lose 25 hp.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path6start)

        pygame.display.update()
        clock.tick(15)

def p5b3():
    path5button3 = True
 
    while path5button3:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                      
        gameDisplay.blit(MALL, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You walk through an empty mall and see ghosts.", largeText)
        TextSurf2, TextRect2 = text_objects("You run to the exit of the mall.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path6start)

        pygame.display.update()
        clock.tick(15)

def p5b4():
    path5button4 = True
 
    while path5button4:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          
        gameDisplay.blit(CITY2, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You find a orange portal and go through", largeText)
        TextSurf2, TextRect2 = text_objects("You come out of a blue portal.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,path6start)

        pygame.display.update()
        clock.tick(15)


def path6start():#PATH 6
    road6start = True
 
    while road6start:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY3, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You finally reach Stevon's office.", largeText)
        TextSurf2, TextRect2 = text_objects("Do you want to enter", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        
        
        button("Yes",150,400,100,50,RED,LIGHTRED,p6b1)
        button("No",300,400,100,50,GREEN,LIGHTGREEN,p6b2)


        pygame.display.update()
        clock.tick(15)
        
def p6b1():
    path6button1 = True
 
    while path6button1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY3, (0,0))
        gameDisplay.blit(HUD, (0,0))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You enter the office and find Steven.", largeText)
        TextSurf2, TextRect2 = text_objects("He looks at you and stands up.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,boss)

        pygame.display.update()
        clock.tick(15)

def p6b2():
    path6button2 = True
 
    while path6button2:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(CITY3, (0,0))
        gameDisplay.blit(HUD, (0,0))
        loot[0][1] = 0
        largeText = pygame.font.SysFont("comicsansms",28)
        TextSurf, TextRect = text_objects("You leave and Steven is never defeated.", largeText)
        TextSurf2, TextRect2 = text_objects("With your failure to defeat Steven you leave the town.", largeText)
        TextRect.center = ((display_width/2),(450))
        TextRect2.center = ((display_width/2),(500))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        TextSurf3, TextRect3 = text_objects(str(loot), largeText)
        TextRect3.center = ((500),(30))
        gameDisplay.blit(TextSurf3, TextRect3)
        TextSurf4, TextRect4 = text_objects(str(stats), largeText)
        TextRect4.center = ((500),(60))
        gameDisplay.blit(TextSurf4, TextRect4)
        
        
        button("->",700,550,100,50,BLUE,LIGHTBLUE,results)

        pygame.display.update()
        clock.tick(15)


def boss():
    bossfight = True
 
    while bossfight:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
              pygame.quit()
              quit()
                
        gameDisplay.blit(OFFICE1, (0,0))
        gameDisplay.blit(STEVEN, (400,300))
        largeText = pygame.font.SysFont("comicsansms",32)
        TextSurf, TextRect = text_objects("You have reached Steven.", largeText)
        TextSurf2, TextRect2 = text_objects("You may win or lose this fight.", largeText)
        TextSurf3, TextRect3 = text_objects("If your health is low you may lose", largeText)
        TextRect.center = ((display_width/2),(30))
        TextRect2.center = ((display_width/2),(70))
        TextRect3.center = ((display_width/2),(110))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(TextSurf2, TextRect2)
        gameDisplay.blit(TextSurf3, TextRect3)

        button("ATTACK",350,500,100,50,BLUE,LIGHTBLUE,results)

        pygame.display.update()
        clock.tick(15)
        
class Stats():
    def __init__ (self, Strength):
        self.Strength = Strength



    def __str__(self):
        rep = self.Strength 
        return rep
        
class Inventory():
    def __init__ (self, coin):
        self.coin = coin
        

    def __str__(self):
        rep = self.coin
        return rep
    
def main():
    welcome = Inventory("WELCOME TO")
    game = Stats("POGGERS THE GAME")
    game_intro(welcome, game)
    quit()


main()
