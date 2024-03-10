class Solution:
    def intersection(self, nums1, nums2):
        intersection=set()
        for i in nums1:
            for j in nums2:
                if i==j:
                    intersection.add(i)
                else:
                    pass
        return list(intersection)



if __name__ == "__main__":
    a=Solution()
    print(a.intersection([1,2,3],[4,5]))
    print(a.intersection([1,2,3,6],[2,3,4,5]))
    print(a.intersection([2,4],[1,2]))
