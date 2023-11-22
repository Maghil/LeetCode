class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        x = 0
        operation = -1
        result = []
        for i in range(0, len(s)):
            if len(result) < numRows:
                result.append([])
            result[x].append(s[i])
            if i % (numRows-1) == 0:
                operation = operation*-1
            x = x+operation
        for i in range(len(result)):
            result[i] = ''.join(result[i])
        return ''.join(result)
