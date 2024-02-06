class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 0
        j = len(arr)-1
        left_fail = False
        right_fail = False
        while (not left_fail or not right_fail) and i<j:
            if arr[i] < arr[i+1]:
                i = i+1
            else:
                left_fail = True
            if arr[j] < arr[j-1]:
                j = j-1
            else:
                right_fail = True
        if i == j and i!=0 and j!=len(arr)-1:
            return True
        else:
            return False
