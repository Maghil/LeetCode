
public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.strStr("sadbutsad", "sad"));
        System.out.println(a.strStr("leetcode", "rabbit"));
        System.out.println(a.strStr("leetcode", "leeto"));
        System.out.println(a.strStr("leetcode", "etc"));
        System.out.println(a.strStr("aaa", "aaaa"));

    }

}

class Solution {

    public int strStr(String haystack, String needle) {
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            int j = 0;
            while (j < needle.length() && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }
            if (j == needle.length()) {
                return i;
            }
        }
        return -1;
    }
}
