package L26_Remove_Duplicates_From_Sorted_Array;

import java.util.Arrays;

public class Solution_1 {
    public int removeDuplicates(int[] nums) {
        int last_index = 0;
        for(int i=1; i<nums.length; i++){
            if(nums[i] == nums[last_index])
                continue;
            else last_index++;
            if(i!=last_index)
                nums[last_index] = nums[i];
        }
        return last_index+1;
    }
    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        System.out.println(solution.removeDuplicates(nums));
        System.out.println(Arrays.toString(nums));
    }
}
