# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        hashmap = {}
        
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            node_copy = Node(node.val)
            hashmap[node] = node_copy
            for i in node.neighbors:
                node_copy.neighbors.append(dfs(i))
            return node_copy
        
        return dfs(node)
    