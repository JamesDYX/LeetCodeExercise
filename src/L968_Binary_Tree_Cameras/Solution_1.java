package L968_Binary_Tree_Cameras;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private int res=0;
    public int minCameraCover(TreeNode root) {
        dfs(root);
        if (root != null && root.val==0) res ++;
        return res;
    }

    private void dfs(TreeNode root){
        if (root == null) return;
        dfs(root.left);
        dfs(root.right);
        if (root.left!=null){
            if (root.left.val==0){
                root.val = 2; // child has a camera
                res ++;
                return;
            }
            else if (root.left.val==2) root.val = 1;
        }
        if (root.right!=null) {
            if (root.right.val==0){
                root.val = 2;
                res ++;
                return;
            }
            else if (root.right.val==2) root.val = 1;
        }
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(0) (0) (0) (0) # 0 # # #");
        System.out.println(solution.minCameraCover(root));
    }
}
