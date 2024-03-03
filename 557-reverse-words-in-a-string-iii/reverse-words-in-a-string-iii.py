class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        new_s = ""
        for i in s:
            new_s+=" "+ i[::-1]
        new_s = new_s.strip()
        return new_s
        