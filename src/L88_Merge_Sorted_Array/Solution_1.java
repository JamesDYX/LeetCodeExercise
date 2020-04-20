package L88_Merge_Sorted_Array;

import java.util.Arrays;

public class Solution_1 {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int i = m + n - 1; m > 0 && n > 0; i --){
            int num1 = nums1[m-1];
            int num2 = nums2[n-1];
            if(num1 >= num2) {
                nums1[i] = num1;
                m--;
            }else{
                nums1[i] = num2;
                n--;
            }
        }
        if (n >= 0) System.arraycopy(nums2, 0, nums1, 0, n);
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] nums1 = {1,2,3,0,0,0};
        int[] nums2 = {2,5,6};

        solution.merge(nums1, 3, nums2, 3);
        System.out.println(Arrays.toString(nums1));
    }
}
