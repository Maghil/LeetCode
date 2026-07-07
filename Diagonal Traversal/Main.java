
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(Arrays.toString(a.findDiagonalOrder(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}})));
        System.out.println(Arrays.toString(a.findDiagonalOrder(new int[][]{{1, 2}, {3, 4}})));
        System.out.println(Arrays.toString(a.findDiagonalOrder(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}})));
    }
}

class Solution {

    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int i = 0, j = 0, k = 0;
        int[] result = new int[m * n];
        while (i < m && j < n) {
            result[k++] = mat[i][j];
            if ((i + j) % 2 == 0) {
                if (j == n - 1) {
                    i++;
                } else {
                    if (i > 0) {
                        i--;
                    }
                    j++;
                }
            } else {
                if (i == m - 1) {
                    j++;
                } else {
                    if (j > 0) {
                        j--;
                    }
                    i++;
                }
            }
        }
        return result;
    }
}

// 1 2 3      00 01 02
// 4 5 6      10 11 12
// 7 8 9      20 21 22