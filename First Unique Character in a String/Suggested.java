class Solution {

    public static int firstUniqChar(String s) {
        int[] counter = new int[26];
        for (int i=0; i<s.length(); i++) {
            int index = s.charAt(i) - 'a';
            counter[index]++;
        }
        for (int i=0; i<s.length(); i++) {
            int index = s.charAt(i) - 'a';
            if (counter[index] == 1) {
                return i;
            }
        }
        return -1;
    }
}
