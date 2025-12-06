public class Main {

    public static void main(String[] args) {
        Solution.merge(new int[]{1, 2, 3, 0, 0, 0}, 3, new int[]{2, 5, 6}, 3);
        Solution.merge(new int[]{1}, 1, new int[]{}, 0);
        Solution.merge(new int[]{0}, 0, new int[]{1}, 1);
        Solution.merge(new int[]{0}, 1, new int[]{}, 0);
        Solution.merge(new int[]{6, 6, 6, 0, 0, 0}, 3, new int[]{2, 5, 6}, 3);
        Solution.merge(new int[]{1, 2, 7, 0, 0, 0}, 3, new int[]{6, 6, 6}, 3);
    }
}

class Solution {

    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int k = m + n - 1;
        m = m - 1;
        n = n - 1;
        while (n >= 0) {
            if (m >= 0 && nums1[m] > nums2[n]) {
                nums1[k--] = nums1[m--];
            } else {
                nums1[k--] = nums2[n--];
            }

        }
        System.out.println(java.util.Arrays.toString(nums1));
    }
}
