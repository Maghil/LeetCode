
public class Main2 {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.strStr("sadbutsad", "sad"));
        System.out.println(a.strStr("leetcode", "code"));
        System.out.println(a.strStr("leetcode", "leeto"));
        System.out.println(a.strStr("leetcode", "etc"));
        System.out.println(a.strStr("aaa", "aaaa"));

    }

}

class Solution {

    public int strStr(String haystack, String needle) {
        int n_len = needle.length();
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(0) && haystack.charAt(i + (n_len - 1)) == needle.charAt(n_len - 1)) {
                for (int j = 0; j < n_len; j++) {
                    if (haystack.charAt(i+j) != needle.charAt(j)) {
                        break;
                    }
                    if (j == n_len - 1) {
                        return i;
                    }
                }
            }
        }
        return -1;
    }
}

// 0 1 2 3 4 5 6 7
// l e e t c o d e       8
// c o d e               4
