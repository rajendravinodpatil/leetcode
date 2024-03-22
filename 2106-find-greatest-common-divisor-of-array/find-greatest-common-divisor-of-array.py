class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd_count = 0
        nums.sort()
        temp = min(nums[0],nums[-1])
        for i in range(1,temp+1):
            if (nums[0]%i==0) and (nums[-1]%i==0):
                gcd_count=i
        return gcd_count
        