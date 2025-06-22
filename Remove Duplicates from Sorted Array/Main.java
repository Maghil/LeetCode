
public class Main {

    public static void main(String[] args) {
        int[] a1 = {1, 1, 2};
        int[] b1 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int[] c1 = {4, 5};
        System.out.print(Solution.removeDuplicates(a1));
        System.out.print(Solution.removeDuplicates(b1));
        System.out.print(Solution.removeDuplicates(c1));
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
