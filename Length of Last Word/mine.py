class Solution:
    def lengthOfLastWord(self, string):
        split = string.split(" ")
        for word in range(len(split)-1,-1,-1):
            if split[word].isalpha():
                print(word)
                return len(split[word])


if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLastWord("Hello World"))
    print(a.lengthOfLastWord("   fly me   to   the moon  "))
    print(a.lengthOfLastWord("luffy is still joyboy"))
    print(a.lengthOfLastWord(" luffy is still joyboy a "))
