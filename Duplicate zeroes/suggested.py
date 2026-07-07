class Solution:
    def duplicateZeros(self, arr) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


if __name__ == "__main__":
    s = Solution()
    s.duplicateZeros([1,0,2,3,0,4,5,0])
    s.duplicateZeros([1,2,3])
    s.duplicateZeros([0])
    s.duplicateZeros([0,1])