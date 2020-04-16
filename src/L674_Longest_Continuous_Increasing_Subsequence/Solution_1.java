package L674_Longest_Continuous_Increasing_Subsequence;

public class Solution_1 {
    public int findLengthOfLCIS(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        int startIndex = 0;
        int endIndex = 0;
        int maxLength = 0;
        int i;
        for(i = 1; i < nums.length; i++){
            if(nums[i] > nums[endIndex]){
                endIndex = i;
            }
            else{
                maxLength = Math.max(maxLength, i - startIndex);
                startIndex = endIndex = i;
            }
        }
        return Math.max(maxLength, i - startIndex);
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {2,2,2,2,2};
        System.out.println(solution.findLengthOfLCIS(nums));
    }
}
