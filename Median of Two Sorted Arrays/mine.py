class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        (nums1_over,nums2_over) = (False,False)
        if len(nums1) < 1:
            nums1_over= True
        if len(nums2) < 1:
            nums2_over=True
        total = (len(nums1)+len(nums2))
        even=True
        if total % 2 !=0:
            even = False
        if not even:
            median_index=[total//2]
        else:
            mid_value = total//2
            median_index=[mid_value-1,mid_value]
        (index_1, index_2) = (0,0)
        result_list=[]
        while (index_1+index_2) <= median_index[-1]:       #[3,4]  [1,2]
            if nums2_over or (not nums1_over and nums1[index_1] <= nums2[index_2]):
                result_list.append(nums1[index_1])
                if index_1 == len(nums1) -1:
                    nums1_over = True
                index_1 = index_1 + 1
            else:
                result_list.append(nums2[index_2])
                if index_2 == len(nums2) -1:
                    nums2_over = True
                index_2 = index_2 + 1
        if even:
            return sum(result_list[-2::])/2
        else:
            return result_list[-1]
