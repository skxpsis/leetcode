# TWO SUM - EASY - O(N)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # empty dictionary to store all (key, value) pairs from enumberate(nums)
        values = {}
        for i, num in enumerate(nums):
            # if difference is in values, halt accept
            if target-num in values:
                return [values[target-num], i]
            else:
                # if a key/value is not in values, add it and look again
                values[num] = i
