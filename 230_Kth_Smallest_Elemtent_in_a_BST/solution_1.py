# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.result = None
        self.have_passed = 0

        def DFS(current: TreeNode):
            if not current:
                return False
            if DFS(current.left):
                return True
            self.have_passed += 1
            if self.have_passed == k:
                self.result = current.val
                return True
            if DFS(current.right):
                return True
            return False

        DFS(root)
        return self.result


def build_tree(l: list):
    nodes = []
    for index in range(len(l)):
        if l[index] is None:
            nodes.append(None)
            continue
        node = TreeNode(l[index])
        nodes.append(node)
        if index == 0:
            continue
        parrent_index = int((index-1)/2)
        if index == 2 * parrent_index + 1:
            nodes[parrent_index].left = node
        else:
            nodes[parrent_index].right = node
    return nodes[0]


if __name__ == '__main__':
    test_cases = [
        ([3, 1, 4, None, 2], 1),
        ([5,3,6,2,4,None,None,1], 3)
    ]

    solution = Solution()
    for test_case, k in test_cases:
        root = build_tree(test_case)
        print(solution.kthSmallest(root, k))
