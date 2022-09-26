class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # first sort the list
        # then use 3 pointers - start, mid, end
        # start = i (for loop), mid = i+1, end = len(nums)-1
        # for each loop iteration:
            # check for duplicate numbers, can skip dupes
            # while mid < end,
            # temp_sum = nums[i] + nums[mid] + nums[end] 
            # return temp_sum if == target
            # if the absolute distance between the temp_sum and target is less than the current result's distance, 
            # update result to new smaller distance
            # if temp_sum is too far away from target, decrease the end pointer (list is sorted, so higher values are toward the end)
            # it the temp_sum is too low, increase the middle pointer
        
        nums.sort()                                               # sort the list
        result = sum(nums[:3])                                    # intialize result to first 3 values in list
        
        if len(nums) == 3:
            return sum(nums)                                      # return list sum if list is size 3
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:                    # duplicate check
                continue                                            # skips if duplicate encountered
            mid = i+1
            end = len(nums)-1
            while mid < end:
                temp_sum = nums[i] + nums[mid] + nums[end]        # initial sum
                if temp_sum == target:                            # if target met
                    return target                                   # return it
                if abs(temp_sum-target) < abs(result-target):     # if current distance is smaller than previously recorded distance
                    result = temp_sum                               # update result to new value
                if temp_sum > target:                             # if sum too large
                    end -= 1                                        # decrement end pointer to shrink sum (since list is sorted)
                if temp_sum < target:                             # if sum too low
                    mid += 1                                        # increment middle pointer to increase sum (since list is sorted)
        return result
                
