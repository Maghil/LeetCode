class Solution:
    def removeElement(self, nums,value):
        index=0
        for i in range(0,len(nums)):
            if nums[i] !=value:
                nums[index]=nums[i]
                index+=1
        return index