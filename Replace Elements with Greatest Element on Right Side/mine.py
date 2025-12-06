class Solution:
    def replaceElements(self, arr):
        max = -1
        for i in range(-1, -len(arr)-1, -1):
            if max < arr[i]:
                temp_max = arr[i]
            arr[i]=max
            max=temp_max
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.replaceElements([17, 18, 5, 4, 6, 1]))
    print(s.replaceElements([400]))
    print(s.replaceElements([1, 2, 3, 4, 0]))
