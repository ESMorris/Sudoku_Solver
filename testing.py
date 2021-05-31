import pyautogui as pg
import time
# This program will use a pre defined sudoku puzzle and then solve it using back tracking

# Will display both the unsolved and solved Sudoku Puzzle
def printSudoku(list, instruction):

    print("Here is the {} Sudoku-Puzzle: ".format(instruction))

    # for loop to loop through the 2d list and print out the grid for the sudoku puzzle
    # Should look like this:
    # -----------------------------------
    # || 6  9  0 || 0  5  0 || 8  0  0 ||
    # || 0  4  5 || 1  7  0 || 2  0  6 ||
    # || 2  0  0 || 8  0  0 || 0  4  0 ||
    # -----------------------------------
    # || 4  1  0 || 0  0  0 || 0  0  0 ||
    # || 3  0  0 || 9  6  1 || 0  0  2 ||
    # || 0  0  0 || 0  0  0 || 0  6  8 ||
    # -----------------------------------
    # || 0  6  0 || 0  0  9 || 0  0  7 ||
    # || 1  0  9 || 0  8  7 || 6  5  0 ||
    # || 0  0  3 || 0  4  0 || 0  2  1 ||
    # -----------------------------------
    for row in range(len(list)):
        if row % 3 == 0:
            print("-------------------------------")
        for col in range(len(list)):
            if col % 3 == 0:
                print("|", end = '')

            if col == 8:
                print(" {} |".format(list[row][col]), end = '')
            else:
                print(" {} ".format(list[row][col]), end = '')
        print()
    print("-------------------------------\n")

def automation(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])
    
    for lists in final:
        for num in lists:
            str_fin.append(str(num))
    
    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            for number in range(1, 10):
                pg.hotkey('left')

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
    return True

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

# main function (also the main runner of the code)
def main():

    # list variable to hold the 9x9 sudoku puzzle
    grid = []
    while True:
        row = list(input('Row: '))
        ints = []

        for n in row:
            ints.append(int(n))
        grid.append(ints)

        if len(grid) == 9:
            break
        print('Row ' + str(len(grid)) + ' Complete')
    
    print()
    printSudoku(grid, 'unsolved')

    # solve the sudokku puzzle
    if solveSudoku(grid) == True:
        print("Solved!")
        time.sleep(3)
        automation(grid)
        printSudoku(grid, 'solved')
    else:
        print("Cannot be solved!")

main()
