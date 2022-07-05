# TITLE:       Palindrome Number
# DESCRIPTION: Given an integer x, return true if x is palindrome integer.
#              An integer is a palindrome when it reads the same backward as forward.
#              For example, 121 is a palindrome while 123 is not.
# DIFFICULTY:  Easy
#
# Algorithm details:
    # if input length == 0, return False
    # if input length == 1, return True
    # else, iterate through half the size of the input
    # confirm that the i-th element of the first half matches the mirrored i-th element of the second half
    # if they do not match, return False
    # iterate through until middle point reached, if not mismatches, return True

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
            
        x2 = str(x)
        size = len(x2)
        if size == 0:        # if x is null, return False
            return False
        elif size == 1:      # if x has only 1 digit, return True
            return True
        else:                               # check for is palindrome
            for i in range(size//2):        # only check half the string to confirm mirroring
                if x2[i] != x2[size-1-i]:   # check that the string mirrors itself; include -1 to prevent index error
                    return False            # if not, return false
            return True                     # if it does, return true
        
