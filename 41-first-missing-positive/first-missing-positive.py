class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        def main(nums,target):
            l=0
            r=len(nums)-1
            while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    return True
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return False    

        for i in range(1,5000000):
                result = main(nums,i)
                if result==False:
                    return i
                