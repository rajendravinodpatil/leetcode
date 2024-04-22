class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single=0
        for i in range(0,len(nums)):
            single = nums[i]^single
        return single