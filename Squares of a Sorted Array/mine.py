class Solution:
    def sortedSquares(self, nums):
        result = []
        left = 0
        right = len(nums)-1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.insert(0, nums[right] * nums[right])
                right = right-1
            else:
                result.insert(0, nums[left]*nums[left])
                left = left+1
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.sortedSquares([-4, -1, 0, 3, 10]))
