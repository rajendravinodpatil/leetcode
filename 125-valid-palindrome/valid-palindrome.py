class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for i in s:
            if i.isalnum()==True:
                new_s+=i
        if new_s.lower()==new_s[::-1].lower():
            return True
        else:
            return False
        