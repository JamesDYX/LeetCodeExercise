package L98_Validate_Binary_Search_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private long lastValue = Long.MIN_VALUE;
    public boolean isValidBST(TreeNode root) {
        if (root==null) return true;
        if (root.left!=null && !isValidBST(root.left)) return false;
        if (lastValue >= root.val) return false;
        lastValue = root.val;
        return root.right == null || isValidBST(root.right);
    }

    public static void main(String[] args) {
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("-2147483648");
        System.out.println(solution.isValidBST(root));
    }
}
