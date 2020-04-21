package L219_Contains_Duplicate_II;

import java.util.HashSet;

public class Solution_1 {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        k = Math.min(k, nums.length-1);
        HashSet<Integer> Set = new HashSet<>();
        for(int i=0; i<=k; i++){
            if(Set.contains(nums[i])) return true;
            Set.add(nums[i]);
        }
        for(int i=1; i+k<nums.length; i++){
            Set.remove(nums[i-1]);
            if(Set.contains(nums[i+k])) return true;
            Set.add(nums[i+k]);
        }
        return false;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums = {1,2,3,1,2,3};
        System.out.println(solution.containsNearbyDuplicate(nums, 2));
    }
}
