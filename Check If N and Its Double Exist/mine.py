class Solution:
    def checkIfExist(self, arr) -> bool:
        length=len(arr)
        for i in range(length):
            for j in range(i+1,length):
                if arr[i]/2 == arr[j] or arr[i]*2 == arr[j]:
                    return True
        return False
