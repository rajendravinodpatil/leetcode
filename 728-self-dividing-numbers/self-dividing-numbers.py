class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        selfvalueno = []
        for number in range(left,right+1):
            count=0
            digits=str(number)
            for digit in digits:
                if '0' !=digit and number%int(digit)==0:
                    count+=1
            if count==len(digits):
                selfvalueno.append(number)
        return selfvalueno


        