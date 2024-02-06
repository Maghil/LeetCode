class Solution:
    def replaceElements(self, arr):
        max = -1
        for i in range(-1, -len(arr)-1, -1):
            if max < arr[i]:
                temp_max = arr[i]
            arr[i]=max
            max=temp_max
        return arr
