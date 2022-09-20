#       TITLE: Intersection of Two Linked Lists
# DESCRIPTION: Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
#              If the two linked lists have no intersection at all, return null.
#  DIFFICULTY: Easy

# Algorithm details:
  # Using two pointers
  # Initialize two pointers p1 and p1  at headA and headB
  # Traverse through the lists, one node at a time
  # When p1 reaches the end of list, then redirect it to headB
  # or when p2 reaches the end of list, redirect it to the headA
  # Once both of them go through reassigning, they will be equidistant from the intersection point
  # If at any time p1 meets p2 at a node, then it is the intersection node
  # After the second iteration if there is no intersection node it will return null

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        
        if p1 == None or p2 == None:
            return None
        
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
            if p1 == p2:    # if p1==p2, that is the intersection node
                return p1
            
            if p1 == None:  # if end of first list is reached, redirect pointer to second list
                p1 = headB  # this will allow the two pointers to now be equidistant from the intersection
            
            if p2 == None:  # if end of second list is reached, redirect pointer to first list
                p2 = headA  # to allow p1 and p2 to be equidistant from intersection
                
        return p1           # returns p1 if initial p1 & p2 vals are equal
            
