
public class Suggested {

    public static void main(String[] args) {
        System.out.println(Solution.thirdMax(new int[]{1, 1, 4, 2, 1, 3}));
        System.out.println(Solution.thirdMax(new int[]{5, 1, 2, 3, 4}));
        System.out.println(Solution.thirdMax(new int[]{1, 2, 3, 4, 5}));
        System.out.println(Solution.thirdMax(new int[]{3, 3, 2, 2, 2}));
        System.out.println(Solution.thirdMax(new int[]{3}));
        System.out.println(Solution.thirdMax(new int[]{3, 20000, 155, 25555534, 343, 2, 0}));
        System.out.println(Solution.thirdMax(new int[]{-24353434, 20000, 155, 25555534, 343, 2, 0}));
        System.out.println(Solution.thirdMax(new int[]{1, 2, 2, 5, 3, 5}));
    }
}

class Solution {

    public static int thirdMax(int[] nums) {
        long first_max = Long.MIN_VALUE;
        long second_max = Long.MIN_VALUE;
        long third_max = Long.MIN_VALUE;
        for (int i : nums) {
            if (i > first_max) {
                third_max = second_max;
                second_max = first_max;
                first_max = i;
            } else if (i > second_max && i != first_max) {
                third_max = second_max;
                second_max = i;
            } else if (i > third_max && (i != second_max && i != first_max)) {
                third_max = i;
            }
        }
        return (int) (third_max > Long.MIN_VALUE ? third_max : first_max);
    }
}
