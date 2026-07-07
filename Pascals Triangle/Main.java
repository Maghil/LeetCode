
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Solution a = new Solution();
        System.out.println(a.generate(5));
    }
}

class Solution {

    public List<List<Integer>> generate(int numRows) {
        List<Integer> prev_row = new ArrayList<>();
        prev_row.add(1);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < numRows; i++) {
            result.add(prev_row);
            List current_row = new ArrayList<>();
            for (int j = 0; j <= prev_row.size(); j++) {
                if (j == 0) {
                    current_row.add(1);
                } else if (j == prev_row.size()) {
                    current_row.add(1);
                } else {
                    current_row.add(prev_row.get(j - 1) + prev_row.get(j));
                }
            }
            prev_row = current_row;
        }
        return result;
    }
}
