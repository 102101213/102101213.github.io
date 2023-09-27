import random
import threading

# 生成数独谜题
def generate_sudoku():
    sudoku = [[0] * 9 for _ in range(9)]
    fill_cell(sudoku, 0, 0)
    remove_cells(sudoku, 40)
    return sudoku

# 递归填充数独谜题的单元格
def fill_cell(sudoku, row, col):
    if col >= 9:
        col = 0
        row += 1
        if row >= 9:
            return True

    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for num in numbers:
        if is_number_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            if fill_cell(sudoku, row, col + 1):
                return True
            sudoku[row][col] = 0

    return False

# 检查数独谜题中数字的合法性
def is_number_valid(sudoku, row, col, num):
    if num in sudoku[row]:
        return False

    for i in range(9):
        if num == sudoku[i][col]:
            return False

    box_row = row - row % 3
    box_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if num == sudoku[box_row + i][box_col + j]:
                return False

    return True

# 随机移除数独谜题中的数字
def remove_cells(sudoku, count):
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)

    for cell in cells:
        row, col = cell
        temp = sudoku[row][col]
        sudoku[row][col] = 0
        solution_count = count_solutions(sudoku)
        if solution_count != 1:
            sudoku[row][col] = temp
            continue

        count -= 1
        if count == 0:
            return

# 计算数独谜题的解的数量
def count_solutions(sudoku):
    count = [0]

    def solve_sudoku(sudoku):
        empty_location = find_empty_location(sudoku)
        if not empty_location:
            count[0] += 1
            return

        row, col = empty_location

        for num in range(1, 10):
            if is_number_valid(sudoku, row, col, num):
                sudoku[row][col] = num
                solve_sudoku(sudoku)
                sudoku[row][col] = 0

    solve_sudoku(sudoku)
    return count[0]

# 寻找数独谜题中的空白位置
def find_empty_location(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                return row, col
    return None

# 生成数独谜题的线程类
class SudokuGeneratorThread(threading.Thread):
    def __init__(self, index):
        super().__init__()
        self.index = index
        self.sudoku = None

    def run(self):
        self.sudoku = generate_sudoku()

# 创建9个线程并生成数独谜题
threads = []
sudokus = []

for i in range(9):
    thread = SudokuGeneratorThread(i)
    thread.start()
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()
    sudokus.append(thread.sudoku)

# 打印生成的数独谜题
for sudoku in sudokus:
    for row in sudoku:
        print(" ".join(str(num) for num in row))
    print()


