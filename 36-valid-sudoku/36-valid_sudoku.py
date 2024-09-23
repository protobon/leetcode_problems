def validSudoku(board):
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    
    Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.
    """
    boxes = {key: value for key, value in 
             zip([str(i) for i in range(9)], [set() for _ in range(9)])}
    
    for i in range(9):
        row_s = set()
        col_s = set()
        for j in range(9):
            # validate row and column
            row = board[i][j]
            col = board[j][i]
            if row in row_s or col in col_s:
                return False
            if col != ".":
                col_s.add(col)
            if row != ".":
                row_s.add(row)

                # validate box
                if i <= 2:
                    if j <= 2:
                        if row in boxes["0"]:
                            return False
                        boxes["0"].add(row)
                    elif j <= 5:
                        if row in boxes["1"]:
                            return False
                        boxes["1"].add(row)
                    else:
                        if row in boxes["2"]:
                            return False
                        boxes["2"].add(row)
                elif i <= 5:
                    if j <= 2:
                        if row in boxes["3"]:
                            return False
                        boxes["3"].add(row)
                    elif j <= 5:
                        if row in boxes["4"]:
                            return False
                        boxes["4"].add(row)
                    else:
                        if row in boxes["5"]:
                            return False
                        boxes["5"].add(row)
                else:
                    if j <= 2:
                        if row in boxes["6"]:
                            return False
                        boxes["6"].add(row)
                    elif j <= 5:
                        if row in boxes["7"]:
                            return False
                        boxes["7"].add(row)
                    else:
                        if row in boxes["8"]:
                            return False
                        boxes["8"].add(row)
    return True


if __name__ == "__main__":
    print(validSudoku(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    ))
    
    print(validSudoku(
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    ))