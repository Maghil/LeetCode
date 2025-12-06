
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution.moveZeroes(new int[]{0, 1, 0, 3, 12});
        Solution.moveZeroes(new int[]{0});
        Solution.moveZeroes(new int[]{0, 3, 2, 0});
        Solution.moveZeroes(new int[]{0, 0, 3, 2, 0});
        Solution.moveZeroes(new int[]{1, 2, 0, 0, 4, 0, 6, 0});
    }
}

class Solution {

    public static void moveZeroes(int[] nums) {
        int zero_index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[zero_index] = nums[i];
                nums[i] = 0;
                zero_index += 1;
            }
        }
        System.out.println(Arrays.toString(nums));
    }
}
