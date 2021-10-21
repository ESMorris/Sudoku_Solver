from django.http import response, JsonResponse
from django.shortcuts import render
import json

# Create your views here.
# where our game lives in the home route
def home(request):
    return render(request, 'Sudoku_Solver/index.html')

# Button that will generate the unsolved Sudoku
def GenerateButton(response):
    responseData = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]
    ]
    jsonStr = json.dumps(responseData)
    return JsonResponse(jsonStr, safe=False)

# Button that will solve the unsolved Sudoku
def SolveButton(request):
    pass