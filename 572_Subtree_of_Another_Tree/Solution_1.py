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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        str_s = self.helper(s)
        str_t = self.helper(t)
        if str_s.find(str_t) == -1:
            return False
        return True

    def helper(self, node: TreeNode):
        if node is None:
            return "#"
        elif node.left is None and node.right is None:
            return '[' + str(node.val) + ']'
        else:
            this = '(' + str(node.val) + ')'
            return this + ' ' + self.helper(node.left) + ' ' + self.helper(node.right)


if __name__ == '__main__':
    solution = Solution()
    test_cases = [
        (Constructor("(4) (-9) # (-1) (-6) # (-2) -3 # 0 (5) # (8) 7 #").construct(),
         Constructor("5").construct()),
    ]

    for s, t in test_cases:
        print(solution.isSubtree(s, t))
        print(Constructor().deconstruct(s))
        print(Constructor().deconstruct(t))
