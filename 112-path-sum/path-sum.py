class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # If it's a leaf node
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recur for left and right subtree
        remaining = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))