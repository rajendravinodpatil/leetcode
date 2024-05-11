class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW,COLS = len(matrix),len(matrix[0])
        self.prefix_mat = [[0]*(COLS+1) for _ in range(ROW+1)]
        for r in range(ROW):
            prefix=0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefix_mat[r][c+1]
                self.prefix_mat[r+1][c+1] = prefix + above
        print("==>",self.prefix_mat)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1
        print("==>",row1,col1,row2,row2)
        bottom_right = self.prefix_mat[row2][col2]
        above = self.prefix_mat[row1-1][col2]
        left = self.prefix_mat[row2][col1-1]
        topleft = self.prefix_mat[row1-1][col1-1]
        return bottom_right-above-left+topleft
        
             
            


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)