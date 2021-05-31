# Imported modules will go here
import pyautogui as pg
import time
from selenium import webdriver
from bs4 import BeautifulSoup

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

    # list variable to hold the final 9x9 sudoku puzzle
    grid = []

    # holds the url needed to webscrape
    url = 'https://nine.websudoku.com/?'

    # the Firefox web browser will be the driver for the web scrape
    driver = webdriver.Firefox()

    # using the Firefox web browser go to the url above
    driver.get(url)

    # Using Beautiful soup we will load the parser we will be using which is lxml
    # the .pagesource tells the beautifulsoup to get the html contents off the opened web browser
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # find the element named table
    table = soup.find('table', class_='t')

    # nested for loop to web scrape the Sudoku puzzle on the web page
    # looking for all elements within table labeled tr
    for element in table.find_all('tr'):
        # a 2nd list to hold the 9 values per row
        ints = []
        # looking for all html elements within tr labeled input
        for number in element.find_all('input'):
            # try/ Exception to catch if there is no html element labeled value
            try:
                # place the value into the ints list
                ints.append(int(number['value']))
            except Exception as e:
                # If there is no element labeled value place a zero at that index
                value = 0
                # place a zero into the ints list
                ints.append(value)
        # append the completed row into the list grid
        grid.append(ints)

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
