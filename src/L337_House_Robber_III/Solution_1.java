package L337_House_Robber_III;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    public int rob(TreeNode root) {
        int[] res = dfsHelper(root);
        return Math.max(res[0], res[1]);
    }

    private int[] dfsHelper(TreeNode root){
        if (root==null) return new int[]{0, 0};
        int[] left = dfsHelper(root.left);
        int[] right = dfsHelper(root.right);
        return new int[]{root.val+left[1]+right[1], Math.max(left[0], left[1])+Math.max(right[0], right[1])};
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(3) (4) 1 3 (5) # 1");
        System.out.println(solution.rob(root));
    }
}
