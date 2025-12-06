

public class Main {

    public static void main(String[] args) {
        System.out.println(Solution.heightChecker(new int[]{5, 1, 2, 3, 4}));           //1, 2, 3, 4, 5
        System.out.println(Solution.heightChecker(new int[]{1, 1, 4, 2, 1, 3}));        //1, 1, 1, 2, 3 ,4
        System.out.println(Solution.heightChecker(new int[]{2, 1, 2, 1, 1, 2, 2, 1}));  //1, 1, 1, 1, 2, 2, 2, 2
        System.out.println(Solution.heightChecker(new int[]{1, 2, 3, 4, 5}));           //1, 2, 3, 4, 5
    }
}

class Solution {

    public static int heightChecker(int[] heights) {
        int[] frequency = new int[100];
        for (int i : heights) {
            frequency[i - 1]++;
        }
        int counter = 0, misplaced_counter = 0;
        for (int i = 0; i < frequency.length; i++) {
            while (frequency[i] > 0) {
                if (heights[counter] != i + 1) {
                    misplaced_counter++;
                }
                counter++;
                frequency[i]--;
            }
        }
        return misplaced_counter;
    }
}
