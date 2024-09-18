class Solution:
    def binarySearch(self, nums, key):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            print(left, right, mid)
            if nums[mid] == key:
                return mid
            elif key < nums[mid]:
                right = mid
            else:
                left = mid
            # print(nums[left],nums[right],nums[mid])


if __name__ == "__main__":
    a = Solution()
    print(a.binarySearch([-7, -4, 0, 1, 2, 4, 6, 7, 8, 9], 1))
    print(a.binarySearch([0, 1, 2, 4, 6, 8], 4))
    print(a.binarySearch([-10, -9, -8, -5, -4, -2, -1, 5, 9, 10], -2))