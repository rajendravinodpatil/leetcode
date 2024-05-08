class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        binary_list = []
        output = 0
        for num in range(len(nums)):
            binary_num = bin(nums[num])[2:]
            padding_binary = binary_num.zfill(32)
            binary_list.append(padding_binary)

        for i in range(32):
            one_count = 0
            zero_count = 0
            for bin_val in binary_list:
                if bin_val[i]=='1':
                    one_count+=1
                else:
                    zero_count+=1

            output+=one_count*zero_count
        return output
            





        # distance = 0
        # count = 0
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         distance = nums[i]^nums[j]
        #         distance = bin(distance)[2:]
        #         for k in str(distance):
        #             if k=="1":
        #                 count+=1
        # return count