from django.http import response, JsonResponse
from django.shortcuts import render
import json
from Sudoku_Solver.Helpers import web_scraping as wb
from Sudoku_Solver.Helpers import Solver as Slvr

# Create your views here.
# where our game lives in the home route
def home(request):
    return render(request, 'Sudoku_Solver/index.html')

def start(request):
    result = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    jsonStr = json.dumps(result)
    return JsonResponse(jsonStr, safe=False)

# Button that will generate the unsolved Sudoku
def GenerateButton(response):
    grid = []
    global result
    result = wb.web_scraping(grid)
    jsonStr = json.dumps(result)
    return JsonResponse(jsonStr, safe=False)

# Button that will solve the unsolved Sudoku
def SolveButton(request):
    Slvr.solveSudoku(result)
    jsonStr = json.dumps(result)
    return JsonResponse(jsonStr, safe=False)
