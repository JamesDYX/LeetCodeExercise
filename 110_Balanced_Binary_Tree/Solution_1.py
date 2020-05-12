class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Constructor:

    def __init__(self, string=''):
        self.string_list = str.split(string, ' ')
        self.string_index = 0

    def construct(self) -> TreeNode:
        if self.string_index >= len(self.string_list) or \
                self.string_list[self.string_index] == '#':
            self.string_index += 1
            return None
        elif self.string_list[self.string_index][0] == '(':
            root = TreeNode(int(self.string_list[self.string_index][1:-1]))
            self.string_index += 1
            left = self.construct()
            right = self.construct()
            root.left = left
            root.right = right
            return root
        else:
            root = TreeNode(int(self.string_list[self.string_index]))
            self.string_index += 1
            return root

    def deconstruct(self, node: TreeNode):
        if node is None:
            return "#"
        elif node.left is None and node.right is None:
            return str(node.val)
        else:
            this = '(' + str(node.val) + ')'
            return this + ' ' + self.deconstruct(node.left) + ' ' + self.deconstruct(node.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.helper(root) == -1:
            return False
        return True

    def helper(self, root):
        if root is None:
            return 0
        left_height = self.helper(root.left)
        if left_height == -1:
            return -1
        right_height = self.helper(root.right)
        if right_height == -1:
            return -1
        if abs(left_height-right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
