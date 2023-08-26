class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char={}
        count=0
        longest_count=0
        for i in s:
            if i in char:
                if count>longest_count:
                    longest_count=count
                count=1
                char={}
                char[i]=1
            else:
                char[i]=1
                count+=1
        if count> longest_count:
            longest_count=count
        return longest_count

