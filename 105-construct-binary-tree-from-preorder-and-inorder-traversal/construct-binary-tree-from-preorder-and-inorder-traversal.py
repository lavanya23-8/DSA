class Solution(object):
    def buildTree(self, preorder, inorder):
        # Map value -> index
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        self.pre_index = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            
            root = TreeNode(root_val)
            
            index = inorder_map[root_val]
        
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)