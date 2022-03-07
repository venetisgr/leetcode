# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Complexity O(N+M) 
        
        #Method 1 Dont modify original nodes
        
        if (list1 == None) and (list2 == None):
            return 
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        head1 = list1
        head2 = list2
        #GOOD PRACTICE TO ADD A DUMMY NODE
        head = ListNode() #always points there, first node is dummy will be removed in the end
        tail = head #moves down the list
        
        while head1 != None  and head2 != None:
            
            
            if head1.val<= head2.val:
                tail.next = ListNode()#create new list node
                tail = tail.next
                tail.val = head1.val
                head1 = head1.next                
                
            elif head2.val< head1.val:
                tail.next = ListNode()#create new list node
                tail = tail.next
                tail.val = head2.val
                head2 = head2.next  
                
                
                
        while head1 != None:
            tail.next = ListNode()#create new list node
            tail = tail.next
            tail.val = head1.val
            head1 = head1.next  
            
                
        while head2 != None:            
            tail.next = ListNode()#create new list node
            tail = tail.next
            tail.val = head2.val
            head2 = head2.next  
        
        return head.next
             

                
#         #Method 2 Modify the original nodes
        
        
#         #edge cases 
#         if (list1 == None) and (list2 == None):
#             return 
#         if list1 == None:
#             return list2
#         if list2 == None:
#             return list1
        
        
#         #modify original nodes to point the next element
#         #we point to the existing list node and change its nexte element
        
#         head1 = list1
#         head2 = list2        
#         head = ListNode()
#         tail = head
        
#         while head1 != None  and head2 != None:
            
#             if head1.val<= head2.val:
#                 tail.next = head1
#                 head1 = head1.next 
#                 tail = tail.next
#             elif head2.val< head1.val:     
#                 tail.next = head2
#                 head2 = head2.next
#                 tail = tail.next
            
#         while head1 != None:
#             tail.next = head1
#             head1 = head1.next 
#             tail = tail.next          
            
#         while head2 != None:
#             tail.next = head2
#             head2 = head2.next 
#             tail = tail.next
            
#         return head.next


        
                
            
                
            