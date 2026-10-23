# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
    
# # Definition of singly linked list:
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        def reverse(head):
            prev = None 
            curr = head 
            while curr:
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next
            return prev 


        rt =[]

        curr = head 
        c = 1

        pres_head = head 

        while curr:
            if c < k:
                curr = curr.next 
                c+=1
            else:
                c = 1
                next_head = curr.next 
                curr.next = None 

                rev_head = reverse(pres_head)
                rt.append([rev_head, pres_head])

                pres_head = next_head
                curr = next_head
        
        if pres_head != None:
            rt.append([pres_head, None])
        

        for i in range(len(rt)-1):
            rt[i][1].next = rt[i+1][0]
        
        return rt[0][0]
                






