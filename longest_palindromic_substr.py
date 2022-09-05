#       TITLE: Longest Palindromic Substring
#  DIFFICULTY: Medium
# DESCRIPTION: Given a string s, return the longest palindromic substring in s.
#
# Algorithm details:
#   Follows the idea that a palindrom is a mirror of itself around the center character
#   Iterates through string and compares palindromic substring length, taking max at each iteration
#   https://leetcode.com/problems/longest-palindromic-substring/solution/
# additional details in progress

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return ""
        if len(s) == 1:
            return s
        
        start, end = 0, 0
        for i, char in enumerate(s):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > (end-start):
                start = i - (max_len-1)/2
                end = i + max_len/2
        return s[start:end+1]
    
    def expandAroundCenter(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1
