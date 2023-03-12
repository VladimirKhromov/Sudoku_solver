from __future__ import annotations

from pprint import pprint


class SudokuException(Exception):
    pass
class SizeSudokuException(SudokuException):
    pass


class Pole:
    def __init__(self, strings: str = None, size: int = 9):
        self.pole = []
        self.size = 9
        self.strings = strings
        self.solve = False
        if self.strings:
            self.init_pole(self.strings)


    def show(self):
        pprint(self.pole)

    def init_pole(self, strings: str):
        self.pole.clear()
        for string in strings.split("\n"):
            self.pole.append([int(char) for char in string])

        for row, i in enumerate(self.pole):
            if len(i) != self.size:
                raise SizeSudokuException("invalid sudoku size")
            for cow, j in enumerate(i):
                self.pole[row][cow] = Cell(row, cow, self.pole[row][cow])

    def __len__(self):
        len_sudoku = 0
        for i in self.pole:
            for j in i:
                if j.value:
                    len_sudoku += 1
        return len_sudoku


    def solve_sudoku(self):
        # while not self.solve:
        value = [1,3,4,5,6,8]
        for i in range(self.size):
            for j in range(self.size):
                self.pole[i][j].update_possible_values(value)
                print(self.pole[i][j].__dict__)




class Cell:
    def __init__(self, x: int, y: int, value: int = 0):
        self.x = x
        self.y = y
        self.value = value
        if not self.value:
            self.possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.possible_values = None

    def check_value(self):
        if len(self.possible_values) == 1:
            self.value = self.possible_values[0]

    def update_possible_values(self, *args):
        for arg in args:
            if self.possible_values and arg in self.possible_values:
                self.possible_values.remove(arg)
        self.check_value()

    def __repr__(self):
        return str(self.value) if self.value else " "


cd = []
test_sudoku = """000000027
050030609
080070000
030000400
005090008
096200703
000928000
409000105
008400962"""

pole = Pole(test_sudoku)
print(len(pole))
pole.show()
pole.solve_sudoku()


