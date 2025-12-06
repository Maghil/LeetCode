
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(Arrays.toString(a.sortArrayByParity(new int[]{3, 1, 2, 4})));
        System.out.println(Arrays.toString(a.sortArrayByParity(new int[]{0})));
    }
}

class Solution {

    public int[] sortArrayByParity(int[] nums) {
        int odd_index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] % 2 == 0) {
                int temp = nums[i];
                nums[i] = nums[odd_index];
                nums[odd_index] = temp;
                odd_index++;
            }
        }
        return nums;
    }
}
