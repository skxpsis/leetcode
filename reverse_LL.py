#       TITLE: Reverse Linked List
# DESCRIPTION: Given the head of a singly linked list, reverse the list, and return the reversed list.
#  DIFFICULTY: Easy

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        https://www.youtube.com/watch?v=XDO6I8jxHtA
        """
        # iterative solution
        prev = None             # initialize prev node to None
        while head:             # iterate through all of LL
            temp = head             # temp value to hold the value of head while we change it
            head = head.next        # head is now next listnode; this does NOT change the value of temp
            temp.next = prev        # assign temp pointer to previous listnode of temp
            prev = temp             # move the previous value up one node to iterate through the list
        return prev
     
        # recursive solution below
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node
