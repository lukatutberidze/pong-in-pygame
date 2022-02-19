import pygame
WHITE=(255,255,255)

class Bot:
    COLOR=WHITE
    VEL=4
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def draw(self,win):
        pygame.draw.rect(win,self.COLOR,(self.x,self.y,self.width,self.height))
    
    def move(self,ball_y):
        if ball_y>self.y+self.height:
            self.y+=self.VEL
        elif ball_y<self.y:
            self.y-=self.VEL