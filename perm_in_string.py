#       TITLE: Permutation in String
# DESCRIPTION: Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#              In other words, return true if one of s1's permutations is the substring of s2.
#  DIFFICULTY: Medium
#        TIME: O(N)
# 
# Algorithm details:
#   Create a dictionary (hash map) containing the counts of characters in the s1 string
#   Removing counts from s1 as the same characters from the counts are encountered in s2
#   If a substring of s2 is a permutation of s1, the counts of s1 should all decrease to zero
#   Instead of creating a new dict each iteration, we can populate a counter variable to see if the number of zeros reached == length of s1
#   If so, a permutation has been found
#   The counter variable is also increased when an element leaves the window

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1_counts = Counter(s1)                                # creates a dict object with counts of chars in the string
        s1_len = len(s1)
        s2_len = len(s2)
        zeros = 0
        
        for i in range(s2_len):
            if s2[i] in s1_counts:                              # if current character is in s1
                s1_counts[s2[i]] -= 1                             # decrease its count in s1
                if s1_counts[s2[i]] == 0:                       # if its count reaches zero
                    zeros += 1                                    # increase our zeros variable
            if i >= s1_len and s2[i-s1_len] in s1_counts:       # if the window too large
                if s1_counts[s2[i-s1_len]] == 0:                  # & counts were previously decreased
                    zeros -= 1                                      # decrease the zeros count
                s1_counts[s2[i-s1_len]] += 1                      # and restore count in dictionary
            
            if zeros == len(s1_counts):                         # if zero count equals the len of s1
                return True                                       # return true
        return False
