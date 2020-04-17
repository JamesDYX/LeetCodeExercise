package L1051_Height_Checker;

import java.util.Arrays;

public class Solution_1 {
    public int heightChecher(int[] heights) {
        int[] heights_temp = new int[heights.length];
        System.arraycopy(heights, 0, heights_temp, 0, heights.length);
        Arrays.sort(heights_temp);
        int res = 0;
        for (int i = 0; i < heights.length; i++){
            res += heights_temp[i] == heights[i] ? 0 : 1;
        }
        return res;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[][] test_cases = {
                {1,1,4,2,1,3},
                {5,1,2,3,4}
        };
        for(int[] heights : test_cases)
            System.out.println(solution.heightChecher(heights));
    }
}
