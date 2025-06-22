
public class Main {

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
        int i = 0, j = nums.length - 1, count = 0;
        while (i <= j) {
            if (nums[i] == val && nums[j] != val) {
                nums[i] = nums[j];
                i++;
                j--;
                count++;
            }
            else if (nums[i] != val) {
                i++;
                count++;
            }
            if (nums[j] == val) {
                j--;
            }
        }
        return count;
    }
}
