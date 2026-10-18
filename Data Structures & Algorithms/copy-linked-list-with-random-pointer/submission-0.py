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

        if head==None : return head

        newHead = Node(head.val)
        d = dict()
        d[None]=None
        d[head]=newHead

        prev=newHead
        temp=head.next

        s=[]

        while temp:
            newNode = Node(temp.val)
            d[temp]=newNode
            prev.next = newNode
            prev=newNode
            temp=temp.next
        
        temp=head
        while temp:
            newNode = d[temp]
            newNode.random = d[temp.random]
            temp=temp.next
        
        return newHead