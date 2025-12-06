class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i = m-1
        j = n-1
        total_len = m+n-1
        while i >=-1 and j >= -1:
            if i==-1:
                nums1[total_len] = nums2[j]
                j = j-1
            if j==-1:
                return nums1
            if i>=0:
                if nums1[i] >= nums2[j]:
                    nums1[total_len] = nums1[i]
                    i = i-1
                else:
                    nums1[total_len]=nums2[j]
                    j=j-1

            total_len = total_len-1
        return nums1


if __name__ == "__main__":
    a = Solution()
    print(a.merge([1, 2, 3, 0, 0, 0, 0], 3, [2, 5, 6, 9], 4))
    print(a.merge([1], 1, [], 0))
    print(a.merge([0, 0, 0, 0, 0], 0, [2, 5, 6, 9,10], 5))
    print(a.merge([1,2,3,0,0,0], 3, [2,5,6], 3))