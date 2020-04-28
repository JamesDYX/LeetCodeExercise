package L987_Vertical_Order_Traversal_of_a_Binary_Tree;


import java.lang.reflect.Array;
import java.util.*;

class TreeNode {
    int val;
    int index;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class Solution_1 {
    HashMap<Integer, List<Integer>> raw_res = new HashMap<>();
    int leftBound = 0;
    int rightBound = 0;
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        List<TreeNode> candidates = new ArrayList<>();

        root.index = 0;
        candidates.add(root);

        while (candidates.size()!=0)
            candidates = helper(candidates);

        List<List<Integer>> res = new ArrayList<>();
        for (int index=leftBound; index<=rightBound; index++) {
            if (!raw_res.containsKey(index)) continue;
            res.add(raw_res.get(index));
        }
        return res;
    }

    private List<TreeNode> helper(List<TreeNode> candidates){
        HashMap<Integer, List<Integer>> temp_res = new HashMap<>();
        List<TreeNode> nextLayer = new ArrayList<>();
        int leftBound = candidates.get(0).index;
        int rightBound = leftBound;
        for (TreeNode thisNode : candidates){
            rightBound = Math.max(rightBound, thisNode.index);
            leftBound = Math.min(leftBound, thisNode.index);
            if (temp_res.containsKey(thisNode.index)){
                List<Integer> list = temp_res.get(thisNode.index);
                list.add(thisNode.val);
            }
            else {
                List<Integer> list = new ArrayList<>();
                list.add(thisNode.val);
                temp_res.put(thisNode.index, list);
            }
            if (thisNode.left!=null){
                thisNode.left.index = thisNode.index-1;
                nextLayer.add(thisNode.left);
            }
            if (thisNode.right!=null) {
                thisNode.right.index = thisNode.index+1;
                nextLayer.add(thisNode.right);
            }
        }
        for (int index : temp_res.keySet()) {
            List<Integer> list = temp_res.get(index);
            list.sort(new Comparator<Integer>() {
                @Override
                public int compare(Integer o1, Integer o2) {
                    return o1-o2;
                }
            });
            if (!raw_res.containsKey(index)) raw_res.put(index, list);
            else{
                List<Integer> raw_list = raw_res.get(index);
                raw_list.addAll(list);
            }
        }
        this.leftBound = Math.min(this.leftBound, leftBound);
        this.rightBound = Math.max(this.rightBound, rightBound);
        return nextLayer;
    }

    public static void main(String[] args) {
        Solution_1 solution = new Solution_1();
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.left = new TreeNode(15);
        root.right.right = new TreeNode(7);
        List<List<Integer>> res = solution.verticalTraversal(root);
        System.out.println(res.toString());
    }
}
