import math
import pygame as pg


pg.init()
size = width, height = 800, 600
screen = pg.display.set_mode(size)

color = pg.color.Color('blue')
hsv = color.hsva


points = 360
radius = min(width, height) // 2.5

running = True
pause = False
multiply = 0
timeout = 0
was_pushed = False

while running:
    if not pause:
        multiply += 0.001
        screen.fill((0, 0, 0))
        color.hsva = ((multiply * 10 + 240) % 360, hsv[1], hsv[2], hsv[3])
        for i in range(0, points, 2):
            x1 = int(math.cos(math.radians(i)) * radius) + width // 2
            y1 = int(math.sin(math.radians(i)) * radius) + height // 2

            x2 = int(math.cos(math.radians(i * multiply)) * radius) + width // 2
            y2 = int(math.sin(math.radians(i * multiply)) * radius) + height // 2
            pg.draw.line(screen, color, (x1, y1), (x2, y2))
    for event in pg.event.get():
        keys = pg.key.get_pressed()
        if event.type == pg.QUIT:
            running = False

        if keys[pg.K_SPACE] and pg.time.get_ticks() - timeout < 180:
            multiply = 0
            timeout = 0
            pause = False

        elif keys[pg.K_SPACE]:
            pause = not pause
            timeout = pg.time.get_ticks()

    pg.display.flip()

pg.quit()
