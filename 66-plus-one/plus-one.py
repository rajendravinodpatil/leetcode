class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit=""
        for i in digits:
            new_digit+=str(i)
        new_digit=int(new_digit)+1
        digits.clear()
        for j in str(new_digit):
            digits.append(int(j))
        return digits

        