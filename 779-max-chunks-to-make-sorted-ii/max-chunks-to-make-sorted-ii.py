class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        st = []
        for i in range(0,len(arr)):
            a = arr[i]
            while st!=[] and st[-1]>arr[i]:
                a = max(a,st[-1])
                st.pop()

            st.append(a)
        return len(st)
        




        # left_max = [arr[0]]
        # right_min = [arr[-1]]
        # for i in range(1,len(arr)):
        #     left_max.append(max(arr[i],left_max[-1]))
                    
        # for j in range(len(arr)-1,0,-1):
        #     right_min.append(min(arr[j],right_min[-1]))
        # ans=0      
        # for cal in range(0,len(left_max)-1):
        #     if left_max[cal]<=right_min[cal+1]:
        #         ans+=1
        # print("==>",arr) 
        # print("==>",left_max) 
        # print("==>",right_min)
        # return ans+1