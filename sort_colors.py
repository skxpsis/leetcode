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
    # 1) Counting sort (first solution) -- okay
    # 2) Using pointers for red, white, and blue (second solution) -- better

# Okay solution
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # leetcode suggested solution using counting sort
        # Iterate the array counting number of 0's, 1's, and 2's
        # Overwrite array with the total number of 0's, then 1's and followed by 2's.
        
        dict_nums = Counter(nums)               # dictionary with element from array as the key and the count of that element as the value
        i = 0                                   # initialize i as starting point to fill elements in nums[]
        for key, value in dict_nums.items():    # iterate through dict_nums{}
            while value > 0:                    # if key has a value > 0 (that is, 1 or more occurrences in nums[])
                nums[i] = key                       # overwrite current index = i as the key from the dict_nums{}
                i += 1                              # for each count that key has in dict_nums{}, so i is incremented
                value -= 1                          # decrement the value in dict_nums{} for the specified key until it is 0
                                                # then the next key will be looked at and repeat
    
# Better solution
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        size_nums = len(nums)               # size of input array
        pointer_red = 0                     # intial value for red pointer
        pointer_white = 0                   # intial value for white pointer
        pointer_blue = size_nums - 1        # initial value for blue pointer -- blue should be at end of array so it's initialized as such
        
        while pointer_white <= pointer_blue:                                                            # compare white and blue pointers
            if nums[pointer_white] == 0:                                                                # if white == red value
                nums[pointer_red], nums[pointer_white] = nums[pointer_white], nums[pointer_red]         #   swap white pointer with red pointer, moving reds to front
                pointer_white += 1                                                                      #   increment white pointer
                pointer_red += 1                                                                        #   increment red pointer
            elif nums[pointer_white] == 1:                                                              # if white pointer == white value
                pointer_white += 1                                                                      #   do nothing but increment the pointer :)
            else:                                                                                       # else white == blue pointer
                nums[pointer_white], nums[pointer_blue] = nums[pointer_blue], nums[pointer_white]       #   swap white pointer with blue pointer, moving blues to end
                pointer_blue -= 1                                                                       #   decrement blue pointer as we don't want to disurb 
                                                                                                        #   the end position just filled
                
