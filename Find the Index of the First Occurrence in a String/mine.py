class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(0, (len(haystack)+1)-len(needle)):
            matched = True
            if haystack[i] == needle[0] and haystack[i+len(needle)-1] == needle[-1]:
                for j in range(0, len(needle)-1):
                    if haystack[i+j] == needle[j]:
                        pass
                    else:
                        matched = False
                        break
                if matched:
                    return i
                else:
                    pass
        return -1


if __name__ == "__main__":
    a = Solution()
    a.strStr("sadbutsad", "sad")
    a.strStr("leetcode", "rabbit")
    a.strStr("leetcode", "leeto")
    a.strStr("leetcode", "etc")
    a.strStr("aaa", "aaaa")
