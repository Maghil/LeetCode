
import java.util.Arrays;
import java.util.Comparator;
import java.util.stream.IntStream;

public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        // a.advantageCount(new int[]{1, 2, 3, 4, 5}, new int[]{3, 5, 4, 6, 2});
        System.out.println(Arrays.toString(a.advantageCount(new int[]{1, 4, 2, 1, 3}, new int[]{2, 3, 1, 2, 2})));
        // a.advantageCount(new int[]{2, 7, 11, 15}, new int[]{1, 10, 4, 11});
        // a.advantageCount(new int[]{12, 24, 8, 32}, new int[]{13, 25, 32, 11});
    }
}

class Solution {

    public int[] advantageCount(int[] nums1, int[] nums2) {
        int len = nums1.length;
        int[] result = new int[nums1.length];
        Arrays.sort(nums1);
        Integer[] temp = IntStream.range(0, len).boxed().toArray(Integer[]::new);
        Arrays.sort(temp, Comparator.comparing(s -> nums2[s]));
        int it = 0;
        int rit = len - 1;
        for (int i = len - 1; i >= 0; i--) {
            int index = temp[i];
            if (nums1[rit] > nums2[index]) {
                result[index] = nums1[rit];
                rit--;
            } else {
                result[index] = nums1[it];
                it++;
            }
        }
        return result;
    }
}
