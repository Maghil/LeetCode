class Solution:
    def moveZeroes(self, nums):
        zero_array=[]
        for i in range(0,len(nums)):
            if nums[i]==0:
                zero_array.append(i)
            if nums[i]!=0 and len(zero_array)>0:
                (nums[zero_array[0]],nums[i])=(nums[i],nums[zero_array[0]])
                zero_array.pop(0)
                zero_array.append(i)