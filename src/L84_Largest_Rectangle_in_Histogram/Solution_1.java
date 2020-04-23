package L84_Largest_Rectangle_in_Histogram;

import java.util.ArrayList;
import java.util.List;

public class Solution_1 {
    public int largestRectangleArea(int[] heights) {
        List<Integer> index_stack = new ArrayList<>();
        int res = 0;
        for(int i=0; i<=heights.length; i++){
            int height = i<heights.length? heights[i] : 0; // add the right bound
            while (!index_stack.isEmpty()){
                int at_index = index_stack.get(index_stack.size()-1);
                int rectHeight = heights[at_index];
                if (rectHeight>height){
                    index_stack.remove(index_stack.size()-1);
                    int startFrom = index_stack.isEmpty()? 0 : index_stack.get(index_stack.size()-1) + 1;
                    res = Math.max(res, rectHeight * (i-startFrom));
                }
                else break;
            }
            index_stack.add(i);
        }
        return res;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        System.out.println(solution.largestRectangleArea(new int[]{2,1,5,6,2,3}));
    }
}
