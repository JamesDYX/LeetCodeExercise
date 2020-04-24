package L105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal;

import java.util.HashMap;
import java.util.Map;

public class Solution_2 {
    private int[] preorder;
    private int preorderIdx;
    private Map<Integer, Integer> idxMap;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) {
            return null;
        }

        this.preorderIdx = 0;
        this.idxMap = new HashMap<>();
        this.preorder = preorder;
        for (int i = 0; i < inorder.length; i++) {
            idxMap.put(inorder[i], i);
        }

        return recur(0, preorder.length - 1);
    }

    private TreeNode recur(int left, int right) {
        if (preorderIdx >= preorder.length) {
            return null;
        }

        int value = preorder[preorderIdx];
        int valueIdx = idxMap.get(value);

        if (valueIdx < left || valueIdx > right) {
            return null;
        }

        TreeNode node = new TreeNode(value);
        preorderIdx++;

        node.left = recur(left, valueIdx - 1);
        node.right = recur(valueIdx + 1, right);

        return node;
    }
}
