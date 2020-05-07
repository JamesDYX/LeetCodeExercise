package L1123_Lowest_Common_Ancestor_of_Deepest_Leaves;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private TreeNode res;
    private int depth=0;
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        dfsHelper(root, 1);
        return res;
    }

    private int dfsHelper(TreeNode root, int depth) {
        if (root==null) return 0;
        if (root.left==null && root.right==null) {
            if (depth>this.depth){
                this.depth = depth;
                this.res = root;
            }
            return 1;
        }
        else {
            int leftLength = dfsHelper(root.left, depth+1);
            int rightLength = dfsHelper(root.right, depth+1);
            if (leftLength==rightLength && depth+leftLength==this.depth){
                this.res = root;
            }
            return Math.max(leftLength, rightLength) + 1;
        }
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(1) (2) # 3 (4) 5 6");
        System.out.println(solution.lcaDeepestLeaves(root).val);
    }
}
