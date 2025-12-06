
public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.removeDuplicates(new int[]{1, 1, 1, 2, 2, 2}));
        System.out.println(Solution.removeDuplicates(new int[]{0, 0, 1, 1, 1, 2, 2, 3, 3, 4}));
        System.out.println(Solution.removeDuplicates(new int[]{-100, 0, 1, 2, 3, 3, 4, 4}));
        System.out.println(Solution.removeDuplicates(new int[]{1}));
        System.out.println(Solution.removeDuplicates(new int[]{1, 2}));
        System.out.println(Solution.removeDuplicates(new int[]{1, 1}));
    }
}

class Solution {

    public static int removeDuplicates(int[] nums) {
        int index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != nums[index]) {
                index++;
                nums[index] = nums[i];
            }
        }
        return index+1;
    }
}
