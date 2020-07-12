import pygame as pg

pg.init()
size = (500, 500)
buff = []
screen = pg.display.set_mode(size)
screen.fill((0, 0, 0))

surf = pg.Surface(screen.get_size())
buff.append(screen.copy())
side_coords = start_coords = [0, 0]

running = True
check = False

keys = []
flag = 1

while running:
    for event in pg.event.get():

        keys = pg.key.get_pressed()

        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            check = True
            start_coords = event.pos

        if event.type == pg.MOUSEBUTTONUP:
            buff.append(screen.copy())
            surf.blit(screen, (0, 0))
            check = False
            side_coords = 0, 0
            flag = 2

        if event.type == pg.MOUSEMOTION and check:
            side_coords = event.pos[0] - start_coords[0], event.pos[1] - start_coords[1]
            screen.fill(pg.Color('black'))

        if (keys[pg.K_LCTRL] or keys[pg.K_RCTRL]) and keys[pg.K_z] and flag:
            if len(buff) > 0:
                surf = buff[-1]
                buff.pop()
                if flag == 2 and len(buff) > 0:
                    surf = buff[-1]
                    buff.pop()
                elif flag == 2:
                    screen.fill((0, 0, 0))
                    surf = pg.Surface(screen.get_size())
            else:
                screen.fill((0, 0, 0))
                surf = pg.Surface(screen.get_size())
            flag = 0

        if (keys[pg.K_LCTRL] != 1 and keys[pg.K_RCTRL] != 1) or keys[pg.K_z] != 1 and flag < 2:
            if flag == 2:
                flag = 2
            else:
                flag = 1

        screen.blit(surf, (0, 0))
        if check:
            pg.draw.rect(screen, (255, 255, 255),
                         ((start_coords[0], start_coords[1]), (side_coords[0], side_coords[1])), 5)
        pg.display.flip()
