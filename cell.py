from sudoku_exception import ValueCellSudokuException


class Cell:
    """
    A class representing a sudoku cell.

    Attributes:
    value (int): the value of the cell.
    possible_values (list): list of possible cell values. Empty if value is defined.
    """

    def __init__(self, value: int = 0) -> None:
        self.value = self._check_value(value)
        self.possible_values = self._get_possible_values()

    @staticmethod
    def _check_value(value):
        if value in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            return value
        else:
            raise ValueCellSudokuException

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

    def update_cell_value(self) -> None:
        """
        Проверяет если у клетки всего одно возможное значение (possible_values), то оно подставляется в self.value.
        """
        if self.possible_values and len(self.possible_values) == 1:
            self.value = self.possible_values[0]
            self.possible_values = []

    def update_possible_values(self, args: list) -> None:
        """
        Обновляет self.possible_values, удаляя значения из переданного списка и вызывает check_value.
        """
        for arg in args:
            self._check_value(arg)
        if self.possible_values:
            self.possible_values = [value for value in self.possible_values if value not in args]

        self.update_cell_value()

    def __repr__(self):
        return str(self.value) if self.value else " "
