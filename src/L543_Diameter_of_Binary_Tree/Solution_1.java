package L543_Diameter_of_Binary_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    int res = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        dfsHelper(root);
        return res;
    }

    private int dfsHelper(TreeNode root){
        if (root==null) return 0;
        int left = dfsHelper(root.left);
        int right = dfsHelper(root.right);
        res = Math.max(left+right, res);
        return Math.max(left, right) + 1;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(1) (2) 4 5 3");
        System.out.println(solution.diameterOfBinaryTree(root));
    }
}
