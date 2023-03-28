from main import Field

test_sudoku = []


# with open(file="sudoku test 1.txt") as file:
#     pass


# init #################
def test_init_field():
    field = Field("")
    assert field.pole == []
    assert field.strings == ""
    assert field.solve == False
    
