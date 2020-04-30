package L958_Check_Completeness_of_a_Binary_Tree;
import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.ArrayDeque;

public class Solution_1 {
    public boolean isCompleteTree(TreeNode root) {
        if (root==null) return true;
        boolean lastLayer = false;
        ArrayDeque<TreeNode> candidates = new ArrayDeque<>();
        candidates.offer(root);
        while (!candidates.isEmpty()) {
            if (lastLayer) {
                for (TreeNode candidate : candidates){
                    if (candidate.left!=null || candidate.right!=null) return false;
                }
                return true;
            }
            int size = candidates.size();
            int i = 0;
            for (i=0; i<size; i++){
                TreeNode candidate = candidates.poll();
                if (candidate.left!=null && candidate.right!=null){
                    candidates.offer(candidate.left);
                    candidates.offer(candidate.right);
                } else{
                    lastLayer = true;
                    if (candidate.left!=null){
                        candidates.offer(candidate.left);
                        i++;
                        break;
                    } else if(candidate.right!=null){
                        return false;
                    } else{
                        i ++;
                        break;
                    }
                }
            }
            for (; i<size; i++) {
                TreeNode candidate = candidates.poll();
                if (candidate.left!=null || candidate.right!=null) return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("1");
        System.out.println(solution.isCompleteTree(root));
    }
}
