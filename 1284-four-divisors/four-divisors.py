class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sum_count = 0
        square = 0
        for num in nums:
            square = int(math.sqrt(num))
            if square*square==num:
                continue
            tmpres=num+1
            count = 0
            for i in range(2,square+1):
                if num%i==0:
                    count+=1
                    tmpres+=(i+num/i)
                if count>1:
                    break
            if count==1:
                sum_count+=tmpres
        return int(sum_count)