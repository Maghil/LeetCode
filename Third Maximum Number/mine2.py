class Solution:
    def thirdMax(self, nums) -> int:
        first_max = second_max = third_max = float('-inf')
        for i in nums:
            if i > first_max:
                third_max = second_max
                second_max = first_max
                first_max = i
            elif i > second_max and i != first_max:
                third_max = second_max
                second_max = i
            elif i > third_max and (i != second_max and i != first_max):
                third_max = i
        return third_max if third_max > float('-inf') else first_max


if __name__ == "__main__":
    a = Solution()
    print(a.thirdMax([1, 1, 4, 2, 1, 3]))
    print(a.thirdMax([5, 1, 2, 3, 4]))
    print(a.thirdMax([1, 2, 3, 4, 5]))
    print(a.thirdMax([3, 3, 2, 2, 2]))
    print(a.thirdMax([3]))
    print(a.thirdMax([3, 20000, 155, 25555534, 343, 2, 0]))
    print(a.thirdMax([-24353434, 20000, 155, 25555534, 343, 2, 0]))
    print(a.thirdMax([1, 2, 2, 5, 3, 5]))
