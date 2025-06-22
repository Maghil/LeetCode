import java.util.Arrays;


public class Main {

    public static void main(String[] args) {
        int a[] = {121, -121, 10, 0, 12321};
        int b[] = {};
        int c[] = {-10};
        int d[] = {10, 100, 1000, 10000, 100000, 1000000};
        System.out.println(Arrays.toString(Solution.insertionSort(a)));
        System.out.println(Arrays.toString(Solution.insertionSort(b)));
        System.out.println(Arrays.toString(Solution.insertionSort(c)));
        System.out.println(Arrays.toString(Solution.insertionSort(d)));
    }
}

class Solution {

    public static int[] insertionSort(int[] array) {
        for (int i = 1; i < array.length; i++) {
            int key = array[i];
            int j = i - 1;
            while (j >= 0 && key < array[j]) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
        return array;
    }
}
