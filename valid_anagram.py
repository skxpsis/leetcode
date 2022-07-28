#       TITLE: Valid Anagram
# DESCRIPTION: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#              An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
#              typically using all the original letters exactly once.
#  DIFFICULTY: Easy
#        TIME: O(N)
# 
# Algorithm details:
#     Create a dictionary (t_dict) with characters of t as each key and the count of that character in t as the value
#     Iterate over the input string, s, checking to see if it is in t_dict
#     If it isn't automatically return False as it is not an anagram
#     Otherwise decrement the count of that character in t_dict
#     After iterating through s, ff any key in t_dict has a value (count) that is not equal to 0, return False (anagram must not contain extraneous letters)
#     Otherwise, return True

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        t_dict = {}
        
        for char in t:
            if char not in t_dict.keys():
                t_dict[char] = 0
            t_dict[char] += 1
        
        for char in s:
            if char in t_dict.keys():
                t_dict[char] -= 1
            else:
                return False
        
        invalid = [key for key, value in t_dict.items() if value != 0]
        
        if invalid:
            return False
        else:
            return True
