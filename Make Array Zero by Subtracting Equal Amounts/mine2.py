class Solution:
    def minimumOperations(self, nums) -> int:
        return len(set(nums)-{0})

if __name__ == "__main__":
    a=Solution()
    print(a.minimumOperations([3,2,1,6,0]))