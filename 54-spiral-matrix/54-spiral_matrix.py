def spiralMatrix(matrix):
    result = []
    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1
    turn = "j"
    step = "+"
    while top <= bottom and left <= right:
        if step == "+":
            if turn == "j":
                # j forward
                for j in range(left, right + 1):
                    result.append(matrix[top][j])
                top += 1
                turn = "i"
            else:
                # i forward
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1
                turn = "j"
                step = "-"
        else:
            if turn == "j":
                # j backwards
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
                turn = "i"
            else:
                # i backwards
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
                turn = "j"
                step = "+"
    return result


if __name__ == "__main__":
    print(spiralMatrix([[1,2,3],[4,5,6],[7,8,9]]))
    print(spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
