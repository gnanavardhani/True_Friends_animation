import pygame
from math import pi
import random 

#initialize colours 
CLOUD=(96,96,96)
TRUNK=(102,20,0)
SKIN = (229,154,122)
BLACK =(0,0,0)
BEAR = (100,40,40)
DARK_BEAR=(60,20,20)
BEAR_EARS = (60,40,40)
SUN =(255,128,0)
SKY = (200,200,200)
GRASS = (100,250,100)
RIVER = (1,170,255)

'''functions
def human(flag,x,y,colour1,colour2,r)
def dead_man(x,y,colour1,colour2,r)
def bear(x,y)
def draw_cloud(x,y)
def right_side_man(x,y,colour1,colour2,flag)
def climbing_man(x,y,colour1,colour2)
def left_side_man(x,y,colour1,colour2,flag)
def draw_tree(x,y,w)
def draw_clouds()
def text_to_screen(screen, text, x, y,size,color):
def set_background()
'''

def human(flag,x,y,colour1,colour2,r):

    pygame.draw.circle(screen, SKIN, [x, y], r) #face
    
    pygame.draw.circle(screen, SKIN, [x-r+2, y-1],4) #ears 
    pygame.draw.circle(screen, SKIN, [x+r-2, y-1], 4) 
    if flag==0:
        pygame.draw.circle(screen, BLACK, [x-r+13, y-1],4) #eyes
        pygame.draw.circle(screen, BLACK, [x+r-13, y-1], 4)
        pygame.draw.line(screen, BLACK, (x-r+10,y+10),(x+r-10,y+10),3)

    pygame.draw.rect(screen, SKIN, [x-4,y+r-1,8,3])  #neck
    pygame.draw.rect(screen, colour1, [x-25, y+r+2,50,30])  #body
    pygame.draw.line(screen, BLACK, (x-25,y+r+32),(x+25,y+r+32),3)
    pygame.draw.rect(screen, colour2, [x-25,y+r+32,50,30])  #body
    pygame.draw.line(screen, BLACK, (x,y+r+32),(x,y+r+62))

    pygame.draw.circle(screen, BLACK, [x-10, y+r+102],4) #foot 
    pygame.draw.circle(screen,BLACK, [x+10, y+r+102], 4)
    pygame.draw.rect(screen, SKIN, [x-15, y+r+62,10 ,40 ])  #left leg
    pygame.draw.rect(screen, SKIN, [x+5, y+r+62,10 , 40])  #right leg
    
    pygame.draw.rect(screen, SKIN, [x-30, y+r+7,5,45])   #left hand
    pygame.draw.rect(screen, SKIN, [x+26, y+r+7, 5,45])  #right hand
    pygame.draw.circle(screen, SKIN , [x-28, y+r+52], 4) #left palm
    pygame.draw.circle(screen, SKIN , [x+29, y+r+52], 4) #right palm

    pygame.draw.circle(screen, colour2, [x-26, y+r+7], 4)   #shoulders
    pygame.draw.circle(screen, colour2, [x+26, y+r+7], 4)

def dead_man(x,y,colour1,colour2,r):
    
    pygame.draw.circle(screen, SKIN, [x, y], r) #face
    
    pygame.draw.circle(screen, SKIN, [x-1, y-r+2],4) #ears 
    pygame.draw.circle(screen, SKIN, [x-1, y+r-2], 4)

    pygame.draw.circle(screen, BLACK, [x-2, y-5], 2)#eyes
    pygame.draw.circle(screen, BLACK, [x-2, y+5], 2)

    pygame.draw.circle(screen, (225,150,120), [x+2, y], 1)
    pygame.draw.line(screen, BLACK, (x+6,y-3),(x+6,y+3))

    pygame.draw.rect(screen, SKIN, [x+r-1,y-4,8,3])  #neck

    pygame.draw.rect(screen, colour1, [x+r-1, y-25,30,50])  #body
    pygame.draw.line(screen, BLACK, (x+r+30,y-25),(x+r+30,y+25),3)
    pygame.draw.rect(screen, colour2, [x+r+32,y-25,30,50])  #body
    pygame.draw.line(screen, BLACK, (x+r+32,y),(x+r+62,y))

    pygame.draw.circle(screen, BLACK, [x+r+102, y-10],4) #foot 
    pygame.draw.circle(screen,BLACK, [x+102+r, y+10], 4)
    pygame.draw.rect(screen, SKIN, [x+r+62, y-15,40 ,10 ])  #left leg
    pygame.draw.rect(screen, SKIN, [x+r+62, y+5,40 , 10])  #right leg
    
    pygame.draw.rect(screen, SKIN, [x+r+7, y-30,45,5])   #left hand
    pygame.draw.rect(screen, SKIN, [x+r+7, y+26, 45,5])  #right hand
    pygame.draw.circle(screen, SKIN , [x+r+52, y-28], 4) #left palm
    pygame.draw.circle(screen, SKIN , [x+r+52, y+29], 4) #right palm

    pygame.draw.circle(screen, colour2, [x+r+7, y-26], 4)   #shoulders
    pygame.draw.circle(screen, colour2, [x+r+7, y+26], 4)


def bear(x,y):
    pygame.draw.circle(screen, BEAR, [x, y], 40)  #back body
    pygame.draw.ellipse(screen, BEAR, (x-7,y+15,25,50)) #rear leg R
    pygame.draw.ellipse(screen, BEAR, (x-12,y+45,25,20)) #rear foot R

    pygame.draw.rect(screen,DARK_BEAR, [x-25, y+30,15 ,15 ])  #rear leg L
    pygame.draw.ellipse(screen,DARK_BEAR, (x-30,y+40,20,12))  #rear foot L

    pygame.draw.circle(screen, BEAR, [x-40, y], 30)
    pygame.draw.polygon(screen, BEAR, [[x-40,y-30], [x, y-40], [x,y]])
    pygame.draw.ellipse(screen, BEAR, (x-50,y+13,22,45)) #front leg R
    pygame.draw.ellipse(screen, BEAR, (x-55,y+43,22,15)) #front foot R

    pygame.draw.polygon(screen,DARK_BEAR, [[x-50, y+28], [x-60, 18+y], [x-55, 43+y]]) 
    pygame.draw.polygon(screen,DARK_BEAR, [[x-63, y+43], [x-60, 18+y], [x-55, 43+y]])
    pygame.draw.ellipse(screen,DARK_BEAR, (x-70,y+40,15,10))

    pygame.draw.circle(screen, BEAR_EARS, [x-100+18, y-15], 8)
    pygame.draw.circle(screen, BEAR_EARS, [x-55, y-12], 8)
    pygame.draw.circle(screen, BEAR, [x-70, y], 20)
    pygame.draw.ellipse(screen, (210,210,210), (x-100,y+5,25,13))
    pygame.draw.circle(screen, BLACK, [x-100+5, y+13], 5)

    pygame.draw.ellipse(screen, BLACK, (x-70,y,7,3))
    pygame.draw.ellipse(screen, BLACK, (x-82,y-5,7,3))

def right_side_man(x,y,colour1,colour2,flag):

    pygame.draw.ellipse(screen,SKIN, (x,y,30,40))
    pygame.draw.ellipse(screen,BLACK, (x+15,y+10,5,8))   
    
    pygame.draw.polygon(screen, (225,150,120) , [[35+x, 18+y], [25+x, 15+y], [25+x, 25+y]])
    pygame.draw.line(screen, BLACK, (x+20,y+28),(x+26,y+29),3)
    pygame.draw.rect(screen, SKIN, [x+10,y+40,8,3])

    pygame.draw.rect(screen, colour1, [x-4,y+43,38,30])
    
    if flag==1:
        pygame.draw.rect(screen, SKIN, [x+15,y+45,30,5])
        pygame.draw.circle(screen, SKIN , [x+45, y+48], 4)
    
    else:
        pygame.draw.rect(screen, SKIN, [x+15,y+45,5,30])
        pygame.draw.circle(screen, SKIN , [x+15, y+78], 4)

    pygame.draw.circle(screen,colour2, [x+15, y+47], 4)   
    pygame.draw.line(screen, BLACK, (x-4,y+73),(x+34,y+73),2)
    pygame.draw.rect(screen, colour2, [x-4,y+73,38,30])

    pygame.draw.circle(screen, BLACK, [x+9, y+143],6) #foot 
    pygame.draw.circle(screen,BLACK, [x+19, y+133], 6)   

    pygame.draw.rect(screen, SKIN, [x+2,y+103,14,40])
    pygame.draw.rect(screen, SKIN, [x+12,y+103,14,30])
    pygame.draw.line(screen, BLACK, (x+16,y+103),(x+16,y+143),2)

def climbing_man(x,y,colour1,colour2):
    
    pygame.draw.ellipse(screen,SKIN, (x,y,30,40))
    pygame.draw.ellipse(screen,BLACK, (x+15,y+10,5,8))   
    
    pygame.draw.polygon(screen, (225,150,120) , [[35+x, 18+y], [25+x, 15+y], [25+x, 25+y]])
    pygame.draw.line(screen, BLACK, (x+20,y+28),(x+26,y+29),3)
    pygame.draw.rect(screen, SKIN, [x+10,y+40,8,3])

    pygame.draw.circle(screen,colour2, [x+15, y+88], 20)#bottom
    pygame.draw.rect(screen, colour2, [x+15,y+73,38,31])

    pygame.draw.rect(screen, colour1, [x-4,y+43,38,30])
    pygame.draw.rect(screen, SKIN, [x+15,y+45,30,5])
    pygame.draw.circle(screen, SKIN , [x+45, y+48], 4)
    pygame.draw.circle(screen,colour2, [x+15, y+47], 4)   
    pygame.draw.line(screen, BLACK, (x-4,y+73),(x+34,y+73),3)
    
    pygame.draw.circle(screen, BLACK, [x+90, y+87],8) #foot 
    pygame.draw.rect(screen, SKIN, [x+53,y+80,40,14])

def left_side_man(x,y,colour1,colour2,flag):
    
    pygame.draw.ellipse(screen,SKIN, (x,y,30,40))
    pygame.draw.ellipse(screen,BLACK, (x+15,y+10,5,8))   
    pygame.draw.ellipse(screen,BLACK, (x+8,y+8,4,6))   

    pygame.draw.polygon(screen, (225,150,120) , [[x-5, 18+y], [x+5, 15+y], [x+5, 25+y]])
    pygame.draw.line(screen, BLACK, (x+4,y+28),(x+20,y+29),3)
    pygame.draw.rect(screen, SKIN, [x+10,y+40,8,3])

    pygame.draw.rect(screen, colour1, [x-4,y+43,38,30])
    
    if flag==1:
        pygame.draw.rect(screen, SKIN, [x-20,y+45,35,5])
        pygame.draw.circle(screen, SKIN , [x-20, y+48], 4)
    
    else:
        pygame.draw.rect(screen, SKIN, [x+15,y+45,5,35])
        pygame.draw.circle(screen, SKIN , [x+15, y+88], 4)

    pygame.draw.circle(screen,colour2, [x+13, y+47], 4)   
    pygame.draw.line(screen, BLACK, (x-4,y+73),(x+34,y+73),2)
    pygame.draw.rect(screen, colour2, [x-4,y+73,38,30])

    pygame.draw.circle(screen, BLACK, [x+9, y+143],6) #foot 
    pygame.draw.circle(screen,BLACK, [x+19, y+133], 6)   

    pygame.draw.rect(screen, SKIN, [x+2,y+103,14,40])
    pygame.draw.rect(screen, SKIN, [x+12,y+103,14,30])
    pygame.draw.line(screen, BLACK, (x+16,y+103),(x+16,y+143),2)

def draw_tree(x,y,w):
    
    pygame.draw.rect(screen, TRUNK, [160+x, 200+y, 30+w, 100])
    pygame.draw.polygon(screen,(0,51+(x/10),25) , [[250+x, 200+y], [175+x, 50+y], [100+x, 200+y]])
    pygame.draw.polygon(screen, (0,51+(x/10),25), [[240+x, 150+y], [175+x, 30+y], [110+x, 150+y]])

def draw_cloud(x,y):
    
    pygame.draw.circle(screen, CLOUD, [20+x, 50+y], 20)
    pygame.draw.circle(screen, CLOUD, [50+x, 50+y], 30)
    pygame.draw.circle(screen, CLOUD, [80+x, 50+y], 20)

def draw_clouds():
    
    draw_cloud(30,0)
    draw_cloud(50,10)
    draw_cloud(10,0)
    
    draw_cloud(300,20)

    draw_cloud(350,40)
    draw_cloud(350,50)

    draw_cloud(400,40)
    draw_cloud(400,50)
    draw_cloud(400,20)

    draw_cloud(450,50)
    draw_cloud(450,60)

    draw_cloud(500,50)
    draw_cloud(500,20)

    draw_cloud(600,30)


def text_to_screen(screen, text, x, y,size,color):
    
    try:

        text = str(text)
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except Exception as e:
        print('Font Error, saw it coming')
        raise e

def set_background():
    
    pygame.draw.rect(screen,SKY, [0, 0, 700, 250])
    pygame.draw.rect(screen,RIVER, [0, 250, 700, 250])
    pygame.draw.rect(screen,GRASS, [0, 250, 400, 250])
    pygame.draw.circle(screen,GRASS, [300, 500],300)
    pygame.draw.circle(screen, SUN , [500, 60], 50)
    
    draw_clouds()
    
    for i in range(4):    
        draw_tree(50+i*70,i*70,5*i)
        draw_tree(-i*50,i*50,5*i)
        draw_tree(200+i*50,i*50,5*i) 
    
    text_to_screen(screen,"True Friends",505,145,30,SUN)

pygame.init()

window_width=700
window_height=500

animation_increment=10
clock_tick_rate=60

#Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

#Set title to the window
pygame.display.set_caption("True Friends")
dead=False

clock = pygame.time.Clock()
#set the back ground colors

while(dead == False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    #add background music
    #initialize mixer
    pygame.mixer.init()
    
    #load file
    pygame.mixer.music.load('/home/vardhani/Downloads/True Friends  English Animated Moral Story For Kids  KidsOne.mp3')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    
    #play music
    pygame.mixer.music.play()

    #scene 1
    set_background()
    pygame.display.update()
    pygame.time.wait(240)
    
    #scene 2
    for i in range(150):
        set_background()
        human(1,150,500-i,(255,0,0),(0,0,255),20)
        human(1,250,520-i,(0,255,255),(255,0,255),18)  
    
        if(i>=80):
            text_to_screen(screen,"Yah..cool lets chill",200,365,15,SUN)  
        else:
            text_to_screen(screen,"Ahh..Nice",170,445-i,15,SUN)
        
        pygame.display.update()
        if(i==149):
            pygame.time.wait(120)
        else:
            pygame.time.wait(60)

    #scene 3
    set_background()
    human(1,150,350,(255,0,0),(0,0,255),20)
    human(1,250,370,(0,255,255),(255,0,255),18)
    pygame.display.update()
    pygame.time.wait(270) 
    
    #scene 4
    set_background()
    human(1,150,350,(255,0,0),(0,0,255),20)
    human(1,250,370,(0,255,255),(255,0,255),18)
    text_to_screen(screen,"ohh..No What to do?",70,475,15,SUN)
    bear(350,280)
    
    pygame.display.update()
    pygame.time.wait(270)
    
    #scene 5
    #bear coming near
    for i in range(40):
        set_background()
        bear(300,280+i)
        text_to_screen(screen,"ohh..No What to do?",70,475,15,SUN)
        human(1,150,350,(255,0,0),(0,0,255),20)
        human(1,250,370,(0,255,255),(255,0,255),18)
        pygame.display.update()
        pygame.time.wait(180)

    #scene 6
    xi=250
    yi=370
    while(xi>=250 and xi<380):
        xi=xi+10
        set_background()
        bear(300,330)
        
        text_to_screen(screen,"?? ",170,345,20,SUN)
        
        human(1,xi,yi,(0,255,255),(255,0,255),20)
        human(1,150,350,(255,0,0),(0,0,255),18)
        pygame.display.update()
        pygame.time.wait(240)

    while(yi>340):
        yi=yi-10
        set_background()
        bear(300,330)
        
        human(1,xi,yi,(0,255,255),(255,0,255),20)
        human(1,150,350,(255,0,0),(0,0,255),18)
        pygame.display.update()
        pygame.time.wait(180)

    while(yi>250):
        if(yi!=250):
            yi=yi-10
            set_background()
            bear(300,330)
            
            climbing_man(xi+20,yi,(0,255,255),(255,0,255))
            human(1,150,350,(255,0,0),(0,0,255),18)
            
            pygame.display.update()
            if(yi==250):
                pygame.time.wait(200)
            else:
                pygame.time.wait(100)
    
    #scene 7
    set_background()
    bear(300,330)
    
    right_side_man(150,350,(255,0,0),(0,0,255),0)
    text_to_screen(screen,"!!! ",170,345,20,SUN)
    climbing_man(380+20,250,(0,255,255),(255,0,255))
    pygame.display.update()

    pygame.time.wait(1500)
    pygame.time.wait(1200)
    pygame.time.wait(1200)
    pygame.time.wait(1200)
    pygame.time.wait(1200)

    for i in range(35):
        set_background()
        
        dead_man(150,450,(255,0,0),(0,0,255),18)
        climbing_man(380+20,250,(0,255,255),(255,0,255))
        
        bear(300-i,330+i)
        pygame.display.update()
        pygame.time.wait(60)

    set_background()
    dead_man(150,450,(255,0,0),(0,0,255),18)
    climbing_man(380+20,250,(0,255,255),(255,0,255))
    bear(250,365)
    text_to_screen(screen,"sniff..sniff..",90,405,15,SUN)
    
    pygame.display.update()
    pygame.time.wait(1500)
    pygame.time.wait(1200)
    pygame.time.wait(1500)
    pygame.time.wait(1500)

    for i in range(250):
        set_background()
        
        dead_man(150,450,(255,0,0),(0,0,255),18)
        climbing_man(380+20,250,(0,255,255),(255,0,255))
        
        bear(250-i,365)
        pygame.display.update()
        pygame.time.wait(10)
  
    #climax
    xi=400
    yi=240
    while(yi>=240 and yi<370):
        if(yi!=370):
            yi=yi+10
            set_background()
            
            climbing_man(xi,yi,(0,255,255),(255,0,255))
            dead_man(150,450,(255,0,0),(0,0,255),18)
            
            pygame.display.update()
            pygame.time.wait(30)

    while(xi<=400 and xi>250):
        if(xi!=250):
            xi=xi-10
            set_background()
            
            human(1,xi,yi,(0,255,255),(255,0,255),20)
            human(1,150,350,(255,0,0),(0,0,255),18)
            
            pygame.display.update()
            pygame.time.wait(30)

    set_background()
    right_side_man(150,350,(255,0,0),(0,0,255),0)
    left_side_man(250,370,(0,255,255),(255,0,255),0)
    text_to_screen(screen,"What did it whisper ?",155,335,15,SUN)
    pygame.display.update()
    pygame.time.wait(900)
    pygame.time.wait(1500)

    set_background()
    right_side_man(150,350,(255,0,0),(0,0,255),0)
    left_side_man(250,370,(0,255,255),(255,0,255),0)
    text_to_screen(screen,"asked me to keep ",170,305,15,SUN)
    text_to_screen(screen,"away from frds",170,323,15,SUN)
    text_to_screen(screen," like you",175,341,15,SUN)
    pygame.display.update()    
    pygame.time.wait(1500)

    pygame.time.wait(1500)
    pygame.time.wait(1200)

    for i in range(200):
        set_background()
        human(0,150,350+i,(255,0,0),(0,0,255),18)    
        left_side_man(250,370,(0,255,255),(255,0,255),1)
        
        text_to_screen(screen,"hmm..",80,335+i,15,SUN)
        pygame.display.update()
        pygame.time.wait(20)
    
    set_background()
    text_to_screen(screen,"THE END",105,405,50,SUN)
    pygame.display.update()
    pygame.time.wait(1800)





