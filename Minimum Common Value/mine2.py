class Solution:
    def getCommon(self, nums1, nums2) -> int:
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return -1



if __name__ == "__main__":
    a=Solution()
    # print(a.getCommon([1,2,3],[4,5]))
    # # print(a.getCommon([1,2,3,6],[2,3,4,5]))
    print(a.getCommon([2,4],[1,2]))
