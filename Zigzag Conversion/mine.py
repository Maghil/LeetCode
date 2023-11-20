class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x=0
        y=0
        operation=+1
        result = [[]]
        print(result)
        for i in range(0,len(s)):
            result[0].append(i)
        print(result)



if __name__=="__main__":
    s="adfadfadf"
    n=2
    a = Solution()
    a.convert(s,n)
