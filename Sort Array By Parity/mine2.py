class Solution:
    def sortArrayByParity(self, nums):
        index = 0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[index],nums[i]=nums[i],nums[index]
                index+=1
        return nums

if __name__ == "__main__":
    a = Solution()
    print(a.sortArrayByParity([3,1,2,4]))
    print(a.sortArrayByParity([0]))
