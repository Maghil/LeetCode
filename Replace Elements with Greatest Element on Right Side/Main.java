
public class Main {

    public static void main(String[] args) {
        Solution.replaceElements(new int[]{17, 18, 5, 4, 6, 1});
        Solution.replaceElements(new int[]{400});
        Solution.replaceElements(new int[]{1, 2, 3, 4, 0});
    }
}

class Solution {

    public static int[] replaceElements(int[] arr) {
        int max = -1;
        for (int i = arr.length - 1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = max;
            if (temp > max) {
                max = temp;
            }
        }
        return arr;
    }

}
