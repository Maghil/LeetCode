class Solution:
    def dominantIndex(self, nums) -> int:
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[max_index]:
                max_index = i
        for i in range(len(nums)):
            if i == max_index:
                continue
            if nums[i]*2 > nums[max_index]:
                return -1
        return max_index


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
