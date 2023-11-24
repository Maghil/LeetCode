class Solution:
    def myAtoi(self, s: str) -> int:
        number_begins = False
        number = 0
        sign = +1
        for character in s:
            if not number_begins:
                if character == " ":
                    pass
                elif character.isdigit() or character == "+" or character == "-":
                    number_begins = True
                    if not character.isdigit():
                        if character== "+":
                            pass
                        else:
                            sign=-1
                    else:
                        number = number * 10 + int(character)
                else:
                    return 0
            else:
                if character.isdigit():
                    number = number * 10 + int(character)
                else:
                    break
        number = sign * number
        number = min(number, 2 ** 31 - 1)
        number = max(-(2 ** 31), number)
        return number
