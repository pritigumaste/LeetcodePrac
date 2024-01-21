#https://leetcode.com/problems/delete-node-in-a-linked-list/

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
        #prev = None 
        temp = None
        temp = node.next
        #print(temp)
        #node = None
        #print
        node.val = temp.val
        node.next = temp.next

        #print(node)
        #node.next = temp.next
        #currNext = node.next


        
