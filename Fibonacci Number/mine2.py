# BOTTOM UP APPROACH/
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(2, n+1):
            temp = a
            a = b
            b = temp + b
        return b


if __name__ == "__main__":
    a = Solution()
    print(a.fib(10))
    print(a.fib(9))

# 0 1 1 2 3 5 8 13 21 34 55
