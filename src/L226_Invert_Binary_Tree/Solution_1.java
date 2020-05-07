package L226_Invert_Binary_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;

public class Solution_1 {
    public TreeNode invertTree(TreeNode root) {
        if (root==null) return root;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
