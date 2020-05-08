package L236_Lowest_Common_Ancestor_of_a_Binary_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private TreeNode res = null;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        helper(root, p, q);
        return res;
    }

    private boolean helper(TreeNode root, TreeNode p, TreeNode q) {
        if (root==null) return false;
        if (res!=null) return false;
        boolean left_exist = helper(root.left, p, q);
        boolean right_exist = helper(root.right, p, q);
        if (left_exist && right_exist) {
            res = root;
            return true;
        }
        else if ((left_exist || right_exist) && (root.val == p.val || root.val == q.val)) {
            res = root;
            return true;
        }
        else return left_exist || right_exist || root.val==p.val || root.val==q.val;
    }

    public static void main(String[] args) {
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(3) (5) 6 (2) 7 4 (1) 0 8");
        TreeNode p = new TreeNode(5);
        TreeNode q = new TreeNode(1);
        System.out.println(solution.lowestCommonAncestor(root, p, q).val);
    }
}
