#
# uses space O(1) it uses same list as order check
#
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            temp = (abs(num)-1)
            if nums[temp] > 0:
                nums[temp] = -nums[temp]
        return[i+1 for i in range(len(nums)) if nums[i] > 0]
