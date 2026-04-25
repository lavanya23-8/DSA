class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            
            while head:
                # Connect left child -> right child
                head.left.next = head.right
                
                # Connect right child -> next node's left child
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            # Move to next level
            leftmost = leftmost.left
        
        return root