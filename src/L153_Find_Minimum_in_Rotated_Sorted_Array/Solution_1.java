package L153_Find_Minimum_in_Rotated_Sorted_Array;

public class Solution_1 {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int mid = -1;
        while (nums[left] > nums[right]){
            mid = (left + right) / 2;
            if (nums[mid] >= nums[left])
                left = mid+1;
            else
                right = mid - 1;
        }
        if (mid == left - 1)
            return nums[left];
        else
            return nums[right+1];
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[][] test_cases = {
                {3,4,5,1,2},
                {4,5,6,7,0,1,2},
                {7, 6},
                {1, 2},
                {3, 1, 2}
        };
        for (int[] nums : test_cases)
            System.out.println(solution.findMin(nums));
    }
}
