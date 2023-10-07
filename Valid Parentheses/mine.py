class Solution:
    def isValid(self, s: str) -> bool:
        char_stack=[]
        mapping={"{":"}","[":"]","(":")"}
        for i in s:
            if i in ("{","[","("):
                char_stack.append(i)
            elif len(char_stack)>0:
                if i == mapping[char_stack[-1]]:
                    char_stack.pop(-1)
                else:
                    return False
            else:
                return False
        if len(char_stack) >0:
            return False
        else:
            return True
        