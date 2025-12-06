class Solution:
    def moveZeroes(self, nums):
        index = 0
        for i in range(0, len(nums)):
            if nums[index] == 0 and nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
            if nums[index] != 0:
                index += 1
        print(nums)


if __name__ == "__main__":
    a = Solution()
    a.moveZeroes([0, 1, 0, 3, 12])
    a.moveZeroes([0])
    a.moveZeroes([0, 3, 2, 0])
    a.moveZeroes([0, 0, 3, 2, 0])
    a.moveZeroes([1, 2, 0, 0, 4, 0, 6, 0])
