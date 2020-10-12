import sys
import re
from termcolor import colored

def isValidSpaceSeparatedValues(toCheck):
    return re.match("^[0-9]+( [0-9]*)*$", toCheck)

def isThereOneSpaceInMatrix(matrix):
    space_count = 0
    for rows in matrix:
        for elem in rows:
            if elem == 0:
                space_count += 1
    return space_count == 1

def isSolvable(matrix, size): 
    inv_count = 0
    for i in range(size - 1): 
        for j in range(i + 1, size): 
            if matrix[i] and matrix[j] and matrix[i] > matrix[j]:
                inv_count += 1
    return (inv_count % 2) == 0

def getData(args):
    matrix = []
    row_size = -1
    col_size = 0
    try:
        with open(args.path, "r") as f:
        # with open(args.path, "r") as f:
            rows = f.readlines()
    except EnvironmentError:
            sys.exit(colored("Could not open the file, the path may be wrong", 'red'))

    try:
        for row in rows:
            if isValidSpaceSeparatedValues(row):
                matrix_row = [int(value) for value in (row.strip()).split(' ')]
                length = len(matrix_row)
                if length > 2:
                    if row_size == -1:
                        row_size = length
                    elif length != row_size:
                        sys.exit(colored("All rows must have the same number of elements", "red"))
                    col_size += 1
                    matrix.append(matrix_row)
            # else:
            #     sys.exit(colored("Man, just use some ints...", 'red'))
    except ValueError:
        sys.exit(colored("Values must be numerals spaces separated", 'red'))

    if row_size != col_size:
        sys.exit(colored("The number of rows and columns must be the same", 'red'))

    if row_size > 3:
        sys.exit(colored("The number of rows and columns must not exceed 3", 'red'))

    if isThereOneSpaceInMatrix(matrix) == False:
        sys.exit(colored("There must be one and only one space symbolised by a zero", "red"))

    puzzle = []
    for row in matrix:
        for elem in row:
            puzzle.append(elem)
    return (tuple(puzzle), row_size, matrix)