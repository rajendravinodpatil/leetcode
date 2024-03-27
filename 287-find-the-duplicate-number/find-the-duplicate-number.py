class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        final = set()
        l=0
        r=len(nums)-1
        while l<=r:
            print("l ==>",nums[l])
            print("r ==>",nums[r])
            if nums[l] not in final:
                final.add(nums[l])
            else:               
                return nums[l]
            if nums[r] not in final:
                final.add(nums[r])
            else:
                return nums[r]
            l+=1
            r-=1
        print("==>",final)
        