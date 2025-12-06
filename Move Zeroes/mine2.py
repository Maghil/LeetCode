class Solution:
    def moveZeroes(self, nums):
        zero_index = 0
        for i in range(0, len(nums)):
            if nums[zero_index] == 0 and nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                zero_index += 1
            if nums[zero_index] != 0:
                zero_index += 1
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.moveZeroes([0, 1, 0, 3, 12]))
    print(a.moveZeroes([0]))
    print(a.moveZeroes([0, 3, 2, 0]))
    print(a.moveZeroes([0, 0, 3, 2, 0]))
