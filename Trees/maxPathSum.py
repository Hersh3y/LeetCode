# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_path_sum = [root.val]
        def path_sum(node):
            if not node:
                return 0
            left_path = max(path_sum(node.left), 0)
            right_path = max(path_sum(node.right), 0)
            max_path_sum[0] = max(max_path_sum[0], node.val + left_path + right_path)
            return node.val + max(left_path, right_path)
        path_sum(root)
        return max_path_sum[0]
