
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] a = {0, 0, 0, 0, 0, 0, 0};
        int[] b = {0};
        // int[] c = {1, 3, 5, 7, 9};

        Solution.duplicateZeros(a);
        Solution.duplicateZeros(b);
        // System.out.println(Arrays.toString(Solution.duplicateZeros(c)));
    }
}

class Solution {

    public static void duplicateZeros(int[] nums) {
        int zero_count = 0;
        for (int i : nums) {
            if (i == 0) {
                zero_count++;
            }
        }
        int n = nums.length;
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] == 0) {
                if (i + zero_count < n) {
                    nums[i + zero_count] = 0;
                }
                zero_count--;
            }
            if (i + zero_count < n) {
                nums[i + zero_count] = nums[i];
            }
        }
        System.out.print(Arrays.toString(nums));
    }
}
// 1, 0, 2, 3, 0, 4, 5, 0
// 1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0
