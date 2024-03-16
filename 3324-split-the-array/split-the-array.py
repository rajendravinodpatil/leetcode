class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):
            print("==>",nums.count(nums[i]))
            if nums.count(nums[i])>2:
                return False
        return True
        