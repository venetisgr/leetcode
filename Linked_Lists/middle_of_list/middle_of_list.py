class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Fast and Slow pointer
        #Fast pointer does two steps while slow one. By the time fast reaches the end, slow is in the middle
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
        
