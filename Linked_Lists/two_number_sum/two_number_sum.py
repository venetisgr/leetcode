# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def find_number(l1,l2):
            #lsb to msb 
            head = ListNode()
            ret = head #return the head of the linked list
            carry = 0
            
            while l1 or l2:#itterate until all numbers are seen
                v1,v2 = 0, 0
                if l1:
                    v1 = l1.val
                if l2:
                    v2 = l2.val
                sm = v1 + v2 + carry
                carry = sm//10
                val = sm%10
                
                #new node
                head.next = ListNode() #creates a new node of the new elements
                head = head.next
                head.val = val
                
                #shift number lists ones
                if l1:#if none we shouldn't updATE
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                
                
            #if equal length we might have an extra carry we need to add in the end
            if carry !=0:
                head.next = ListNode() #creates a new node of the new elements
                head = head.next
                head.val = carry
                
            return ret.next
        
        return find_number(l1,l2)
                
                

            
                