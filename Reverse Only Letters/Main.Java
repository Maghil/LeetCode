
public class Main {

    public static void main(String[] args) {
        String a = "abc---def";
        String b = "---abc---";
        String c = "Test1ng-Leet=code-Q!";
        System.out.println(Solution.reverseOnlyLetters(a));
        System.out.println(Solution.reverseOnlyLetters(b));
        System.out.println(Solution.reverseOnlyLetters(c));
    }
}

class Solution {

    public static String reverseOnlyLetters(String s) {
        StringBuilder sb = new StringBuilder(s);
        int i = 0, j = s.length() - 1;
        while (i < j) {
            if (! Character.isLetter(sb.charAt(i))) {
                i++;
            } else if (!Character.isLetter(sb.charAt(j))) {
                j--;
            } else {
                sb.setCharAt(i, s.charAt(j));
                sb.setCharAt(j--, s.charAt(i++));
            }
        }
        return  sb.toString();
    }
}
