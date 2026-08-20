# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(head):
            length, cur = 0, head
            while cur:
                cur = cur.next
                length += 1
            return length

        len1 = getLength(headA)
        len2 = getLength(headB)
        list1, list2 = headA, headB
        
        if len1 < len2:
            len1, len2 = len2, len1
            list1, list2 = headB, headA

        while len1 - len2:
            len1 -= 1
            list1 = list1.next

        while list1 != list2:
            list1 = list1.next
            list2 = list2.next
        return list1