class Solution:
    def moveZeroes(self, nums):
        zero_array=[]
        for i in range(0,len(nums)):
            if nums[i]==0:
                zero_array.append(i)
            if nums[i]!=0 and len(zero_array)>0:
                (nums[zero_array[0]],nums[i])=(nums[i],nums[zero_array[0]])
                zero_array.pop(0)
                zero_array.append(i)

if __name__ == "__main__":
    a = Solution()
    a.moveZeroes([0, 1, 0, 3, 12])
    a.moveZeroes([0])
    a.moveZeroes([0, 3, 2, 0])
    a.moveZeroes([0, 0, 3, 2, 0])
    a.moveZeroes([1, 2, 0, 0, 4, 0, 6, 0])
