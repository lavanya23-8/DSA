class Solution(object):
    def sortedListToBST(self, head):
        
        # Base case
        if not head:
            return None
        
        # If only one node
        if not head.next:
            return TreeNode(head.val)
        
        # Find middle using slow-fast pointer
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect left half
        if prev:
            prev.next = None
        
        # Middle becomes root
        root = TreeNode(slow.val)
        
        # Recursively build left & right
        root.left = self.sortedListToBST(head if slow != head else None)
        root.right = self.sortedListToBST(slow.next)
        
        return root