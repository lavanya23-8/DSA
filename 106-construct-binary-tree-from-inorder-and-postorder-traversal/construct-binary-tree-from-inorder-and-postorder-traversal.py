class Solution(object):
    def buildTree(self, inorder, postorder):
        # Map value -> index for fast lookup
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        self.post_idx = len(postorder) - 1
        
        def helper(left, right):
            if left > right:
                return None
            
            # Get root
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            
            root = TreeNode(root_val)
            
            # Find position in inorder
            index = inorder_map[root_val]
            
            # IMPORTANT: build right first
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)