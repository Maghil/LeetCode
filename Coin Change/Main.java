
public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.pivotIndex(new int[]{5, 1, 2, 3, 4}));          //-1
        System.out.println(a.pivotIndex(new int[]{1, 1, 4, 2, 1, 3}));       //-1
        System.out.println(a.pivotIndex(new int[]{-10, 10, 10, -10}));       //-1
        System.out.println(a.pivotIndex(new int[]{-10, 10, 1, 10, -10}));    //2
        System.err.println(a.pivotIndex(new int[]{1}));                      //0
        System.err.println(a.pivotIndex(new int[]{1, 7, 3, 6, 5, 6}));       //3
        System.err.println(a.pivotIndex(new int[]{1, 2, 3}));                //-1
        System.err.println(a.pivotIndex(new int[]{2, 1, -1}));               //0
    }
}

class Solution {

    public int pivotIndex(int[] nums) {
        int left_sum = 0, total_sum = 0;
        for (int num : nums) {
            total_sum += num;
        }
        for (int i = 0; i < nums.length; i++) {
            if (left_sum * 2 == total_sum - nums[i]) {
                return i;
            }
            left_sum += nums[i];
        }
        return -1;
    }
}
