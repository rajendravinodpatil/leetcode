class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        output = []
        for i in nums:
            i=str(i)
            i=list(i)
            digit = max(i)
            digit = digit*len(i)
            output.append(int(digit))
        return sum(output)
           
        