package L75_Sort_Colors;

import java.util.Arrays;

public class Solution_1 {
    public void sortColors(int[] nums) {
        int left= 0;
        int right = nums.length - 1;
        int left_counter = 0;
        int right_counter = 0;
        while(true){
            while(left<=right){
                if(nums[left] == 2) break;
                else if (nums[left]==1) left_counter++;
                else if (left_counter!=0) {
                    nums[left-left_counter] = 0;
                    nums[left] = 1;
                }
                left ++;
            }
            while(left<=right){
                if(nums[right] == 0) break;
                else if (nums[right]==1) right_counter++;
                else if (right_counter!=0) {
                    nums[right+right_counter] = 2;
                    nums[right] = 1;
                }
                right --;
            }
            if(left>=right) break;
            nums[left-left_counter] = 0;
            nums[right+right_counter] = 2;
            if(left_counter!=0) nums[left] = 1;
            if(right_counter!=0) nums[right] = 1;
            left ++;
            right --;
        }
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {2,0,2,1,1,0,1, 0, 2};
        solution.sortColors(nums);
        System.out.println(Arrays.toString(nums));
    }
}
