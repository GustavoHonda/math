import pygame as pg
import sys
import numpy as np


screen_dim = np.array([1000,1000])
screen_certer = np.array([500,500])
black = np.array([0,0,0])
white = np.array([255,255,255])
red = np.array([255,0,0])
green = np.array([0,255,0])
blue = np.array([0,0,255])
dark_green = np.array([100,150,50])


Red    = np.array([255,0,0]);
Orange = np.array([255,127,0]);
Yellow = np.array([255,255,0]);
Green  = np.array([0,255,0]);
Blue   = np.array([0,0,255]);
Indigo = np.array([75,0,130]);
Violet = np.array([148,0,211]);
Trunk  = np.array([165,42,42]);
Grass  = np.array([80,250,80]);
Leaf   = np.array([80,150,80]);
rainbow = [Red,Orange,Yellow,Green,Blue, Indigo,Violet,Trunk,Grass,Leaf]



def quit():
    sys.exit()

key_map = {
    pg.K_q:quit
    }

def entries():
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key in key_map:
                func = key_map[event.key]
                func()
            else:
                print("invalid")

def timer(screen):
    i = pg.time.get_ticks()
    my_font = pg.font.SysFont('Arial', 30)
    time_text = my_font.render(str(i) , False, black)
    screen.blit(time_text,np.array([0,0]))

def line(screen):
    i = 100
    j = 200
    line_start = screen_certer  
    line_end =  screen_certer+ [i,j]
    pg.draw.line(screen,black,line_start,line_end)

def clock(screen):
    t = pg.time.get_ticks()
    i = np.cos(t/100)* 500
    j = np.sin(t/100)* 500
    line_start = screen_certer  
    line_end =  screen_certer+ [i,j]
    pg.draw.line(screen,blue,line_start,line_end)

def reverse_clock(screen):
    t = pg.time.get_ticks()
    i = np.sin(t/100)* 500
    j = np.cos(t/100)* 500
    line_start = screen_certer  
    line_end =  screen_certer+ [i,j]
    pg.draw.line(screen,red,line_start,line_end)


def alpha_circle(screen):
    r = 200
    target_rect = pg.Rect(screen_certer, (0, 0)).inflate((r * 2, r * 2))
    surf = pg.Surface(target_rect.size, pg.SRCALPHA)
    surf.set_alpha(80)
    pg.draw.circle(surf, dark_green, (r, r), r)
    screen.blit(surf, target_rect)

def circle(screen):
    pg.draw.circle(screen,center=screen_certer,color=green,radius=100)

def rainbow_circles(screen):
    i=0
    while True:
        i = i % len(rainbow)
        pg.draw.circle(screen,center=screen_certer + [20*i,0],color=rainbow[i],radius=10)
        i +=1
        yield None
        

def main():
    pg.init()
    screen = pg.display.set_mode(screen_dim)
    screen.fill(color=white)
    gen = rainbow_circles(screen)
    while True:
        # screen.fill(white)
        entries()
        timer(screen)
        # line(screen)
        # clock(screen)
        # reverse_clock(screen)
        # circle(screen)
        # alpha_circle(screen)
        # next(gen)
        next(gen)
        pg.display.flip()

if __name__ == '__main__':
    main()