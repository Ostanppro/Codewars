# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        if not cur:
            return head

        odd_list = head
        even_list = head.next
        save = even_list
        while odd_list.next and even_list.next:
            odd_list.next = even_list.next
            odd_list = odd_list.next
            if odd_list:
                even_list.next = odd_list.next
                even_list = even_list.next
        odd_list.next = save
        return head