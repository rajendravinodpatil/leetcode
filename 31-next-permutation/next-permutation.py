class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        pivit = None
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                pivit =i-1
                break
        else:
            nums.reverse()
            return 
        swap=len(nums)-1
        while nums[swap]<=nums[pivit]:
            swap-=1
        nums[pivit],nums[swap]=nums[swap],nums[pivit]
        nums[pivit+1:]=reversed(nums[pivit+1:])
        return 
        


            
        
        