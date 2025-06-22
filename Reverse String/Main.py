class Solution:
    def reverseString(self, s) -> None:
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        return s

if __name__ == "__main__":
    a = Solution()
    print(a.reverseString(["h","e","l","l","o"]))
    print(a.reverseString(["H","a","n","n","a","h"]))
    print(a.reverseString(["a"]))
