package L965_Univalued_Binary_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.ArrayDeque;
import java.util.Queue;

public class Solution_1 {
    public boolean isUnivalTree(TreeNode root) {
        if (root==null) return true;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node.left!=null){
                if (node.val==node.left.val) queue.offer(node.left);
                else return false;
            }
            if (node.right!=null) {
                if (node.val==node.right.val) queue.offer(node.right);
                else return false;
            }
        }
        return true;
    }
}
