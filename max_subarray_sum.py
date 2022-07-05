#       TITLE: Maximum Sum Subarray of Size K
# DESCRIPTION: Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.
#  DIFFICULTY: Medium
#        TIME: O(N)  
#       SPACE: O(1)

class Solution(object):
    def maxAbsoluteSum(self, target, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window_sum   = 0                # total of that window
        window_start = 0                # left window boundary
        window_end   = 0                # right window boundary
        max_sum      = float("-inf")    # inital max value set to -infinity
        nums_size    = len(nums)        # length of input array
        
        for window_end in range(nums_size):                               # iterate through array
            window_sum += nums[window_end]                                # add current element to sum of the window
            if(window_end - window_start + 1) == target:                  # if the window equals the target:
                max_sum = max(max_sum, window_sum)                          # get new max window size if applicable by comparing max_size with window_sum
                window_sum -= nums[window_start]                            # remove head of window to see if the window can shrink while retaining target value
                window_start += 1                                           # increment window head
              
        return max_sum
