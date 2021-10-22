# Will display both the unsolved and solved Sudoku Puzzle
def printSudoku(list, instruction):

    print("Here is the {} Sudoku-Puzzle: ".format(instruction))
    
    '''
    # for loop to loop through the 2d list and print out the grid for the sudoku puzzle
    # Should look like this:
    -----------------------------------
    || 6  9  0 || 0  5  0 || 8  0  0 ||
    || 0  4  5 || 1  7  0 || 2  0  6 ||
    || 2  0  0 || 8  0  0 || 0  4  0 ||
    -----------------------------------
    || 4  1  0 || 0  0  0 || 0  0  0 ||
    || 3  0  0 || 9  6  1 || 0  0  2 ||
    || 0  0  0 || 0  0  0 || 0  6  8 ||
    -----------------------------------
    || 0  6  0 || 0  0  9 || 0  0  7 ||
    || 1  0  9 || 0  8  7 || 6  5  0 ||
    || 0  0  3 || 0  4  0 || 0  2  1 ||
    -----------------------------------
    '''
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