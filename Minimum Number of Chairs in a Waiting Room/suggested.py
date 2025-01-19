class Solution:
    def minimumChairs(self, s: str) -> int:

        arr = map(lambda x: 1 if x == 'E' else -1, s) 
        return max(accumulate(arr))