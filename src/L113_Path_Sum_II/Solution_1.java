package L113_Path_Sum_II;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Solution_1 {
    private List<Integer> curPath = new LinkedList<>();
    private List<List<Integer>> res = new LinkedList<>();
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root==null) return res;
        helper(root, sum);
        return res;
    }
    private void helper(TreeNode root, int targetSum){
        curPath.add(root.val);
        targetSum -= root.val;
        if (root.left==null && root.right==null && targetSum==0){
            List<Integer> curRes = new LinkedList<>(curPath);
            res.add(curRes);
        }
        if (root.left!=null) helper(root.left, targetSum);
        if (root.right!=null) helper(root.right, targetSum);
        curPath.remove(curPath.size()-1);
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(-2) # -3");
        List<List<Integer>> res = solution.pathSum(root, -5);
        for (List<Integer> path : res) {
            for (int node : path) System.out.print(node+" ");
            System.out.println();
        }
    }
}
