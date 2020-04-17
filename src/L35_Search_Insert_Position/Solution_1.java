package L35_Search_Insert_Position;

public class Solution_1 {
    public int searchInsert(int[] nums, int target) {
        // binary search
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (nums[mid] == target){
                left = mid;
                break;
            }
            else if (nums[mid] < target)
                left = mid + 1;
            else right = mid - 1;
        }
        return left;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {1,3,5,6};
        System.out.println(solution.searchInsert(nums, 0));
    }
}
