class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        count=0
        for elem in nums:
            if elem-1 not in num_set:
                next = elem+1
                while next in num_set:
                    next+=1
                count = max(count,next-elem)
        return count
        