class Solution:
    def thirdMax(self, nums) -> int:
        max_1 = None
        max_2 = None
        max_3 = None
        for num in nums:
            if max_1 == num or max_2 == num or max_3 == num:
                continue
            else:
                if max_1 == None or num > max_1:
                    max_3 = max_2
                    max_2 = max_1
                    max_1 = num
                elif max_2 == None or num > max_2:
                    max_3 = max_2
                    max_2 = num
                elif max_3 == None or num > max_3:
                    max_3 = num
        if max_3 == None and max_1 != None:
            return max_1
        else:
            return max_3


if __name__ == "__main__":
    a = Solution()
    print(a.thirdMax([1, 1, 4, 2, 1, 3]))
    print(a.thirdMax([5, 1, 2, 3, 4]))
    print(a.thirdMax([1, 2, 3, 4, 5]))
    print(a.thirdMax([3, 3, 2, 2, 2]))
    print(a.thirdMax([3]))
    print(a.thirdMax([3, 20000, 155, 25555534, 343, 2, 0]))
    print(a.thirdMax([-24353434, 20000, 155, 25555534, 343, 2, 0]))
