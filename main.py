def spiral(cols, rows):
    '''
    Возвращает матрицу размера cols x rows, заполненую числами от 1 до cols*rows в виде спирали.
    '''
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    border_top = 0
    border_left = 0
    border_right = cols - 1
    border_bottom = rows - 1
    num = 1

    #! Возможно для случаев когда кол-во строк или столбцов == 0
    #! есть вариант исправить алгоритм чтобы он обрабатывал их нормально.
    #! Однако я и так много времени упустил. 
    if cols == 1:
        return [[i] for i in range(1, rows+1)]
    elif rows == 1:
        return [[i for i in range(1, cols+1)]]
    elif rows == 0 or cols == 0:
        return []
    else:
        while border_left <= border_right and border_top <= border_bottom and num != rows * cols + 1:
            # вправо
            if n != rows * cols + 1:
                for i in range(border_left, border_right + 1):
                    matrix[border_top][i] = num
                    num += 1
                border_top += 1

            # вниз
            if num != rows * cols + 1:
                for i in range(border_top, border_bottom + 1):
                    matrix[i][border_right] = num
                    num += 1
                border_right -= 1

            # влево
            if num != rows * cols + 1:
                for i in range(border_right, border_left - 1, -1):
                    matrix[border_bottom][i] = num
                    num += 1
                border_bottom -= 1

            # вверх
            if num != rows * cols + 1:
                for i in range(border_bottom, border_top - 1, -1):
                    matrix[i][border_left] = num
                    num += 1
                border_left += 1

        return matrix


if __name__ == '__main__':
    # n - столбцы
    # m - строки
    m, n = map(int, input().split())
    result = spiral(n, m)
    with open("output.txt", "w") as f:
        for elem in result:
            text = " ".join(['%3i' % i for i in elem]) + "\n"
            f.write(text)

    #* для отладки в терминале
    # import numpy as np
    # print(np.matrix(result))