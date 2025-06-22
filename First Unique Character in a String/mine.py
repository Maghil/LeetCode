class Solution:
    def firstUniqChar(self, str):
        count={}
        for i in str:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        for key, value in count.items():
            if value ==1:
                return str.index(key)
        return -1


if __name__ == "__main__":
    a = Solution()
    print(a.firstUniqChar("leetcode"))
    print(a.firstUniqChar("loveleetcode"))
    print(a.firstUniqChar("aabb"))
