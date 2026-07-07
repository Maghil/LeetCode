class Solution:
    def advantageCount(self, nums1, nums2):
        length = len(nums1)
        result = [-1] * length
        nums1.sort(reverse=True)
        indexes = [i for i in range(length)]
        indexes.sort(key=lambda i: nums2[i],reverse=True)
        left, right = 0, length -1
        for index in indexes:
            if nums1[left] > nums2[index]:
                result[index] = nums1[left]
                left+=1
            else:
                result[index] = nums1[right]
                right-=1
        return result


if __name__ == "__main__":
    a = Solution()
    print(a.advantageCount([1, 2, 3, 4, 5], [3, 5, 4, 6, 2]))
    print(a.advantageCount([1, 4, 2, 1, 3], [2, 3, 1, 2, 2]))
    print(a.advantageCount([2, 7, 11, 15], [1, 10, 4, 11]))
    print(a.advantageCount([12, 24, 8, 32], [13, 25, 32, 11]))
