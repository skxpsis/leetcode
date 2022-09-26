#       TITLE: Duplicate Number
#  DIFFICULTY: Medium
# DESCRIPTION: Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
#              There is only one repeated number in nums, return this repeated number.
#              You must solve the problem without modifying the array nums and uses only constant extra space.
#
# Algorithm details:
#   - Uses fast (hare) and slow (tortoise) pointers

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the intersection point of the two runners
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
