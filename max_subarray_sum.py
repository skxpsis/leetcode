#       TITLE: Maximum Sum Subarray of Size K
# DESCRIPTION: Given an array of positive integers, and a positive number k, find the maximum sum of any contiguous subarray of size k.
#  DIFFICULTY: Medium
#        TIME: O(N)  
#       SPACE: O(1)
# 
# Algorithm details:
    # Using sliding window technique where each subarray is a sliding window
    # Initial sliding window has size == 1 where the window both starts and ends at index 0 of the array
    # Iterate over the array, increment the end of the window each time
    # If the window size is equal to the target size, then we have a sum of a k-sized subarray in the window
        # Update the maximum sum and slide the window to calculate the next sum
            # Check is the current window sum > maximum sum; if so, update maximum to the current sum
            # Slide the window by removing the head of the window; increment the new head by 1  

# class Solution(object):
def maxAbsoluteSum(size, nums):
    """
    :type size: int
    :type nums: List[int]
    :rtype: int
    """
    window_sum   = 0                # total sum of the current window
    window_start = 0                # left window boundary
    window_end   = 0                # right window boundary
    max_sum      = float("-inf")    # max sum among all subarrays (windows); inital max value set to -infinity
    nums_size    = len(nums)        # length of input array
    
    for window_end in range(nums_size):                               # iterate through array
        window_sum += nums[window_end]                                # add current element to sum of the window
        if(window_end - window_start + 1) == size:                    # if the window equals the size:
            max_sum = max(max_sum, window_sum)                          # get new max window size if applicable by comparing max_size with window_sum
            window_sum -= nums[window_start]                            # remove head of window
            window_start += 1                                           # increment window head
            
    return max_sum

if __name__ == "__main__":
    size = 3
    nums = [4, 2, 3, 5, 1, 2]
    result = maxAbsoluteSum(size, nums)
    print(result)
