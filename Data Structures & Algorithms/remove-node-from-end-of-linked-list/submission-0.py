# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(head):
            c=0 
            while head:
                c+=1
                head = head.next 
            return c 
        
        l = length(head)

        if l == n: 
            return head.next

        k = 1
        curr = head 
        while k < (l-n):
            curr = curr.next 
            k+=1
        
        nn = curr.next.next 
        curr.next = nn 
        return head

        