# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2:
            return None
        head = ListNode()
        current = head
        while list1 or list2:
            if not list2:
                current.val = list1.val
                list1 = list1.next
            elif not list1:
                current.val = list2.val
                list2 = list2.next
            elif list1.val <= list2.val:
                current.val = list1.val
                list1 = list1.next
            else:
                current.val = list2.val
                list2 = list2.next
            if list1 or list2:
                current.next = ListNode()
                current = current.next
        current = None
        return head