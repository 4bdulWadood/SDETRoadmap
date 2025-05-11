# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def dfs(node, total):
            if not node:
                return False
            
            # Add current node's value before traversing
            total += node.val
            
            # Check if leaf node
            if not node.left and not node.right:
                return total == targetSum
            
            # Recurse left and right
            left_has_sum = dfs(node.left, total)
            right_has_sum = dfs(node.right, total)
            
            # Subtract node value after traversal (backtracking - not strictly needed here due to scope)
            total -= node.val
            
            #So when there is a path that sums to targetSum, recursively send back True to the root.
            return left_has_sum or right_has_sum

    # O(n) and O(log n)
        
        return dfs(root, 0)
