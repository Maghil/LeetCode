class Solution:
    def reverseOnlyLetters(self, str):
        i,j=0,len(str)-1
        str = list(str)
        while i<j:
            if str[i].isalpha():
                if str[j].isalpha():
                    str[i],str[j]=str[j],str[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        return "".join(str)

if __name__ == "__main__":
    a = Solution()
    print(a.reverseOnlyLetters("abc---def"))  #fed---cba
    print(a.reverseOnlyLetters("---abc---"))  #---cba---
    print(a.reverseOnlyLetters("Test1ng-Leet=code-Q!")) #Qedo1ct-eeLg=ntse-T!
