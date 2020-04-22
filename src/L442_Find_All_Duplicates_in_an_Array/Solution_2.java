package L442_Find_All_Duplicates_in_an_Array;

import java.util.ArrayList;
import java.util.List;

public class Solution_2 {
    /*
    view the array aas hash table
     */
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            int n=Math.abs(nums[i]);
            if (nums[n-1] < 0) {
                list.add(n);
            } else {
                nums[n-1] = -nums[n-1];
            }
        }
        return list;
    }
}
