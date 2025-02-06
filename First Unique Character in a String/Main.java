import java.util.HashMap;

public class Main {

    public static void main(String[] args) {
        String a = "leetcode";
        String b = "loveleetcodle";
        String c = "aabb";
        System.out.println(Solution.firstUniqChar(a));
        System.out.println(Solution.firstUniqChar(b));
        System.out.println(Solution.firstUniqChar(c));
    }
}

class Solution {

    public static int firstUniqChar(String s) {
        HashMap<Character,Integer> counter = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            counter.put(c, counter.getOrDefault(c,0)+1);
        }
        for (int i=0; i<s.length(); i++) {
            if (counter.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }
}
