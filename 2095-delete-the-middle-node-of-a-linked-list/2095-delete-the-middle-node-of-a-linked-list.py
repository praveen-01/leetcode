# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return None
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            if fast==None or fast.next==None:
                continue
            slow=slow.next
        slow.next=slow.next.next
        return head
        