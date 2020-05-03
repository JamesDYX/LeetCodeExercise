package L99_Recover_Binary_Search_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private TreeNode first;
    private TreeNode second;
    private TreeNode pre;
    public void recoverTree(TreeNode root) {
        inorderTraverse(root);
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }

    public void inorderTraverse(TreeNode root){
        if (root==null) return;
        inorderTraverse(root.left);
        if (pre!=null && root.val<pre.val){
            if (first==null) first = pre;
            second = root;
        }
        pre = root;
        inorderTraverse(root.right);
    }
}
