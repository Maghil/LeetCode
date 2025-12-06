class Solution:
    def insertionSort(self, nums):
        for i in range(0, len(nums)):
            index = i
            key = nums[index]
            while index > 0 and nums[index-1] > key:
                nums[index] = nums[index-1]
                index -= 1
            nums[index] = key
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.insertionSort([0, 2, 1, 3, 2, 4, 5, 6, 7, 8]))
    print(a.insertionSort([3]))
    print(a.insertionSort([0, 3, 2, 1]))
    print(a.insertionSort([2, 1]))
    print(a.insertionSort([3, 0, 3, 3, 2, 1, 0]))
