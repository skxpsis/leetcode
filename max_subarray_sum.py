# TITLE:       Maximum Absolute Sum of Any Subarray
# DESCRIPTION: You are given an integer array nums. The absolute sum of a subarray is abs(nums[l] + nums[l+1] + ... + nums[r-1] + nums[r]).
#              Return the maximum absolute sum of any (possibly empty) subarray of nums.
# DIFFICULTY:  Medium
# TIME:        O(N)
# SPACE:       O(1)

class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's Algorithm
            # Calculates maximum sum of a subarray of an array
            # Using maximum positive sum (max) and maximum negative sum (min) ending at the previous position
            # At each iteration of the loop:
                # If the current_sum is larger than the max_sum,
                    # the max_sum assumes the value of the current_sum
                # If the current_sum is smaller than the min_sum,
                    # the min_sum assumes the value of the current_sum
                # As current_sum compares with max/min sum:
            # The final absolute sum to return is the absolute max of the max/min difference
            
        current_sum = 0             # maximum sum ending here
        max_sum     = 0             # maxiumum sum so far
        min_sum     = 0             # minumum sum so far
        abs_max     = 0             # absolute max to return
        
        for num in nums:                         # iterate through nums[] list
            current_sum += num                   # append to sum ending here
            if current_sum > max_sum:            # if current sum > than max sum so far
                max_sum = current_sum               # current num becomes the new max sum
            if current_sum < min_sum:            # if current sum < min sum so far
                min_sum = current_sum               # current num becomes the new min sum 
            
            abs_max = max_sum - min_sum          # return difference of max & min
        return abs_max
   
