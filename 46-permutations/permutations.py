class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums)==1:
            return [nums[:]]
        for  num in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for per in perms:
                per.append(n)
            result.extend(perms)
            nums.append(n)
        return result
        