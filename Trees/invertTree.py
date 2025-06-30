# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            node_left = node.left
            node.left = node.right
            node.right = node_left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
