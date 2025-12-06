
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(Arrays.toString(a.sortedSquares(new int[]{-4, -1, 0, 3, 10})));
        System.out.println(Arrays.toString(a.sortedSquares(new int[]{-7, -3, 2, 3, 11})));
        System.out.println(Arrays.toString(a.sortedSquares(new int[]{-7, -3, -2, 3, 12})));
    }
}

class Solution {

    public int[] sortedSquares(int[] nums) {
        int[] result = new int[nums.length];
        int left = 0, right = nums.length - 1, index = nums.length - 1;
        while (left <= right) {
            if (Math.abs(nums[left]) > Math.abs(nums[right])) {
                result[index] = nums[left] * nums[left];
                left += 1;
            } else {
                result[index] = nums[right] * nums[right];
                right -= 1;
            }
            index -= 1;
        }
        return result;
    }
}