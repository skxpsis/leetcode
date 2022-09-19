#       TITLE: 3Sum
#  DIFFICULTY: Medium
# DESCRIPTION: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
#              such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]: # makes sure that we do not have any duplicates in result
                continue 
            mid = left + 1 # pointer between left and right pointers
            right = len(nums) - 1 # right pointer
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right] # sum up 3 pointer values
                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]: # Another conditional for not calculating duplicates
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                        right -= 1
                    mid += 1
                    right -= 1
        return result
