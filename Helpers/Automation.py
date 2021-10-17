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