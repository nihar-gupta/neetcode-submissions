# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reverse(head):
            if not head or not head.next:
                return head 
            
            headnext = head.next
            newhead = reverse(head.next)

            headnext.next = head 
            head.next = None 
            return newhead


        curr = head
        prev = None 
        i = 1
        
        while curr:
            if i == left:
                if prev:
                    left_head = head
                else: left_head = None
                reverse_head = curr
                if prev:
                    prev.next = None
            
            if i == right:
                right_head = curr.next 
                curr.next = None
            
            prev = curr
            curr = curr.next
            i+=1
        
        reverse_head = reverse(reverse_head)

        if left_head:
            return_head = left_head

            curr= left_head
            while curr.next:
                curr=curr.next
            
            curr.next = reverse_head

            while curr.next:
                curr = curr.next
            
            curr.next = right_head

            return return_head


        else:
            return_head = reverse_head

            curr=reverse_head
            while curr.next:
                curr= curr.next 

            curr.next = right_head

            return return_head 
        

        




        
        return reverse(head)
        