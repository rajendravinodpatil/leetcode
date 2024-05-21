class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list1 = [nums[0]]
        final = []
        for i in range(1,len(nums)):
            list1.append(nums[i])
            if len(list1)==2:
                freq = list1[0]
                val = list1[1]
                for j  in range(0,freq):
                    final.append(val)
                list1.clear()
        return final
            
    