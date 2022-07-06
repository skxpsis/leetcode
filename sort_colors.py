# In progress - posted in Leetcode suggested solution based on problem "Hints"

#       TITLE: Sort Colors
# DESCRIPTION: Given an array nums with n objects colored red, white, or blue, 
#              sort them in-place so that objects of the same color are adjacent, 
#              with the colors in the order red, white, and blue.
#              We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#              You must solve this problem without using the library's sort function.
#  DIFFICULTY: Medium
#        TIME: O(N)
# 
# Algorithm details:
    # 

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # leetcode suggested solution using counting sort
        # Iterate the array counting number of 0's, 1's, and 2's
        # Overwrite array with the total number of 0's, then 1's and followed by 2's.
        
        dict_nums = Counter(nums)
        i = 0
        for key, value in dict_nums.items():
            while value > 0:
                nums[i] = key
                i += 1
                value -= 1
        
