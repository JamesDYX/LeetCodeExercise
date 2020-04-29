package L173_Binary_Search_Tree_Iterator;

import L297_Serialize_and_Deserialize_Binary_Tree.TreeNode;
import L297_Serialize_and_Deserialize_Binary_Tree.Codec;

public class Solution_1 {
    private TreeNode head;
    public Solution_1(TreeNode root) {
        if (root==null){
            head = null;
            return;
        }
        TreeNode[] nodeLink = reSort(root);
        nodeLink[1].left=null;
        head = nodeLink[0];
    }

    private TreeNode[] reSort(TreeNode root){
        TreeNode[] nodeLink = new TreeNode[2];
        if (root.left==null) nodeLink[0] = root;
        else {
            TreeNode[] leftLink = reSort(root.left);
            nodeLink[0] = leftLink[0];
            leftLink[1].left = root;
        }
        if (root.right==null) nodeLink[1] = root;
        else{
            TreeNode[] rightLink = reSort(root.right);
            nodeLink[1] = rightLink[1];
            root.left = rightLink[0];
        }
        return nodeLink;
    }

    /** @return the next smallest number */
    public int next() {
        int res = head.val;
        head = head.left;
        return res;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return head != null;
    }

    public static void main(String[] args){
        TreeNode root = new Codec().deserialize("(7) 3 (15) 9 20");
        Solution_1 solution = new Solution_1(root);
        while (solution.hasNext())
            System.out.println(solution.next());
    }
}
