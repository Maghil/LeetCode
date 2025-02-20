class Solution:
    def searchRange(self, nums, target):
        self.nums = nums
        self.target = target

        def binarySearch(side):
            left = 0
            right = len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    index = mid
                    if side == -1:
                        right = mid-1
                    else:
                        left = mid+1
            return index
        left = binarySearch(-1)
        right = binarySearch(1)
        return [left, right]

if __name__ == "__main__":
    a = Solution()
    print(a.searchRange([1, 2, 2, 3, 4, 4, 4,
          5, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10], 4))
    print(a.searchRange([2, 2, 4, 4, 6, 6, 8, 8, 10, 10], 2))
    print(a.searchRange([1, 3, 5, 7, 9], 10))
