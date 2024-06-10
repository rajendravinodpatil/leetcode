class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub = []
        def subset_cal(idx):
            if idx>=len(nums):
                result.append(sub.copy())
                return
            
            sub.append(nums[idx])
            subset_cal(idx+1)
            sub.pop()
            subset_cal(idx+1)
        subset_cal(0)
        return result