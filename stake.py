#stake (stupid snake)

import pygame, pyautogui,random
pygame.init()

name='Stake'
pyautogui.alert(title=name, text=f"Are you ready to play {name} (stupid snake)? Good!",button="START")

width=800
height=600
screen=pygame.display.set_mode((width,height))

x=width//2
y=height//2
radius=15

xchange=0
ychange=0

ax=random.randint(20,width-20)
ay=random.randint(20,height-20)

parts=[]

points=0

font=pygame.font.SysFont('comicsansms',40)

text=font.render(f"{points}",True,(255,0,204))
textRect=text.get_rect(topright=(width,-10))

pygame.display.set_caption(name)

while True:
    text=font.render(f"{points}",True,(255,0,204))
    textRect=text.get_rect(topright=(width,-10))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_j:
                xchange=-1
                ychange=0
            elif event.key==pygame.K_l:
                xchange=1
                ychange=0
            elif event.key==pygame.K_i:
                ychange=-1
                xchange=0
            elif event.key==pygame.K_k:
                ychange=1
                xchange=0
                
    pygame.time.wait(5)
            
                        
    screen.fill((0,0,0))
        
    x+=xchange
    y+=ychange
        
    vstawkl=pygame.draw.circle(screen,(177,186,132),(x,y),radius)
    palappl=pygame.draw.circle(screen,(115,32,199),(ax,ay),10)
    
    for i in parts:
        pygame.draw.circle(screen,(163,135,82),i,radius-8)
        
    screen.blit(text,textRect)
        
    pygame.display.update()
        
    if vstawkl.colliderect(palappl):
        ax=random.randint(20,width-20)
        ay=random.randint(20,height-20)
        points+=1
        parts.append((x+30,y+30))
        
    if x>=width:
        x=0
    elif x<=0:
        x=width
    
    if y>=height:
        y=0
    elif y<=0:
        y=height
                     
    for i in parts:
        if vstawkl.colliderect(pygame.draw.circle(screen,(177,186,132),i,radius-3)):
            print(points)
            points=0
            parts=[]
            ax=random.randint(20,width-20)
            ay=random.randint(20,height-20)
            x=width//2
            y=height//2
            xchange=ychange=0
        