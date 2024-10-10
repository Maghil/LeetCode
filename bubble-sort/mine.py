class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1):
            swapped = False
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.bubbleSort([0, 2, 1, 3, 2, 4, 5, 6, 7, 8]))
    print(a.bubbleSort([3]))
    print(a.bubbleSort([3, 2, 1]))
    print(a.bubbleSort([3, 2, 5, 6, 4, 2, 2, 1]))
    print(a.bubbleSort([2, 1]))
    print(a.bubbleSort([3, 0, 3, 3, 2, 1, 0]))
