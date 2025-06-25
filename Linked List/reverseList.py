# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    prev = None
    current = head
    while current:
        node_next = current.next
        current.next = prev
        prev = current
        current = node_next
    return prev
