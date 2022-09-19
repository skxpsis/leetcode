#       TITLE: Backspace String Compare
# DESCRIPTION: Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#              Note that after backspacing an empty text, the text will continue empty.
#  DIFFICULTY: Easy

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # ignore = backspace_index-1
        # check that s and t are equal, ignore the remove character
        s_res = self.strCompare(s)
        t_res = self.strCompare(t)
        if s_res == t_res:
            return True
        else:
            return False
        
    def strCompare(self, string):
        skip = 0
        result = ""
        for char in reversed(string):
            if char == '#':
                skip += 1
            elif skip:
                skip -=1
            else:
                result += char
        return result
