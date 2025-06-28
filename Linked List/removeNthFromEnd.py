# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        counter = 0
        prev = None
        current = head
        while current:
            counter += 1
            if counter == (length - n + 1):
                if prev:
                    prev.next = current.next
                else:
                    head = head.next
            else:
                prev = current
                current = current.next
        return head
