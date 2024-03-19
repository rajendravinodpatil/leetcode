class Solution:
    def maximum(self,a,b,c):
        if a>b:
            return max(a,c)
        else:
            return max(b,c)

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        max1 = -sys.maxsize-1
        min1 = sys.maxsize
        max2 = -sys.maxsize-1
        min2 = sys.maxsize
        max3 = -sys.maxsize-1
        min3 = sys.maxsize
        max4 = -sys.maxsize-1
        min4 = sys.maxsize 
        i=0
        while i<len(arr1):
            val1 = arr1[i] + arr2[i]+ i            
            val2 = arr1[i] + arr2[i] - i
            val3 = arr1[i] - arr2[i] + i
            val4 = arr1[i] - arr2[i]- i

            max1 = max(max1,val1)
            min1 = min(min1,val1)
            max2 = max(max2,val2)
            min2 = min(min2,val2)
            max3 = max(max3,val3)
            min3 = min(min3,val3)
            max4 = max(max4,val4)
            min4 = min(min4,val4)
            i+=1
        c1 = max1-min1
        c2 = max2-min2
        c3 = max3-min3
        c4 = max4-min4

        final = self.maximum(c1,c2,c3)
        return max(final,c4)
