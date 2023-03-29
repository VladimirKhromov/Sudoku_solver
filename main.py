import os

from field import Field


def show_sudoku(string: str) -> str:
    if type(string) != str or len(string) != 81:
        return string
    result = ""
    for i in range(0, 81, 3):
        if i % 27 == 0 and i != 0:
            result += "\n---+---+---"
            result += "\n" + string[i:i + 3] + "|"

        elif i % 9 == 0 and i != 0:
            result += "\n" + string[i:i + 3] + "|"
        else:
            result += string[i:i + 3] + "|"
    result += "\n"
    return result


def get_txt_files() -> list[str]:
    current_dir = os.getcwd()
    files_name = [file for file in os.listdir(current_dir)
                  if file[-4:] == ".txt" and file != "sudoku_solve.txt"]
    return files_name


def write_solve_to_file(sudoku: str, solve: str) -> None:
    with open("sudoku_solve.txt", "a") as solve_file:
        solve_file.write("***SUDOKU***\n")
        solve_file.write(show_sudoku(sudoku) + "\n")
        solve_file.write("***SOLVE***\n")
        solve_file.write(show_sudoku(solve) + "\n")
        solve_file.write("\n")


def solve_sudoku_from_file(file: str) -> None:
    with open(file=file, mode="r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 81:
                sudoku = Field(line)
                write_solve_to_file(line, sudoku.solve_sudoku())


if __name__ == "__main__":
    for file_name in get_txt_files():
        solve_sudoku_from_file(file_name)
