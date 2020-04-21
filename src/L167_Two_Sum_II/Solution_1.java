package L167_Two_Sum_II;

public class Solution_1 {
    public int[] twoSum(int[] numbers, int target) {
        int first = 0;
        int second = numbers.length - 1;
        while (true){
            int sum = numbers[first] + numbers[second];
            if(sum > target) second --;
            else if(sum < target) first++;
            else break;
        }
        return new int[]{first+1, second+1};
    }
}
