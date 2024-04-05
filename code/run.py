import pygame as pg
from plot import *
from physics import *
from mathe import *
import sys


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

def mouse_pos(screen):
    pos =  pg.mouse.get_pos()
    my_font = pg.font.SysFont('Arial', 30)
    time_text = my_font.render(str(pos) , False, black)
    screen.blit(time_text,np.array([400,0]))

def main():
    pg.init()
    screen = pg.display.set_mode(screen_dim)
    screen.fill(color=white)
    gen = rainbow_circles(screen)
    ent = Entity()
    timer_on = False
    mouse_pos_on = True



    while True:
        screen.fill(white)
        entries()
        if timer_on:
            timer(screen)
        if mouse_pos_on:
            mouse_pos(screen)

        # line(screen)
        # clock(screen)
        # reverse_clock(screen)
        # circle(screen)
        # triangle(screen)
        # square(screen)
        # alpha_circle(screen)
        # next(gen)
        # next(gen)
        # print(matrix)

        # ent.update()
        # position = ent.get_position()
        # point(screen,position)
        
        points = [[100,150],[150,100],[150,150]]

        points2 = [[100,100],
              [300,130],
              [460,330],
              [500,500],
              [200,400],
              [100,300]]

        poligon(screen, points)

        points3 = rotate_polygon(points, 1,[500,500])

        print(points3)

        poligon(screen, points3)
        

        pg.display.flip()

if __name__ == '__main__':
    main()
    