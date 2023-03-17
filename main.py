from __future__ import annotations

from pprint import pprint


class Pole:
    def __init__(self, strings: str):
        self.pole = []  # само двухмерное поле с экземплярами класса Cell
        self.pole_size = 9  # размер поля
        self.strings = strings  # входные данные в формате строк / должна быть форматом 3*3
        self.solve = False
        if self.strings:
            self.init_pole(self.strings)

    def show(self):
        pprint(self.pole)

    def init_pole(self, strings: str):
        """Инициализация поля"""
        self.pole.clear()  # Очищаем предыдущие значения
        # Формируем поле из цифр
        for string in strings.split("\n"):
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

    def __udpade_row(self, values: list):
        pass

    def solve_sudoku(self):

        # формируем координаты ячеек для поля 3*3
        list_cells = []
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                cells = [(i + ii, j + jj) for ii in (0, 1, 2) for jj in (0, 1, 2)]
                list_cells.append(cells)

        actual_len = len(self)
        while not self.solve:
            # step 1. циклом проверяет каждую строку, столбец и квадрат 3*3 на наличие уже отгаданных цифр
            # и если у клетки остается только одна цифра, то она обновляется.

            # Для каждой строки.
            for row in self.pole:
                value = [cell.value for cell in row if cell.value]
                for cell in row:
                    cell.update_possible_values(value)

            # Для каждого столбца
            for row, _ in enumerate(self.pole):
                value = [self.pole[col][row].value for col in range(self.pole_size) if self.pole[col][row].value]
                for col in range(self.pole_size):
                    self.pole[col][row].update_possible_values(value)

            # для каждой ячейки 3*3
            for i in list_cells:
                value = [self.pole[row][col].value for row, col in i if self.pole[row][col].value]
                for row, col in i:
                    self.pole[row][col].update_possible_values(value)

            # цикл останавливаеться если все разгадано
            if len(self) == self.pole_size ** 2:
                self.solve = True
                break
            # цикл останавливаеться в случае если изменений не произошло
            elif len(self) == actual_len:
                break
            else:
                actual_len = len(self)

            # Step 2. если решить на шаге 1 не получилось, переходим к перебору значений

            # TODO

        self.show()
        print(len(self))


class Cell:
    """
    A class representing a sudoku cell.

    Attributes:
    value (int): the value of the cell.
    possible_values (list): list of possible cell values. Empty if value is defined.
    """

    def __init__(self, value: int = 0) -> None:
        self.value = value
        self.possible_values = self._get_possible_values()

    def _get_possible_values(self) -> list:
        """
        Возвращает список возможных значений клетки, если само значение не определено.
        Если Value определено, то возвращает пустой список.
        """
        if not self.value:
            possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            possible_values = []
        return possible_values

    def check_value(self) -> None:
        """
        Проверяет если у клетки всего одно возможное значение (possible_values), то подставляет его в self.value.
        """
        if self.possible_values and len(self.possible_values) == 1:
            self.value = self.possible_values[0]
            self.possible_values = []

    def update_possible_values(self, args: list) -> None:
        """
        Обновляет self.possible_values, удаляя значения из переданного списка и вызывает check_value.
        """
        if self.possible_values:
            self.possible_values = [value for value in self.possible_values if value not in args]

        self.check_value()

    def __repr__(self):
        return str(self.value) if self.value else " "


# Exception #############################
class SudokuException(Exception):
    pass


class SizeSudokuException(SudokuException):
    pass


if __name__ == "__main__":
    test_sudoku = """000000027
050030609
080070000
030000400
005090008
096200703
000928000
409000105
008400962"""
    test_sudoku2 = """005300000
800000020
070010500
400005300
010070006
003200080
060500009
004000030
000009700"""
    pole = Pole(test_sudoku)
    pole2 = Pole(test_sudoku2)
    poles = [pole, pole2]
    for pole in poles:
        pole.solve_sudoku()