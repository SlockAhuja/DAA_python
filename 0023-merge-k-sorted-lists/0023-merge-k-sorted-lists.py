# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def merge(self, a, b):

        if a is None:
            return b

        if b is None:
            return a

        if a.val <= b.val:
            a.next = self.merge(a.next, b)
            return a
        else:
            b.next = self.merge(a, b.next)
            return b

    def mergeLists(self, lists, left, right):

        if left == right:
            return lists[left]

        mid = left + (right - left) // 2

        l1 = self.mergeLists(lists, left, mid)
        l2 = self.mergeLists(lists, mid + 1, right)

        return self.merge(l1, l2)

    def mergeKLists(self, lists):

        if not lists:
            return None

        return self.mergeLists(lists, 0, len(lists) - 1)