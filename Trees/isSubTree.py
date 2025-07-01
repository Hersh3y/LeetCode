# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isSameTree(p, q):
            stack = [(p, q)]
            while stack:
                node1, node2 = stack.pop()
                if not node1 and not node2:
                    continue
                elif not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            return True
        main_stack = [root]
        while main_stack:
            node = main_stack.pop()
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                main_stack.append(node.left)
            if node.right:
                main_stack.append(node.right)
        return False
