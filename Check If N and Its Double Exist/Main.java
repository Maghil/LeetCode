
import java.util.HashSet;
import java.util.Set;


public class Main {

    public static void main(String[] args) {
        int[] a = {10, 2, 5, 3};
        int[] b = {7, 1, 14, 11};
        int[] c = {3, 1, 7, 11};
        System.out.println(Solution.checkIfExist(a));
        System.out.println(Solution.checkIfExist(b));
        System.out.println(Solution.checkIfExist(c));
    }
}

class Solution {
    public static boolean checkIfExist(int[] arr) {
        Set<Integer> set = new HashSet<>();
        for (int i : arr) {
            if (set.contains(i * 2) || (i % 2 == 0 && set.contains(i / 2))) {
                return true;
            }
            set.add(i);
        }

        return false;
    }
}
