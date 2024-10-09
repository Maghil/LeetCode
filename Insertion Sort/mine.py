class Solution:
    def insertionSort(self, nums):
        if len(nums) < 1:
            return nums
        for i in range(1, len(nums)):
            index = i-1
            key = nums[i]
            while index >= 0 and key < nums[index]:
                nums[index+1] = nums[index]
                index -= 1
            nums[index+1] = key
        return nums


if __name__ == "__main__":
    a = Solution()
    print(a.insertionSort([0, 2, 1, 3, 2, 4, 5, 6, 7, 8]))
    print(a.insertionSort([3]))
    print(a.insertionSort([0, 3, 2, 1]))
    print(a.insertionSort([2, 1]))
    print(a.insertionSort([3, 0, 3, 3, 2, 1, 0]))
