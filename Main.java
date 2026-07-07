
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class Main {

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
        int[] result = new int[nums1.length];
        Integer[] nums2_index = new Integer[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            nums2_index[i] = i;
        }
        Arrays.sort(nums2_index, (a, b) -> Integer.compare(nums2[b], nums2[a]));
        Arrays.sort(nums1);
        // System.out.println(Arrays.toString(nums2_index));
        // System.out.println(Arrays.toString(nums1));
        int left = 0, right = nums1.length - 1;
        for (int i : nums2_index) {
            if (nums1[right] > nums2[i]) {
                result[i] = nums1[right];
                right--;
            } else {
                result[i] = nums1[left];
                left++;
            }
        }
        return result;
    }
}

// 1 4 2 1 3    4 3 2 1 1       1 1 2 3 4
// 2 3 1 2 2    3 2 2 2 1 
// 0 1 2 3 4    1 0 3 4 2
