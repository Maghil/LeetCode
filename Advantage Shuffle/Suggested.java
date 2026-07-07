
import java.util.Arrays;

public class Suggested {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(Arrays.toString(a.advantageCount(new int[]{1, 2, 3, 4, 5}, new int[]{3, 5, 4, 6, 2})));
        System.out.println(Arrays.toString(a.advantageCount(new int[]{1, 4, 2, 1, 3}, new int[]{2, 3, 1, 2, 2})));
        System.out.println(Arrays.toString(a.advantageCount(new int[]{2, 7, 11, 15}, new int[]{1, 10, 4, 11})));
        System.out.println(Arrays.toString(a.advantageCount(new int[]{12, 24, 8, 32}, new int[]{13, 25, 32, 11})));
    }
}

class Solution {

    public int[] advantageCount(int[] nums1, int[] nums2) {
        Integer[] ord = new Integer[nums2.length];
        int[] ans = new int[nums1.length];
        for (int i = 0; i < nums2.length; i++) {
            ord[i] = i;
        }
        Arrays.sort(ord, (a, b) -> Integer.compare(nums2[a], nums2[b]));
        Arrays.sort(nums1);
        int i = 0, j = nums2.length - 1;
        for (int index : ord) {
            if (nums1[j] > nums2[index]) {
                ans[index] = nums1[j];
                j--;
            } else {
                ans[index] = nums1[i];
                i++;
            }
        }
        return ans;
    }
}
