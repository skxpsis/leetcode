# SORT ARRAY BY PARITY - EASY
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
