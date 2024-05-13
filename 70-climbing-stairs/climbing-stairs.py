class Solution:
    def climbStairs(self, n: int) -> int:
        first_no ,second_no = 1,1
        for i in range(n-1):
            temp = first_no
            first_no = first_no+second_no
            second_no = temp

        return first_no
        