
import java.util.HashSet;
import java.util.Set;

class Main {

    public static void main(String[] args) {
        int[] a;
        int b;
        a = new int[]{1, 5, 0, 3, 5};
        b = Solution.minimumOperations(a);
        System.out.println(b);
    }
}

class Solution {

    public static int minimumOperations(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int a : nums) {
            if (a > 0) {
                set.add(a);
            }
        }
        return set.size();
    }
}
