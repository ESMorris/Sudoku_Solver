# Imports for this Helper function
import requests
from bs4 import BeautifulSoup

def web_scraping(grid):
    url = 'https://nine.websudoku.com/?' # holds the url needed to webscrape

    page = requests.get(url) # requesting the url

    # Using Beautiful soup we will load the parser we will be using which is lxml
    # the page.text tells the beautifulsoup to get the html contents off the opened web browser
    soup = BeautifulSoup(page.text, 'lxml')

    table = soup.find(id="puzzle_grid") # find puzzle grid by id using beautiful soup

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