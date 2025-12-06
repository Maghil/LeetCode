class Solution:
    def duplicateZeros(self, arr) -> None:
        zero_count = arr.count(0)
        for i in range(len(arr) -1, -1,-1):
            if arr[i] ==0:
                if i + zero_count < len(arr):
                    arr[i + zero_count] = 0
                zero_count -= 1
            if i + zero_count < len(arr):
                arr[i + zero_count] = arr[i]
    
if __name__ == "__main__":
    s = Solution()
    s.duplicateZeros([1,0,2,3,0,4,5,0])
    s.duplicateZeros([1,2,3])
    s.duplicateZeros([0])
    s.duplicateZeros([0,1])
          
    
        
