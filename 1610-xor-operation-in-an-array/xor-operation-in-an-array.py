class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        count = start
        for i in range(start,start+n*2,2):
            print(i)
            count ^=i
        count^=start
        return count
        