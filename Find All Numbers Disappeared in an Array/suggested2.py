#
# uses space O(1) it uses same list as order check
#
class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            temp = (abs(num)-1)
            if nums[temp] > 0:
                nums[temp] = -nums[temp]
        return [i+1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    a = Solution()
    print(a.findDisappearedNumbers([1, 1, 4, 2, 1, 3]))
    print(a.findDisappearedNumbers([5, 1, 2, 3, 4]))
    print(a.findDisappearedNumbers([1, 2, 3, 4, 5]))
    print(a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
