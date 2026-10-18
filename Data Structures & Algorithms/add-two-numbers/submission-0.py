# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def lenght(head):
            c=0
            while head:
                c+=1
                head=head.next 
            return c
        
        h1 = l1 
        h2 = l2
        l1 = lenght(h1)
        l2 = lenght(h2)
        
        if l2 > l1:
            l2, l1 = l1, l2
            h1, h2 = h2, h1
        

        t1 = h1 
        t2 = h2 
        carry = 0
        while t1 and t2:
            t1.val = t1.val + t2.val + carry 
            if t1.val >= 10:
                t1.val = t1.val%10
                carry = 1
            else:
                carry = 0
            t1 = t1.next 
            t2 = t2.next 
        
        if carry == 1:
            while t1 and carry == 1:
                t1.val = t1.val + carry 
                if t1.val >= 10:
                    t1.val = t1.val%10 
                    carry = 1
                else:
                    carry = 0
                t1=t1.next 
            
            if carry == 1:
                t1 = h1 
                while t1.next:
                    t1=t1.next
                t1.next = ListNode(1)
            

        
        return h1
