
import java.util.Arrays;

public class Main {

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
        int carry_over = 1, index = digits.length - 1;
        while (carry_over > 0 && index >= 0) {
            digits[index] = digits[index] + carry_over;
            carry_over = 0;
            if (digits[index] > 9) {
                digits[index] = 0;

                carry_over = 1;
            }
            index--;
        }
        if (carry_over == 1) {
            int[] result = new int[digits.length + 1];
            System.arraycopy(digits, 0, result, 1, digits.length);
            result[0] = 1;
            return result;
        }
        return digits;
    }
}
