class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        boolean_series=[]
        for i in candies:
            print(max(candies))
            if i+extraCandies>=max(candies):
                boolean_series.append(True)
            else:
                boolean_series.append(False)
        return boolean_series

        