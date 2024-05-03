class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcount=0
        rcount = 0
        split_count = 0
        for i in s:
            if i=="L":
                lcount+=1
            if i=="R":
                rcount+=1
            if lcount==rcount:
                split_count+=1
        return split_count
        