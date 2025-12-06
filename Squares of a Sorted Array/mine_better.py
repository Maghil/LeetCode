class Solution:
    def sortedSquares(self, nums):
        result = [1] * len(nums)
        left, right, index = 0, len(nums)-1, len(nums)-1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.sortedSquares([-4, -1, 0, 3, 10]))
    print(a.sortedSquares([-7, -3, 2, 3, 11]))
