class Solution:
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            if ((num >= 10 and num < 100) or (num >= 1000 and num < 10000) or (num == 100000)):
                count += 1
        return count


if __name__ == "__main__":
    a = Solution()
    print(a.findNumbers([555, 901, 482, 1771]))
    print(a.findNumbers([12, 345, 2, 6, 7896]))
    print(a.findNumbers([12, 7896, 7896, 7896, 7896]))
