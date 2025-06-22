class Solution:
    def gcd(self, num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def findGCD(self, nums):
        min, max = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]
            if nums[i] > max:
                max = nums[i]
        return (self.gcd(min, max))


if __name__ == "__main__":
    a = Solution()
    print(a.findGCD([2, 5, 6, 9, 10]))
    print(a.findGCD([7, 5, 6, 8, 3]))
    print(a.findGCD([3, 3]))
    print(a.findGCD([2, 1]))
    print(a.findGCD([3, 0, 3, 3, 2, 1, 0]))
