class Solution:
    def removeDuplicates(self, nums):
        index = 1
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index += 1
        return index

if __name__ == "__main__":
    a = Solution()
    print(a.removeDuplicates([1, 1, 1, 2, 2, 2]))
    print(a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(a.removeDuplicates([-100, 0, 1, 2, 3, 3, 4, 4]))
    print(a.removeDuplicates([1]))
    print(a.removeDuplicates([1,2]))
    print(a.removeDuplicates([1,1]))
