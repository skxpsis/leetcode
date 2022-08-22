#       TITLE: Longest Repeating Character Replacement
# DESCRIPTION: You are given a string s and an integer k. 
#              You can choose any character of the string and change it to any other uppercase English character. 
#              You can perform this operation at most k times.
#              Return the length of the longest substring containing the same letter you can get after performing the above operations.
#  DIFFICULTY: Medium
#        TIME: O(N), where N is the magnitude of the input string
# 
# Algorithm details:
#   Using the sliding window technique where each substring of the input, s, is a sliding window
#   At each iteration, start by adding the current current (if not already present) to the counts dict
#   Update the count of the character by 1
#   Find the current substring size by finding the difference between the end of the window and the start of the window
#   Given the current window (substring), find the character with the highest frequency
#   Substract the highest frequency from the current window to see how many replacements must be made in the substring
#   If the number of replacements to be made <= k, compare that replacement cost with the previous and pick the maximum
#     Note that the next iteration will expand this current window (not slide) to see if there's a new maximum to be made out of it
#   If it is > k, slide the window over by 1 to look at new substring
#     Decrease the current start characters count in the counts dictionary to remove it from the window
#     Increment the the start value to form new window

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        start, end = 0, 0           # window start and end; this will correlate to substring being looked at
        counts = {}                 # dict to hold counts of characters in s
        result = 0                  # return value
        
        for end in range(len(s)):                       # loop through input
            counts[s[end]] = counts.get(s[end], 0) + 1  # get() inserts char into counts dict if not already there
                                                        # with inital value of 0
                                                        # then increases value by 1
            window = (end-start)+1                      # get window (substring) length/size
            if (window - max(counts.values())) <= k:    # substract max of counts to get number of replacements to be made
                result = max(result, window)            # if replacement cost <= k, record new max value
            else:                                       # if replacement cost > k, slide window (new substring)
                counts[s[start]] -= 1                   # decrement char count of the start
                start += 1                              # increase window end
        return result
