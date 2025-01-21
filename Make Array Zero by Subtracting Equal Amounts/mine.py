class Solution:
    def minimumOperations(self, nums) -> int:
        nums= set(nums)
        nums.discard(0)
        return len(nums)

if __name__ == "__main__":
    a=Solution()
    print(a.minimumOperations([3,2,1,6,0]))