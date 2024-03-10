class Solution:
    def intersection(self, nums1, nums2):
        hash={}
        result=set()
        for i in nums1:
            hash[i]=1
        for j in nums2:
            if hash.get(j):
                result.add(j)
                del hash[j]
        return list(result)





if __name__ == "__main__":
    a=Solution()
    print(a.intersection([1,2,3],[4,5]))
    print(a.intersection([1,2,3,6],[2,3,4,5]))
    print(a.intersection([2,4],[1,2]))
