class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.build(1, n)
    
    def build(self, start, end):
        res = []
        
        if start > end:
            return [None]
        
        for i in range(start, end + 1):
            left_trees = self.build(start, i - 1)
            right_trees = self.build(i + 1, end)
            
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)
        
        return res