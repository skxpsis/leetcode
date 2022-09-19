#       TITLE: Merge Two Sorted Lists
#  DIFFICULTY: Easy
# DESCRIPTION: You are given the heads of two sorted linked lists list1 and list2.
#              Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#              Return the head of the merged linked list.
  
"""
        Taken from LC discussions to help clarify process:
        
        cur visits each node in original input lists and updates their next to point to the node with next larger value after cur's value. 
        It jumps between list 1 and list 2 based on which node is smaller in value and updates it's next to next larger value node.

        The first iteration serves two purposes. 
        It updates dummy's next to point to the smallest number which can either be in list 1 or list 2 
        and it moves cur to that node so that it can update that node next.

        We break out of loop when one of the lists reaches end of nodes (i.e. list 1 or list 2 becomes None).
        
        Other notes on purpose of dummy:
        When the line "dummy = cur = ListNode()" is executed, 
        first, ListNode() creates a unique object (whose val = 0, next = None) of class ListNode. 
        Then dummy and cur both are assigned to (a.k.a point to) this ListNode object 
        (which happens to be the very first LinkNode in the "chain" or "Singly-linked list"), 
        which means both cur and dummy can access the "val" and "next" attributes of such object 
        (which I will keep referring to as the "first node").
        
        Then what happens during the first iteration the while loop is:
        we only modify the "next" attribute of the "first node" 
        (keep in mind dummy never stops pointing to the "first node") 
        by updating cur.next = list1. At this point dummy is still pointing to the "first node", 
        but now dummy.next is no longer None... now dummy.next is list1, 
        which means dummy.next.val == list1.val and dummy.next.next == list1.next. 
        What this means is that dummy points to the first ListNode in the singly-linked list that we 
        are building and that we need to return.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = result = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1                    # assign next value of cur == list1 val
                list1, cur = list1.next, list1      # look at next element in list1 since we assigned current element
            else:
                cur.next = list2                    # make next val == list2 val
                list2, cur = list2.next, list2      # look at next element in list2 since we assigned current element
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return result.next
