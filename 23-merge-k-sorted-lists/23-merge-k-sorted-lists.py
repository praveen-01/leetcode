# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            temp1=list1
            temp2=list2
            cur=ListNode(0,None)
            ans=cur
            while temp1 or temp2:
                if not temp1:
                    cur.next=temp2
                    break
                if not temp2:
                    cur.next=temp1
                    break
                if temp1.val<temp2.val:
                    cur.next=temp1
                    cur=cur.next
                    temp1=temp1.next
                else:
                    cur.next=temp2
                    cur=cur.next
                    temp2=temp2.next
            return ans.next
        res=ListNode(0,None)
        temp=res
        temp=temp.next
        i=0
        while i<len(lists):
            temp=merge(temp,lists[i])
            i+=1
        return temp
                
        