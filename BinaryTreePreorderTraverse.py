"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example: Given binary tree {1,#,2,3},

        1
         \
          2
         /
        3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        temp = []
        res = []
        if not root:
            return res
        temp.append(root)
        while len(temp):
            node = temp.pop()
            res.append(node.val)
            if node.right:
                temp.append(node.right)
            if node.left:
                temp.append(node.left)
        return res