from __future__ import annotations

from pprint import pprint

from cell import Cell


class Field:
    def __init__(self, strings: str):
        self.pole = []  # само двухмерное поле с экземплярами класса Cell
        self.pole_size = 9  # размер поля
        self.strings = strings  # входные данные в формате строки длиной 81 символ (9х9)
        self.solve_string = ""
        self.solve = False
        if self.strings:
            self.init_field(self.strings)

    def show(self):
        pprint(self.pole)

    def init_field(self, strings: str):
        """Инициализация поля"""
        self.pole.clear()  # Очищаем предыдущие значения
        # Формируем поле из цифр
        for string in [strings[9 * i:((9 * i) + 9)] for i in range(9)]:
            self.pole.append([int(char) for char in string.strip()])

        # Формируем поле и закладываем в него объекты класса Cell со значением клетки
        for row, i in enumerate(self.pole):
            for cow, j in enumerate(i):
                self.pole[row][cow] = Cell(self.pole[row][cow])

    def __len__(self):
        """Метод для определения количества разгаданных клеток в судоку. Для поля размером 9*9 это 81."""
        len_sudoku = 0
        # у клетки есть не нулевое значение value, значит она считается заполненой.
        for i in self.pole:
            for j in i:
                if j.value:
                    len_sudoku += 1
        return len_sudoku

    def is_solve(self):
        if len(self) == self.pole_size ** 2 and not self.is_collision():
            self.solve = True

        return self.solve

    @staticmethod
    def get_list_cells() -> list:
        """ формируем координаты ячеек для поля 3*3 """
        list_cells = []
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                cells = [(i + ii, j + jj) for ii in (0, 1, 2) for jj in (0, 1, 2)]
                list_cells.append(cells)
        return list_cells

    def fill(self):
        """Метод заполняет поле возможными значениями."""
        if self.is_collision():
            return False

        if not self.solve:
            for i in range(self.pole_size):
                for j in range(self.pole_size):
                    cel = self.pole[i][j]
                    if cel.value == 0:
                        for possible_value in cel.possible_values:
                            cel.value = possible_value
                            if self.fill():
                                return True
                            else:
                                cel.value = 0
                        return False
        return True

    def make_solve_string(self):
        result = []
        for row in self.pole:
            st = ""
            for cell in row:
                st += str(cell.value)
            result.append(st)
        self.solve_string = "".join(result)

    def solve_sudoku(self):
        if self.fill():
            self.make_solve_string()
        else:
            self.solve_string = "Невозможно решить"

    def is_collision(self):
        """
        Проверяет наличие коллизий (одинаковых значений) при решение судоку.
        возвращает True если коллизии есть, False если коллизий нет.
        """

        # Для каждой строки.
        for row in self.pole:
            value = [cell.value for cell in row if cell.value]
            if len(value) != len(set(value)):
                return True

        # Для каждого столбца
        for col in range(self.pole_size):
            value = [self.pole[row][col].value for row in range(self.pole_size) if self.pole[row][col].value]
            if len(value) != len(set(value)):
                return True

        # для каждой ячейки 3*3
        list_cells = self.get_list_cells()
        for i in list_cells:
            value = [self.pole[row][col].value for row, col in i if self.pole[row][col].value]
            if len(value) != len(set(value)):
                return True

        return False


s = '527831649894672531163549827738415962651928374249763185382157496475396218916284753'
f = Field(s)
f.show()
f.solve_sudoku()
print(f.solve_string)
