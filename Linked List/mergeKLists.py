# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        def mergeTwoLists(list1, list2):
            dummy = ListNode()
            current = dummy
            while list1 and list2:
                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            if list1:
                current.next = list1
            else:
                current.next = list2
            return dummy.next
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                if i != len(lists) - 1:
                    l2 = lists[i+1]
                    merged.append(mergeTwoLists(l1, l2))
                else:
                    merged.append(lists[i])
            lists = merged
        if lists:
            return lists[0]
