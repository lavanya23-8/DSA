class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from end
        slow.next = slow.next.next

        return dummy.next
