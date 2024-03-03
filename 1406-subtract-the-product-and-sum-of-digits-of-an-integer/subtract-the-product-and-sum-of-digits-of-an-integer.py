class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sum_of_digit = 0
        product_of_digit = 1
        for i in n:
            sum_of_digit += int(i)
            product_of_digit*=int(i)
        
        return product_of_digit-sum_of_digit

        