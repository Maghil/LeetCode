
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
        return nums;
    }
}