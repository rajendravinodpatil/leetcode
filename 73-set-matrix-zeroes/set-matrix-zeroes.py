class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] ==0:
                    self.wholezero(matrix,row-1,column,"U")
                    self.wholezero(matrix,row+1,column,"D")
                    self.wholezero(matrix,row,column-1,"L")
                    self.wholezero(matrix,row,column+1,"R")
        
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] =="*":
                    matrix[row][column]=0
        return matrix
    
    def wholezero(self,matrix,row,column,direction):
        if (0<=row<len(matrix)) and (0<=column<len(matrix[0])) and (matrix[row][column]!=0):
            matrix[row][column]="*"
            if direction=="U":
                self.wholezero(matrix,row-1,column,"U")

            if direction=="D":
                self.wholezero(matrix,row+1,column,"D")

            if direction=="L":
                self.wholezero(matrix,row,column-1,"L")

            if direction=="R":
                self.wholezero(matrix,row,column+1,"R")
