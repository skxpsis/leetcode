#       TITLE:  Minimum Size Subarray Sum
# DESCRIPTION:  Given an array of positive integers nums and a positive integer target, 
#               return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r-1], nums[r]] of which the sum is greater than or equal to target.
#               If there is no such subarray, return 0 instead.
#  DIFFICULTY:  Medium
#        TIME:  O(N)
#       SPACE:  O(1)
# 
# Algorithm details:
    # Using sliding window technique where each subarray is a sliding window
    # Initial sliding window has size == 1 where the window both starts and ends at index 0 of the array
    # Iterate over the array, adding elements to the window until the window's sum is >= to the target
    # Shrink the window from the left until the sum becomes smaller than the target
        # At each shrink, if the sum is still >= the target, update the minimum length to the new minimum
        # Shrink again

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        window_sum   = 0                # total of that window
        window_start = 0                # left window boundary
        window_end   = 0                # rightw window boundary
        min_size     = float("inf")     # minimum size of window for target
        nums_size    = len(nums)        # length of input array
        
        for window_end in range(nums_size):                               # iterate through array
            window_sum += nums[window_end]                                # add current element to sum of the window
            while (window_sum >= target):                                 # if the window sum meets or exceeds the target:
                min_size = min(min_size, window_end - window_start + 1)   # get new minimum window size if applicable by comparing it with the previous size
                window_sum -= nums[window_start]                          # remove head of window to see if the window can shrink while retaining target value
                window_start += 1                                         # increment window head
              
        if min_size < float("inf"):                                       # return min_size if less than initial value
            return min_size
        else:
            return 0                                                      # else return 0
