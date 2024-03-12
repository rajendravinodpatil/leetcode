class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
        # for i in range(0,len(nums)):
        #     print(target)
        #     if nums[i]==target:
        #         return i
        #     else:
        #         return -1
        