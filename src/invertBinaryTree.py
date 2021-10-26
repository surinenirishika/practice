'''
Created on Oct 25, 2021

@author: rishikasurineni
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if not node:
                return root
            helper(node.left)
            helper(node.right)
            node.left,node.right = node.right, node.left
        helper(root)
        return root
            