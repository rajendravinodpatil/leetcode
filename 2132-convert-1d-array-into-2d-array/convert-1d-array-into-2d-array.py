class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        ans = [[] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                x =original.pop(0)
                ans[i].append(x)
        return ans