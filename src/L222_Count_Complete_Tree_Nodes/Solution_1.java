package L222_Count_Complete_Tree_Nodes;


import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution_1 {
    TreeNode root;
    public int countNodes(TreeNode root) {
        this.root = root;
        if (root==null) return 0;
        int depth = 1;
        while (root.left!=null){
            root = root.left;
            depth ++;
        }
        int left = (int)Math.pow(2, depth-1) + 1;
        int right = (int)Math.pow(2, depth) - 1;
        while (left <= right){
            int mid = (left+right) / 2;
            if (exist(mid)) left = mid + 1;
            else right = mid - 1;
        }
        return right;
    }
    private boolean exist(int length){
        List<Integer> path = new ArrayList<>();
        while (length!=1){
            if (length % 2 == 0) path.add(0);
            else path.add(1);
            length /= 2;
        }
        TreeNode root = this.root;
        for (int i=path.size()-1; i>=0; i--){
            int direction = path.get(i);
            if (root==null) return false;
            if (direction==0) root = root.left;
            else root = root.right;
        }
        return root!=null;
    }
    public static void main(String[] args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        Solution_1 solution = new Solution_1();
        System.out.println(solution.countNodes(root));
    }
}
