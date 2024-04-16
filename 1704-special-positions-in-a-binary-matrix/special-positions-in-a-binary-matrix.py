class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        row=len(mat)
        column=len(mat[0])
        for i in range(row):
            for j in range(column):
                if mat[i][j] == 1 and sum(mat[i]) == 1 and sum(row[j] for row in mat) == 1:
                    count += 1
        return count