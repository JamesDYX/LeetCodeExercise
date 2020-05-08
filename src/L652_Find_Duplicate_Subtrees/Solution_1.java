package L652_Find_Duplicate_Subtrees;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.*;

public class Solution_1 {
    private HashMap<String, TreeNode> map = new HashMap<>();
    private HashSet<String> res = new HashSet<>();
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        serialize(root);
        List<TreeNode> ans = new ArrayList<>();
        for (String key : res) ans.add(map.get(key));
        return ans;
    }

    private String serialize(TreeNode root) {
        if (root==null) return "#";
        if (root.left==null && root.right==null) {
            String key = Integer.toString(root.val);
            if (map.containsKey(key)) res.add(key);
            else map.put(key, root);
            return key;
        }
        String node = "(" + Integer.toString(root.val) + ")";
        String left = serialize(root.left);
        String right = serialize(root.right);
        String key = node + " " + left + " " + right;
        if (map.containsKey(key)) res.add(key);
        else map.put(key, root);
        return key;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = new Codec().deserialize("(1) (2) 4 # (3) (2) 4 # 4");
        for (TreeNode node : solution.findDuplicateSubtrees(root)){
            System.out.print(node.val);
        }
    }
}
