class Solution:
    def pivotIndex(self, nums) -> int:
        left_sum = total_sum = 0
        for num in nums:
            total_sum += num
        for i in range(len(nums)):
            if left_sum * 2 == total_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.pivotIndex([-10, 10, 10, -10]))
    print(a.pivotIndex([-10, 10, 1, 10, -10]))
    print(a.pivotIndex([1]))
    print(a.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(a.pivotIndex([1, 2, 3]))
    print(a.pivotIndex([2, 1, -1]))
