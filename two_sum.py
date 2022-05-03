# TWO SUM - EASY - O(N^2)
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
