package L81_Search_in_Rotated_Sorted_Array_II;

public class Solution_1 {
    public boolean search(int[] nums, int target) {
        if(nums.length==0) return false;
        int i = 0;
        int j = nums.length - 1;
        // first step is to make the first and the last number not same.
        if(nums[0] == nums[nums.length-1]){
            if(nums[0] == target) return true;
            int duplicate = nums[0];
            for(i=1; i<nums.length && nums[i]==duplicate; i++);
            for(j=nums.length-2; j>=i && nums[j]==duplicate; j--);
        }
        if (i>=nums.length || j<0) return false;

        // if from i to j is rotated, then find the peak and make i to j sorted
        if(nums[i]>nums[j]){
            int left = i;
            int right = j;
            int mid = 0;
            while (nums[left] > nums[right]){
                mid = (left + right) / 2;
                if (nums[mid] >= nums[left])
                    left = mid+1;
                else
                    right = mid - 1;
            }
            int peak;
            if (mid == left - 1)
                peak = mid;
            else
                peak = right;
            if(target>=nums[i]) j = peak;
            else i = peak + 1;
        }

        // binary search
        while (i<=j){
            int mid = (i+j) / 2;
            if(nums[mid] == target) return true;
            else if (nums[mid] > target) j = mid - 1;
            else i = mid + 1;
        }
        return false;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {5, 1, 3};
        System.out.println(solution.search(nums, 1));
    }
}
