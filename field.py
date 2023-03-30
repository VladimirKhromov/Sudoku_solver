from __future__ import annotations

from pprint import pprint

from cell import Cell


class Field:
    """
    A class representing a sudoku field.

    Attributes:
    pole (list): list of cell class objects.
    pole_size (int): the value of the cell.
    strings (str): string with sudoku values.
    solve_string (str): solved string sudoku.
    solve(bool): is sudoku solved.
    """

    def __init__(self, strings: str):
        self.pole = []
        self.pole_size = 9
        self.strings = strings
        self.solve_string = ""
        self.solve = False
        if self.strings:
            self.init_field(self.strings)

    def show(self):
        """Show the sudoku field."""
        pprint(self.pole)

    def init_field(self, strings: str):
        """Field initialization. """
        self.pole.clear()
        # Forming a field of numbers
        for string in [strings[9 * i:((9 * i) + 9)] for i in range(9)]:
            self.pole.append([int(char) for char in string.strip()])

        # Form the field and put Cell class objects into it
        for row, i in enumerate(self.pole):
            for cow, j in enumerate(i):
                self.pole[row][cow] = Cell(self.pole[row][cow])

    def __len__(self):
        """
        Method for determining the number of solved cells in Sudoku.
        For classic sudoku it is 81 (9x9).
        """
        len_sudoku = 0
        # if a cell has a non-zero value, it's solved
        for i in self.pole:
            for j in i:
                if j.value:
                    len_sudoku += 1
        return len_sudoku

    def is_solve(self):
        """Checks sudoku solution."""
        if len(self) == self.pole_size ** 2 and not self.is_collision():
            self.solve = True

        return self.solve

    def _get_list_cells(self) -> list:
        """Form the coordinates of the cells for the field 3 * 3. """
        list_cells = []
        for i in range(0, self.pole_size, 3):
            for j in range(0, self.pole_size, 3):
                cells = [(i + ii, j + jj) for ii in (0, 1, 2) for jj in (0, 1, 2)]
                list_cells.append(cells)
        return list_cells

    def fill(self):
        """The method fills the field with possible values."""
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
        """Make a sudoku solution string."""
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
            self.solve_string = "Impossible to decide"
        return self.solve_string

    def is_collision(self):
        """
        Checks for collisions (same values) when solving Sudoku.
        Returns True if there are collisions or returns False if there are no collisions.
        """

        # for row
        for row in self.pole:
            value = [cell.value for cell in row if cell.value]
            if len(value) != len(set(value)):
                return True

        # for column
        for col in range(self.pole_size):
            value = [self.pole[row][col].value for row in range(self.pole_size) if self.pole[row][col].value]
            if len(value) != len(set(value)):
                return True

        # for field 3*3
        list_cells = self._get_list_cells()
        for i in list_cells:
            value = [self.pole[row][col].value for row, col in i if self.pole[row][col].value]
            if len(value) != len(set(value)):
                return True

        return False
