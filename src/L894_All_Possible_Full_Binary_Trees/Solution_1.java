package L894_All_Possible_Full_Binary_Trees;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

import java.util.ArrayList;
import java.util.List;

public class Solution_1 {
    private List<List<TreeNode>> res = new ArrayList<>();
    public List<TreeNode> allPossibleFBT(int N) {
        if (N%2==0) return new ArrayList<>();
        for(int n=1; n<=N; n+=2) {
            int total = n-1;
            List<TreeNode> new_res = new ArrayList<>();
            if (total==0){
                TreeNode root= new TreeNode(0);
                root.left=null;
                root.right=null;
                new_res.add(root);
            }
            for(int left=1; left<=total/2; left+=2){
                int left_index = (left-1) / 2;
                int right_index = (total - left - 1) / 2;
                for (TreeNode left_root : res.get(left_index)){
                    for (TreeNode right_root : res.get(right_index)){
                        TreeNode root1= new TreeNode(0);
                        root1.left = left_root;
                        root1.right = right_root;
                        new_res.add(root1);
                        if (left_index!=right_index){
                            TreeNode root2 = new TreeNode(0);
                            root2.left = right_root;
                            root2.right = left_root;
                            new_res.add(root2);
                        }
                    }
                }
            }
            res.add(new_res);
        }
        return res.get((N-1)/2);
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        Codec printer = new Codec();
        List<TreeNode> res = solution.allPossibleFBT(4);
        for (TreeNode root : res){
            System.out.println(printer.serialize(root));
        }
    }
}
