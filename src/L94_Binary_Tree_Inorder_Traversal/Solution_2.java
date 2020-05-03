package L94_Binary_Tree_Inorder_Traversal;

import L297_Serialize_and_Deserialize_Binary_Tree.Codec;
import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class Solution_2 {
    public List<Integer> inorderTraversal(TreeNode root) {
        TreeNode current = root;
        List<Integer> res = new ArrayList<>();
        while (current!=null){
            if (current.left!=null){
                TreeNode node = current.left;
                while (node.right!=null && node.right!=current) node = node.right;
                if (node.right==null){
                    node.right = current;
                    current = current.left;
                    continue;
                }
                else node.right = null;
            }
            res.add(current.val);
            current = current.right;
        }
        return res;
    }

    public static void main(String[] args){
        Solution_2 solution = new Solution_2();
        TreeNode root = new Codec().deserialize("(2) (3) 1 # #");
        System.out.println(solution.inorderTraversal(root));
    }
}
