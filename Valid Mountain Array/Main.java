
public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.validMountainArray(new int[]{2, 1}));                   //False
        System.out.println(Solution.validMountainArray(new int[]{3, 5, 5}));                //False
        System.out.println(Solution.validMountainArray(new int[]{0, 3, 2, 1}));             //True
        System.out.println(Solution.validMountainArray(new int[]{1, 2, 3, 4, 5}));          //False
        System.out.println(Solution.validMountainArray(new int[]{5, 4, 3, 2, 1}));          //False
        System.out.println(Solution.validMountainArray(new int[]{1, 2, 3, 3, 3, 3, 2, 1})); //False
        System.out.println(Solution.validMountainArray(new int[]{1, 3, 5, 7, 2, 1}));       //True
    }
}

class Solution {

    public static boolean validMountainArray(int[] arr) {
        int i = 0, j = arr.length - 1, k = arr.length;
        if (!(k > 3 || arr[0] < arr[1])) {
            return false;
        }
        while (i < k - 1 && arr[i] < arr[i + 1]) {
            i--;
        }
        while (j > 0 && arr[j] > arr[j - 1]) {
            j--;
        }
        return (0 < i) == (j < k - 1);
    }
}
