class Solution:
    def removeElement(self, nums, val) -> int:
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.pop(i)
            else:
                i=i+1
        return i
