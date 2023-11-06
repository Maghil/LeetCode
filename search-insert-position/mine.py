class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1   
        while start<end and start+end>-1:
            middle=(start+end)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start=middle+1
            else:
                end=middle-1
        if target > nums[start]:
            if(start+1)>len(nums):
                return start
            return start+1
        else:
            if(start-1)<len(nums):
                return start
            return start-1
