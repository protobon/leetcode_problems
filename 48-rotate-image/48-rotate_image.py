def rotate(matrix):
    level = 1
    dim = len(matrix)
    while level <= dim // 2:
        for i in range(level - 1, dim - level):
            tmp = matrix[level-1][i]
            matrix[level-1][i] = matrix[-i-1][level-1]
            matrix[-i-1][level-1] = matrix[-level][-i-1]
            matrix[-level][-i-1] = matrix[i][-level]
            matrix[i][-level] = tmp
        level += 1
    return matrix


if __name__ == "__main__":
    print(rotate([[1]]))
    print(rotate([[1,2],[3,4]]))
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
