# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        prev = None
        while slow:
            slow_next = slow.next
            slow.next = prev
            prev = slow
            slow = slow_next
        while head or prev:
            if (not head.next) and (prev):
                head.next = prev
                break
            head_next = head.next
            prev_next = prev.next
            head.next = prev
            prev.next = head_next
            head = head_next
            prev = prev_next
        return None
