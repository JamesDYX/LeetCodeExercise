package L105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal;

import java.util.HashMap;
import java.util.Map;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution_1 {
    private int[] preorder;
    private int[] inorder;
    private Map<Integer, int[]> order_map = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        for (int i=0; i<preorder.length; i++){
            if(order_map.containsKey(preorder[i]))
                order_map.get(preorder[i])[0] = i;
            else
                order_map.put(preorder[i], new int[]{i, 0});
            if(order_map.containsKey(inorder[i]))
                order_map.get(inorder[i])[1] = i;
            else
                order_map.put(inorder[i], new int[]{0, i});
        }
        return recur(0, preorder.length-1, 0, preorder.length-1);
    }

    private TreeNode recur(int pre_left, int pre_right, int in_left, int in_right){
        if (pre_left > pre_right) return null;
        int rootValue = this.preorder[pre_left];
        TreeNode root = new TreeNode(rootValue);
        int root_index_inorder = order_map.get(rootValue)[1];
        int next_pre_right = pre_left;
        for (int i=Math.max(in_left, root_index_inorder-2); i<root_index_inorder; i++){
            next_pre_right = Math.max(next_pre_right, order_map.get(inorder[i])[0]);
        }
        root.left = recur(pre_left+1, next_pre_right, in_left, root_index_inorder - 1);
        root.right = recur(next_pre_right+1, pre_right, root_index_inorder+1, in_right);
        return root;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        int[] preorder = {3,2, 1, 4};
        int[] inorder = {1, 2, 3, 4};
        TreeNode root = solution.buildTree(preorder, inorder);
        System.out.println("finish");
    }
}
