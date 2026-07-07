
class Solution:
    def plusOne(self, digits: int) -> int:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits


if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([1, 2, 3]))
    print(a.plusOne([8, 9, 9, 9]))
    print(a.plusOne([9, 8, 9, 9, 9]))
    print(a.plusOne([1, 0]))
    print(a.plusOne([0]))
    print(a.plusOne([9, 9]))
    print(a.plusOne([9]))
