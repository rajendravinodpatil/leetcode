class Solution:
    def isHappy(self, n: int) -> bool: 
        
        while n>=1:
            print("==>",n)
            cal = 0
            for i in str(n):
                cal += int(i)*int(i)
                print("cal ==>",cal)
            if cal==1:
                return True
            elif cal==4:
                return False
            n=cal
        return False

        
        