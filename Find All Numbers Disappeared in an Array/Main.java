
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.findDisappearedNumbers(new int[]{4, 3, 2, 7, 8, 2, 3, 1}));
        System.out.println(Solution.findDisappearedNumbers(new int[]{5, 1, 2, 3, 4}));
        System.out.println(Solution.findDisappearedNumbers(new int[]{1, 2, 3, 4, 5}));
        System.out.println(Solution.findDisappearedNumbers(new int[]{1, 1, 4, 2, 1, 3}));
    }
}

class Solution {

    public static List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> result = new ArrayList<>();
        for (int num : nums) {
            num = Math.abs(num);
            if (nums[num - 1] > 0) {
                nums[num - 1] = -nums[num - 1];
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                result.add(i+1);
            }
        }
        return result;
    }
}
