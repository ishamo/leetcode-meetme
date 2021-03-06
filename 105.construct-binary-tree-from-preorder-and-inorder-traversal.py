# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        node = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        preorder.pop(0)
        node.left = self.buildTree(preorder, inorder[0:idx])
        node.right = self.buildTree(preorder, inorder[idx+1:])
        return node
