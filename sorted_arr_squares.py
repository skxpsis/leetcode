#       TITLE: Squares of a Sorted Array
# DESCRIPTION: Given an integer array nums sorted in non-decreasing order, 
#              return an array of the squares of each number sorted in non-decreasing order.
#              Example:
#               Input: nums = [-4,-1,0,3,10]
#               Output: [0,1,9,16,100]
#               Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].
#  DIFFICULTY: Easy
#        TIME: O(N)
# 
# Algorithm details:
        # Using two pointers technique
        # input: array of numbers arrange in ascending order
        # output: array with square of each number in input array
        #         in ascending order
        # here the issue is that just because a number is smallest in the input array
        # doesn't mean it will be the smallest in the output array as a result of squaring
        # so we assign two pointers - one at start of input array, one at the end of input array
        # then we compare squared values of the pointers
        #   the larger value gets appended to start of a result array (deque) in O(1) time using collections.deque
        #   > it's pointer incremented if it's the left pointer
        #   > or decremented if it's the right pointer
        # repeat the process until pointers meet

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        size = len(nums)                                # length of array
        pointer_left = 0                                # start pointer at index 0
        pointer_right = size-1                          # end pointer at index 0
        result = collections.deque()                    # where the resultant array will go
        
        while pointer_left <= pointer_right:            # check that pointers haven't met in middle
            left_num = abs(nums[pointer_left])          # get abs values of left num
            right_num = abs(nums[pointer_right])        # get abs values of right num
            if left_num >= right_num:                   # compare left_num with right_num
                result.appendleft(left_num*left_num)        # append left_num to deque
                pointer_left += 1                           # increment the left pointer
            else:                                       # else if left_num < right_num
                result.appendleft(right_num*right_num)      # append right_num to deque 
                pointer_right -= 1                          # decrement the right pointer
                
        return result
    
