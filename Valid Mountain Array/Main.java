
public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.validMountainArray(new int[]{2, 1}));                       //False
        System.out.println(Solution.validMountainArray(new int[]{3, 5, 5}));                    //False
        System.out.println(Solution.validMountainArray(new int[]{1, 2, 3, 4, 5}));              //False
        System.out.println(Solution.validMountainArray(new int[]{0, 3, 2, 1}));                 //True
        System.out.println(Solution.validMountainArray(new int[]{5, 4, 3, 2, 1}));              //False
        System.out.println(Solution.validMountainArray(new int[]{1, 2, 3, 3, 3, 3, 2, 1}));     //False
        System.out.println(Solution.validMountainArray(new int[]{1, 3, 5, 7, 2, 1}));           //True
        System.out.println(Solution.validMountainArray(new int[]{1, 1, 1, 1, 1, 1, 1, 2, 1}));  // False
    }
}

class Solution {

    public static boolean validMountainArray(int[] arr) {
        int i = 0, len = arr.length;
        while (i < len - 1 && arr[i] < arr[i + 1]) {
            i++;
        }
        if ((i == 0) || (i == len - 1)) {
            return false;
        }
        while (i < len - 1 && arr[i] > arr[i + 1]) {
            i++;
        }
        return (i == len - 1);
    }
}
