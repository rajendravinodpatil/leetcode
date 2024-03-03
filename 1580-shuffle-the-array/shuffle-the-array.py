class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x_series = nums[:n]
        y_series = nums[n:]
        nums.clear()
        for i in range(0,n):
            nums.append(x_series[i])
            nums.append(y_series[i])
        return nums

        