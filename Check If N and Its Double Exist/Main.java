
import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.checkIfExist(new int[]{10, 2, 5, 3}));
        System.out.println(Solution.checkIfExist(new int[]{7, 1, 14, 11}));
        System.out.println(Solution.checkIfExist(new int[]{3, 1, 7, 11}));
        System.out.println(Solution.checkIfExist(new int[]{0, 0}));
        System.out.println(Solution.checkIfExist(new int[]{7, 3, 8}));
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
