class Solution:
    def reverse(self, number: int) -> int:
        reversed_number = 0
        negative=False
        if number == 0:
            return 0
        if number < 0:
            negative = True
            number = number*-1
        while number != 0:
            last_number = number % 10
            reversed_number = (reversed_number*10) + last_number
            number = number//10
        return (-reversed_number if negative else reversed_number) if reversed_number.bit_length() < 32 else 0