
public class Main {

    public static void main(String[] args) {
        int[] a = {2, 5, 6, 9, 10};
        int[] b = {7, 5, 6, 8, 3};
        int[] c = {3, 3};
        int[] d = {2, 1};
        System.out.println(Solution.findGCD(a));
        System.out.println(Solution.findGCD(b));
        System.out.println(Solution.findGCD(c));
        System.out.println(Solution.findGCD(d));
    }
}

class Solution {

    public static int findGCD(int[] nums) {
        int min = nums[0], max = nums[0];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < min) {
                min = nums[i];
            }
            if (nums[i] > max) {
                max = nums[i];
            }
        }
        return gcd(min, max);
    }

    public static int gcd(int num1, int num2) {
        int remainder;
        remainder = num2 % num1;
        while (remainder > 0) {
            num2 = num1;
            num1 = remainder;
            remainder = num2 % num1;
        }
        return num1;
    }
}