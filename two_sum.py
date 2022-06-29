# TITLE:        Two Sum
# DESCRIPTION:  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#               You may assume that each input would have exactly one solution, and you may not use the same element twice.
#               You can return the answer in any order.
# DIFFICULTY:   Easy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        arr = []
        for i in range(size):
            for j in range(i+1, size):
                two_sum = nums[i] + nums[j]
                if(two_sum == target):
                    return [i, j]
