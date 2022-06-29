# TITLE:       Palindrome Number
# DESCRIPTION: Given an integer x, return true if x is palindrome integer.
#              An integer is a palindrome when it reads the same backward as forward.
#              For example, 121 is a palindrome while 123 is not.
# DIFFICULTY:  Easy

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Algorithm details:
            # find the reverse of the input
            # if the reverse of the input is equal to the input, the input is a palindrome (return True)
            # else, return False
        x2 = str(x)
        size = len(x2)
        if size == 0:        # if x is null, return False
            return False
        elif size == 1:      # if x has only 1 digit, return True
            return True
        else:                               # check for is palindrome
            for i in range(size//2):        # only check half the string to confirm mirroring
                if x2[i] != x2[size-1-i]:   # check that the string mirrors itself
                    return False            # if not, return false
            return True                     # if it does, return true
        
