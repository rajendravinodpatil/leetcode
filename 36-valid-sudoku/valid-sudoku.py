class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        column_dict = defaultdict(set)
        matrix_dict = defaultdict(set)
        for row in range(9):
            for column in range(9):
                num = board[row][column]

                if not num.isdigit():
                    continue

                matix = (row // 3, column // 3)
                if num in row_dict[row] or num in column_dict[column] or num in matrix_dict[matix]:
                    return False
                else:
                    row_dict[row].add(num)
                    column_dict[column].add(num)
                    matrix_dict[matix].add(num)
        return True
