class Solution:
    def validMountainArray(self, arr) -> bool:
        i, j, n = 0, len(arr) - 1, len(arr)
        while i+1 < n and arr[i] < arr[i+1]:
            i += 1
        while j > 0 and arr[j] < arr[j-1]:
            j -= 1
        return 0 < i == j < n-1


if __name__ == "__main__":
    a = Solution()
    print(a.validMountainArray([2, 1]))                    # False
    print(a.validMountainArray([3, 5, 5]))                 # False
    print(a.validMountainArray([0, 3, 2, 1]))              # True
    print(a.validMountainArray([1, 2, 3, 4, 5]))           # False
    print(a.validMountainArray([5, 4, 3, 2, 1]))           # False
    print(a.validMountainArray([1, 2, 3, 3, 3, 3, 2, 1]))  # False
    print(a.validMountainArray([1,3,5,7,2,1]))             # True
