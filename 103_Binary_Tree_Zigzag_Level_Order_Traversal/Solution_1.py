class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list:
        if root is None:
            return []

        res = []
        candidates = [root]
        left_to_right = 1
        while candidates:
            temp_candidatea = []
            temp_res = []
            for candidate in candidates:
                if candidate.left is not None:
                    temp_candidatea.append(candidate.left)
                if candidate.right is not None:
                    temp_candidatea.append(candidate.right)
                temp_res.append(candidate.val)
            if left_to_right:
                res.append(temp_res)
            else:
                res.append(temp_res[::-1])
            left_to_right = 1 - left_to_right
            candidates = temp_candidatea
        return res


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


if __name__ == '__main__':
    solution = Solution()
    root = Constructor("(3) 9 (20) 15 7").construct()
    print(solution.zigzagLevelOrder(root))
