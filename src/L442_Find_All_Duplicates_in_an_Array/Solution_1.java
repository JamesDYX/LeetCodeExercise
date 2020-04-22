package L442_Find_All_Duplicates_in_an_Array;

import java.util.ArrayList;
import java.util.List;

public class Solution_1 {
    /*
    resort the array
     */
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        for(int i=0; i<nums.length; i++){
            if (nums[i]==i+1 || nums[i]==0) continue;
            int leave = nums[i];
            nums[i] = 0;
            while (true){
                if (nums[leave-1] == 0){
                    nums[leave-1] = leave;
                    break;
                }
                else if (nums[leave-1] == leave) {
                    res.add(leave);
                    break;
                }
                else{
                    int temp = leave;
                    leave = nums[temp - 1];
                    nums[temp - 1] = temp;
                }
            }
        }
        return res;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {13,8,5,3,20,12,3,20,5,16,9,19,12,11,13,19,11,1,10,2};
        List<Integer> res = solution.findDuplicates(nums);
        System.out.println(res.toString());
    }
}
