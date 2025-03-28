class Solution {

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1, j = n - 1;
        while (j >= 0) {
            if (i>=0 && nums1[i] > nums2[j]) {
                nums1[i+j+1] = nums1[i];
                i--;
            }else {
                nums1[i+j+1] = nums2[j];
                j--;
            }
        }
        System.out.println(java.util.Arrays.toString(nums1));
    }
}
