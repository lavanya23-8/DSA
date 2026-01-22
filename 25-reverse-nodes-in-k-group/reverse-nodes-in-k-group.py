class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            # Step 1: check if there are k nodes
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next

            # Step 2: reverse k nodes
            prev, curr = group_next, prev_group.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Step 3: connect with previous part
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
