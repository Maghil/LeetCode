
public class Main {

    public static void main(String[] args) {
        int a = 121, b = 1, c = -121, d = 10;
        System.out.println(Solution.isPalindrome(a));
        System.out.println(Solution.isPalindrome(b));
        System.out.println(Solution.isPalindrome(c));
        System.out.println(Solution.isPalindrome(d));
    }
}

class Solution {

    public static boolean isPalindrome(int number) {
        if (number < 0 || (number % 10 == 0 && number != 0)) {
            return false;
        }
        int reversed = 0;
        while (number > reversed) {
            reversed = reversed * 10 + number % 10;
            number = number / 10;
        }
        return number == reversed || number == reversed / 10;
    }
}
