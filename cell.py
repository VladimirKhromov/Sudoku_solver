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
        Returns a list of possible cell values if the value is not defined (equals 0).
        If the value is defined, it returns an empty list.
        """

        if not self.value:
            possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:  # the value is defined
            possible_values = []
        return possible_values

    def update_cell_value(self) -> None:
        """
        Check possible cell values.
        If possible_values have one value the cell value is updated.
        """
        if self.possible_values and len(self.possible_values) == 1:
            self.value = self.possible_values[0]
            self.possible_values = []

    def update_possible_values(self, remove_values: list) -> None:
        """
        Remove values from self.possible_values.
        """
        for remove_value in remove_values:
            self._check_value(remove_value)
        if self.possible_values:
            self.possible_values = [value for value in self.possible_values
                                    if value not in remove_values]

        self.update_cell_value()

    def __repr__(self):
        return str(self.value) if self.value else " "


# Exception #########

class SudokuException(Exception):
    pass


class ValueCellSudokuException(SudokuException):
    pass


class SizeSudokuException(SudokuException):
    pass
