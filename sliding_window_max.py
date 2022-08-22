#       TITLE: Sliding Window Maximum
# DESCRIPTION: You are given an array of integers nums, there is a sliding window of size k 
#              which is moving from the very left of the array to the very right. 
#              You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#              Return an array with the maximum from each sliding window.
#  DIFFICULTY: Hard
#        TIME: O(N)
#
# Algorithm details:
#   Use a deque (which can perform pop/append operations at both ends quickly) to store the indices of the max numbers from each sliding window
#   Where the head (front) of the deque is the maximum of the current window
#   Iterate over the input array
#   - While the deque has values in it AND while the last element in the deque is less than the current number in the array,
#     Remove the last element in the deque
#     This ensures that maximum numbers are only stored in the deque
#   - Then append the current element's index to the deque
#   - If the start of the deque contains a maximum element from outside of the current window, remove it
#   - If the current window meets the required window size,
#       Append the head of the deque to the results array as it should be the maximum from the window
#       Note: This executes always after the very first window is created
#       It ensures that the premature values are added the the results array before the window is the required size
#   Repeat as necessary

from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        result = []
        
        for i, num in enumerate(nums):
            while deque and nums[deque[-1]] < num:          # while the last element in deque is < current element in nums
                deque.pop()                                 # pop the last element in the deque; repeat as necessary
            deque.append(i)                                 # append index of current element
            if deque[0] == i-k:                             # if the head of the deque is outside of the window leftmost boundary
                deque.popleft()                                 # pop the head
            if i >= k-1:                                    # allows for first 0-k window to fully populate before getting result
                result.append(nums[deque[0]])               # append the head (always the max) of the deque to the result array
        return result
