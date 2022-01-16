# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=l1
        temp2=l2
        ans=ListNode(0)
        temp=ans
        ca=0
        while temp1 or temp2:
            if not temp1:
                s=temp2.val+ca
                ca=s//10
                s=s%10
                
                temp.next=ListNode(s)
                temp=temp.next
                temp2=temp2.next
            elif not temp2:
                s=temp1.val+ca
                ca=s//10
                s=s%10
                
                temp.next=ListNode(s)
                temp=temp.next
                temp1=temp1.next
            else:
                s=temp2.val+temp1.val+ca
                ca=s//10
                s=s%10
                
                temp.next=ListNode(s)
                temp=temp.next
                temp1=temp1.next
                temp2=temp2.next
        if ca!=0:
            temp.next=ListNode(ca)
        return ans.next
            
                
        