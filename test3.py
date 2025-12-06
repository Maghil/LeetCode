class Solution:
    def removeDuplicates(self, nums) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[index] < nums[i]:
                index+=1
                nums[index] = nums[i]
        return index +1
    
if __name__ == "__main__":
    a = Solution()
    print(a.removeDuplicates([1, 1, 1, 2, 2, 2]))
    print(a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(a.removeDuplicates([-100, 0, 1, 2, 3, 3, 4, 4]))
    print(a.removeDuplicates([1]))
    print(a.removeDuplicates([1, 2]))
    print(a.removeDuplicates([1, 1]))
