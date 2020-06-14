import copy

WHITE = 1
BLACK = 2
is_incorrect_coords = False
is_cast_not_done = False
is_begin_of_game = True
is_check = False
is_mate = False
is_stalemate = False
col_list = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}


def print_board(board):  # Распечатать доску в текстовом виде
    print('      +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row + 1, end='   ')
        for col in range(8):
            print('|', board.cell(row, col), end=' ')
        print('|')
        print('      +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(chr(col + 65), end='    ')
    print()


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def parse_coords(coords):
    if len(coords) != 5:
        return -1, -1, -1, -1
    if coords[2] != " ":
        return -1, -1, -1, -1
    try:
        col, row, col1, row1 = col_list[coords[0].upper()], int(coords[1]), col_list[coords[3].upper()], int(coords[4])
    except ValueError and KeyError:
        return -1, -1, -1, -1
    return row - 1, col - 1, row1 - 1, col1 - 1,


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


def vertical_horizontal_check(board, row, col, row1, col1):  # проверяет наличие фигур по вертикали и горизонтали;
    # возвращает True, если есть
    step = 1 if (row1 >= row) else -1
    for r in range(row + step, row1, step):
        # Если на пути по горизонтали есть фигура
        if not (board.get_piece(r, col) is None):
            return True

    step = 1 if (col1 >= col) else -1
    for c in range(col + step, col1, step):
        # Если на пути по вертикали есть фигура
        if not (board.get_piece(row, c) is None):
            return True
    return False


def diagonal_check(board, row, col, row1, col1):  # проверяет наличие фигур по диагонали; возвращает True, если есть
    for i in range(1, abs(row - row1)):
        if not board.field[row + i * int((row1 - row) / abs(row1 - row))][col + i * int((col1 - col) / abs(col1 - col))] \
               is None:
            return True
    return False


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        global game_mode
        for i in range(8):
            self.field[1][i] = Pawn(WHITE)
            self.field[6][i] = Pawn(BLACK)
            if i == 0 or i == 7:
                self.field[0][i] = Rook(WHITE)
                self.field[7][i] = Rook(BLACK)
            elif i == 1 or i == 6:
                self.field[0][i] = Knight(WHITE)
                self.field[7][i] = Knight(BLACK)
            elif i == 2 or i == 5:
                self.field[0][i] = Bishop(WHITE)
                self.field[7][i] = Bishop(BLACK)
            elif i == 4:
                self.field[0][i] = King(WHITE)
                self.field[7][i] = King(BLACK)
            elif i == 3:
                self.field[0][i] = Queen(WHITE)
                self.field[7][i] = Queen(BLACK)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]

    def move_piece(self, row, col, row1, col1):
        """ Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False """

        if not (correct_coords(row, col) and correct_coords(row1, col1)):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:  # фигуры в этой координате нет
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:  # если идет в пустую клетку
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == self.color:  # если идет в клетку, где стоит его фигура
            return False
        else:  # если идет в клетку с чужой фигурой
            if not piece.can_move(self, row, col, row1, col1):
                return False

        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)  # поменять цвет
        return True

    def is_under_attack(self, row, col, color):
        if not correct_coords(row, col):
            return False
        for i in range(8):
            for j in range(8):
                if self.get_piece(i, j) is not None and self.get_piece(i, j).color == color:
                    if self.get_piece(i, j).can_move(self, i, j, row, col) and not isinstance(self.get_piece(i, j),
                                                                                              Pawn):
                        return True
                    elif isinstance(self.get_piece(i, j), Pawn):
                        tmp = self.field[row][col]
                        self.field[row][col] = Rook(not self.get_piece(i, j).color)
                        if self.get_piece(i, j).can_attack(self, i, j, row, col):
                            self.field[row][col] = tmp
                            return True
                        self.field[row][col] = tmp
        return False

    def castling0(self):
        if self.current_player_color() == WHITE:
            if isinstance(self.get_piece(0, 0), Rook) and isinstance(self.get_piece(0, 4), King):
                if self.get_piece(0, 0).not_moved and self.get_piece(0, 4).not_moved:
                    if self.get_piece(0, 1) is None and self.get_piece(0, 2) is None and self.get_piece(0, 3) is None:
                        self.field[0][3] = Rook(WHITE)
                        self.field[0][2] = King(WHITE)
                        self.field[0][0] = None
                        self.field[0][4] = None
                        self.color = opponent(self.color)
                        return True
        else:
            if isinstance(self.get_piece(7, 0), Rook) and isinstance(self.get_piece(7, 4), King):
                if self.get_piece(7, 0).not_moved and self.get_piece(7, 4).not_moved:
                    if self.get_piece(7, 1) is None and self.get_piece(7, 2) is None and self.get_piece(7, 3) is None:
                        self.field[7][3] = Rook(BLACK)
                        self.field[7][2] = King(BLACK)
                        self.field[7][0] = None
                        self.field[7][4] = None
                        self.color = opponent(self.color)
                        return True
        return False

    def castling7(self):
        if self.current_player_color() == WHITE:
            if isinstance(self.get_piece(0, 7), Rook) and isinstance(self.get_piece(0, 4), King):
                if self.get_piece(0, 7).not_moved and self.get_piece(0, 4).not_moved:
                    if self.get_piece(0, 5) is None and self.get_piece(0, 6) is None:
                        self.field[0][5] = Rook(BLACK)
                        self.field[0][6] = King(BLACK)
                        self.field[0][7] = None
                        self.field[0][4] = None
                        self.color = opponent(self.color)
                        return True
        else:
            if isinstance(self.get_piece(7, 7), Rook) and isinstance(self.get_piece(7, 4), King):
                if self.get_piece(7, 7).not_moved and self.get_piece(7, 4).not_moved:
                    if self.get_piece(7, 5) is None and self.get_piece(7, 6) is None:
                        self.field[7][5] = Rook(BLACK)
                        self.field[7][6] = King(BLACK)
                        self.field[7][7] = None
                        self.field[7][4] = None
                        self.color = opponent(self.color)
                        return True
        return False

    def promotion(self, row, col, row1, col1, figure):
        figures = {'R': Rook, 'B': Bishop, 'Q': Queen, 'N': Knight}
        if all(figure != i for i in figures.keys()):
            return False
        if self.move_piece(row, col, row1, col1):
            self.field[row1][col1] = figures[figure](self.current_player_color())
            return True
        return False

    def check(self):
        i, j = self.find_cur_king_coords()
        if self.is_under_attack(i, j, opponent(self.current_player_color())):
            return True
        return False

    def mate(self):
        if self.check():
            row, col = self.find_cur_king_coords()
            for i in range(8):
                for j in range(8):
                    if self.get_piece(row, col).can_move(self, row, col, i, j) and not self.is_under_attack(i, j, opponent(self.color)):
                        print(self.get_piece(i, j))
                        return False
            for i in range(8):
                for j in range(8):
                    if self.get_piece(i, j) is not None and self.get_piece(i, j).color == self.color:
                        for k in range(8):
                            for m in range(8):
                                tmp_board = copy.deepcopy(self)
                                if tmp_board.move_piece(i, j, k, m):
                                    tmp_board.color = opponent(tmp_board.color)
                                    q, w = tmp_board.find_cur_king_coords()
                                    if not tmp_board.is_under_attack(q, w, opponent(tmp_board.color)):
                                        return False
            return True
        return False

    def stalemate(self):
        if not self.check():
            row, col = self.find_cur_king_coords()
            for i in range(8):
                for j in range(8):
                    if self.get_piece(i, j) is not None and self.get_piece(i, j).color == self.color:
                        for k in range(8):
                            for m in range(8):
                                tmp_board = copy.deepcopy(self)
                                if tmp_board.move_piece(i, j, k, m):
                                    tmp_board.color = opponent(tmp_board.color)
                                    q, w = tmp_board.find_cur_king_coords()
                                    if not tmp_board.is_under_attack(q, w, opponent(tmp_board.color)):
                                        return False
            return True
        return False


    def find_cur_king_coords(self):
        for i in range(8):
            for j in range(8):
                if isinstance(self.get_piece(i, j), King) and self.get_piece(i, j).color == self.current_player_color():
                    return i, j


class Piece:  # фигура
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Rook(Piece):  # слон
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True

    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if not (row == row1 or col == col1):
            return False

        if vertical_horizontal_check(board, row, col, row1, col1):
            # проверка по горизонтали и вертикали на наличие фигур
            return False
        self.moved()
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)

    def moved(self):
        self.not_moved = False


class Pawn(Piece):  # пешка
    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        if col != col1:
            if self.can_attack(board, row, col, row1, col1):
                return True
            else:
                return False
        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1 and board.field[row1][col1] is None:
            return True

        # ход на 2 клетки из начального положения
        if row == start_row and row + 2 * direction == row1 and board.field[row + direction][col] is None and board.field[row + direction * 2][col] is None:
            return True

        return False

    def can_attack(self, board, row, col, row1, col1):
        if abs(col - col1) == 1 and row1 - row == (1 if self.color == WHITE else -1) and board.get_piece(row1,
                                                                                                         col1) is not None:
            return True
        return False


class King(Piece):  # Король
    def __init__(self, color):
        super().__init__(color)
        self.not_moved = True

    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if not (abs(row1 - row) < 2 and abs(col - col1) < 2):  # король может ходить только вокруг себя на одну клетку
            return False
        if board.get_piece(row1, col1) is not None:
            return False
        return True

    def moved(self):
        self.not_moved = False


class Queen(Piece):  # Ферзь
    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if abs(row - row1) != abs(col - col1) and row != row1 and col != col1:
            return False
        if row == row1 or col == col1:
            if vertical_horizontal_check(board, row, col, row1, col1):  # проверка по вертикали и горизонтали
                # на наличие фигур
                return False
        elif abs(row - row1) == abs(col - col1):
            if diagonal_check(board, row, col, row1, col1):  # проверка по диагонали на наличие фигур
                return False

        return True


class Bishop(Piece):  # Офицер
    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if abs(row - row1) != abs(col - col1):  # офицер может ходить только по диагонали
            return False

        # нет ли фигур на пути
        if diagonal_check(board, row, col, row1, col1):
            return False

        return True


class Knight(Piece):  # Конь
    def char(self):
        return 'N'

    def can_move(self, board, row, col, row1, col1):
        if abs(col1 - col) == 2 and abs(row1 - row) == 1:
            return True
        elif abs(col1 - col) == 1 and abs(row1 - row) == 2:
            return True
        return False


def main():
    # Создаём доску

    board = Board()

    # Цикл ввода команд игроков
    while True:
        # переменная используемая в проверке на наличие ошибки
        global is_incorrect_coords
        global is_cast_not_done
        global is_begin_of_game
        global is_check
        global is_mate
        global is_stalemate
        # Выводим доску
        print_board(board)
        if is_incorrect_coords:
            print('Координаты некорректы! Попробуйте другой ход!')
        elif is_cast_not_done:
            print('Рокировка неудачна, попробуйте другой ход')
        elif not is_begin_of_game:
            print('Ход успешен!')
        else:
            is_begin_of_game = False

        if is_stalemate:
            print('ПАТ!')
            break

        if is_mate:
            print('МАТ!')
            break

        if is_check:
            print('ШАХ!')

        is_cast_not_done = False
        is_incorrect_coords = False
        # Подсказка по командам
        print('Команды:')
        print('    exit                               -- выход')
        print('    <coord1> <coord2>                  -- ход из клетки (coord1) в клетку (coord2)')
        print('    \'cast_left\' or \'cast_right\'    -- рокировка слева или справа')
        print('Example:\n    a2 a3  or  cast_left')

        # Выводим чей ход
        if board.current_player_color() == WHITE:
            print('\033[36mХод белых: \033[0m\n    ', end='')
        else:
            print('\033[36mХод чёрных: \033[0m\n    ', end='')

        # если написали exit
        command = input()
        if command == 'exit' or command == 'эксит':
            break

        # распарсить координаты или вывести рокировку
        if command != 'cast_left' and command != 'cast_right':
            row, col, row1, col1 = parse_coords(command)
            if is_check:
                if not isinstance(board.get_piece(row, col), King) or not board.get_piece(row, col).color == board. \
                        current_player_color() or board.is_under_attack(row1, col1,
                                                                        opponent(board.current_player_color())) \
                        or not board.move_piece(row, col, row1, col1):
                    is_incorrect_coords = True
            else:
                if not board.move_piece(row, col, row1, col1):
                    is_incorrect_coords = True
        elif command == 'cast_left':
            if not board.castling0():
                is_cast_not_done = True
        elif command == 'cast_right':
            if not board.castling7():
                is_cast_not_done = True
        else:
            is_incorrect_coords = True

        is_check = False
        is_mate = False
        is_stalemate = False

        if board.check():
            is_check = True

        if board.mate():
            is_mate = True

        if board.stalemate():
            is_stalemate = True


main()
