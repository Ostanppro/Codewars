# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        fictivniy_node = ListNode(0)
        fictivniy_node.next = head#фиктивный элемент указывает на голову
        prev = fictivniy_node
        curr = head  
        while curr:
            #удаляем значение
            if curr.val == val:
                prev.next = curr.next # перенаправляем указатели
            else:
                prev = curr
            curr = curr.next
        return fictivniy_node.next