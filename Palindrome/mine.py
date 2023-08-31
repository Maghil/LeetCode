class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_number = 0
        temp = x
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            while temp != 0:
                last_digit = temp % 10
                temp = temp // 10
                reversed_number = (reversed_number * 10) + last_digit
        print(f"{reversed_number}")
        if x == reversed_number:
            return True
        return False
