class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def isMirror(left_node, right_node):
            if not left_node and not right_node:
                return True
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            outer_match = isMirror(left_node.left, right_node.right)
            inner_match = isMirror(left_node.right, right_node.left)
            
            return outer_match and inner_match
        
        if not root:
            return True
            
        return isMirror(root.left, root.right)