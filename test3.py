class Solution:
    def validMountainArray(self, arr) -> bool:
        i, length = 0, len(arr)
        increased, decreased = False, False
        while i < length-1 and arr[i] < arr[i+1]:
            increased = True
            i += 1
        while i < length - 1 and arr[i] > arr[i+1]:
            decreased = True
            i += 1
        return increased and decreased and i == length-1


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