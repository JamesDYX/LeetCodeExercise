class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if root is None:
            return root
        queue = [root]
        while queue[0].left is not None:
            new_queue = [queue[0].left, queue[0].right]
            queue[0].left.next = queue[0].right
            lastnode = queue[0].right
            for node in queue[1:]:
                lastnode.next = node.left
                new_queue.append(node.left)
                node.left.next = node.right
                new_queue.append(node.right)
                lastnode = node.right
            queue = new_queue
        return root


if __name__ == '__main__':
    solution = Solution()
    root = Node(0)
    left = Node(1)
    right = Node(2)
    root.left = left
    root.right = right
    solution.connect(root)
    print(root.next)
    print(left.next.val)
    print(right.next)
