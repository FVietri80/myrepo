##### Paddle
import pygame as py


class Paddle :
    VEL = 5
    def __init__(self,x,y,widht,height,color):
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.color = color


    def draw(self,win):
        py.draw.rect(win,self.color,(self.x,self.y,self.width,self.height))