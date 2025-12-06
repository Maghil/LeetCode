class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums 
    
if __name__ == "__main__":
    a = Solution()
    a.moveZeroes([0, 1, 0, 3, 12])
    a.moveZeroes([0])
    a.moveZeroes([0, 3, 2, 0])
    a.moveZeroes([0, 0, 3, 2, 0])
    a.moveZeroes([1, 2, 0, 0, 4, 0, 6, 0])