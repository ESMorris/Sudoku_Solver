# Imported modules go here
import Helpers as Hp



# main function (also the main runner of the code)
def main():
    result = [] # list variable to hold the final 9x9 sudoku puzzle

    Hp.web_scraping.web_scraping(result)

    print()
    Hp.print.printSudoku(result, 'unsolved')

    # solve the sudokku puzzle
    if Hp.Solver.solveSudoku(result) == True:
        print("Solved!")
        # time.sleep(3)
        # automation(result)
        Hp.print.printSudoku(result, 'solved')
    # cannot be solved print that it cannot!
    else:
        print("Cannot be solved!")


main()