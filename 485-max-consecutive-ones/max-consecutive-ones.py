class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        running_max=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count=0
            running_max=max(running_max,count)
            
        return running_max
        