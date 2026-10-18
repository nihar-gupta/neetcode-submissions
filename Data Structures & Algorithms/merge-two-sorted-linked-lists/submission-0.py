# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if list1 == None and list2 == None: return None 
        if list1 == None: return list2 
        if list2 == None: return list1 
    

        dummy_head = ListNode(7)

        curr = dummy_head
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val < p2.val:
                next = p1.next 
                p1.next = None 
                curr.next = p1 
                curr = p1 
                p1 = next 
            else:
                next = p2.next 
                p2.next = None 
                curr.next = p2 
                curr=p2 
                p2 = next 
            
        if p1: 
            curr.next = p1 
        elif p2: 
            curr.next = p2 
        
        return dummy_head.next
        