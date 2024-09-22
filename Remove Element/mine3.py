class Solution:
    def removeElement(self, nums, val):
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter],nums[i]=nums[i],nums[counter]
                counter += 1
        return counter

if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([1, 2, 3, 0, 0, 0], 3))
    print(a.removeElement([3, 2, 2, 3], val=3))
    print(a.removeElement([0, 1, 2, 2, 3, 0, 4, 2], val=2))
