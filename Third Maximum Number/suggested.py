class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   v = [num, v[0], v[1]]
                elif num > v[1]: v = [v[0], num, v[1]]
                elif num > v[2]: v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]


if __name__ == "__main__":
    a = Solution()
    print(a.thirdMax([1,1,4,2,1,3]))
    print(a.thirdMax([5,1,2,3,4]))
    print(a.thirdMax([1,2,3,4,5]))
    print(a.thirdMax([3,3,2,2,2]))
    print(a.thirdMax([3]))
    print(a.thirdMax([3,20000,155,25555534,343,2,0]))
    print(a.thirdMax([-24353434,20000,155,25555534,343,2,0]))
