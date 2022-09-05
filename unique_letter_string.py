#       TITLE: Count Unique Characters of All Substrings of a Given String
# DESCRIPTION: Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
#              For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters 
#              since they appear only once in s, therefore countUniqueChars(s) = 5.
#              Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. 
#              The test cases are generated such that the answer fits in a 32-bit integer.
#              Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
#  DIFFICULTY: Hard
#        TIME: O(N)
# 
# Algorithm details:
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1651064/1D-DP-Approach
# in progress

class Solution(object):    
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        index, dp, answer = {}, 0, 0
        for i, char in enumerate(s):
            j, k = index.get(char, [-1, -1])
            dp = dp + (i-j) - (j-k)
            answer += dp
            index[char] = [i, j]
        return answer
