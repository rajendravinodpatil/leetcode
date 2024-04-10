class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # even_list = []
        # odd_list = []
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         even_list.append(nums[i])
        #     else:
        #         odd_list.append((nums[i]))

        # even_list.extend(odd_list)
        # print(even_list)
        # return even_list
        i = 0
        j = 0

        while i < len(nums):
            if nums[i] % 2 == 0:
                [nums[i], nums[j]] = [nums[j], nums[i]]
                i += 1
                j += 1
            else:
                i += 1

        return nums