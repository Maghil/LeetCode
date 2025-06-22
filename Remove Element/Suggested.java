
public class Suggested {

    public static void main(String[] args) {
        int[] a1 = {3, 2, 2, 3};
        int[] b1 = {0, 1, 2, 2, 3, 0, 4, 2};
        int[] c1 = {4, 5};
        int a2 = 3, b2 = 2, c2 = 4;
        System.out.print(Solution.removeElement(a1, a2));
        System.out.print(Solution.removeElement(b1, b2));
        System.out.print(Solution.removeElement(c1, c2));
    }
}

class Solution {
    public static int removeElement(int[] nums, int val) {
        int index = 0;
        for (int i =0; i<nums.length;i++) {
            if (nums[i] != val) {
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
}
