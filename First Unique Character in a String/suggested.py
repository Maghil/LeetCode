class Solution:
    def firstUniqChar(self, str):
        counter={}
        for char in str:
            counter[char] = counter.get(char,0)+1
        for i in range(len(str)):
            if counter[str[i]] == 1:
                return i
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.firstUniqChar("leetcode"))
    print(a.firstUniqChar("loveleetcode"))
    print(a.firstUniqChar("aabb"))
