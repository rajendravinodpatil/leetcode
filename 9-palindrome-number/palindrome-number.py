class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x).strip()==str(x)[::-1].strip():
            return(True)
        else:
            return(False)
        