#       TITLE: Sort Array by Parity
# DESCRIPTION: Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#              Return any array that satisfies this condition.
# DIFFICULTY:  Easy
#       TIME: O(N)
# 
# Algorithm details:
    # First solution (niave): iterate through the list, create new lists based on even and odd numbers. Concatentate lists to each other at the end.  
    # Second Solution: Improved in-place solution using two pointers
    # They both share the same time complexity but the first solution consumes more memory

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_size = len(nums)
        even_nums = []
        odd_nums = []
        new_list = []
        
        for i in nums:
            if i % 2 == 0:
                even_nums.append(i)
            else:
                odd_nums.append(i)

        new_list = even_nums + odd_nums
        return new_list
    
class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_size = len(nums)                       # length of the array
        moving_pointer = 0                          # start of array
        leftmost_pointer = 0                        # nonchanging point in array
                                                    # when new element moved to front
        
        for moving_pointer in range(nums_size):     # iterate through the array
            if nums[moving_pointer] % 2 == 0:       # if element is even, move to front of array unchanged elements
                nums[leftmost_pointer], nums[moving_pointer] = nums[moving_pointer], nums[leftmost_pointer]
                leftmost_pointer += 1               # increment to next index as new leftmost point
        return nums
