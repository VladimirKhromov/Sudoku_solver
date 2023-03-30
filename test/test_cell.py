import pytest

from cell import Cell
from cell import ValueCellSudokuException


# init #################
def test_zero_init_cell_1():
    cell = Cell()
    assert cell.value == 0
    assert cell.possible_values == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_zero_init_cell_2():
    cell = Cell(0)
    assert cell.value == 0
    assert cell.possible_values == [1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.parametrize("value", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_good_init_cell(value):
    cell = Cell(value)
    assert cell.value == value
    assert cell.possible_values == []


@pytest.mark.parametrize("value", [-1, "d", "5", None,
                                   list(), dict(), set()])
def test_incorrect_init(value):
    with pytest.raises(ValueCellSudokuException):
        Cell(value)


# check_value #################

@pytest.mark.parametrize("value", [1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_good_check(value):
    cell = Cell()
    cell.possible_values = [value]
    cell.update_cell_value()
    assert cell.value == value
    assert cell.possible_values == []


def test_zero_check():
    cell = Cell()
    cell.update_cell_value()
    assert cell.value == 0
    assert cell.possible_values == [1, 2, 3, 4, 5, 6, 7, 8, 9]


# update_possible_values #################


@pytest.mark.parametrize("up_list, possible_values",
                         [([1], [2, 3, 4, 5, 6, 7, 8, 9]),
                          ([2], [1, 3, 4, 5, 6, 7, 8, 9]),
                          ([3], [1, 2, 4, 5, 6, 7, 8, 9]),
                          ([5], [1, 2, 3, 4, 6, 7, 8, 9]),
                          ([6], [1, 2, 3, 4, 5, 7, 8, 9]),
                          ([9], [1, 2, 3, 4, 5, 6, 7, 8]),
                          ([2, 7], [1, 3, 4, 5, 6, 8, 9]),
                          ([4, 7], [1, 2, 3, 5, 6, 8, 9]),
                          ([3, 6, 7], [1, 2, 4, 5, 8, 9]),
                          ([2, 5, 9], [1, 3, 4, 6, 7, 8]),
                          ([1, 2, 3, 4, 5, 6, 7], [8, 9]),
                          ])
def test_invalid_value_update(up_list, possible_values):
    cell = Cell()
    cell.update_possible_values(up_list)

    assert cell.value == 0
    assert cell.possible_values == possible_values


@pytest.mark.parametrize("value, up_list",
                         [(1, [2, 3, 4, 5, 6, 7, 8, 9]),
                          (2, [1, 3, 4, 5, 6, 7, 8, 9]),
                          (3, [1, 2, 4, 5, 6, 7, 8, 9]),
                          (4, [1, 2, 3, 5, 6, 7, 8, 9]),
                          (5, [1, 2, 3, 4, 6, 7, 8, 9]),
                          (6, [1, 2, 3, 4, 5, 7, 8, 9]),
                          (7, [1, 2, 3, 4, 5, 6, 8, 9]),
                          (8, [1, 2, 3, 4, 5, 6, 7, 9]),
                          (9, [1, 2, 3, 4, 5, 6, 7, 8]),
                          ])
def test_good_update(value, up_list):
    cell = Cell()
    cell.update_possible_values(up_list)
    assert cell.value == value
    assert cell.possible_values == []


@pytest.mark.parametrize("value", [["sadf"], ["D"], [None]])
def test_invalid_value_update(value):
    with pytest.raises(ValueCellSudokuException):
        cell = Cell()
        cell.update_possible_values(value)
