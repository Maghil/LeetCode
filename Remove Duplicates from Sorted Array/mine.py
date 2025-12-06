class Solution:
    def removeDuplicates(self, nums) -> int:
        unique_element_count=1
        for i in nums:
            if i == nums[unique_element_count-1]:
                pass
            else:
                nums[unique_element_count]=i
                unique_element_count=unique_element_count+1
        return unique_element_count

if __name__ == "__main__":
    a = Solution()
    print(a.removeDuplicates([1, 1, 1, 2, 2, 2]))
    print(a.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
    print(a.removeDuplicates([-100, 0, 1, 2, 3, 3, 4, 4]))
    print(a.removeDuplicates([1]))
    print(a.removeDuplicates([1,2]))
    print(a.removeDuplicates([1,1]))
