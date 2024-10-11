class Solution:
    def lengthOfLastWord(self, string):
        count=0
        for i in range(len(string)-1,-1,-1):
            if count>0:
                if string[i]!= " ":
                    count+=1
                else:
                    break
            if count<=0 and string[i]!= " ":
                count+=1
        return count