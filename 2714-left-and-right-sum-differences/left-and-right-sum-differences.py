class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]
        rightsum=[0]
        for i in range(0,len(nums)-1):
            leftsum.append(leftsum[-1]+nums[i])
        for i in range(len(nums)-1,0,-1):
            rightsum.append(rightsum[-1]+nums[i])
        rightsum = rightsum[::-1]
        final = []
        for i in range(0,len(leftsum)):
            final.append(abs(leftsum[i]-rightsum[i]))
        return final
            
