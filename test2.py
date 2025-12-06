class Solution:
    def removeElement(self, nums, val) -> int:
        val_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[val_index] = nums[i]
                val_index += 1
        return val_index

if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([1, 2, 3, 0, 0, 0], 3))
    print(a.removeElement([3, 2, 2, 3], val=3))
    print(a.removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))
