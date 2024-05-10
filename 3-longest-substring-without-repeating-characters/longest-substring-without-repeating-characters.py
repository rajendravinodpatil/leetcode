class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        l = 0
        r = 0
        max_count = 0
        while r<len(s):
            if s[r] not in hash_set:
                print("hash_set ==>",hash_set)
                hash_set.add(s[r])
                r+=1
                max_count = max(len(hash_set),max_count)

            else:
                hash_set.remove(s[l])
                l+=1

        return max_count









        # hash_set = defaultdict(set)
        # max_length = 0
        # last_combination = ""
        # for i in range(0, len(s)):
        #     if s[i] not in hash_set:
        #         hash_set.add(s[i])
        #         last_combination += s[i]
        #         max_length+=1
        #     if s[i] in hash_set:
        #         if max_length <= len(last_combination):
        #             max_length = len(last_combination)
        #             last_combination = ""
        #             hash_set.clear()
        # return len(last_combination)
        


        
        