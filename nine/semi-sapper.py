import pygame as pg
import random as rand

class Board:
    def __init__(self, w, h, count_cells_in_row, count_bombs):
        self.width = w
        self.height = h
        self.cell_size = w // count_cells_in_row
        self.count_cells = (self.height // self.cell_size, count_cells_in_row)
        self.count_bombs = count_bombs
        self.is_bomb = (False, True)
        self.cells = []
        for i in range(self.count_cells[0]):
            self.cells.append([])
            for j in range(self.count_cells[1]):
                self.cells[i].append(self.is_bomb[0])
        self.fillCells()

    def render(self, screen):
        for i in range(self.count_cells[0]):
            for j in range(self.count_cells[1]):
                if self.cells[i][j] == self.is_bomb[1]:
                    pg.draw.rect(screen, pg.color.Color('firebrick'), (self.cell_size * j, self.cell_size * i, self.
                                                                       cell_size * (j + 1), self.cell_size * (i + 1)))
                else:
                    pg.draw.rect(screen, pg.color.Color('black'),
                                 (self.cell_size * j, self.cell_size * i, self.cell_size
                                  * (j + 1), self.cell_size * (i + 1)))
                pg.draw.rect(screen, pg.color.Color('white'), (self.cell_size * j, self.cell_size * i,
                                                               self.cell_size * (j + 1),
                                                               self.cell_size * (i + 1)), 1)

    def fillCells(self):
        for i in range(self.count_bombs):
            x = rand.randint(0, self.count_cells[1] - 1)
            y = rand.randint(0, self.count_cells[0] - 1)
            while self.cells[y][x] == self.is_bomb[1]:
                x = rand.randint(0, self.count_cells[1] - 1)
                y = rand.randint(0, self.count_cells[0] - 1)
            self.cells[y][x] = True

    def click(self, screen, pos):
        coord_cell = (pos[0] // self.cell_size, pos[1] // self.cell_size)
        if self.cells[coord_cell[1]][coord_cell[0]] == self.is_bomb[0]:
            value = self.checkBombsAround(coord_cell)
            text = pg.font.Font(None, self.cell_size // 2).render(str(value), 255, (255, 255, 255))
            screen.blit(text, (coord_cell[0] * self.cell_size + self.cell_size // 2, coord_cell[1] * self.cell_size + self.cell_size // 2))

    def checkBombsAround(self, coords):
        dy = [1, 1, 1, 0, 0, -1, -1, -1]
        dx = [1, 0, -1, 1, -1, 1, 0, -1]
        value = int()
        for i in range(8):
            if 0 <= coords[1] + dy[i] < self.count_cells[0] and 0 <= coords[0] + dx[i] < self.count_cells[1]:
                value += 1 if self.cells[coords[1] + dy[i]][coords[0] + dx[i]] == self.is_bomb[1] else 0
        return value


pg.init()

size = width, height = 800, 600
screen = pg.display.set_mode(size)

cells_count = 20
bombs_count = 30

board = Board(width, height, cells_count, bombs_count)
screen.fill((0, 0, 0))
board.render(screen)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.MOUSEBUTTONDOWN:
            board.click(screen, event.pos)
    pg.display.flip()

pg.quit()
