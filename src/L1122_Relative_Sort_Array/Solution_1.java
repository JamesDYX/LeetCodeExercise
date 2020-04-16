package L1122_Relative_Sort_Array;

import java.util.Arrays;
import java.util.HashMap;

public class Solution_1 {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        HashMap<Integer, Integer> res_dict = new HashMap<Integer, Integer>();
        for(int num : arr2){
            res_dict.put(num, 0);
        }
        for(int i = 0; i < arr1.length; i++){
            int num = arr1[i];
            if(res_dict.containsKey(num)){
                res_dict.put(num, res_dict.get(num) + 1);
                arr1[i] = 0;
            }
        }
        Arrays.sort(arr1);
        int i = 0;
        for(int num: arr2){
            for(int j=0; j<res_dict.get(num); j++){
                arr1[i++] = num;
            }
        }
        return arr1;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[][][] test_cases = {
                {
                        {2,3,1,3,2,4,6,7,9,2,19}, {2,1,4,3,9,6}
                }
        };
        for(int[][] test_case : test_cases){
            int[] nums1 = test_case[0];
            int[] nums2 = test_case[1];
            int[] res = solution.relativeSortArray(nums1, nums2);
            System.out.println(Arrays.toString(res));
        }
    }
}
