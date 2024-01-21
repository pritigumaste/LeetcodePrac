#TimeL O(n) 
#space O(n) 
#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #base 
        if head is None:
            return 0 
        slow = head
        fast = head.next 

        while fast.next != None and fast != None:
            slow = slow.next
            fast = fast.next.next
        #print(slow)
        #print(fast)
        #slow.next = None

        st =[]
        while slow.next:
            slow = slow.next
            st.append(slow)
        #print(st)
        currSum =0
        while st:
            node = st.pop()
            #print(node)
            currSum = max(head.val + node.val , currSum)
            head= head.next

        return currSum

        #return 0
      
    
        
    
