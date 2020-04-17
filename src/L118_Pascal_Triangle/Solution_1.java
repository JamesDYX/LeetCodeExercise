package L118_Pascal_Triangle;

import java.util.ArrayList;
import java.util.List;

public class Solution_1 {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        if (numRows == 0)
            return triangle;
        List<Integer> row = new ArrayList<>();
        row.add(1);
        triangle.add(row);
        for (int row_counter = 2; row_counter <= numRows; row_counter++) {
            row = new ArrayList<>();
            row.add(1);
            for (int i = 1; i < row_counter-1; i++)
                row.add(triangle.get(row_counter-2).get(i-1) + triangle.get(row_counter-2).get(i));
            row.add(1);
            triangle.add(row);
        }
        return triangle;
    }

    public static void main(String[] args) {
        Solution_1 solution = new Solution_1();
        List<List<Integer>> triangle = solution.generate(5);
        for (List<Integer> row : triangle){
            System.out.println(row.toString());
        }
    }
}
