# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        left=head
        right=head
        while right.next and right.next.next:
            left=left.next
            right=right.next.next
            if left==right:
                return True
        return False


        