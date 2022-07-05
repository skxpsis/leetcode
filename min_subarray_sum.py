# TITLE:        Minimum Size Subarray Sum
# DESCRIPTION:  Given an array of positive integers nums and a positive integer target, 
#               return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r-1], nums[r]] of which the sum is greater than or equal to target.
#               If there is no such subarray, return 0 instead.
# DIFFICULT:    Medium
# TIME:         O(N)
# SPACE:        O(1)

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Using sliding window technique
        # If new window size == target is < old window size, reassign
        # if target not found, return 0
        
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
