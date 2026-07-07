import timeit

setup_mine = '''
class Solution:
    def strStr(self, haystack, needle):
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
        return -1
a = Solution()
'''

setup_suggested2 = '''
class Solution:
    def strStr(self, haystack, needle):
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
        return -1
a = Solution()
'''

tests = [
    ("sadbutsad/sad", 'a.strStr("sadbutsad", "sad")'),
    ("leetcode/rabbit", 'a.strStr("leetcode", "rabbit")'),
    ("aaa/aaaa", 'a.strStr("aaa", "aaaa")'),
    ("large (10k a + ab)", 'a.strStr("a" * 10000 + "ab", "ab")'),
]

print(f"{'Test':<20} {'mine.py':<15} {'suggested2.py':<15}")
print("-" * 50)
for name, stmt in tests:
    t1 = timeit.timeit(stmt, setup=setup_mine, number=10000)
    t2 = timeit.timeit(stmt, setup=setup_suggested2, number=10000)
    print(f"{name:<20} {t1:.4f}s        {t2:.4f}s")
