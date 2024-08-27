class Solution:
    def removeElement(self, nums,value):
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] == value:
                while nums[end] == value and start < end:
                    end -= 1
                nums[start], nums[end]= nums[end], nums[start]
                end -= 1
            start +=1
        return end+1
