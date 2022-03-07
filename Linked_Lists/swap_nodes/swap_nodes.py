class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #head
        ret = head #points to the head of linked list
        while head and head.next:
            nod1 = head
            nod2 = head.next
            nod1.val,nod2.val = nod2.val,nod1.val          
            #if head.next.next ==None:
            #    break
            head = head.next.next
            
        return ret
        