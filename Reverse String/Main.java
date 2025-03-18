
public class Main {

    public static void main(String[] args) {
        String a = "hello";
        String b = "hannan";
        String c = "h";
        char[] a1 = a.toCharArray();
        char[] b1 = b.toCharArray();
        char[] c1 = c.toCharArray();
        Solution.reverseString(a1);
        Solution.reverseString(b1);
        Solution.reverseString(c1);
        System.out.println(a1);
        System.out.println(b1);
        System.out.println(c1);
    }
}

class Solution {
    public static void reverseString(char[] s) {
        for(int i =0; i<s.length/2;i++){
            char temp = s[i];
            s[i] = s[s.length-1-i];
            s[s.length-1-i] = temp;
        }
    }
}
