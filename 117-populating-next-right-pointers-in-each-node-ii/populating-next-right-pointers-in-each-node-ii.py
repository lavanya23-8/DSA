class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return root
        
        # Start from the first node of each level
        curr = root
        
        while curr:
            dummy = Node(0)   # Dummy node for next level
            tail = dummy      # Tail to build next level links
            
            # Traverse current level using next pointers
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next
            
            # Move to next level
            curr = dummy.next
        
        return root