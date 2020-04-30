package L662_Maximum_Width_of_Binary_Tree;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.ArrayDeque;

public class Solution_1 {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) return 0;
        root.val = 1;
        ArrayDeque<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        int maxWidth = 1;
        while(!q.isEmpty()){
            int size = q.size();
            int left = q.peek().val;
            int right = left;
            for (int i = 0; i < size; i++){
                root = q.poll();
                right = root.val;
                if (root.left != null) {
                    root.left.val = root.val * 2 - 1;
                    q.offer(root.left);
                }
                if (root.right != null){
                    root.right.val = root.val * 2;
                    q.offer(root.right);
                }
            }
            if ((right - left + 1) > maxWidth) maxWidth = right - left + 1;
        }
        return maxWidth;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(1) (3) (5) 6 # # (2) # (9) # 7");
        System.out.println(solution.widthOfBinaryTree(root));
    }
}
