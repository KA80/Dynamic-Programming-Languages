import pygame as pg


sq_pos = [0, 0]
sq_size = (100, 100)
sq_color = pg.Color('Red')

screen_size = (300, 300)
screen = pg.display.set_mode(screen_size)
pg.init()

running = True
was_clicked_on_rect = False
prev_mouse_pos = ()

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            prev_mouse_pos = mouse_pos = pg.mouse.get_pos()
            if sq_pos[0] <= mouse_pos[0] <= sq_pos[0] + sq_size[0] and\
                    sq_pos[1] <= mouse_pos[1] <= sq_pos[1] + sq_size[1]:
                was_clicked_on_rect = True
            else:
                was_clicked_on_rect = False

        if was_clicked_on_rect and event.type == pg.MOUSEMOTION and event.buttons == (1, 0, 0):
            mouse_pos = pg.mouse.get_pos()
            sq_pos[0] = sq_pos[0] + mouse_pos[0] - prev_mouse_pos[0]
            sq_pos[1] = sq_pos[1] + mouse_pos[1] - prev_mouse_pos[1]
            prev_mouse_pos = mouse_pos

    screen.fill((0, 0, 0))
    pg.draw.rect(screen, sq_color, (sq_pos, sq_size))
    pg.display.flip()

pg.quit()
