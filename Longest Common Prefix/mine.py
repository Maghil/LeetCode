class Solution:
    def longestCommonPrefix(self, strs) -> str:
        pattern = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or char != strs[j][i]:
                    return pattern
            pattern += char
        return pattern


if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(["flower", "flow", "flight"]))
    print(a.longestCommonPrefix(["flower", "flow", "flows"]))
    print(a.longestCommonPrefix(["dog", "racecar", "car"]))
    print(a.longestCommonPrefix(["ab", "abc", "abd"]))
    print(a.longestCommonPrefix(["flow"]))
