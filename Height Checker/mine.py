class Solution:
    def heightChecker(self, nums):
        frequency = [0]*100
        counter = 0
        misplaced_counter = 0
        for i in nums:
            frequency[i-1] += 1
        for j in range(len(frequency)):
            while frequency[j] > 0:
                if nums[counter] != j+1:
                    misplaced_counter += 1
                counter += 1
                frequency[j] -= 1
        return misplaced_counter


if __name__ == "__main__":
    a = Solution()
    print(a.heightChecker([1, 1, 4, 2, 1, 3]))
    print(a.heightChecker([5,1,2,3,4]))
    print(a.heightChecker([1,2,3,4,5]))
