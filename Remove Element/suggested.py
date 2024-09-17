class Solution:
    def removeElement(self, nums,value):
        index=0
        for i in range(0,len(nums)):
            if nums[i] !=value:
                nums[index]=nums[i]
                index+=1
        return index

if __name__ == "__main__":
    a = Solution()
    print(a.removeElement([1, 0, 2, 3, 0, 4, 5, 0], 0))
    print(a.removeElement([1, 2, 3], 1))
    print(a.removeElement([3, 2, 2, 3], 3))