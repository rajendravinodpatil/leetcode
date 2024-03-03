import os
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = os.path.commonprefix(strs)
        return prefix

        