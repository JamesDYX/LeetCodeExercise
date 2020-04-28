package L117_Populating_Next_Right_Pointers_in_Each_Node_II;


import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}


public class Solution_1 {
    public Node connect(Node root) {
        if (root==null) return null;

        Queue<Node> queue = new ArrayDeque<>();

        queue.offer(root);
        queue.offer(new Node(101));
        Node lastNode = null;
        while (!queue.isEmpty()){
            Node thisNode= queue.poll();
            if (thisNode.val==101){
                if (!queue.isEmpty())
                    queue.offer(new Node(101));
                lastNode.next = null;
                lastNode = null;
            }
            else {
                if (thisNode.left != null) queue.offer(thisNode.left);
                if (thisNode.right != null) queue.offer(thisNode.right);
                if (lastNode!=null) lastNode.next = thisNode;
                lastNode = thisNode;
            }
        }

        return root;
    }

    public static void main(String[] args){
        Solution_1 solution = new Solution_1();
        Node root = new Node(1);
        root = solution.connect(root);
    }
}
