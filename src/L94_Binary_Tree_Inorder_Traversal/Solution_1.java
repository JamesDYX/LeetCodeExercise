package L94_Binary_Tree_Inorder_Traversal;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.*;

public class Solution_1 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root==null) return res;
        ArrayDeque<TreeNode> stack = new ArrayDeque<>();
        TreeNode returnNode = null;
        while (true){
            if (root.left!=null){
                stack.offer(root);
                root = root.left;
                continue;
            } else{
                if (returnNode!=null){
                    root.left = returnNode.right;
                    returnNode.right = null;
                    returnNode = null;
                }
                res.add(root.val);
            }
            if (root.right!=null) root = root.right;
            else if (stack.isEmpty()) return res;
            else {
                returnNode = root;
                root = stack.pollLast();
                returnNode.right = root.left;
                root.left = null;
            }
        }
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(2) (3) 1 # #");
        System.out.println(solution.inorderTraversal(root));
    }
}
