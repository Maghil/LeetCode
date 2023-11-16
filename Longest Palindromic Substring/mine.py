class Solution:
    def longestPalindrome(self, s: str) -> str:
        existing = (0, 0)
        for i in range(0, len(s)):
            for j in range(len(s)-1, i, -1):
                if s[i] == s[j]:
                    if (j-i+1 > existing[1]-existing[0]+1):
                        if self.isPalindrome(s, i, j):
                            existing = (i, j)
        return s[existing[0]:existing[1]+1]

    def isPalindrome(self, s: str, start: int, end: int) -> bool:
        for i in range(0, (end-start+1)//2):
            if not (s[start+i] == s[end-i]):
                return False
        return True
