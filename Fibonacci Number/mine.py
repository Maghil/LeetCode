#TOP DOWN APPROACH/ MEMONIZATION
class Solution:
    memo = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n not in self.memo:
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]


if __name__ == "__main__":
    a = Solution()
    print(a.fib(10))

# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)
# fib(2) = fib(1) + fib(0)
