class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        for i in range(len(haystack) - (n_len-1)):
            if haystack[i] == needle[0] and haystack[i+(n_len-1)] == needle[n_len-1]:
                for j in range(0, n_len):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == n_len-1:
                        return i
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.strStr("sadbutsad", "sad"))
    print(a.strStr("leetcode", "code"))
    print(a.strStr("leetcode", "leeto"))
    print(a.strStr("leetcode", "etc"))
    print(a.strStr("aaa", "aaaa"))
    print(a.strStr("hello", "ll"))

# 0 1 2 3 4 5 6 7
# l e e t c o d e       8
# c o d e               4
