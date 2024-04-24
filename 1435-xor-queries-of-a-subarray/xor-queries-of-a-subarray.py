class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # for i in range(0,len(queries)):
        #     xor_output = 0
        #     for j in range(queries[i][0],queries[i][1]+1):
        #         xor_output = xor_output^arr[j]
        #     final_list.append(xor_output)
        n = len(arr)
        prefix = [0 for _ in range(n+1)]
        print("==>",prefix)
        for i in range(n):
            prefix[i+1]=prefix[i]^arr[i]
        print("==>",prefix)
        output = []
        for l,r in queries:
            output.append(prefix[r+1]^prefix[l])
        return output
