##### Brick Breaker

import pygame as py

WIDTH,HEIGHT = 800,600

FPS = 60

win = py.display.set_mode((WIDTH,HEIGHT))

py.display.set_captation("Brick Braker")

def draw(win):
    win.fill("white")
    py.display.update()



def main() :
    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type = py.QUIT:
                run = False
                break
        draw(win)
    py.quit()
    quint()

if __name__ = "__main__":
    main()