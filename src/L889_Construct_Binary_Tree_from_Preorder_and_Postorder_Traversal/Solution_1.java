package L889_Construct_Binary_Tree_from_Preorder_and_Postorder_Traversal;


import java.util.HashMap;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


public class Solution_1 {
    HashMap<Integer, Integer> preMap = new HashMap<>();
    int postIndex;
    int[] post;
    public TreeNode constructFromPrePost(int[] pre, int[] post) {
        for (int i=0; i<pre.length; i++) preMap.put(pre[i], i);
        this.postIndex = post.length-1;
        this.post = post;
        return recur(0, post.length-1);
    }
    private TreeNode recur(int left, int right){
        TreeNode root = new TreeNode(this.post[this.postIndex]);
        if (this.postIndex==0) return root;
        this.postIndex--;
        int value = this.post[this.postIndex];
        int valueIndex = this.preMap.get(value);
        if (valueIndex<=right && valueIndex>left)
            root.right = recur(valueIndex, right);
        if (valueIndex-1<=right && valueIndex-1>left)
            root.left = recur(left+1, valueIndex-1);
        return root;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        TreeNode root = solution.constructFromPrePost(
                new int[] {2, 1},
                new int[] {1, 2}
        );
        System.out.println("finish");
    }
}
