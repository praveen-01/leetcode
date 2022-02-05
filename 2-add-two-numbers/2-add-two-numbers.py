# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        c=0
        cur=ListNode(0,None)
        temp=cur
        while l1 or l2:
            if not l1:
                k=l2.val+c
                l2=l2.next
            elif not l2:
                k=l1.val+c
                l1=l1.next
            else:
                k=l2.val+l1.val+c
                l1=l1.next
                l2=l2.next
            c=k//10
            k=k%10
            temp.next=ListNode(k)
            temp=temp.next
        if c==1:
            temp.next=ListNode(1)
        return cur.next
        