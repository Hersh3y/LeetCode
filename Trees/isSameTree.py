# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if (node1 and not node2) or (not node1 and node2):
                return False
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
        return True
