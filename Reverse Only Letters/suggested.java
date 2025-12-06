
public class Suggested {

    public static void main(String[] args) {
        System.out.println(Solution.reverseOnlyLetters("abc---def"));
        System.out.println(Solution.reverseOnlyLetters("---abc---"));
        System.out.println(Solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"));
    }
}

class Solution {

    public static String reverseOnlyLetters(String S) {
        StringBuilder sb = new StringBuilder(S);
        for (int i = 0, j = S.length() - 1; i < j; ++i, --j) {
            while (i < j && !Character.isLetter(sb.charAt(i))) {
                ++i;
            }
            while (i < j && !Character.isLetter(sb.charAt(j))) {
                --j;
            }
            sb.setCharAt(i, S.charAt(j));
            sb.setCharAt(j, S.charAt(i));
        }
        return sb.toString();
    }
}
