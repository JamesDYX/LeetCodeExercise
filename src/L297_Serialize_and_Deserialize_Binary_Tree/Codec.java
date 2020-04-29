package L297_Serialize_and_Deserialize_Binary_Tree;

public class Codec {
    String[] rawNodes;
    int index;
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root==null) return "#";
        if (root.left==null && root.right==null) return Integer.toString(root.val);
        String node = "(" + Integer.toString(root.val) + ")";
        String left = serialize(root.left);
        String right = serialize(root.right);
        return node + " " + left + " " + right;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        this.rawNodes = data.split(" ");
        this.index = 0;
        return preorder();
    }

    private TreeNode preorder(){
        String raw_node = rawNodes[index++];
        if (raw_node.startsWith("#")) {
            return null;
        }
        else if (raw_node.startsWith("(")){
            raw_node = raw_node.substring(1, raw_node.length()-1);
            TreeNode root = new TreeNode(Integer.valueOf(raw_node));
            root.left = preorder();
            root.right = preorder();
            return root;
        }
        else return new TreeNode(Integer.valueOf(raw_node));
    }

    public static void main(String[] args){
        Codec solution = new Codec();
        TreeNode root = solution.deserialize("(1) 2 (3) 4 5");
        System.out.println(solution.serialize(root));
    }
}
