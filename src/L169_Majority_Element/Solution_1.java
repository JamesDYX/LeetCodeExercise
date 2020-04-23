package L169_Majority_Element;

public class Solution_1 {
    /*
    Boyer-Moore Voting Algorithm
     */
    public int majorityElement(int[] nums) {
        int majority = 0;
        int counter = 0;
        for(int num: nums) {
            if (counter==0) majority = num;
            counter += (majority==num)? 1: -1;
        }
        return majority;
    }
}
