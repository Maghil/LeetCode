class Solution:
    def findDisappearedNumbers(self, nums):
        result = []
        for num in nums:
            num = abs(num)
            if nums[num-1] > 0:
                nums[num-1] = -nums[num-1]
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.findDisappearedNumbers([5, 1, 2, 3, 4]))
    print(a.findDisappearedNumbers([1, 2, 3, 4, 5]))
    print(a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
    print(a.findDisappearedNumbers([1, 1, 4, 2, 1, 3]))
