from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not left_to_right:
                level.reverse()
            
            result.append(level)
            
            left_to_right = not left_to_right
        
        return result