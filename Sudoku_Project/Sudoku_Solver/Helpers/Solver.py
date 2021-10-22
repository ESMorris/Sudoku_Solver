def solveSudoku(list):

    # loop through the 2d list
    for row in range(len(list)):
        for col in range(len(list)):
            # check if the number is 0
            if checkIfZero(list[row][col]) == True:
                # if number is zero
                # loop through every number to find the correct number
                for number in range(1, 10):
                    if checkIfValid(list, row, col, number):
                        list[row][col] = number
                        if solveSudoku(list):
                            return True
                        else:
                            list[row][col] = 0
                return False
    return list

def checkIfZero(number):

    if number == 0:
        return True
    else:
        return False

def checkIfValid(list, row, col, number):

    if ((checkRow(list, row, number) == True) or (checkCol(list, col, number) == True) or (checkSubSquare(list, row, col, number) == True)):
        return False
    return True

def checkRow(list, row, number):

    for i in range(len(list)):
        if list[row][i] == number:
            return True
    return False

def checkCol(list, col, number):

    for j in range(len(list)):
        if list[j][col] == number:
            return True
    return False

def checkSubSquare(list, row, col, number):

    temp_r = row - row % 3
    temp_c = col - col % 3
    for i in range(temp_r, temp_r + 3):
        for j in range(temp_c, temp_c + 3):
            if list[i][j] == number:
                return True
    return False