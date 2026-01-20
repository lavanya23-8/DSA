import heapq

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        
        # Step 1: push first node of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        # Step 2: extract min and push next node
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
