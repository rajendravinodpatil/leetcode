class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat)*len(mat[0]))!=(r*c):
            return mat
        output = []
        row = []
        col_num = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if col_num==c:
                    output.append(list(row))
                    row.clear()
                    col_num=0
                row.append(mat[i][j])
                col_num+=1
        if row:
            output.append(list(row))
     
        print(output)
        return output



    