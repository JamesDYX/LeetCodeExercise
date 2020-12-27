class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    index_preord = 0
    map_inord = {}
    preorder = None

    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        self.preorder = preorder
        for i in range(len(inorder)):
            self.map_inord[inorder[i]] = i
        return self.helper(0, len(self.preorder)-1)

    def helper(self, left_range, right_range):
        if self.index_preord >= len(self.preorder):
            return None
        if left_range > right_range:
            return None
        index_inord = self.map_inord[self.preorder[self.index_preord]]
        if index_inord < left_range or index_inord > right_range:
            return None

        node = TreeNode(self.preorder[self.index_preord])
        self.index_preord += 1
        node.left = self.helper(left_range, index_inord-1)
        node.right = self.helper(index_inord+1, right_range)
        return node


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    node = Solution().buildTree(preorder, inorder)
    print('ends')
