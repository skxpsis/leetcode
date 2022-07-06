#       TITLE: Minimum Window Susbtring
# DESCRIPTION: Given two strings s and t of lengths m and n respectively, 
#              return the minimum window substring of s such that every character in t (including duplicates) is included in the window. 
#              If there is no such substring, return the empty string "".
#              The testcases will be generated such that the answer is unique.
#              A substring is a contiguous sequence of characters within the string.
#  DIFFICULTY: Hard
#  still in progress

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
        
        # covering edge/corner cases
        if len(s) == 1:
            if s[window_start] == t:
                return t
            else:
                return ""
        if s == t:
            return s
        if not s or not t:
            return ""
        if len(t) == 1:
            if t not in s:
                return ""
            else:
                return t
        
        for window_end in range(s_len):
            current_char = s[window_end]                      # get current character
            window_counts[current_char] = window_counts.get(current_char, 0) + 1
            # if current_char not in window_counts.keys():    # if current character not in window_counts dict
            #      window_counts[current_char] = 0            # add it
            # window_counts[current_char] += 1                # increment the count of the current char in the window_counts dict
            
            if current_char in t_dict and window_counts[current_char] == t_dict[current_char]:
                    needed += 1                                          # if desired frequence is reached in s, increment needed by 1
            
            while window_start < window_end and needed == required:      # shrink the window as much as possible
                current_char = s[window_start]
                calc = window_end - window_start + 1
                if (calc) < result[0]:                                   # get smallest window by comparing it with previous window
                    result = (calc, window_start, window_end)
                    
                window_counts[current_char] -= 1                         # remove head of window as it is no longer part of the window
                if current_char in t_dict and window_counts[current_char] < t_dict[current_char]:
                    needed -= 1
                
                window_start += 1                                        # move window_start up by 1
        
        if result[0] == float("inf"):
            return ""
        else:
            return s[result[1] : result[2] + 1]
        
