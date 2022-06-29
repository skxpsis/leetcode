# TITLE:       Longest Substring Without Repeating Characters
# DESCRIPTION: Given a string s, find the length of the longest substring without repeating characters.
# DIFFICULTY:  MEDIUM

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Algorithm details:
            # Slide Window Algorithm
            # left-window = beginning of window
            # right-window = end of window
            # both left & right window start at index 0
            # slide/increment the right window until duplicate character encountered
            # reassign longest length variable at each right-window increment where no duplicate encountered
            # if duplicate encountered, then increment left-window by 1
                # decrease longest length count by 1
                # repeat until as needed (no duplicates in window)
            # if left-window & right-window are at same index
                # move right-window first
        
        left_window  = 0      # start of window
        right_window = 0      # end of window
        longest      = 0      # length of longest substring without repeating characters
        counts       = {}     # dict with key:value = s-character : # of times seen
        input_size   = len(s)
        
        for right_window in range(input_size):
            current_char = s[right_window]                  # right-window
            if current_char not in counts.keys():           # check if new character exists in counts dict
                counts[current_char] = 0                    # add to dict with count = 0
            counts[current_char] += 1                       # increment count of current_char by 1 outside of loop to catch duplicates
            
            # when & how to slide the window
                # a char that is not a duplicate causes the right-window to increment
                # a char that is a duplicate shrinks the window (left increments)
                # so check if a value in counts has a count > 1 using list comprehension
             
            invalid = [key for key, value in counts.items() if value > 1]     # looking for key, value pairs where value > 1 for that key
            if invalid:                                                       # if a value > 1 exists,
                counts[s[left_window]] -= 1                                   # decrement the count of that character, as it is no longer in the window
                left_window += 1                                              # slide/increment the left_window by 1
            
            longest = max(longest, right_window - left_window + 1)            # update the longest variable to the largest of the two: current longest or new window
            right_window += 1                                                 # slide/increment right_window to look at new character in string
                
        return longest
