class Solution:
    def dominantIndex(self, nums) -> int:
        first_max, second_max = 0, -1
        for i in range(1, len(nums)):
            if nums[i] > nums[first_max]:
                second_max, first_max = first_max, i
            elif second_max == -1 or nums[i] > nums[second_max]:
                second_max = i
        return first_max if nums[first_max] >= nums[second_max] * 2 else -1


if __name__ == "__main__":
    a = Solution()
    print(a.dominantIndex([3, 6, 1, 0]))     # 1
    print(a.dominantIndex([6, 2, 1, 0]))     # 0
    print(a.dominantIndex([6, 2, 12, 0]))    # 2
    print(a.dominantIndex([1, 2, 3, 4]))     # -1
    print(a.dominantIndex([1, 2, 3, 1, 5]))  # -1
    print(a.dominantIndex([5, 2]))           # 0
    print(a.dominantIndex([5, 3]))           # -1
    print(a.dominantIndex([1, 0]))           # 0
    print(a.dominantIndex([0, 1]))           # 1
