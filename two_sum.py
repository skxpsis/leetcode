# TITLE:        Two Sum
# DESCRIPTION:  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#               You may assume that each input would have exactly one solution, and you may not use the same element twice.
#               You can return the answer in any order.
# DIFFICULTY:   Easy

# Niave solution
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

# Improved solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}                             # empty dictionary to store all (key, value) pairs from enumberate(nums)
        for i, num in enumerate(nums):          # if difference is in values, halt accept
            if target-num in values:
                return [values[target-num], i]
            else:
                values[num] = i                 # if a key/value is not in values, add it and look again
