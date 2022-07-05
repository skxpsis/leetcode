#       TITLE: First Negative Number in Every Window of Size K
# DESCRIPTION: Given an array of integers a, and a positive integer k, find the first negative integer for each and every window of size k. 
#              If a window does not contain a negative integer, then print 0 for that window.
#  DIFFICULTY: Medium
#        TIME: O(N)
# 
# Algorithm details:
#   Using the sliding window technique where each subarray of size k is a sliding window
#   Initial window size is 1 where the start/end of the window are both at index 0
#   Use a FIFO queue that stores the negative numbers in the current window
#   Iterate over the array with the window end incrementing by one
#   If negative number encountered, add it to the queue
#   If window size == k, then get its first negative number from the queue
#       If the queue is empty, then no negative number was in the window so return 0
#       Slide the window -- remove window head, incremenet window start by 1
#   Repeat as necessary

def firstNegativeNum(size, nums):
    """
    :type size: int
    :type nums: List[int]
    :rtype: int
    """
    window_start = 0                                    # start of the window at index 0
    window_end   = 0                                    # end of the window at index 0
    queue        = []                                   # first in first out queue (FIFO)
    nums_size    = len(nums)                            # length of input array for iteration

    for window_end in range(nums_size):             # iterate through array
        if nums[window_end] < 0:                            # if the element is negative,
            queue.append(nums[window_end])                      # add to the queue
        window_size = window_end - window_start + 1         # increment window size
        if window_size == size:                             # if we've reached the target window size, retrieve result & slide window
            if len(queue) == 0:                             # if the queue is empty
                print("0", end=" ")                             # print 0
            else:
                queue_head = queue[0]                           # first element of the queue
                print(queue_head, end=" ")                      # else print first element of the queue per FIFO
            if queue_head == nums[window_start]:            # if the head of teh queue is equal to the start of the window 
                queue.remove(queue_head)                        # remove it as we are sliding the window out of its range
            window_start += 1                               # slide (increment) the window by 1

if __name__ == "__main__":
    size = 3
    nums = [10, -1, -5, 7, -15, 20, 18, 24]
    firstNegativeNum(size, nums)
