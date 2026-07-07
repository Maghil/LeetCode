
public class Main2 {

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
        int max = 1, second_max = 0;
        if (nums[0] > nums[1]) {
            max = 0;
            second_max = 1;
        }
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] > nums[max]) {
                second_max = max;
                max = i;
            } else if (nums[i] > nums[second_max]) {
                second_max = i;
            }
        }
        return nums[second_max] * 2 <= nums[max] ? max : -1;
    }
}
