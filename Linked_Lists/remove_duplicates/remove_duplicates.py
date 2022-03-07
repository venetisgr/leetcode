# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = head
        
        while head and head.next:
#             if head.next.val ==None: #end value stop
#                 break            
            if head.next.val != head.val: #if next value different than current, no duplicate, move right
                head = head.next
                
            else:
                #delete next node, they are equal
                head.next = head.next.next
                
        return ret
        
        
                    
        