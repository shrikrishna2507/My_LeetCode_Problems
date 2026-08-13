# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def get_height(self, node):
        # Base case: height of empty node is 0
        if not node:
            return 0
        
        # Height of current node is 1 + max height of its subtrees
        return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        
        left_h = self.get_height(root.left)
        right_h = self.get_height(root.right)
        

        if abs(left_h - right_h) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
            
        return False