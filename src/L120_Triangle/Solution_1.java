package L120_Triangle;

import java.util.ArrayList;
import java.util.List;

public class Solution_1 {
    public int minimumTotal(List<List<Integer>> triangle) {
        for (int row_id = triangle.size() - 2; row_id >= 0; row_id --) {
            List<Integer> next_row = triangle.get(row_id+1);
            for (int i = 0; i < triangle.get(row_id).size(); i++){
                int path_1 = next_row.get(i);
                int path_2 = next_row.get(i + 1);
                List<Integer> this_row = triangle.get(row_id);
                int path = this_row.get(i);
                path += Math.min(path_1, path_2);
                this_row.set(i, path);
            }
        }
        return triangle.get(0).get(0);
    }
}
