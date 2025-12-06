
public class Main {

    public static void main(String[] args) {
        System.out.print(Solution.removeElement(new int[]{3, 2, 2, 3}, 3));
        System.out.print(Solution.removeElement(new int[]{0, 1, 2, 2, 3, 0, 4, 2}, 2));
        System.out.print(Solution.removeElement(new int[]{4, 5}, 4));
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
            } else if (nums[i] != val) {
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
