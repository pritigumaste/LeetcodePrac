#https://leetcode.com/problems/copy-list-with-random-pointer/

#did using 2 passes 
#	1. made copy of the list completely just the nodes, using hashmap
#	2. added the pointers random and next pointer keeping the track of the nodes using hashmap

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #copyList ={} we could have a null pointer pointing to null pointer as well 
        #hence do as below 
        copyList ={None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copyList[curr] = copy
            curr = curr.next
        
        #print(copyList)

        curr=  head
        while curr:
            copy = copyList[curr]
            copy.next = copyList[curr.next]
            copy.random = copyList[curr.random]
            curr = curr.next

        return copyList[head]
