# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow=head
        fast=head
        n=0
        prev=slow
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
            n+=1
        if n==0:
            return None
        prev.next=slow.next
        return head