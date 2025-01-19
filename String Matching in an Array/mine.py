class Solution:
    def stringMatching(self, words):
        result=[]
        for word in words:
            for word2 in words:
                if len(word) < len(word2) and word in word2:
                    result.append(word)
                    break
        return result

if __name__ == "__main__":
    a = Solution()
    print(a.stringMatching(["mass", "as", "hero", "superhero"]))
    print(a.stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
