class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_element_count=1
        for i in nums:
            if i == nums[unique_element_count-1]:
                pass
            else:
                nums[unique_element_count]=i
                unique_element_count=unique_element_count+1
        return unique_element_count
