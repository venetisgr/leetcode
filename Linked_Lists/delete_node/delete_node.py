# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #Since we don't have access to the previous element in order to delete the current one
        #We will bring the values of the next node here and delete the next one
        
        cur_node = node
        next_node = cur_node.next
        next_next_node = cur_node.next.next
        
        cur_node.val = next_node.val #make current node identical to the next one
        cur_node.next = next_next_node 
        
        next_node.next = None #deleted node shouldnt point anywhere
        
