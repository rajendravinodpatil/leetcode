class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        while n:
            if n&1:
                count+=1
            n = n>>1
        
        # for i in str(n):
        #     print("==>",i)
        #     if i=="1":
        #         count+=1
        return count
        