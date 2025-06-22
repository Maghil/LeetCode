
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int[] a = {1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10};
        int[] b = {2, 2, 4, 4, 6, 6, 8, 8, 10, 10};
        int[] c = {1, 3, 5, 7, 9};
        int target = 10, target2 = 2, target3 = 2;
        System.out.println(Arrays.toString(Solution.searchRange(a, target)));
        System.out.println(Arrays.toString(Solution.searchRange(b, target2)));
        System.out.println(Arrays.toString(Solution.searchRange(c, target3)));
    }
}

class Solution {

    public static int[] searchRange(int[] nums, int target) {
        int left, right;
        Solution search = new Solution();
        left = search.binarySearch(nums, target, -1);
        right = search.binarySearch(nums, target, 1);
        return new int[]{left, right};
    }

    private int binarySearch(int[] nums, int target, int side) {
        int low = 0, high = nums.length - 1, result = -1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] > target) {
                high = mid - 1;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                result = mid;
                if (side == -1) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
        }
        return result;
    }
}

// 1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6, 7, 7, 7, 8, 9, 10
// 0, 1, 3, 4, 5, 6, 7, 8 ,9 ,0, 1, 2, 3, 4, 5, 6, 7, 8
// 1, 2, 2, 2, 4, 4, 4, 4, 6, 6, 8, 8, 10, 10
// 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 2, 13
