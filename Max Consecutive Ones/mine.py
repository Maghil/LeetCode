class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_len, cur_len=0, 0
        for num in nums:
            if num==0:
                max_len = cur_len if cur_len > max_len else max_len
                cur_len=0
            else:
                cur_len+=1
        return max_len if max_len > cur_len else cur_len
