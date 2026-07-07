class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        i,j = len(a), len(b)


if __name__ == "__main__":
    a = Solution()
    a.addBinary("11", "1")
    a.addBinary("1010", "1011")
m