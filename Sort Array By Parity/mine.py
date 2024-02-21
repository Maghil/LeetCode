class Solution:
    def sortArrayByParity(self, nums):
        mid= len(nums)//2
        left,right=(0,len(nums)-1)
        while left<right:
            if nums[left]%2==0:
                left+=1
            elif nums[right]%2!=0:
                right-=1
            else:
                nums[left],nums[right]=nums[right],nums[left]
        return nums
