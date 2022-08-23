#       TITLE: Minimum Number of K Consecutive Bit Flips
#  DIFFICULTY: Hard
# DESCRIPTION: You are given a binary array nums and an integer k.
#              A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#              Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
#              A subarray is a contiguous part of an array.

class Solution(object):
    def minKBitFlips(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)                # input size
        result = 0                      # stores amount of flips done
        dq = collections.deque()        # deque to keep track of flips
        
        for i, num in enumerate(nums):
            if (num == 0 and len(dq) % 2 == 0) or (num == 1 and len(dq) % 2 == 1):            # if current num is 0/1 & number of flips is even/odd
                result += 1                                                                   # increment result
                if i+k > size:                                                                # if last index of the flip is greater than the size of the input
                    return -1                                                                   # return -1 as there's no more room to flip to achieve result
                dq.append(i+k-1)                                                              # append new end to deque
            if len(dq) > 0 and dq[0] == i:                                                    # once last index of flip is reached
                dq.popleft()                                                                    # remove head of the deque
        return result
