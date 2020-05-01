package L979_Distribute_Coins_in_Binary_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private int res = 0;
    public int distributeCoins(TreeNode root) {
        dfs(root);
        return res;
    }

    public void dfs(TreeNode root){
        if (root==null) return;
        dfs(root.left);
        dfs(root.right);
        if (root.left!=null) {
            res += Math.abs(root.left.val-1);
            root.val += root.left.val-1;
        }
        if (root.right!=null) {
            res += Math.abs(root.right.val-1);
            root.val += root.right.val-1;
        }
    }

    public static void main(String[] args) {
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(1) (0) # 3 0");
        System.out.println(solution.distributeCoins(root));
    }
}
