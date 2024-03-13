class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        arr2 = range(n+1)
        for i in arr2:
            if i not in nums:
                return i
        