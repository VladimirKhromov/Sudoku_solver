import pytest

from field import Field

test_sudoku = []


# with open(file="sudoku test 1.txt") as file:
#     pass


# init #################
def test_init_field():
    field = Field("")
    assert field.pole == []
    assert field.strings == ""
    assert field.solve_string == ""
    assert field.solve == False


@pytest.mark.parametrize("string, value00, value88",
                         [('000000000000000000000000000000000000000000000000000000000000000000000000000000000', 0, 0),
                          ('125368497846759123379412568487695312512873946693241785261534879754986231938127654', 1, 4),
                          ])
def test_init_field_with_start_string(string, value00, value88):
    field = Field(string)
    assert field.pole != []
    assert field.strings != ""
    assert field.solve_string == ""
    assert field.pole[0][0].value == value00
    assert field.pole[8][8].value == value88


@pytest.mark.parametrize("string, solve_string",
                         [('000000000000000000000000000000000000000000000000000000000000000000000000000000000',
                           '123456789456789123789123456214365897365897214897214365531642978642978531978531642'),
                          ('000000027050030609080070000030000400005090008096200703000928000409000105008400962',
                           '613549827257831649984672531832157496745396218196284753561928374429763185378415962'),
                          ('005300000800000020070010500400005300010070006003200080060500009004000030000007000',
                           '125368497846759123379412568487695312512873946693241785261534879754986231938127654'),
                          ('520800640804672531003000020008000000000908070240060185380057490470306000910000003',
                           '527831649894672531163549827738415962651928374249763185382157496475396218916284753'),
                          ])
def test_solve(string, solve_string):
    field = Field(string)
    field.solve_sudoku()
    assert field.solve_string == solve_string
