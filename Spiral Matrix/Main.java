
import java.util.ArrayList;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println((a.spiralOrder(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}})));
        System.out.println((a.spiralOrder(new int[][]{{1, 2}, {3, 4}})));
        System.out.println((a.spiralOrder(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}})));
    }
}

class Solution {

    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        List<Integer> result = new ArrayList<>(m * n);
        result.add(matrix[0][0]);
        int i = 0, j = 0, delta = 1;
        while (result.size() < m * n) {
            while ((result.size() < m * n) && (j < n - delta)) {
                j++;
                result.add(matrix[i][j]);
            }
            // System.out.println(result);
            while ((result.size() < m * n) && (i < m - delta)) {
                i++;
                result.add(matrix[i][j]);
            }
            // System.out.println(result);
            while ((result.size() < m * n) && (j > delta - 1)) {
                j--;
                result.add(matrix[i][j]);
            }
            // System.out.println(result);
            delta++;
            while ((result.size() < m * n) && (i > delta - 1)) {
                i--;
                result.add(matrix[i][j]);
            }
            // System.out.println(result);
        }
        return result;
    }
}

// 1  2  3  4       00 01 02 03
// 5  6  7  8       10 11 12 13
// 9 10 11 12       20 21 22 23
