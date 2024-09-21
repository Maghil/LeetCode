class Solution:
    def binarySearch(self, arr, low, high, x):
        if high >= low:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, low, mid-1, x)
            else:
                return self.binarySearch(arr, mid + 1, high, x)
        else:
            return -1


if __name__ == "__main__":
    a = Solution()
    print(a.binarySearch([-7, -4, 0, 1, 2, 4, 6, 7, 8, 9], 0, 9, 1))
    print(a.binarySearch([0, 1, 2, 3, 4, 5], 0, 5, 0))
    print(a.binarySearch([-10, -9, -8, -5, -4, -2, -1, 5, 9, 10], 0, 9, -2))
