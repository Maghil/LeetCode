class Solution:
    def romanToInt(self, s: str) :
        mapping={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        value=0
        prev_char=0
        for i in reversed(s):
            char = mapping[i]
            if prev_char==0:
                value=char
            else:
                if prev_char<= char:
                    value=value+char
                if prev_char > char:
                    value=value-char
            prev_char=char
        return value
        
