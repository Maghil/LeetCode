
public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.longestCommonPrefix(new String[]{"flower", "flow", "flight"}));
        System.out.println(a.longestCommonPrefix(new String[]{"flower", "flow", "flows"}));
        System.out.println(a.longestCommonPrefix(new String[]{"dog", "racecar", "car"}));
        System.out.println(a.longestCommonPrefix(new String[]{"ab", "abc", "abd"}));
        System.out.println(a.longestCommonPrefix(new String[]{"flow"}));
    }
}

class Solution {

    public String longestCommonPrefix(String[] strs) {
        String result = "";
        for (int i = 0; i < strs[0].length(); i++) {
            char chr = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (i == strs[j].length() || chr != strs[j].charAt(i)) {
                    return result;
                }
            }
            result += chr;
        }
        return result;
    }
}
