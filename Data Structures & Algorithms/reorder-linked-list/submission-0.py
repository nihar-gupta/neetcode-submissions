# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []
        curr = head 
        prev = None
        while curr:
            nodes.append(curr)
            prev = curr
            curr = curr.next
            prev.next = None
        

        n = len(nodes)
        j = n-1
        for i in range(n//2):
            nodes[i].next = nodes[j]
            j=j-1
        
        for i in range(n//2):
            nodes[i].next.next = nodes[i+1]
            if n%2 == 0 and i == n//2 -1:
                nodes[i].next.next = None
        
        

        