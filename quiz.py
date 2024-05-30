def reverse_list(l: list):
    """
    The function should return a sorted list.
    Input l is a list which can contain any type of data.
    """
    left = 0
    right = len(l) - 1
    while (left < right):
        temp = l[left]
        l[left] = l[right]
        l[right] = temp
        left += 1
        right -= 1
    return l


def solve_sudoku(matrix):
    """
    Args:
        matrix (list): 9x9 matrix representing the Sudoku puzzle.
        row (list): 9x9 matrix to track numbers in each row.
        column (list): 9x9 matrix to track numbers in each column.
        section (list): 9x9 matrix to track numbers in each 3x3 section.

    Returns:
        bool: True if the Sudoku puzzle is solvable, False otherwise.
    """
    def helper(matrix, row, column, section):
        for i in range(9):
            for j in range(9):
                if not matrix[i][j]:
                    for k in range(1, 10):
                        if (row[i][k-1] or column[j][k-1] or section[i//3*3+i % 3][k-1]):
                            continue
                        matrix[i][j] = k
                        row[i][k-1] = column[j][k -
                                                1] = section[i//3*3+i % 3][k-1] = 1
                        if (helper(matrix, row, column, section)):
                            return True
                        row[i][k-1] = column[j][k -
                                                1] = section[i//3*3+i % 3][k-1] = 0
                    return False
        return True

    # Initialize matrices to track numbers in each row, column, and section
    row = [[0 for _ in range(9)] for _ in range(9)]
    column = [[0 for _ in range(9)] for _ in range(9)]
    section = [[0 for _ in range(9)] for _ in range(9)]

    # Populate matrices with initial numbers from the Sudoku puzzle
    for i in range(9):
        for j in range(9):
            if (matrix[i][j]):
                row[i][matrix[i][j]-1] = 1
                column[j][matrix[i][j]-1] = 1
                section[i//3*3 + i % 3][matrix[i][j]-1] = 1

    return helper(matrix, row, column, section)


def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


# Example usage:
if __name__ == "__main__":
    # example_list = [1, 2, 3, 4, 5]
    # reversed_list = reverse_list(example_list)
    # print("Reversed list:", reversed_list)  # Output: [5, 4, 3, 2, 1]

    # example_str_list = ["a", "b", "c", "d"]
    # reversed_str_list = reverse_list(example_str_list)
    # print("Reversed string list:", reversed_str_list)

    # Example Sudoku board (0 represents empty cells)
    example_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(example_board):
        print("Sudoku solved successfully:")
        print_board(example_board)
    else:
        print("No solution exists.")
