package L1110_Delet_Nodes_And_Return_Forest;


import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution_1 {
    private List<TreeNode> res = new ArrayList<>();
    private HashSet<Integer> to_delete = new HashSet<>();
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        for (int delete: to_delete)
            this.to_delete.add(delete);
        TreeNode base = new TreeNode(-1);
        base.left = root;
        prune(base);
        if (base.left!=null)
            res.add(root);
        return res;
    }

    private void prune(TreeNode root){
        if (root==null) return;
        prune(root.left);
        prune(root.right);
        if (root.left!=null && this.to_delete.contains(root.left.val)){
            if (root.left.left!=null) res.add(root.left.left);
            if (root.left.right!=null) res.add(root.left.right);
            root.left = null;
        }
        if (root.right!=null && this.to_delete.contains(root.right.val)){
            if (root.right.left!=null) res.add(root.right.left);
            if (root.right.right!=null) res.add(root.right.right);
            root.right = null;
        }
    }

    public static void main(String[] args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        List<TreeNode> res = new Solution_1().delNodes(root, new int[]{1});
        System.out.println("Finish");
    }
}
