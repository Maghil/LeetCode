
import java.util.Arrays;

public class Sugggested {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(Arrays.toString(a.plusOne(new int[]{0})));
        System.out.println(Arrays.toString(a.plusOne(new int[]{9, 9})));
        System.out.println(Arrays.toString(a.plusOne(new int[]{9})));
        System.out.println(Arrays.toString(a.plusOne(new int[]{1, 2, 3, 4})));
        System.out.println(Arrays.toString(a.plusOne(new int[]{8, 9, 9, 9})));
        System.out.println(Arrays.toString(a.plusOne(new int[]{9, 8, 9, 9, 9})));
    }
}

class Solution {

    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        digits = new int[digits.length + 1];
        digits[0] = 1;
        return digits;
    }
}
