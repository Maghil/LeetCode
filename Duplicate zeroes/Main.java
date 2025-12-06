
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution.duplicateZeros(new int[]{0});
        Solution.duplicateZeros(new int[]{1, 3, 5, 7, 9});
        Solution.duplicateZeros(new int[]{1, 0, 2, 3, 0, 4, 5, 0});
    }
}

class Solution {

    public static void duplicateZeros(int[] nums) {
        int zero_count = 0;
        for (int n : nums) {
            if (n == 0) {
                zero_count++;
            }
        }
        int n = nums.length;
        for (int j = n - 1; j >= 0; j--) {
            if (nums[j] == 0) {
                if (j + zero_count < n) {
                    nums[j + zero_count] = 0;
                }
                zero_count--;
            }
            if (j + zero_count < n) {
                nums[j + zero_count] = nums[j];
            }
        }
        System.out.println(Arrays.toString(nums));
    }
}
