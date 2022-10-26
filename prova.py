##### Brick Breaker

import pygame as py
import Paddle

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15 # diverse prove

WIDTH,HEIGHT = 800,600

FPS = 60

win = py.display.set_mode((WIDTH,HEIGHT))

py.display.set_caption("Brick Breaker")

#########Oggetti
class Paddle :
    VEL = 5
    def __init__(self,x,y,widht,height,color):
        self.x = x
        self.y = y
        self.width = widht
        self.height = height
        self.color = color


    def draw(self,win):
        py.draw.rect(win,self.color,(self.x,self.y,self.width,self.height)) ### diverse prove con height

    def move(self,direction = 1):
        self.x = self.x + self.VEL*direction
paddle = Paddle(WIDTH/2-PADDLE_WIDTH,HEIGHT-PADDLE_HEIGHT-5,PADDLE_WIDTH,PADDLE_HEIGHT,"black")


def draw(win,paddle):
    win.fill("white")
    paddle.draw(win)
    py.display.update()



def main() :
    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        #####  aggiungo movimento paddle
        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            paddle.move(-1) # va a sx
            #pass ###  per provare
        if keys[py.K_RIGHT]:
            paddle.move(1)  # va a dx
            #pass ###  per provare
        draw(win,paddle)
    py.quit()
    quit()

if __name__ == "__main__":
    main()


