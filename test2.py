class Solution:
    def validMountainArray(self, arr) -> bool:
        i = 0
        n = len(arr)
        mark1, mark2 = False, False

        while i+1 < n and arr[i] < arr[i+1]:
            mark1 = True
            i += 1
        while i+1 < n and arr[i] > arr[i+1]:
            mark2 = True
            i += 1

        # print(mark1, mark2, i)
        if mark1 and mark2 and i == n-1:
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    print(a.validMountainArray([2, 1]))                             # False
    print(a.validMountainArray([3, 5, 5]))                          # False
    print(a.validMountainArray([1, 2, 3, 4, 5]))                    # False
    print(a.validMountainArray([0, 3, 2, 1]))                       # True
    print(a.validMountainArray([5, 4, 3, 2, 1]))                    # False
    print(a.validMountainArray([1, 2, 3, 3, 3, 3, 2, 1]))           # False
    print(a.validMountainArray([1, 3, 5, 7, 2, 1]))                 # True
    print(a.validMountainArray([[1, 1, 1, 1, 1, 1, 1, 2, 1]]))      # False
