# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=ListNode(0)
        curr=res

        
        while True:
            min=-1


            for i in range(len(lists)):
                if not lists[i]:
                    continue 
                if min==-1 or lists[min].val>lists[i].val:
                    min=i
            if min ==-1:
                break
            curr.next=lists[min]
            lists[min]=lists[min].next
            curr=curr.next
        return res.next


