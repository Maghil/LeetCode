class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.strStr("sadbutsad", "sad"))
    print(a.strStr("leetcode", "rabbit"))
    print(a.strStr("leetcode", "leeto"))
    print(a.strStr("leetcode", "etc"))
    print(a.strStr("aaa", "aaaa"))
