class Solution:
    def getCommon(self, nums1, nums2) -> int:
        if len(nums2) < len(nums1):
            nums1,nums2=nums2,nums1
        for i in nums1:
            if len(nums2)>=2:
                found=self.binarySearch(nums2,i)
                if found:
                    return i
            else:
                if i == nums2[0]:
                    return i
        return -1

    def binarySearch(self,iterable,value) -> bool:
        start=0
        end=len(iterable)-1
        while start <= end:
            mid=(end+start)//2
            if iterable[mid]==value:
                return True
            elif iterable[mid]<value:
                start=mid+1
            else:
                end=mid-1
        return False




if __name__ == "__main__":
    a=Solution()
    print(a.getCommon([1,2,3],[2,4]))
    print(a.getCommon([1,2,3,6],[2,3,4,5]))
    print(a.getCommon([2,4],[1,2]))
