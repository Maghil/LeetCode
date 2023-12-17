import math


class Solution:
    def findNumbers(self, nums) -> int:
        even_count = 0
        for number in nums:
            if (int(math.log10(number)+1) % 2) == 0:
                even_count = even_count+1
        return even_count

if __name__=="__main__":
    a=Solution()
    print(a.findNumbers([1000]))

