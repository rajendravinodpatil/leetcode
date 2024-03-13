class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        if len(arr)%2!=0:
            return False
        hm = defaultdict(int)
        res = 0
        
        for i in arr:
            temp = i % k
            print("==>",temp,i,k)
            
            if temp == 0:
                res += 1
            elif k - temp in hm and hm[k - temp] != 0:
                res += 2
                hm[k - temp] -= 1
                # print("==>",hm)
            else:
                hm[temp] += 1

        return res == len(arr)


        