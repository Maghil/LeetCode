
public class Main {

    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int[] b = {2, 4, 6, 8, 10};
        int[] c = {1, 3, 5, 7, 9};
        int target = 5, target2 = 2, target3 = 2;
        System.out.println(Solution.search(a, target));
        System.out.println(Solution.search(b, target2));
        System.out.println(Solution.search(c, target3));
    }
}

class Solution {

    public static int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
}
