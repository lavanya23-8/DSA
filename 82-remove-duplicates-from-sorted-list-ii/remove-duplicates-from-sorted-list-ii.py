
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
    
        dummy = ListNode(0, head)   
        prev = dummy                
        curr = head                 
        while curr:
           
            if curr.next and curr.val == curr.next.val:
                
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  
            else:
                prev = prev.next       
            curr = curr.next          
        return dummy.next