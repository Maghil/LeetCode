class Solution:
    def findDisappearedNumbers(self, nums):
        n_elements=set(range(1, len(nums)+1))
        return(n_elements.difference(nums))

if __name__ == "__main__":
    a = Solution()
    print(a.findDisappearedNumbers([1,1,4,2,1,3]))
    # print(a.findDisappearedNumbers([5,1,2,3,4]))
    # print(a.findDisappearedNumbers([1,2,3,4,5]))
    # print(a.findDisappearedNumbers([3]))
    # print(a.findDisappearedNumbers([3]))
