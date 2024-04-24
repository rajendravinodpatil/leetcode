class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        output=1
        
        if (dividend<0 and divisor>=0) or (dividend>0 and divisor<=0):
            sign=-1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        output=0
        while dividend>=divisor:
            tmp = divisor
            mul=1
            while dividend>=tmp:
                dividend -= tmp 
                output+=mul
                mul+=mul
                tmp+=tmp

        return min(2**31-1,max(-2**31,sign*output))        