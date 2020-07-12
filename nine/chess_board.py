import pygame as pg


width, num = [int(i) for i in input().split()]
cell_width = width // num
screen = pg.display.set_mode((width, width))
pg.init()


def draw():
    screen.fill((255, 255, 255))
    black = pg.color.Color('Black')
    for i in range(num):
        start = (0, 1)
        for j in range(start[i % 2], num, 2):
            pg.draw.rect(screen, black, (cell_width * j, cell_width * i, cell_width, cell_width))


draw()

pg.display.flip()
while pg.event.wait().type != pg.QUIT:
    pass

pg.quit()
