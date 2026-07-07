
public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.dominantIndex(new int[]{3, 6, 1, 0}));     //1
        System.out.println(a.dominantIndex(new int[]{6, 2, 1, 0}));     //0
        System.out.println(a.dominantIndex(new int[]{6, 2, 12, 0}));    //2
        System.out.println(a.dominantIndex(new int[]{1, 2, 3, 4}));     //-1
        System.out.println(a.dominantIndex(new int[]{1, 2, 3, 1, 5}));  //-1
        System.out.println(a.dominantIndex(new int[]{5, 2}));           //0
        System.out.println(a.dominantIndex(new int[]{5, 3}));           //-1
    }
}

class Solution {

    public int dominantIndex(int[] nums) {
        int max_index = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > nums[max_index]) {
                max_index = i;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (i != max_index) {
                if (nums[i] * 2 > nums[max_index]) {
                    return -1;
                }
            }
        }
        return max_index;
    }
}
