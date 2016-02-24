result = []
GRID = 8

def nqueens(row, columns):
    if row == GRID:
        result.append(columns)
    else:
        for col in xrange(GRID):
            if valid(row, col, columns):
                #print row, col, columns
                if row >= 5:
                    print row, col, columns 
                columns[row] = col
                nqueens(row + 1,  columns)


def valid(row, col, columns):

    for r in range(row):
        # check same column
        if col == columns[r]:
            return False

        # check diagonals
        if abs(r - row) == abs(col - columns[r]):
            return False

    return True

columns = [-1] * GRID
nqueens(0, columns)

print columns
