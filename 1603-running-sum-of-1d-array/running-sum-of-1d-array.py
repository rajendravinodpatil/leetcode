class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums2= [nums[0]]
        count = nums[0]
        for i in range(1,len(nums)):
            count+=nums[i]
            nums2.append(count)
        return nums2