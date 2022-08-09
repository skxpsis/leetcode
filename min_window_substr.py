#       TITLE: Minimum Window Susbtring
# DESCRIPTION: Given two strings s and t of lengths m and n respectively, 
#              return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
#              If there is no such substring, return the empty string "".
#              The testcases will be generated such that the answer is unique.
#              A substring is a contiguous sequence of characters within the string.
#  DIFFICULTY: Hard
#  
# Algorithm details:
#   Using sliding window technique
#   Left window (window_start) and right window (window_end) both start at 0
#   The right window is expanded until the window contains all the characters of 't'
#       Then t is incremented one at a time, checking for desirability at each increment (that the window contains all characters of 't')
#       If the window is still desirable, the minimum window size is adjusted accordingly
#       If the window is not desirable, the right pointer is expanded and repeat from line 12 onward

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window_start  = 0                          # left window
        window_end    = 0                          # right window
        s_len         = len(s)                     # size of s
        t_dict        = Counter(t)                 # convert t to a dict with (key, value) pair as (char in t, count)
        required      = len(t_dict)                # num of unique chars in t
        needed        = 0                          # how many unique chars in t are in current window
        window_counts = {}                         # all unique chars in the current window
        result        = float("inf"), None, None   # answer tuple (window length, window start, window end)
        
        for window_end in range(s_len):                                                 # iterate through s
            current_char = s[window_end]                                                # get current character
            window_counts[current_char] = window_counts.get(current_char, 0) + 1        # count current character in window_counts dict
            
            """ lines 38-40 are alternative to line 35 """
            # if current_char not in window_counts.keys():    # if current character not in window_counts dict
            #      window_counts[current_char] = 0            # add it
            # window_counts[current_char] += 1                # increment the count of the current char in the window_counts dict
            
            if current_char in t_dict and window_counts[current_char] == t_dict[current_char]:
                    needed += 1                                                                         # if desired frequence of a char 
                                                                                                        # from t is reached in s, increment needed by 1
            
            while window_start < window_end and needed == required:                                     # once all needs meet the requirements
                current_char = s[window_start]                                                          
                calc = window_end - window_start + 1                                                    
                if (calc) < result[0]:                                                                  # get smallest window by comparing it with prev window
                    result = (calc, window_start, window_end)
                window_counts[current_char] -= 1                                                        # shrink window by removing head of window
                if current_char in t_dict and window_counts[current_char] < t_dict[current_char]:       # if required chars are no longer satisfied in window
                    needed -= 1                                                                             # decrement need and repeat loop
                window_start += 1                                                                       # move window_start up by 1 for next iteration
        
        if result[0] == float("inf"):
            return ""
        else:
            return s[result[1] : result[2] + 1]
