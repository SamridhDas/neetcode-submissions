# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        gprev=dummy
        while True:
            kth=self.getk(gprev,k)
            if not kth:
                break
            curr=gprev.next
            gnext=kth.next
            prev=kth.next
            while curr!=gnext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            itr=gprev.next
            gprev.next=kth
            gprev=itr
        return dummy.next




    def getk(self,curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr