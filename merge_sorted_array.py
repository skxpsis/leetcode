#       TITLE:  Merge Sorted Array
# DESCRIPTION:  You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
#               and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#               Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#               The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
#               To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
#               and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
#  DIFFICULTY:  Easy
#        TIME:  O(M+N), where M and N are the lengths of the sorted arrays
#       SPACE:  O(1), no extra memory necessary
# 
# Algorithm details:
#   Using two pointer technique
#   One pointer for the first array, the other for the second array, both start at index = m-1, n-1 respectively
#   Compare the two pointer values each m and n
#     If m value is >= n value, assign m to the last unfilled entry in nums1 (last entry with a 0)
#     Else assign n value to the last unfilled entry
#   Repeat until m, n = 0
#   Note in the code that the "m value" mentioned aboved is reference as "m-1"
#   This is simply because indexing starts at 0 instead of 1, so we have to adjust based on that :)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:                # if nums1 entry is >= nums2 entry at same index
                nums1[m+n-1] = nums1[m-1]               # move the nums1 entry to the last empty index in nums1
                m -= 1                                  # decrement m (size of nums1)
            else:                                       # else nums1 entry is < nums2 entry as same index
                nums1[m+n-1] = nums2[n-1]               # moves the nums2 entry to the last empty index in nums1
                n -= 1                                  # decrement n (size of nums2)
                
        if n > 0:                                       # if nums2 exists, but nums1 may be null
            nums1[:n] = nums2[:n]                       # assign all of nums2 to nums1
        
